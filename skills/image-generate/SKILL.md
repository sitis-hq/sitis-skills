---
description: Generate AI images from text prompts. Use when asked to "create an image", "generate a picture", "make artwork", "design a visual", or "create illustration".
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
  --prompt "..."
```

Output is always JSON: `{ success, command, data }` or `{ success, command, error: { message, type } }`.
Response contains `data.files[].file_url` - pass these URLs directly to send-message.

## Command

```bash
ai-generator --type image --command generate \
  --prompt "<description>"
```

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--prompt` | Yes | Image description (max 5000 chars) |
| `--size` | No | Aspect ratio (`1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `5:4`, `4:5`, `21:9`) or exact pixels (`2560x1440`). Default: `1:1` |
| `--model` | No | `wan-2.7-image` (default) or `wan-2.7-image-pro` (higher fidelity, ~2.5x the price) |

There is **no** `--resolution` for images — passing it is rejected. Output size is set by
`--size` alone, and the price is the same whatever size you ask for.

> **Shell-safe values**: `--prompt` has a parallel `--prompt-file <path>` form (gh-CLI convention). Use the file form for prompts containing quotes, dollar signs, backticks, or other shell-special chars. Write the prompt to `${WORK_DIR}/{uuid}.txt` then pass `--prompt-file`. Inline and `-file` forms are mutually exclusive.

## Sizing

Output is capped at **4.19 Mpx (2048×2048)**, and each side is rounded up to a multiple of 16.
An aspect ratio resolves to the largest exact size that fits:

| `--size` | pixels | | `--size` | pixels |
|---|---|---|---|---|
| `1:1` | 2048×2048 | | `3:2` / `2:3` | 2496×1664 / 1664×2496 |
| `16:9` / `9:16` | 2560×1440 / 1440×2560 | | `5:4` / `4:5` | 2240×1792 / 1792×2240 |
| `4:3` / `3:4` | 2304×1728 / 1728×2304 | | `21:9` | 3024×1296 |

Ask for exact pixels when a platform demands them (e.g. a YouTube banner is `2560x1440`).
Anything over the cap is rejected with the largest size that fits at that ratio — pick that
size, do not silently accept a smaller image.

## Examples

```bash
# Basic generation
ai-generator --type image --command generate \
  --prompt "A cyberpunk street scene with neon signs"

# Wide cinematic frame
ai-generator --type image --command generate \
  --prompt "Mountain landscape at sunset" \
  --size "16:9"

# Exact pixel size required by a platform
ai-generator --type image --command generate \
  --prompt "Channel banner artwork, bold central subject, wide empty margins" \
  --size "2560x1440"
```

## STRICT: No Auto-Retry

If generation takes too long or fails — DO NOT retry without user approval.
