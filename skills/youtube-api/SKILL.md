---
description: Upload videos to YouTube, update video metadata after upload, manage channels, and fetch subtitles of any YouTube video as text. Use when asked to "upload video to youtube", "update video metadata", "authenticate youtube", "list youtube channels", "check youtube quota", "configure youtube project", "schedule youtube video", "get youtube subtitles", "transcript of a video", or "summarize a youtube video".
allowed-tools: Bash(youtube-commands:*)
---

Example with JSON output:

```bash
youtube-commands --command upload --project-id <id> --video ./video.mp4 --title "My Video" --json
```

## Commands

### 1. upload

Upload video to YouTube with metadata.

```bash
youtube-commands --command upload --project-id <id> --video <path> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--project-id` | Yes | Project ID for credential isolation |
| `--video` | Yes | Path to video file |
| `--title` | No | Video title (max 100 chars) |
| `--description` | No | Video description (max 5000 chars) |
| `--tags` | No | Comma-separated list of tags |
| `--privacy` | No | `private`, `unlisted`, `public` (default: `private`) |
| `--category` | No | YouTube category ID (1-44) |
| `--thumbnail` | No | Path to custom thumbnail |
| `--playlist` | No | Playlist ID to add video to |
| `--language` | No | Default language code (ISO 639-1) |
| `--embeddable` | No | Allow video to be embedded |
| `--license` | No | `youtube` or `creativeCommon` (default: `youtube`) |
| `--publish-at` | No | Schedule publish date (ISO 8601, e.g. `2026-03-01T15:00:00Z`). Sets privacy to `private` automatically |
| `--force-reauth` | No | Force re-authentication before upload |
| `--verbose` | No | Enable debug logging |
| `--json` | No | JSON output for MCP |

**Examples:**

```bash
# Basic upload
youtube-commands --command upload --project-id <id> --video ./video.mp4 --title "My Video"

# Full metadata upload
youtube-commands --command upload --project-id <id> \
  --video ./video.mp4 \
  --title "My Amazing Video" \
  --description "This is a great video about..." \
  --tags "tutorial,education,youtube" \
  --privacy unlisted \
  --category 27

# JSON output for MCP
youtube-commands --command upload --project-id <id> --video ./video.mp4 --title "My Video" --json

# Scheduled upload (publish later)
youtube-commands --command upload --project-id <id> \
  --video ./video.mp4 \
  --title "Scheduled Video" \
  --publish-at "2026-03-01T15:00:00Z"
```

---

### 2. auth

Initiate OAuth2 authentication flow.

```bash
youtube-commands --command auth --project-id <id> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--project-id` | Yes | Project ID for credential isolation |
| `--verbose` | No | Enable debug logging |
| `--json` | No | JSON output for MCP |

**Examples:**

```bash
# Start authentication
youtube-commands --command auth --project-id <id>

# JSON output
youtube-commands --command auth --project-id <id> --json
```

---

### 3. auth-complete

Complete OAuth2 flow with authorization code.

```bash
youtube-commands --command auth-complete --project-id <id> --code <code> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--project-id` | Yes | Project ID for credential isolation |
| `--code` | Yes | Authorization code from Google |
| `--verbose` | No | Enable debug logging |
| `--json` | No | JSON output for MCP |

**Examples:**

```bash
# Complete authentication
youtube-commands --command auth-complete --project-id <id> --code "4/0AX4XfWh..."

# JSON output
youtube-commands --command auth-complete --project-id <id> --code "4/0AX4XfWh..." --json
```

---

### 4. config

Manage project configuration.

```bash
youtube-commands --command config --project-id <id> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--project-id` | Yes | Project ID for credential isolation |
| `--list` | No | List current configuration |
| `--set-default-privacy` | No | Set default privacy: `private`, `unlisted`, `public` |
| `--set-default-category` | No | Set default category ID (1-44) |
| `--set-default-tags` | No | Set default tags (comma-separated) |
| `--set-default-language` | No | Set default language code (ISO 639-1) |
| `--verbose` | No | Enable debug logging |
| `--json` | No | JSON output for MCP |

**Examples:**

```bash
# List configuration
youtube-commands --command config --project-id <id> --list

# Set default privacy
youtube-commands --command config --project-id <id> --set-default-privacy private

# Set multiple defaults
youtube-commands --command config --project-id <id> \
  --set-default-privacy unlisted \
  --set-default-category 27 \
  --set-default-tags "music,video"

# JSON output
youtube-commands --command config --project-id <id> --list --json
```

---

### 5. channels

List available YouTube channels.

```bash
youtube-commands --command channels --project-id <id> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--project-id` | Yes | Project ID for credential isolation |
| `--verbose` | No | Enable debug logging (includes channel descriptions) |
| `--json` | No | JSON output for MCP |

**Examples:**

```bash
# List channels
youtube-commands --command channels --project-id <id>

# JSON output
youtube-commands --command channels --project-id <id> --json

# Verbose with descriptions
youtube-commands --command channels --project-id <id> --verbose
```

---

### 6. quota

Display API quota information.

```bash
youtube-commands --command quota --project-id <id> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--project-id` | Yes | Project ID for credential isolation |
| `--verbose` | No | Enable debug logging (includes optimization tips) |
| `--json` | No | JSON output for MCP |

**Examples:**

```bash
# Check quota
youtube-commands --command quota --project-id <id>

# JSON output
youtube-commands --command quota --project-id <id> --json

# Verbose with tips
youtube-commands --command quota --project-id <id> --verbose
```

---

### 7. update

Patch metadata of an already-uploaded video. Symmetric to `upload` but mutates an existing video — costs only 51 quota units (vs 1600 for a fresh upload).

```bash
youtube-commands --command update --project-id <id> --video-id <id> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--project-id` | Yes | Project ID for credential isolation |
| `--video-id` | Yes | YouTube video ID (11 chars `[A-Za-z0-9_-]`) |
| `--title` | No | New title (max 100 chars) |
| `--title-file` | No | Read `--title` from file |
| `--description` | No | New description (max 5000 chars; pass `''` to clear) |
| `--description-file` | No | Read `--description` from file (rejected if file is empty) |
| `--tags` | No | New CSV tags (≤500 total chars) |
| `--tags-file` | No | Read tags CSV from file |
| `--privacy` | No | `private`, `unlisted`, `public` |
| `--category` | No | New category ID (1-44) |
| `--thumbnail` | No | Path to new thumbnail (+50 quota units) |
| `--language` | No | New default language (ISO 639-1) |
| `--publish-at` | No | New schedule (ISO 8601 future datetime) |
| `--force-reauth` | No | Force re-authentication before update |
| `--verbose` | No | Debug logging |
| `--json` | No | JSON output for MCP |

At least one updatable field is required (otherwise validation error). Quota cost: 51 units without thumbnail, +50 with thumbnail.

**PUT semantics.** YouTube's update endpoint deletes any field not specified in the requested `part`. The CLI fetches current state first and merges only the fields you change — your other fields stay intact.

**Privacy/`publishAt` auto-fix (bidirectional, warns to stderr):**

- `--privacy public` while a `publishAt` exists → clears `publishAt` (immediate publish).
- `--publish-at` while target privacy is not `private` → switches privacy to `private`.

**Examples:**

```bash
# Patch description only — title/tags/privacy preserved
youtube-commands --command update --project-id <id> --video-id dQw4w9WgXcQ --description-file ./new-desc.md

# Publish a scheduled video immediately
youtube-commands --command update --project-id <id> --video-id dQw4w9WgXcQ --privacy public

# Replace thumbnail post-upload
youtube-commands --command update --project-id <id> --video-id dQw4w9WgXcQ --thumbnail ./cover.png

# Reschedule a private video
youtube-commands --command update --project-id <id> --video-id dQw4w9WgXcQ --publish-at "2026-06-01T15:00:00Z"

# JSON output for MCP
youtube-commands --command update --project-id <id> --video-id dQw4w9WgXcQ --title "New Title" --json
```

---

### 7. subtitles

Fetch subtitles of ANY YouTube video (not only your own) as plain text — use this to summarize or
analyze a video's content.

```bash
youtube-commands --command subtitles --video <id-or-url> [options]
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--video` | Yes | Video ID or full URL |
| `--lang` | No | Comma-separated languages by preference (default: `ru,en`); `all` = every real track, never auto-translations |
| `--format` | No | `text` — transcript without timecodes (default) / `srt` — raw subtitle file |
| `--out` | No | Write to file instead of stdout |
| `--json` | No | Machine-readable result |

**This command is different from every other one here:**

- **No `--project-id`, no OAuth, no API quota.** It does not touch the YouTube Data API at all —
  extraction goes through `yt-dlp`. Do not ask the user for credentials for it.
- Manual (author-uploaded) subtitles are preferred; when they are missing, auto-generated ones are
  used automatically. You do not need to choose.
- Default output is a de-timecoded, de-duplicated transcript — ready to be read or summarized.
  Auto-generated tracks repeat lines heavily; that noise is already stripped.
- **If none of the requested languages exist, the video's original track is returned instead** —
  an empty answer helps nobody. Always read `language` in the result to know what you actually got.
- `--lang all` means "every track the video really has". It never pulls YouTube's ~200
  auto-translations: requesting those trips rate limiting (HTTP 429) and fails the whole call.

```bash
# transcript straight to stdout — read it and answer the user's question about the video
youtube-commands --command subtitles --video dQw4w9WgXcQ

# a specific language, into a file
youtube-commands --command subtitles --video "https://www.youtube.com/watch?v=dQw4w9WgXcQ" \
  --lang en --out /tmp/transcript.txt
```

If a video has no subtitles in the requested languages the command fails with
`SUBTITLES_NOT_AVAILABLE` — try `--lang all` to see what exists, and tell the user if there is
nothing at all. Do not retry blindly.

---

## YouTube Categories Reference

| ID | Category | ID | Category |
|----|----------|----|---------| 
| 1 | Film & Animation | 17 | Sports |
| 2 | Autos & Vehicles | 19 | Travel & Events |
| 10 | Music | 20 | Gaming |
| 15 | Pets & Animals | 22 | People & Blogs |
| 23 | Comedy | 24 | Entertainment |
| 25 | News & Politics | 26 | Howto & Style |
| 27 | Education | 28 | Science & Technology |

## Setup Requirements

Before using youtube-commands, you need:

1. **Google Cloud Project** with YouTube Data API v3 enabled
2. **OAuth2 Client Secret** downloaded from Google Cloud Console
3. **Client secret file** placed at: `~/.config/youtube-uploader/{project-id}/client_secret.json`

## Authentication Flow

1. Run `youtube-commands --command auth --project-id <id>`
2. Open the provided URL in browser
3. Complete Google authorization
4. Copy the authorization code
5. Run `youtube-commands --command auth-complete --project-id <id> --code <code>`

## STRICT: No Auto-Retry

If upload or authentication fails — present error to user and offer retry. DO NOT auto-retry without user approval.
