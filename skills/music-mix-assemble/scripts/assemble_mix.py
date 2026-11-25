#!/usr/bin/env python3
"""Join released songs' videos into one mix video, deterministically.

  assemble_mix.py --songs songs.json --out mix.mp4 [--tracklist tracklist.json]
                  [--lufs -14] [--true-peak -1.5] [--fade 1.5] [--audio-bitrate 192k]

songs.json is a JSON list in play order: [{"file": "…/song-a-16x9.mp4", "title": "Song A"}, …].

The video stream of every song is copied as it is — no re-encode, so the picture is bit for bit the
release's and the mix is assembled in seconds. That is only valid when every file has the same video
and audio parameters (codec, profile, size, pixel format, frame rate, time base, sample rate,
channels); the script checks them with ffprobe first and refuses, naming the file that differs,
rather than producing a mix that stutters at a join. Only the audio is re-encoded: each song is
normalised to --lufs (two-pass loudnorm, linear) so no song is louder than the next, and gets a
--fade fade-in and fade-out inside its own length, so audio and video stay the same length and in
sync. The joins of the picture are hard cuts; the releases' own intros carry the change.

Prints JSON: the mix's duration, each song's start, and description chapter lines ("0:00 Song A").
Writes --tracklist with the same data. A refusal exits 2 with {"ok": false, "error": …}.
Needs ffmpeg and ffprobe on PATH. Standard library only: Python 3.11.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

# What must be equal for the concat demuxer to copy the video without a stutter at a join.
VIDEO_KEYS = ("codec_name", "profile", "width", "height", "pix_fmt", "r_frame_rate", "time_base")
AUDIO_KEYS = ("codec_name", "sample_rate", "channels")


class Refusal(Exception):
    pass


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def need_tools() -> None:
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise Refusal(f"{tool} is not on PATH")


def probe(path: Path) -> dict[str, Any]:
    r = run(["ffprobe", "-v", "error", "-show_entries",
             "stream=codec_type," + ",".join(sorted(set(VIDEO_KEYS + AUDIO_KEYS))) + ":format=duration",
             "-of", "json", str(path)])
    if r.returncode:
        raise Refusal(f"ffprobe cannot read {path}: {r.stderr.strip()[:300]}")
    doc = json.loads(r.stdout)
    streams = doc.get("streams", [])
    video = [s for s in streams if s.get("codec_type") == "video"]
    audio = [s for s in streams if s.get("codec_type") == "audio"]
    if len(video) != 1 or len(audio) != 1:
        raise Refusal(f"{path} must have exactly one video and one audio stream")
    return {"video": {k: video[0].get(k) for k in VIDEO_KEYS},
            "audio": {k: audio[0].get(k) for k in AUDIO_KEYS},
            "duration": float(doc["format"]["duration"])}


def check_same(probes: list[tuple[Path, dict[str, Any]]]) -> None:
    first_path, first = probes[0]
    for path, p in probes[1:]:
        for kind in ("video", "audio"):
            diff = {k: (first[kind][k], p[kind][k]) for k in first[kind] if first[kind][k] != p[kind][k]}
            if diff:
                raise Refusal(f"{path.name} differs from {first_path.name} in {kind}: {diff}; the video "
                              "cannot be copied — render it with the same template settings")


def measure(path: Path, lufs: float, tp: float) -> dict[str, str]:
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-vn",
             "-af", f"loudnorm=I={lufs}:TP={tp}:LRA=11:print_format=json", "-f", "null", "-"])
    text = r.stderr
    try:
        return json.loads(text[text.rindex("{"):text.rindex("}") + 1])
    except ValueError:
        raise Refusal(f"loudness of {path} could not be measured: {text[-300:]}") from None


def stamp(seconds: float) -> str:
    s = int(seconds)
    h, rest = divmod(s, 3600)
    m, sec = divmod(rest, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m}:{sec:02d}"


def assemble(songs: list[dict[str, str]], out: Path, lufs: float, tp: float, fade: float,
             bitrate: str) -> dict[str, Any]:
    if len(songs) < 2:
        raise Refusal("a mix needs at least two songs")
    paths = []
    for s in songs:
        if not isinstance(s, dict) or not s.get("file") or not s.get("title"):
            raise Refusal("each song is {\"file\": …, \"title\": …}")
        p = Path(s["file"])
        if not p.is_file():
            raise Refusal(f"no such file: {p}")
        paths.append(p)
    probes = [(p, probe(p)) for p in paths]
    check_same(probes)
    sample_rate = probes[0][1]["audio"]["sample_rate"]
    with tempfile.TemporaryDirectory(dir=out.parent) as tmp:
        parts, tracks, start = [], [], 0.0
        for i, ((path, pr), song) in enumerate(zip(probes, songs)):
            if pr["duration"] <= 2 * fade:
                raise Refusal(f"{path.name} is {pr['duration']:.1f}s, too short for two {fade}s fades")
            m = measure(path, lufs, tp)
            af = (f"loudnorm=I={lufs}:TP={tp}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
                  f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
                  f"offset={m['target_offset']}:linear=true,aresample={sample_rate},"
                  f"afade=t=in:st=0:d={fade},afade=t=out:st={pr['duration'] - fade:.3f}:d={fade}")
            part = Path(tmp) / f"part{i:03d}.mp4"
            r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(path), "-map", "0:v",
                     "-map", "0:a", "-c:v", "copy", "-af", af, "-c:a", "aac", "-b:a", bitrate,
                     "-ar", str(sample_rate), str(part)])
            if r.returncode:
                raise Refusal(f"processing {path.name} failed: {r.stderr.strip()[:300]}")
            length = probe(part)["duration"]
            tracks.append({"title": song["title"], "file": str(path), "start": round(start, 3),
                           "duration": round(length, 3), "measured_lufs": float(m["input_i"])})
            start += length
            parts.append(part)
        listing = Path(tmp) / "list.txt"
        listing.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
        r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
                 "-i", str(listing), "-c", "copy", "-movflags", "+faststart", str(out)])
        if r.returncode:
            raise Refusal(f"joining failed: {r.stderr.strip()[:300]}")
    total = probe(out)["duration"]
    if abs(total - start) > 0.5:
        raise Refusal(f"the mix is {total:.2f}s but its songs add up to {start:.2f}s — not written as valid")
    chapters = [f"{stamp(t['start'])} {t['title']}" for t in tracks]
    return {"ok": True, "out": str(out), "duration": round(total, 3), "lufs": lufs, "fade": fade,
            "tracks": tracks, "chapters": chapters}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="assemble_mix.py", description=__doc__.split("\n\n")[0])
    p.add_argument("--songs", required=True, help="JSON list in play order: [{file, title}, …]")
    p.add_argument("--out", required=True, help="the mix video to write (.mp4)")
    p.add_argument("--tracklist", help="also write the tracks and chapters here (JSON)")
    p.add_argument("--lufs", type=float, default=-14.0, help="integrated loudness target (default -14)")
    p.add_argument("--true-peak", type=float, default=-1.5, help="true peak ceiling (default -1.5 dBTP)")
    p.add_argument("--fade", type=float, default=1.5, help="fade in and out of each song, seconds (1.5)")
    p.add_argument("--audio-bitrate", default="192k", help="AAC bitrate (default 192k)")
    a = p.parse_args(argv)
    try:
        need_tools()
        try:
            songs = json.loads(Path(a.songs).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            raise Refusal(f"cannot read {a.songs}: {e}") from None
        if not isinstance(songs, list):
            raise Refusal("--songs must hold a JSON list")
        if a.fade < 0 or a.fade > 10:
            raise Refusal("--fade must be between 0 and 10 seconds")
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        result = assemble(songs, out, a.lufs, a.true_peak, a.fade, a.audio_bitrate)
        if a.tracklist:
            Path(a.tracklist).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    except Refusal as e:
        print(json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
