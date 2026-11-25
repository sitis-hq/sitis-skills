---
name: music-mix-assemble
description: Join released songs' videos into one mix video deterministically — video copied without re-encoding, each song's audio normalised to one loudness with a short fade in and out, chapters for the description. Use when a step assembles a mix, compilation or playlist video from the channel's own release videos.
---

# Assemble a mix video

One script does the assembly, so every mix is made the same way:

```bash
python3 <base>/scripts/assemble_mix.py --songs songs.json --out mix.mp4 --tracklist tracklist.json
```

- `songs.json` — the songs in play order: `[{"file": "<path to the song's 16:9 video>", "title": "<song title>"}, …]`,
  at least two.
- Options: `--lufs -14` (loudness target), `--true-peak -1.5`, `--fade 1.5` (seconds, in and out of
  each song), `--audio-bitrate 192k`. Keep the defaults unless the step says otherwise.
- Output (stdout and `--tracklist`): `duration`, `tracks` (title, start, duration, measured loudness)
  and `chapters` — lines such as `0:00 Song A` for the description, in order.

## What it does, and what it refuses

- **The picture is copied, not re-encoded**: the mix is assembled in seconds and every frame is the
  release's. That works only when all videos share their parameters (codec, profile, size, pixel
  format, frame rate, time base; audio codec, sample rate, channels). The script checks with ffprobe
  first and **refuses, naming the file that differs** — then the step reports it; it never re-encodes
  around it. Videos rendered by the same visualizer template match.
- **Only the audio is processed**: each song is measured and normalised to `--lufs` (two-pass
  loudnorm), so no song is louder than the next, and fades in and out inside its own length. Audio and
  video keep the same length and stay in sync; the script checks the mix's length against the sum of
  its songs and refuses a mismatch over 0.5 s.
- **Joins of the picture are cuts**; each release's own intro carries the change.
- A refusal exits 2 with `{"ok": false, "error": "…"}`. Needs `ffmpeg` and `ffprobe` (in the worker
  image).
