#!/usr/bin/env python3
"""Join released songs into one mix video, deterministically.

  assemble_mix.py --songs songs.json --out mix.mp4 [--tracklist tracklist.json]
                  [--lufs -14] [--fade 1.5] [--audio-bitrate 192k] [--video auto|copy|encode]

songs.json is a JSON list in play order:
  [{"video": "…/song-a-16x9.mp4", "audio": "…/song-a-master.wav", "title": "Song A"}, …]
`audio` is the song's master (the WAV the release's video was made from); it starts where the
video's own audio starts, so it replaces it sample for sample.

Audio — one pass for the whole mix: every master is cut or padded with silence to its video
stream's exact length (so the songs' starts in the sound and in the picture are the same instant,
with nothing adding up over many songs), raised or lowered by a constant gain to --lufs (measured
with EBU R128; a constant gain keeps each master's own dynamics; held 1 dB below true peak), faded in and out by --fade inside
its length, joined, and encoded once to AAC. A master more than 0.1 s longer or shorter than its
video is refused — it is not that video's master.

Video — `--video copy` joins the streams without re-encoding (seconds, every frame the release's);
it needs every video to share codec, profile, level, size, pixel format, frame rate, time base,
sample aspect ratio and colour fields, which ffprobe checks first. `encode` re-encodes all videos
once to 1920×1080 at 60 fps (libx264, CRF 18). `auto` (default) copies when they
match and encodes when they do not, saying which file differed. Joins of the picture are cuts; each
release's own intro carries the change.

Prints JSON: the mix's duration, the video mode used, each song's start, and description chapter
lines ("0:00 Song A"); writes the same to --tracklist. A refusal exits 2 with {"ok": false, …}.
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

# What must be equal for the concat demuxer to copy the picture without a glitch at a join.
VIDEO_KEYS = ("codec_name", "profile", "level", "width", "height", "pix_fmt", "r_frame_rate", "time_base",
              "sample_aspect_ratio", "color_range", "color_space", "color_transfer", "color_primaries",
              "field_order")
# A master is rendered to its video's timeline; renderers round the picture up to a whole frame.
LENGTH_SLACK = 0.1
# The sound and the picture of the finished mix: two frames at 60 fps.
SYNC_SLACK = 0.034
TRUE_PEAK = -1.0
FRAME = (1920, 1080, "60")


class Refusal(Exception):
    pass


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def need_tools() -> None:
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise Refusal(f"{tool} is not on PATH")


def probe_video(path: Path) -> dict[str, Any]:
    r = run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries",
             "stream=" + ",".join(VIDEO_KEYS) + ",duration", "-of", "json", str(path)])
    if r.returncode:
        raise Refusal(f"ffprobe cannot read {path}: {r.stderr.strip()[:300]}")
    streams = json.loads(r.stdout).get("streams", [])
    if len(streams) != 1:
        raise Refusal(f"{path} must have exactly one video stream")
    s = streams[0]
    if not s.get("duration"):
        raise Refusal(f"{path}: the video stream has no duration")
    return {"params": {k: s.get(k) for k in VIDEO_KEYS}, "duration": float(s["duration"])}


def audio_length(path: Path) -> float:
    r = run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=duration",
             "-of", "csv=p=0", str(path)])
    try:
        return float(r.stdout.strip())
    except ValueError:
        raise Refusal(f"{path} has no readable audio stream") from None


def loudness(path: Path) -> tuple[float, float]:
    """Integrated loudness (LUFS) and true peak (dBTP)."""
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-map", "0:a:0",
             "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"])
    i = [ln.split() for ln in r.stderr.splitlines() if ln.strip().startswith("I:")]
    tp = [ln.split() for ln in r.stderr.splitlines() if ln.strip().startswith("Peak:")]
    if not i or not tp:
        raise Refusal(f"the loudness of {path} could not be measured")
    return float(i[-1][1]), float(tp[-1][1])


def stamp(seconds: float) -> str:
    s = int(seconds)
    h, rest = divmod(s, 3600)
    m, sec = divmod(rest, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m}:{sec:02d}"


def first_difference(probes: list[tuple[Path, dict[str, Any]]]) -> str | None:
    base_path, base = probes[0]
    for path, p in probes[1:]:
        diff = {k: (base["params"][k], p["params"][k]) for k in VIDEO_KEYS if base["params"][k] != p["params"][k]}
        if diff:
            return f"{path.name} differs from {base_path.name}: {diff}"
    return None


def build_video(probes: list[tuple[Path, dict[str, Any]]], mode: str, tmp: Path) -> tuple[Path, str, str | None]:
    out = tmp / "video.mp4"
    diff = first_difference(probes)
    if mode == "copy" and diff:
        raise Refusal(f"--video copy, but {diff}")
    use = "copy" if mode == "copy" or (mode == "auto" and not diff) else "encode"
    if use == "copy":
        listing = tmp / "videos.txt"
        # Without `duration` the demuxer steps by each file's container length — the longer of its
        # audio and video — and every join opens a gap in the picture against the sound.
        listing.write_text("".join(f"file '{p.resolve().as_posix()}'\nduration {pr['duration']:.6f}\n"
                                   for p, pr in probes), encoding="utf-8")
        r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
                 "-i", str(listing), "-map", "0:v", "-c", "copy", str(out)])
    else:
        # One fixed frame, not the first song's: an old 30 fps song opening the mix would otherwise
        # set the whole mix to 30 fps.
        w, h, fps = FRAME
        inputs: list[str] = []
        chains = []
        for i, (p, pr) in enumerate(probes):
            inputs += ["-i", str(p)]
            # Each video normalised to the first one's frame, then trimmed to its own length so the
            # audio cut to the same lengths stays in step.
            chains.append(f"[{i}:v]scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:"
                          f"(oh-ih)/2,setsar=1,fps={fps},format=yuv420p,trim=0:{pr['duration']:.6f},"
                          f"setpts=PTS-STARTPTS[v{i}]")
        graph = ";".join(chains) + ";" + "".join(f"[v{i}]" for i in range(len(probes))) + \
            f"concat=n={len(probes)}:v=1:a=0[vout]"
        r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", graph,
                 "-map", "[vout]", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                 str(out)])
    if r.returncode:
        raise Refusal(f"building the picture failed: {r.stderr.strip()[-400:]}")
    return out, use, diff


def build_audio(songs: list[dict[str, Any]], lufs: float, fade: float, bitrate: str, tmp: Path) -> Path:
    out = tmp / "audio.m4a"
    inputs: list[str] = []
    chains = []
    for i, s in enumerate(songs):
        inputs += ["-i", str(s["audio_path"])]
        d = s["video_duration"]
        chains.append(f"[{i}:a]aresample=48000,atrim=0:{d:.6f},apad=whole_dur={d:.6f},asetpts=N/SR/TB,"
                      f"volume={s['gain_db']:.2f}dB,afade=t=in:st=0:d={fade},"
                      f"afade=t=out:st={max(d - fade, 0):.6f}:d={fade}[a{i}]")
    graph = ";".join(chains) + ";" + "".join(f"[a{i}]" for i in range(len(songs))) + \
        f"concat=n={len(songs)}:v=0:a=1[aout]"
    r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", graph,
             "-map", "[aout]", "-c:a", "aac", "-b:a", bitrate, "-ar", "48000", str(out)])
    if r.returncode:
        raise Refusal(f"building the sound failed: {r.stderr.strip()[-400:]}")
    return out


def assemble(songs: list[dict[str, str]], out: Path, lufs: float, fade: float, bitrate: str,
             video_mode: str) -> dict[str, Any]:
    if len(songs) < 2:
        raise Refusal("a mix needs at least two songs")
    prepared = []
    for s in songs:
        if not isinstance(s, dict) or not s.get("video") or not s.get("audio") or not s.get("title"):
            raise Refusal('each song is {"video": …, "audio": …, "title": …}')
        v, a = Path(s["video"]), Path(s["audio"])
        for f in (v, a):
            if not f.is_file():
                raise Refusal(f"no such file: {f}")
        pv = probe_video(v)
        i, tp = loudness(a)
        al = audio_length(a)
        if abs(al - pv["duration"]) > LENGTH_SLACK:
            raise Refusal(f"{a.name} is {al:.2f}s but its video {v.name} is {pv['duration']:.2f}s — "
                          "not that video's master")
        if pv["duration"] <= 2 * fade:
            raise Refusal(f"{v.name} is {pv['duration']:.1f}s, too short for two {fade}s fades")
        prepared.append({"title": s["title"], "video_path": v, "audio_path": a, "probe": pv,
                         "video_duration": pv["duration"], "measured_lufs": i, "true_peak": tp,
                         # A constant gain to the target, held below the true-peak ceiling so a quiet
                         # master is not pushed into clipping; no limiter, so its dynamics stay.
                         "gain_db": min(lufs - i, TRUE_PEAK - tp)})
    with tempfile.TemporaryDirectory(dir=out.parent) as tmpdir:
        tmp = Path(tmpdir)
        video, used, diff = build_video([(s["video_path"], s["probe"]) for s in prepared], video_mode, tmp)
        audio = build_audio(prepared, lufs, fade, bitrate, tmp)
        r = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video), "-i", str(audio),
                 "-map", "0:v", "-map", "1:a", "-c", "copy", "-movflags", "+faststart", str(out)])
        if r.returncode:
            raise Refusal(f"muxing failed: {r.stderr.strip()[-300:]}")
    expected = sum(s["video_duration"] for s in prepared)
    got_v = probe_video(out)["duration"]
    got_a = audio_length(out)
    if abs(got_v - expected) > LENGTH_SLACK or abs(got_a - got_v) > SYNC_SLACK:
        out.unlink(missing_ok=True)
        raise Refusal(f"the mix came out {got_v:.2f}s video / {got_a:.2f}s audio, expected {expected:.2f}s")
    tracks, start = [], 0.0
    for s in prepared:
        tracks.append({"title": s["title"], "video": str(s["video_path"]), "audio": str(s["audio_path"]),
                       "start": round(start, 3), "duration": round(s["video_duration"], 3),
                       "measured_lufs": s["measured_lufs"], "gain_db": round(s["gain_db"], 2)})
        start += s["video_duration"]
    return {"ok": True, "out": str(out), "duration": round(got_v, 3), "video_mode": used,
            "video_mismatch": diff, "lufs": lufs, "fade": fade, "tracks": tracks,
            "chapters": [f"{stamp(t['start'])} {t['title']}" for t in tracks]}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="assemble_mix.py", description=__doc__.split("\n\n")[0])
    p.add_argument("--songs", required=True, help='JSON list in play order: [{"video", "audio", "title"}, …]')
    p.add_argument("--out", required=True, help="the mix video to write (.mp4)")
    p.add_argument("--tracklist", help="also write the tracks and chapters here (JSON)")
    p.add_argument("--lufs", type=float, default=-14.0, help="integrated loudness of every song (default -14)")
    p.add_argument("--fade", type=float, default=1.5, help="fade in and out of each song, seconds (1.5)")
    p.add_argument("--audio-bitrate", default="192k", help="AAC bitrate (default 192k)")
    p.add_argument("--video", choices=["auto", "copy", "encode"], default="auto",
                   help="copy the picture, re-encode it once, or copy when the videos match (default)")
    a = p.parse_args(argv)
    try:
        need_tools()
        try:
            songs = json.loads(Path(a.songs).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            raise Refusal(f"cannot read {a.songs}: {e}") from None
        if not isinstance(songs, list):
            raise Refusal("--songs must hold a JSON list")
        if not 0 <= a.fade <= 10:
            raise Refusal("--fade must be between 0 and 10 seconds")
        out = Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        result = assemble(songs, out, a.lufs, a.fade, a.audio_bitrate, a.video)
        if a.tracklist:
            Path(a.tracklist).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    except Refusal as e:
        print(json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
