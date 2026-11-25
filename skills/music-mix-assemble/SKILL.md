---
name: music-mix-assemble
description: Join released songs into one mix video deterministically — the sound built once from each song's master WAV at one loudness with a short fade in and out, cut to its video's exact length; the picture copied without re-encoding when the videos match, re-encoded once when they do not; chapters for the description. Use when a step assembles a mix, compilation or playlist video from the channel's own release videos.
---

# Assemble a mix video

One script does the assembly, so every mix is made the same way:

```bash
python3 <base>/scripts/assemble_mix.py --songs songs.json --out mix.mp4 --tracklist tracklist.json
```

- `songs.json` — the songs in play order, at least two:
  `[{"video": "<the song's 16:9 video>", "audio": "<the song's master WAV>", "title": "<song title>"}, …]`.
  The master is the WAV the release's video was made from (Create Music Release's audio step); it
  starts where the video's audio starts.
- Options: `--lufs -14`, `--fade 1.5` (seconds, in and out of each song), `--audio-bitrate 192k`,
  `--video auto|copy|encode` (default auto). Keep the defaults unless the step says otherwise.
- Output (stdout and `--tracklist`): `duration`, `video_mode` (copy or encode, and the file that
  differed when it encoded), `tracks` (title, start, duration, measured loudness) and `chapters` —
  lines such as `0:00 Song A` for the description, in order.

## What it does, and what it refuses

- **Sound, in one pass**: each master is cut or padded with silence to its video's exact length, so
  the songs start at the same instant in sound and picture and nothing adds up over many songs; a
  constant gain brings it to `--lufs`, held 1 dB below true peak (its own dynamics kept, no limiter); it fades in and out inside its length;
  the whole mix is encoded once to AAC from the masters. A master more than 0.1 s off its video's
  length, or 20 ms or more off the video's own sound over the first 30 s, is refused — it is not on
  that video's timeline. Each track reports its `master_offset_ms`.
- **Picture**: copied without re-encoding when every video shares its parameters (codec, profile,
  level, size, pixel format, frame rate, time base, aspect, colour) — seconds, every frame the
  release's. When they differ (videos from different renderers), `auto` re-encodes the picture once
  (libx264 CRF 18, 1920×1080 at 60 fps) and says which file differed; `copy` refuses.
  Joins of the picture are cuts; each release's own intro carries the change.
- The script checks the mix's length against its songs, and its sound against its picture to two frames, and refuses a mismatch. A refusal exits 2
  with `{"ok": false, "error": "…"}`. Needs `ffmpeg` and `ffprobe` (in the worker image).
