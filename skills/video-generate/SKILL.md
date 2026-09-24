---
description: Generate AI videos from text prompts. Use when asked to "create a video", "generate video", "make a clip", "animate", or "create motion content".
allowed-tools: Bash(ai-generator:*)
---

## Sending Results to User

WHEN sending generated files to user via `ai-integration send-attachments` (Bash):
- Use `file_url` directly from JSON output (DO NOT download files locally first)
- MCP accepts both local paths AND direct web URLs
- This avoids unnecessary download/upload cycle

Example usage:
```bash
ai-generator --type video --command generate \
  --prompt "..."
```

Output is always JSON: `{ success, command, data }` or `{ success, command, error: { message, type } }`.
Response contains `data.files[].file_url` - pass these URLs directly to send-message.

## Command

```bash
ai-generator --type video --command generate \
  --prompt "<description>"
```

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--prompt` | Yes | Video description (max 1000 chars) |
| `--size` | No | `16:9` (landscape) or `9:16` (portrait). Default: `16:9` |
| `--resolution` | No | `1080p`, `4k`. Default: `1080p` |
| `--model` | No | `veo3.1-fast` (default) or `veo3.1-quality` (only when explicitly requested) |
| `--image-url` | No | Reference image URL (repeatable, max 3) |
| `--generation-type` | With 2+ images | `frame` (exactly 2 images: start frame + end frame) or `reference` (1-3 images as identity/style references). **REQUIRED with 2+ `--image-url`**, optional with 1 (omitted = image is the first frame), forbidden without images |

### `--generation-type` rules

- 0 images → do NOT pass `--generation-type` (text-to-video)
- 1 image → optional: omit for first-frame mode, or pass `reference` to use the image as identity/style reference
- 2 images → REQUIRED: `frame` (start/end frames) or `reference` (two references)
- 3 images → REQUIRED: `reference` only (`frame` accepts exactly 2)
- `veo3.1-quality` does NOT support `reference` — use `veo3.1-fast` (validation rejects locally)

> **Shell-safe values**: `--prompt` and `--image-url` each have a parallel `--X-file <path>` form (gh-CLI convention). **Mandatory for `--image-url`** when it's a presigned S3 URL — `&` in query params reliably breaks shell quoting at multi-layer escape. For repeatable `--image-url`, the file form expects one URL per line. Write the value to `${WORK_DIR}/{uuid}.txt` then pass `--prompt-file` / `--image-url-file`. Inline and `-file` forms are mutually exclusive per option.

## Examples

```bash
# Basic generation
ai-generator --type video --command generate \
  --prompt "Dolphins jumping in a bright blue ocean"

# Custom size and resolution
ai-generator --type video --command generate \
  --prompt "A sunset timelapse over mountains" \
  --size "16:9" \
  --resolution "1080p"

# Quality mode (only when user explicitly requests)
ai-generator --type video --command generate \
  --prompt "A cat playing with yarn" \
  --model "veo3.1-quality"

# From start/end frames (frame mode — exactly 2 images)
ai-generator --type video --command generate \
  --prompt "Smooth transition between scenes" \
  --generation-type frame \
  --image-url "https://example.com/start.jpg" \
  --image-url "https://example.com/end.jpg"

# From reference images (reference mode — veo3.1-fast only)
ai-generator --type video --command generate \
  --prompt "The character walks through a forest" \
  --generation-type reference \
  --image-url "https://example.com/character.jpg" \
  --image-url "https://example.com/style.jpg"
```


## STRICT: No Auto-Retry

If generation fails or takes too long — present error to user and offer retry. DO NOT auto-retry without user approval.
