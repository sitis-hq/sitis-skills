---
description: Edit existing images using AI. Use when asked to "edit an image", "modify a picture", "change an image", "add something to image", or "transform a photo".
allowed-tools: Bash(ai-generator:*)
---

## Sending Results to User

WHEN sending generated files to user via `ai-integration send-attachments` (Bash):
- Use `file_url` directly from JSON output (DO NOT download files locally first)
- MCP accepts both local paths AND direct web URLs
- This avoids unnecessary download/upload cycle

Example usage:
```bash
ai-generator --type image --command generate \
  --prompt "..." \
  --image-url "..."
```

Output is always JSON: `{ success, command, data }` or `{ success, command, error: { message, type } }`.
Response contains `data.files[].file_url` - pass these URLs directly to send-message.

## Command

```bash
ai-generator --type image --command generate \
  --prompt "<edit description>" \
  --image-url "<source image URL>"
```

**Edit mode is not a separate model.** The same model does text-to-image without references
and editing with them — passing `--image-url` is what switches the mode. There is no `--model`
value to remember and no `edit` command (`--command` is always `generate`).

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--prompt` | Yes | Edit description (max 5000 chars) |
| `--image-url` | Yes | Reference image URL (repeatable, up to 9) |
| `--size` | No | Aspect ratio (`1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `5:4`, `4:5`, `21:9`) or exact pixels (`2560x1440`). Default: `1:1` |
| `--model` | No | `wan-2.7-image` (default) or `wan-2.7-image-pro` — use `-pro` when facial identity must survive the edit |

There is **no** `--resolution` for images — passing it is rejected. Output size is set by
`--size` alone, and the price is the same whatever size you ask for.

**`--size` is honoured in edit mode** — a square source can be reframed into `16:9` and the
model will fill the widened frame. It does not inherit the source's aspect ratio; if you want
that, pass the source's own dimensions explicitly.

> **Shell-safe values**: every text/URL flag has a parallel `--X-file <path>` form (gh-CLI convention). Use the file form for values containing spaces, commas, ampersands, or other shell-special chars — **mandatory for presigned S3 URLs** (they have `&` in query params and break shell quoting). Write the value to `${WORK_DIR}/{uuid}.txt` then pass `--prompt-file` / `--image-url-file` / etc. For repeatable `--image-url`, the file form expects one URL per line. Inline and `-file` forms are mutually exclusive per option.

## Sizing

Output is capped at **4.19 Mpx (2048×2048)**, and each side is rounded up to a multiple of 16.
An aspect ratio resolves to the largest exact size that fits: `1:1` → 2048×2048,
`16:9` → 2560×1440, `9:16` → 1440×2560, `4:3` → 2304×1728, `3:2` → 2496×1664,
`5:4` → 2240×1792, `21:9` → 3024×1296. Anything over the cap is rejected with the largest
size that fits at that ratio.

## Multiple Reference Images

Use `--image-url` multiple times to pass several images (up to 9). Order matters — refer to
them in the prompt as the first image, the second image, and so on:

```bash
ai-generator --type image --command generate \
  --prompt "Combine the face from the first image with the background from the second" \
  --image-url "https://example.com/avatar.jpg" \
  --image-url "https://example.com/background.jpg"
```

## Examples

```bash
# Add element to image
ai-generator --type image --command generate \
  --prompt "Add a rainbow to the sky" \
  --image-url "https://example.com/landscape.jpg"

# Transform image style
ai-generator --type image --command generate \
  --prompt "Convert to watercolor painting style" \
  --image-url "https://example.com/photo.jpg"

# Reframe a square portrait into a wide shot, preserving identity
ai-generator --type image --command generate \
  --model "wan-2.7-image-pro" \
  --prompt "Reframe into a wide cinematic frame, same man, same face, placed off-center to the right" \
  --size "16:9" \
  --image-url "https://example.com/portrait.jpg"
```

## STRICT: No Auto-Retry

If generation takes too long or fails — DO NOT retry without user approval.
