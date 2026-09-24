---
description: Edit and process media files (video/audio/images). Use when asked to "create music video", "normalize audio", "loop video", "remove audio from video", "resize image", "add watermark", "overlay image", "process media", "prepare audio for distribution", "trim audio", "cut audio", "test youtube banner safe zone", or "check banner safe zone".
allowed-tools: Bash(media-commands:*)
---

Example usage:

```bash
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3
```

Output is always JSON: `{ success, command, data }` or `{ success, command, error: { message, type } }`.

## Commands

### 1. create-music-video

Create professional music videos with GPU acceleration.

```bash
media-commands --command create-music-video --video <path> --audio <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--video` | Yes | Source video file path or URL |
| `--audio` | Yes | Source audio file path or URL |
| `--aspect-ratios` | No | Comma-separated: `16:9,9:16,1:1` (default: `16:9`) |
| `--compression` | No | `maximum`, `balanced`, `fast` (default: `maximum`) |
| `--audio-only` | No | Export only normalized audio |
| `--video-only` | No | Export only video files |
| `--audio-start` | No | Audio start time in seconds (for trimming) |
| `--audio-end` | No | Audio end time in seconds (for trimming) |
| `--audio-duration` | No | Audio duration in seconds (alternative to `--audio-end`) |
| `--loop-playback-speed` | No | Playback speed for looped video footage, 0.25-4.0 (default: `1.0`) |
| `--loudnorm` | No | Loudness `I:TP:LRA` (default: `-14:-1:11` YouTube standard) |
| `--format` | No | `m4a`, `mp3`, `wav` (default: `m4a`) |
| `--sample-rate` | No | Sample rate in Hz (default: `48000`) |
| `--channels` | No | `1` (mono) or `2` (stereo, default) |
| `--bitrate` | No | Audio bitrate (default: `320k`) |
| `--output` | No | Output file path |
| `--verbose` | No | Enable debug logging |

**Examples:**

```bash
# Basic music video (16:9 + audio)
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3

# Multiple aspect ratios
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3 --aspect-ratios 16:9,9:16

# All aspect ratios
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3 --aspect-ratios 16:9,9:16,1:1

# Custom loudness
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3 --loudnorm "-14:-1:11"

# Trimmed audio (30 seconds starting from 10s) - for short previews
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3 --audio-start 10 --audio-duration 30

# Trimmed audio with end time
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3 --audio-start 10 --audio-end 40

# Vertical preview for TikTok/Reels (30s clip)
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3 --aspect-ratios 9:16 --audio-start 0 --audio-duration 30

# Speed up looped video footage 2x (video plays faster, audio unchanged)
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3 --loop-playback-speed 2

# Slow motion looped footage at 0.5x
media-commands --command create-music-video --video ./video.mp4 --audio ./audio.mp3 --loop-playback-speed 0.5
```

---

### 2. normalize-audio

Normalize audio for streaming platforms with preset configurations.

```bash
media-commands --command normalize-audio --audio <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--audio` | Yes | Source audio file path or URL |
| `--output` | No | Output file path |
| `--preset` | No | `youtube`, `distrokid`, `custom` (default: `distrokid`) |
| `--loudnorm` | No | Custom `I:TP:LRA` params |
| `--format` | No | `m4a`, `mp3`, `wav` |
| `--sample-rate` | No | Sample rate in Hz |
| `--channels` | No | `1` or `2` |
| `--bitrate` | No | Audio bitrate |
| `--verbose` | No | Enable debug logging |

**Distributor Presets:**

| Preset | Loudness | Format | Sample Rate |
|--------|----------|--------|-------------|
| `youtube` | -14 LUFS, -1 dBTP | M4A | 48 kHz |
| `distrokid` | -14 LUFS, -1 dBTP | WAV | 44.1 kHz |

**Examples:**

```bash
# Normalize for DistroKid (default)
media-commands --command normalize-audio --audio ./audio.mp3

# Normalize for YouTube
media-commands --command normalize-audio --audio ./audio.mp3 --preset youtube

# Custom loudness settings
media-commands --command normalize-audio --audio ./audio.mp3 --loudnorm "-14:-1:11" --format wav
```

---

### 3. loop-video

Loop video to match target duration with aspect ratio transformation.

```bash
media-commands --command loop-video --video <path> --duration <seconds> --aspect-ratio <ratio> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--video` | Yes | Source video file path or URL |
| `--duration` | Yes | Target duration in seconds |
| `--aspect-ratio` | Yes | `16:9`, `9:16`, or `1:1` |
| `--output` | No | Output file path |
| `--compression` | No | `maximum`, `balanced`, `fast` |
| `--loop-playback-speed` | No | Playback speed for looped video footage, 0.25-4.0 (default: `1.0`) |
| `--verbose` | No | Enable debug logging |

**Examples:**

```bash
# Loop video to 2 minutes, horizontal
media-commands --command loop-video --video ./video.mp4 --duration 120 --aspect-ratio 16:9

# Loop video to 3 minutes, vertical for TikTok
media-commands --command loop-video --video ./video.mp4 --duration 180 --aspect-ratio 9:16

# Loop with 2x speed footage
media-commands --command loop-video --video ./video.mp4 --duration 120 --aspect-ratio 16:9 --loop-playback-speed 2
```

---

### 4. remove-audio

Strip audio tracks from video while preserving quality.

```bash
media-commands --command remove-audio --video <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--video` | Yes | Source video file path or URL |
| `--output` | No | Output file path |
| `--compression` | No | `maximum`, `balanced`, `fast` |
| `--verbose` | No | Enable debug logging |

**Examples:**

```bash
# Remove audio from video
media-commands --command remove-audio --video ./video.mp4
```

---

### 5. resize-image

Resize images with flexible width/height options and fit modes.

```bash
media-commands --command resize-image --input <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--input` | Yes | Source image file path or URL |
| `--width` | No* | Target width in pixels |
| `--height` | No* | Target height in pixels |
| `--fit` | No | `contain`, `cover`, `fill`, `inside` (default: `contain`) |
| `--quality` | No | JPEG quality 1-100 (default: `100`) |
| `--output` | No | Output file path |
| `--verbose` | No | Enable debug logging |

*At least one of `--width` or `--height` required.

**Fit Modes:**

| Mode | Description |
|------|-------------|
| `contain` | Fit within dimensions, preserve aspect ratio |
| `cover` | Fill dimensions, crop if needed |
| `fill` | Stretch to exact dimensions (may distort) |
| `inside` | Like contain, but never upscale |

**Examples:**

```bash
# Resize to width 64px (preserves aspect ratio)
media-commands --command resize-image --input ./image.jpg --width 64

# Resize to exact dimensions with cover
media-commands --command resize-image --input ./image.png --width 800 --height 600 --fit cover

# Resize with custom quality
media-commands --command resize-image --input ./photo.jpg --width 1024 --quality 85
```

---

### 6. overlay-image

Add watermark or overlay image onto another image.

```bash
media-commands --command overlay-image --input <path> --overlay <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--input` | Yes | Background image path or URL |
| `--overlay` | Yes | Overlay/watermark image path or URL |
| `--position` | No | `top-left`, `top-right`, `bottom-left`, `bottom-right`, `center` (default: `bottom-right`) |
| `--offset-x` | No | Horizontal offset in pixels (default: `10`) |
| `--offset-y` | No | Vertical offset in pixels (default: `10`) |
| `--opacity` | No | Overlay opacity 0-1 (default: `1`) |
| `--scale` | No | Overlay scale factor 0.1-2.0 (default: `1`) |
| `--overlay-fit` | No | `none`, `contain`, `cover`, `stretch` (default: `none`) |
| `--quality` | No | JPEG quality 1-100 (default: `100`) |
| `--output` | No | Output file path |
| `--verbose` | No | Enable debug logging |

**Overlay Fit Modes:**

| Mode | Description |
|------|-------------|
| `none` | Original overlay size (with optional scale multiplier) |
| `contain` | Fit overlay within background, preserve aspect ratio |
| `cover` | Cover entire background, preserve aspect ratio |
| `stretch` | Stretch overlay to exact background size |

**Examples:**

```bash
# Add watermark to bottom-right corner
media-commands --command overlay-image --input ./photo.jpg --overlay ./logo.png

# Centered watermark with 50% opacity
media-commands --command overlay-image --input ./photo.jpg --overlay ./logo.png --position center --opacity 0.5

# Scaled watermark in top-left
media-commands --command overlay-image --input ./photo.jpg --overlay ./logo.png --position top-left --scale 0.3

# Fit overlay to cover entire background (e.g., YouTube safe zone template)
media-commands --command overlay-image --input ./banner.png --overlay ./safe-zone.png --overlay-fit cover --position center --offset-x 0 --offset-y 0
```

---

### 7. trim-audio

Extract a portion of an audio file based on start time, end time, or duration. Uses stream copy (no re-encoding) for fast extraction.

**Use cases:**
- Create short audio previews for social media
- Extract specific segments from longer recordings
- Prepare audio clips for `create-music-video` command

```bash
media-commands --command trim-audio --audio <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--audio` | Yes | Source audio file path or URL |
| `--start-time` | No | Start time in seconds (default: `0`) |
| `--end-time` | No | End time in seconds |
| `--duration` | No | Duration in seconds (alternative to `--end-time`) |
| `--output` | No | Output file path |
| `--verbose` | No | Enable debug logging |

**Note:** Cannot specify both `--end-time` and `--duration` - use one or the other.

**Output includes:**
- `outputPath` - Path to trimmed audio file
- `duration` - Actual duration of trimmed audio
- `originalDuration` - Original audio duration
- `startTime` / `endTime` - Actual trim points used
- `size` - Output file size in bytes

**Examples:**

```bash
# Trim first 30 seconds
media-commands --command trim-audio --audio ./audio.mp3 --duration 15

# Extract from 10s to 40s
media-commands --command trim-audio --audio ./audio.mp3 --start-time 10 --end-time 40

# Extract 30 seconds starting from 10s
media-commands --command trim-audio --audio ./audio.mp3 --start-time 10 --duration 15

# With custom output path
media-commands --command trim-audio --audio ./audio.mp3 --start-time 10 --duration 15 --output ./preview.mp3
```

---

### 8. test-youtube-banner-safe-zone

Draw safe zone overlay on YouTube banner to verify critical content placement. Darkens areas outside safe zone and draws border around it.

```bash
media-commands --command test-youtube-banner-safe-zone --input <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--input` | Yes | Banner image path or URL |
| `--overlay-opacity` | No | Darkening opacity 0-1 (default: `0.8`) |
| `--border-color` | No | Border color hex (default: `#FF0000`) |
| `--border-width` | No | Border width 1-20px (default: `3`) |
| `--quality` | No | JPEG quality 1-100 (default: `100`) |
| `--output` | No | Output file path |
| `--verbose` | No | Enable debug logging |

**Safe Zone:** 1546×423 px centered (60.4% × 29.4% of banner). Visible on all devices.

**Examples:**

```bash
# Basic safe zone preview
media-commands --command test-youtube-banner-safe-zone --input ./banner.png

# Custom border color and opacity
media-commands --command test-youtube-banner-safe-zone --input ./banner.png --border-color "#00FF00" --overlay-opacity 0.7
```

---

### 9. create-video-programmatically

Render music visualizer videos via Remotion. Produces full 16:9 video, 9:16 loop (no text/audio), 9:16 short (60s), 9:16 preview (30s, monochrome), and screenshots.

```bash
media-commands --command create-video-programmatically --audio <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--audio` | Yes | Source audio file path |
| `--color-preset` | No | `cyan-blue`, `black-red`, `orange-red-yellow`, `black-green`, `lavender-pink-violet`, `magenta-red-violet`, `blue-green`, `black-white`, `yellow-green`, `orange-blue-green`, `lime-cyan`, `magenta-red-blue` (default: `cyan-blue`) |
| `--title-text` | No | Title text overlay — the song title (use `--title-text-file` for values with spaces or shell-special chars) |
| `--background-src-16x9` | No | Background image for 16:9 renders (local path or URL; use `--background-src-16x9-file` for presigned URLs containing `&`) |
| `--background-src-9x16` | No | Background image for 9:16 renders (local path or URL; same `-file` form available) |
| `--bg-effect` | No | `ken_burns`, `scale_pulse`, `none` |
| `--preview-start` | No | Start time in seconds for 30s preview clip (default: `0`) |

**Auto-resolved overlays (you do NOT pass these):**
- The "where to listen" subtitle (Apple Music / Spotify / YouTube Music blocks) is rendered automatically under the visualizer.
- The bottom-corner credit `<performer> • <label>` is composed automatically by `media-commands` from project env vars `MUSIC_PERFORMER_NAME` and `MUSIC_LABEL_NAME`. Both must be set as project credentials, otherwise the command fails fast.

**`--X-file` forms (gh-CLI convention, applies to all text/URL parameters above):**

For any value that contains spaces, commas, ampersands, or other shell-special characters — write the value to a file and pass `--X-file <path>` instead of `--X "<value>"`. This bypasses shell quoting entirely. Inline and `-file` forms are mutually exclusive per option. Example use cases: presigned S3 URLs (have `&` in query params), multi-word titles, lyrics-derived strings.

**Output files (always 6 files):**

| File | Description |
|------|-------------|
| `16x9-full-[UUID].mp4` | Full-length 16:9 video with text and audio |
| `16x9-full-[UUID].jpg` | Screenshot (first frame of 16:9 video) |
| `9x16-loop-[UUID].mp4` | ~4.8s seamless color-cycle loop 9:16 without text/audio (for Spotify Canvas) |
| `9x16-short-[UUID].mp4` | 60s 9:16 video with text and audio (from start of audio) |
| `9x16-short-[UUID].jpg` | Screenshot (first frame of 9:16 short video — color) |
| `9x16-preview-[UUID].mp4` | 30s 9:16 preview clip — `black-white` (monochrome) visualizer + desaturated background (ffmpeg `hue=s=0`) |

Note: The 30s preview always renders with the `black-white` color preset (monochrome) and desaturated (B&W) background, regardless of the `--color-preset` passed. The 9:16 screenshot is taken from the color short video, not the monochrome preview. All passes (full / short / preview) show the same auto-rendered platform blocks under the visualizer and the same auto-composed `performer • label` credit at the bottom.

**Runtime & progress expectations — READ BEFORE RUNNING:**

- **Expected duration**: 10–20 minutes for a typical 3-minute audio (4 render passes × Remotion + FFmpeg encoding). The hard timeout in the CLI is 45 minutes — anything below that is normal.
- **Output directory stays empty for the first ~5 minutes** of each pass. Remotion buffers frames internally and writes the final `.mp4` only when the pass completes. **An empty output dir does NOT mean the process is stuck.**
- **Stderr/stdout may stay quiet for long stretches** between passes — this is normal Remotion behaviour, not a hang.
- **DO NOT poll, restart, kill, or run `ps` in the first 10 minutes.** Just wait. Premature kills create orphaned partial outputs and confuse subsequent runs.
- **Run in the foreground**, never with `&` (background). claude tolerates foreground bash up to 30 minutes without timeout, and foreground gives you the exit code directly. Background processes are notoriously hard to track in this environment (PID-vs-shell-status drift) — avoid them for this command.

**Examples (always single-line — see CLAUDE.md "Single-line bash" rule):**

```bash
# Basic music visualizer — only the song title is passed; performer/label credit
# is composed from MUSIC_PERFORMER_NAME + MUSIC_LABEL_NAME env vars automatically.
media-commands --command create-video-programmatically --audio ./audio.mp3 --color-preset cyan-blue --title-text "My Song"

# Backgrounds via presigned S3 URLs — pass URLs through files to avoid shell escaping
echo 'https://cdn.example.com/bg-wide.jpg?X-Amz-Signature=...&X-Amz-Date=...' > /tmp/bg16-uuid.txt
echo 'https://cdn.example.com/bg-tall.jpg?X-Amz-Signature=...&X-Amz-Date=...' > /tmp/bg9-uuid.txt
media-commands --command create-video-programmatically --audio ./audio.mp3 --color-preset magenta-red-blue --title-text "Ride On" --background-src-16x9-file /tmp/bg16-uuid.txt --background-src-9x16-file /tmp/bg9-uuid.txt --bg-effect ken_burns --preview-start 59
```

---

## Loudness Standards Reference

| Platform | I (LUFS) | TP (dBTP) | LRA (LU) |
|----------|----------|-----------|----------|
| YouTube | -14 | -1 | 11 |
| Broadcast | -23 | -1 | 7 |

## Aspect Ratios

- `16:9` — Horizontal (1920x1080) for YouTube, landscape
- `9:16` — Vertical (1080x1920) for Reels, Shorts, TikTok
- `1:1` — Square (1080x1080) for Instagram Feed

## STRICT: No Auto-Retry

If processing fails — present error to user and offer retry. DO NOT auto-retry without user approval.
