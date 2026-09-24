---
description: Remix/cover existing audio tracks into new styles while preserving the original melody. Use when asked to "remix a track", "cover a song", "transform audio", "make a cover version", or "restyle music".
allowed-tools: Bash(ai-generator:*)
---

## Sending Results to User

WHEN sending generated files to user via `ai-integration send-attachments` (Bash):
- Use `audio_url` directly from JSON output (DO NOT download files locally first)
- MCP accepts both local paths AND direct web URLs
- This avoids unnecessary download/upload cycle

Example usage:
```bash
ai-generator --type music --command generate-remix \
  --upload-url "<source audio url>" \
  --prompt "..." --style "..." --title "..."
```

Output is always JSON: `{ success, command, data }` or `{ success, command, error: { message, type } }`.
Response contains `data.files[].audio_url` - pass these URLs directly to send-message.

## Command

```bash
ai-generator --type music --command generate-remix \
  --upload-url "<source audio URL>" \
  --prompt "<lyrics or description>" \
  --style "<genre, mood, instruments>" \
  --title "<track title>"
```

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--upload-url` | Yes | Publicly accessible URL of source audio (max 8 min) |
| `--prompt` | Yes | Lyrics or transformation description (max 5000 chars) |
| `--style` | Yes | Genre, mood, instruments (max 1000 chars) |
| `--title` | Yes | Track title (max 80 chars) |
| `--instrumental` | No | Generate without vocals |
| `--vocal-gender` | No | `m` (male) or `f` (female), default: `m` |
| `--negative-tags` | No | Styles, moods or instruments to keep OUT of the track, comma-separated |
| `--performer-id` | No | Performer ID for consistent style |
| `--style-weight` | No | How literally to follow `--style`: `0`–`1`, max 2 decimals |
| `--weirdness-constraint` | No | Creative deviation: `0`–`1`, max 2 decimals (higher = more experimental) |
| `--model-version` | No | Model version: `V4`, `V4_5`, `V4_5ALL`, `V4_5PLUS`, `V5`, `V5_5`. Default `V4_5PLUS` — do NOT change it unless the user asks, a different version changes the sound of the track |

> **Model character limits**: `V4` caps `--prompt` at 3000 and `--style` at 200 chars; every later version allows 5000 / 1000.

> **Shell-safe values**: `--upload-url`, `--prompt`, `--style`, `--title`, `--negative-tags` each have a parallel `--X-file <path>` form (gh-CLI convention). **Mandatory for `--upload-url`** when it's a presigned S3 URL — `&` in query params reliably breaks shell quoting at multi-layer escape. Also mandatory for `--prompt` when passing full lyrics. Write the value to `${WORK_DIR}/{uuid}.txt` then pass `--upload-url-file` / `--prompt-file` / etc. Inline and `-file` forms are mutually exclusive per option.

## Examples

```bash
# Basic remix
ai-generator --type music --command generate-remix \
  --upload-url "https://example.com/audio/track.mp3" \
  --prompt "Transform into an upbeat electronic dance version" \
  --style "EDM, Electronic, Upbeat" \
  --title "Dance Remix"

# Instrumental remix with exclusions
ai-generator --type music --command generate-remix \
  --upload-url "https://example.com/audio/track.mp3" \
  --prompt "Epic orchestral transformation" \
  --style "Orchestral, Cinematic" \
  --title "Epic Orchestra Version" \
  --instrumental \
  --negative-tags "Slow, Sad"

# Female vocal cover
ai-generator --type music --command generate-remix \
  --upload-url "https://example.com/audio/track.mp3" \
  --prompt "Smooth jazz rendition with saxophone" \
  --style "jazz, smooth, saxophone" \
  --title "Jazz Cover" \
  --vocal-gender f

# Tight adherence to style, little experimentation
ai-generator --type music --command generate-remix \
  --upload-url "https://example.com/audio/track.mp3" \
  --prompt "Hypnotic techno rework" \
  --style "techno, minimal, hypnotic" \
  --title "Hollow Rework" \
  --style-weight 0.8 \
  --weirdness-constraint 0.3
```

## STRICT: No Auto-Retry

If generation fails or takes too long — present error to user and offer retry. DO NOT auto-retry without user approval.
