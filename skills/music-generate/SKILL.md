---
description: Generate AI music tracks with vocals or instrumental. Use when asked to "create music", "generate a song", "make a track", "compose music", or "create audio".
allowed-tools: Bash(ai-generator:*)
---

## Sending Results to User

WHEN sending generated files to user via `ai-integration send-attachments` (Bash):
- Use `audio_url` directly from JSON output (DO NOT download files locally first)
- MCP accepts both local paths AND direct web URLs
- This avoids unnecessary download/upload cycle

Example usage:
```bash
ai-generator --type music --command generate \
  --prompt "..." --style "..." --title "..."
```

Output is always JSON: `{ success, command, data }` or `{ success, command, error: { message, type } }`.
Response contains `data.files[].audio_url` - pass these URLs directly to send-message.

## Command

```bash
ai-generator --type music --command generate \
  --prompt "<lyrics or description>" \
  --style "<genre, mood, instruments>" \
  --title "<track title>"
```

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--prompt` | Yes | Lyrics or description (max 5000 chars) |
| `--style` | Yes* | Genre, mood, instruments. *Optional if `MUSIC_STYLE` env var set |
| `--title` | Yes | Track title (max 80 chars) |
| `--instrumental` | No | Generate without vocals |
| `--vocal-gender` | No | `m` (male) or `f` (female), default: `m` |
| `--negative-tags` | No | Styles, moods or instruments to keep OUT of the track, comma-separated |
| `--style-weight` | No | How literally to follow `--style`: `0`–`1`, max 2 decimals |
| `--weirdness-constraint` | No | Creative deviation: `0`–`1`, max 2 decimals (higher = more experimental) |
| `--model-version` | No | Model version: `V4`, `V4_5`, `V4_5ALL`, `V4_5PLUS`, `V5`, `V5_5`. Default `V4_5PLUS` — do NOT change it unless the user asks, a different version changes the sound of the track |

> **Model character limits**: `V4` caps `--prompt` at 3000 and `--style` at 200 chars; every later version allows 5000 / 1000.

> **Shell-safe values**: `--prompt`, `--style`, `--title` each have a parallel `--X-file <path>` form (gh-CLI convention). **Mandatory for `--prompt`** when passing full lyrics — multi-line text with apostrophes/quotes/dollar signs reliably breaks shell quoting at multi-layer escape. Write the value to `${WORK_DIR}/{uuid}.txt` then pass `--prompt-file` / `--style-file` / `--title-file`. Inline and `-file` forms are mutually exclusive per option.

## Examples

```bash
# Basic song
ai-generator --type music --command generate \
  --prompt "Soulful jazz ballad about lost love" \
  --style "jazz, ballad, saxophone" \
  --title "Midnight Blues"

# Instrumental
ai-generator --type music --command generate \
  --prompt "Epic orchestral piece" \
  --style "orchestral, cinematic" \
  --title "Heroes March" \
  --instrumental

# Female vocals
ai-generator --type music --command generate \
  --prompt "Pop song about summer" \
  --style "pop, upbeat" \
  --title "Summer Days" \
  --vocal-gender f

# Excluding unwanted styles
ai-generator --type music --command generate \
  --prompt "Acoustic ballad about the sea" \
  --style "folk, acoustic guitar, warm" \
  --title "Tide" \
  --negative-tags "Heavy Metal, Upbeat Drums"

# Tight adherence to style, little experimentation
ai-generator --type music --command generate \
  --prompt "Hypnotic techno with a hollow bassline" \
  --style "techno, minimal, hypnotic" \
  --title "Hollow" \
  --style-weight 0.8 \
  --weirdness-constraint 0.3
```


## STRICT: No Auto-Retry

If generation fails or takes too long — present error to user and offer retry. DO NOT auto-retry without user approval.
