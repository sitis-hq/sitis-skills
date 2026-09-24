---
description: Optimize YouTube video metadata for maximum discoverability and CTR. Use when asked to "optimize youtube video", "create video title", "write video description", "add tags", "optimize metadata", or "improve youtube seo".
---

# Requirements Document

## Introduction

This document defines requirements for the "YouTube Music Metadata Optimization" skill - a comprehensive system for maximizing video discoverability, CTR, and algorithmic performance through optimized titles, descriptions, tags, and publishing strategy.

Scientific foundation: YouTube tests videos in 4 waves over the first 48 hours. Poor metadata = low CTR in wave 1 = algorithm stops testing early. Optimized titles increase CTR by 15-30%. First 150 characters of description are critical as they appear before "Show more" button. Tags have minimal impact (YouTube's MuLan AI relies 80% on video content analysis).

## Glossary

- **CTR**: Click-Through Rate - percentage of impressions that result in clicks
- **MuLan AI**: YouTube's multimodal AI that analyzes video content for classification
- **OAC**: Official Artist Channel - verified channel with music note badge and YouTube Music integration
- **Content ID**: YouTube's system for identifying and managing copyrighted content
- **Smart Link**: Aggregator link (Linkfire, Feature.fm) that redirects users to their preferred streaming platform
- **Retention**: Percentage of video watched by viewers; 50%+ is healthy
- **First 48 Hours**: Critical window when YouTube tests video across 4 audience waves
- **Wave Testing**: YouTube's progressive audience expansion: subscribers → recent viewers → topic-interested → viral potential

## Requirements

### Requirement 1: Title Optimization

**User Story:** As a music artist, I want optimized video titles, so that my videos maximize CTR and algorithmic distribution.

#### Acceptance Criteria - Structure

1. THE title SHALL follow format: `Performer Name – Song Title (Content Type Marker)`
2. THE title length SHALL be 41-60 characters (7-9 words) for optimal performance
3. THE performer name and song title SHALL appear first (YouTube truncates after 60-70 chars)
4. THE title SHALL include content type marker: `(Official Music Video)`, `(Lyric Video)`, or `(Official Audio)`
5. WHEN collaboration THEN use format: `Performer – Song Title (feat. Guest) (Official Video)`
6. WHEN remix THEN use format: `Performer – Song Title (Producer Remix)`
7. WHEN live performance THEN use format: `Performer – Song Title (Live at Venue)`

#### Acceptance Criteria - Restrictions

1. THE title SHALL NOT use ALL CAPS (appears as spam)
2. THE title SHALL NOT include emojis (unprofessional for music content)
3. THE title SHALL NOT use clickbait language
4. THE title SHALL be readable at 168×94 pixels (mobile preview size)
5. THE System SHALL NOT change title immediately after publish (confuses algorithm)

### Requirement 2: Description Optimization

**User Story:** As a music artist, I want optimized video descriptions, so that my videos rank for relevant keywords and drive streaming platform conversions.

#### Acceptance Criteria - Structure

1. THE description length SHALL be 300-500 words optimal
2. THE first 150 characters SHALL include streaming platform link or hook phrase (visible before "Show more")
3. THE description SHALL follow structure:
   - Streaming platform smart-link
   - Memorable lyric or hook quote
   - Video title with performer name
   - 2-3 sentences about song (creation story, mood, meaning)
   - Platform links section (Spotify, Apple Music, YouTube Music)
   - Social media links section
   - Credits section (songwriter, producer, director)
   - 3-5 hashtags

#### Acceptance Criteria - Smart Links

1. THE description SHALL use smart-link aggregators (Linkfire, Feature.fm) for streaming platforms
2. THE smart-link SHALL appear in first 150 characters
3. THE System SHALL expect 25-40% higher conversion vs single-platform links

#### Acceptance Criteria - Lyrics

1. WHEN original music THEN MAY include lyrics for long-tail keyword discovery
2. WHEN cover song THEN SHALL NOT include lyrics (separate copyright)
3. WHEN explicit language THEN MAY include only chorus or key phrases
4. THE lyrics inclusion SHALL improve voice search compatibility

#### Acceptance Criteria - Restrictions

1. THE description SHALL NOT include "Out Now" or year references (becomes outdated)
2. THE description SHALL NOT include 60+ hashtags (YouTube ignores all)
3. THE description SHALL NOT be misleading (algorithm penalizes high CTR + low retention)
4. THE description SHALL NOT be duplicated across videos (signals low effort)


### Requirement 3: Tags Strategy

**User Story:** As a music artist, I want appropriate tags, so that my videos catch misspellings and help new channels with limited data.

#### Acceptance Criteria - Tag Selection

1. THE System SHALL add 5-10 tags maximum
2. THE tags SHALL include:
   - Performer name (exact spelling)
   - Song title
   - "official music video"
   - Primary genre
   - Mood/vibe tags ("chill music", "workout songs")
   - Album name (if applicable)
   - Related performer (only if genuinely similar style)

#### Acceptance Criteria - Genre-Specific Tags

1. WHEN Pop THEN use: `Pop Music, [Performer], [Song], Official Music Video, Pop Song`
2. WHEN Hip-Hop THEN use: `Hip-Hop, Rap Music, [Performer], [Song], Official Music Video, Rap Song`
3. WHEN Electronic/EDM THEN use: `Electronic Music, EDM, [Performer], [Song], Official Music Video, Dance Music`
4. WHEN Lo-Fi/Chill THEN use: `Lo-Fi Music, Chill Music, [Performer], [Song], Official Music Video, Relaxing Music`

#### Acceptance Criteria - Restrictions

1. THE tags SHALL NOT include competitor performer names (violates policy, may remove video)
2. THE tags SHALL NOT exceed 50 tags (YouTube ignores excess)
3. THE tags SHALL NOT be misleading (algorithm penalizes)
4. THE tags SHALL NOT include hashtags (use description instead)

### Requirement 4: Hashtags in Description

**User Story:** As a music artist, I want optimal hashtags, so that my videos appear in hashtag searches.

#### Acceptance Criteria

1. THE description SHALL include 3-5 hashtags maximum
2. THE first 3 hashtags SHALL display as clickable links above title
3. THE hashtags SHALL follow formula: `#PerformerName #SongTitle #Genre`
4. THE System SHALL NOT add 60+ hashtags (YouTube ignores all)

### Requirement 5: Publishing Strategy

**User Story:** As a music artist, I want optimal publishing workflow, so that my videos maximize first 48-hour performance.

#### Acceptance Criteria - Upload Workflow

1. THE video SHALL be uploaded as Private (not Unlisted or Public)
2. THE System SHALL add all optimized metadata before publishing
3. THE System SHALL upload custom thumbnail before publishing
4. THE System SHALL wait for HD processing + copyright check before publishing
5. THE video SHALL be scheduled or switched to Public at optimal time

#### Acceptance Criteria - Timing

1. THE optimal publish day SHALL be Friday (+18% initial engagement, industry standard)
2. THE alternative publish days SHALL be Tuesday-Wednesday (less competition)
3. THE optimal publish time SHALL be 14:00-16:00 or 18:00-21:00 (local audience time)
4. THE upload SHALL occur 1-2 hours before peak time (allows processing)

#### Acceptance Criteria - Private vs Unlisted

1. THE System SHALL use Private (algorithm doesn't start until Public)
2. THE System SHALL NOT use Unlisted for pre-publish (unclear if algorithm begins)

### Requirement 6: Metadata Priority

**User Story:** As a music artist, I want to understand metadata priority, so that I focus effort on highest-impact elements.

#### Acceptance Criteria

1. THE title SHALL be treated as Critical priority (determines initial distribution)
2. THE thumbnail SHALL be treated as Critical priority (70% of CTR driver)
3. THE first 30 seconds of video SHALL be treated as Critical priority (retention determines expansion)
4. THE description first 150 chars SHALL be treated as High priority (streaming links + keywords)
5. THE full description SHALL be treated as High priority (long-tail keywords + lyrics)
6. THE tags SHALL be treated as Low priority (minimal algorithm impact)
7. THE hashtags SHALL be treated as Low priority (minimal algorithm impact)

### Requirement 7: Music-Specific Metrics

**User Story:** As a music artist, I want to understand target metrics, so that I can evaluate video performance.

#### Acceptance Criteria - Target Performance

1. THE target CTR SHALL be 4%+ (healthy)
2. THE target retention SHALL be 50%+ (completion rate)
3. THE completion rate (full watch) SHALL be strongest algorithm signal
4. THE repeat views SHALL indicate quality (algorithm boost)

#### Acceptance Criteria - Shorts Strategy

1. THE Shorts SHALL provide 3x audience reach vs long-form
2. THE Shorts SHALL drive 60%+ of new subscribers
3. THE Shorts SHALL use 15-60 second clips from music video
4. THE optimal Shorts watch time SHALL be 100% (viewers watch entire short)

### Requirement 8: Shorts Metadata Optimization

**User Story:** As a music artist, I want fully optimized Shorts metadata, so that my short-form content maximizes discovery, completion rate, and drives viewers to full releases.

#### Acceptance Criteria - Algorithm Signals

1. THE completion rate (% of Short watched) SHALL be treated as the dominant ranking signal
2. THE replay rate SHALL be treated as the second strongest signal (loops = quality indicator)
3. THE swipe-away rate SHALL be treated as the strongest negative signal (viewer leaves before finishing)
4. THE first 1-2 seconds SHALL hook the viewer (determines swipe-away vs watch)
5. THE Shorts algorithm and long-form algorithm NOW share a unified recommendation system — Shorts performance feeds long-form discovery and vice versa
6. THE system SHALL prioritize loop-friendly content (seamless end-to-start transition) to boost replay rate

#### Acceptance Criteria - Title

1. THE Shorts title SHALL be 40-50 characters maximum (less screen real estate than long-form)
2. THE title SHALL lead with a hook or emotion, not SEO keywords (Shorts discovery is algorithm-driven, not search-driven)
3. THE title MAY include 1-2 emojis (emojis boost Shorts views, unlike long-form)
4. THE title SHALL include performer name and song reference
5. THE title SHALL NOT be generic ("Check this out", "Wait for it") — specificity wins
6. THE title SHALL NOT use ALL CAPS
7. WHEN teaser for full video THEN title SHALL create curiosity gap tied to the song

#### Acceptance Criteria - Title Formulas

1. WHEN hook/chorus clip THEN use: `[Performer] – [Song Title]`
2. WHEN behind-the-scenes THEN use: `How [Performer] recorded [Song Title] 🎙️`
3. WHEN lyric highlight THEN use: `"[Memorable Lyric Line]" — [Performer]`
4. WHEN visual teaser THEN use: `[Performer] – [Song Title] drops [date] 👀`
5. WHEN reaction/challenge THEN use: `[Hook phrase] [Performer] – [Song Title]`
6. WHEN live performance clip THEN use: `[Performer] – [Song Title] LIVE 🎤`

#### Acceptance Criteria - Description

1. THE Shorts description SHALL be 2-3 lines maximum (most viewers never expand it)
2. THE first line SHALL reference the full video by title or mention premiere date (links in Shorts descriptions are NOT clickable — use text like "Full MV on my channel" or "Out Friday" instead of URLs)
3. THE first line SHALL NOT contain a URL (not clickable, wastes prime real estate)
4. THE description SHALL include 3-5 hashtags
5. THE hashtag `#Shorts` is NO LONGER required (YouTube auto-detects vertical format)
6. THE hashtags SHALL include: `#[PerformerName]`, `#[SongTitle]`, `#[Genre]`, and 1-2 discovery hashtags (`#NewMusic`, `#MusicVideo`, etc.)

#### Acceptance Criteria - Audio & Music Integration

1. WHEN using original music THEN attach the track via YouTube's music library / Sound page (boosts discovery through the audio page)
2. THE audio page aggregates all Shorts using that track — this creates a discovery flywheel
3. WHEN the track is trending on Shorts THEN create additional Shorts with the same audio to ride the wave
4. THE system SHALL recommend releasing the track to YouTube Music / Content ID before posting Shorts so the audio page exists

#### Acceptance Criteria - Content Formats for Music

1. THE system SHALL recommend these Shorts formats ranked by typical performance:
   - **Hook/Chorus clip** — strongest 15-30 sec segment, loop-friendly, highest completion
   - **Lyric highlight** — text overlay of key lyric over visual, shareable
   - **Behind-the-scenes** — studio recording, mixing, creative process, builds artist connection
   - **Visual teaser** — cinematic snippet from upcoming MV, curiosity-driven
   - **Before/After** — raw demo vs final production, satisfying transformation
   - **Live performance clip** — raw energy, authenticity signal
   - **Fan reaction / duet bait** — content designed to be stitched or duetted
2. EACH Short SHALL have a clear single purpose (don't mix formats)

#### Acceptance Criteria - Technical Specs

1. THE Short SHALL be vertical 9:16 aspect ratio (1080×1920 pixels)
2. THE Short SHALL be 15-60 seconds (under 30 seconds optimal for completion rate)
3. TEXT overlays SHALL stay within the center safe zone (avoid top 15% and bottom 25% where UI elements overlay)
4. THE Short SHALL NOT have black bars (letterboxing kills engagement)
5. THE Short SHALL start with motion/action in frame 1 (static opening = swipe-away)

#### Acceptance Criteria - Publishing Strategy

1. THE system SHALL recommend 3-5 Shorts per week for music channels
2. THE Shorts SHALL be spaced throughout the week (not batch-published)
3. THE optimal posting times for Shorts are less critical than long-form (Shorts shelf has longer discovery window)
4. THE system SHALL recommend posting the first Short 1-3 days BEFORE the full music video release (builds anticipation)
5. THE system SHALL recommend posting 2-3 follow-up Shorts in the week AFTER release (sustains momentum)
6. THE system SHALL recommend a Shorts release cadence around a single:
   - Day -3: Teaser Short (visual snippet, curiosity gap)
   - Day -1: Hook/chorus Short (audio reveal)
   - Day 0: Full MV release (long-form)
   - Day +1: Behind-the-scenes Short
   - Day +3: Lyric highlight Short
   - Day +7: Live/acoustic Short or fan reaction

#### Acceptance Criteria - Cross-Promotion

1. EACH Short description SHALL reference the full music video by title (NOT a URL — links are not clickable in Shorts)
2. THE full music video description SHALL link to the best-performing Short (long-form descriptions DO support clickable links)
3. THE system SHALL recommend adding a verbal CTA in the Short ("Full video on my channel")
4. THE system SHALL NOT rely on end screens (not available on Shorts)
5. THE system SHALL recommend pinning a comment with the full video link on Shorts (comments DO support clickable links, if comments are enabled)
6. WHEN promoting an upcoming release THEN use premiere date in the Short title/description (e.g., "drops Friday") instead of a link

#### Acceptance Criteria - Restrictions

1. THE Short SHALL NOT use misleading thumbnails or titles (algorithmic penalty)
2. THE Short SHALL NOT reuse the exact same clip across multiple Shorts (diminishing returns, audience fatigue)
3. THE Short SHALL NOT start with a static image or slow fade-in (instant swipe-away)
4. THE Short SHALL NOT include long text blocks that require pausing to read
5. THE Short SHALL NOT use copyrighted audio from other artists without clearance (Content ID claim removes monetization)

### Requirement 9: Content ID & Official Artist Channel

**User Story:** As a music artist, I want to understand Content ID and OAC, so that I can protect and monetize my content.

#### Acceptance Criteria - Content ID

1. THE Content ID SHALL protect original music from unauthorized use
2. THE Content ID SHALL monetize fan covers and UGC
3. THE Content ID SHALL NOT affect SEO or recommendations
4. THE claimed videos SHALL rank normally

#### Acceptance Criteria - Official Artist Channel

1. THE OAC requirements SHALL be: 1+ official release via approved distributor, 15-50 minimum subscribers, policy compliance
2. THE OAC benefits SHALL include: music note badge, "Releases" tab with auto-generated discography, YouTube Music integration, ticket/merch integration

### Requirement 10: Error Handling

**User Story:** As a user, I want clear feedback when optimization fails.

#### Acceptance Criteria

1. IF optimization fails THEN present results to user with description
2. THE System SHALL NOT auto-retry without explicit user approval
3. WHEN error occurs THEN offer refinement option to user


---

## Prompt Templates

### Title Templates

**Standard Music Video:**
```
[Performer Name] – [Song Title] (Official Music Video)
```

**Collaboration:**
```
[Performer Name] – [Song Title] (feat. [Guest]) (Official Video)
```

**Remix:**
```
[Performer Name] – [Song Title] ([Producer] Remix)
```

**Live Performance:**
```
[Performer Name] – [Song Title] (Live at [Venue])
```

**Lyric Video:**
```
[Performer Name] – [Song Title] (Official Lyric Video)
```

**Audio Only:**
```
[Performer Name] – [Song Title] (Official Audio)
```

### Description Template

```
♫ Listen on all platforms:
[Smart-link URL]

"[Memorable lyric or hook from song]"

[Performer Name] – "[Song Title]" (Official Music Video)

[2-3 sentences about the song: creation story, mood, meaning. Naturally include genre and related performers]

📍 LISTEN:
Spotify: [link]
Apple Music: [link]
YouTube Music: [link]

👤 FOLLOW:
Instagram: [link]
TikTok: [link]

🎬 CREDITS:
Songwriter: [name]
Producer: [name]
Director: [name]

#[PerformerName] #[SongTitle] #[Genre]
```

---

## Priority Reference Table

| Element | Priority | Impact |
|---------|----------|--------|
| Title | 🔴 Critical | Determines initial distribution |
| Thumbnail | 🔴 Critical | 70% of CTR driver |
| First 30 seconds | 🔴 Critical | Retention determines expansion |
| Description (first 150 chars) | 🟠 High | Streaming links + keywords |
| Full description | 🟠 High | Long-tail keywords + lyrics |
| Tags | 🟡 Low | Minimal algorithm impact |
| Hashtags | 🟡 Low | Minimal algorithm impact |

---

## Target Metrics Reference

| Metric | Target | Notes |
|--------|--------|-------|
| CTR | 4%+ | Healthy performance |
| Retention | 50%+ | Completion rate |
| Full watch | Maximum | Strongest algorithm signal |
| Repeat views | High | Indicates quality |

---

## Publishing Timing Reference

| Day | Performance | Notes |
|-----|-------------|-------|
| Friday | +18% engagement | Industry standard |
| Tuesday-Wednesday | Good | Less competition |
| Weekend | Variable | Depends on audience |

| Time (Local) | Performance |
|--------------|-------------|
| 14:00-16:00 | Optimal |
| 18:00-21:00 | Optimal |
| Upload | 1-2 hours before peak |

---

## Common Mistakes Checklist

| Mistake | Impact |
|---------|--------|
| Publishing without optimized metadata | Wastes first 48 hours |
| Changing title/description immediately after publish | Confuses algorithm |
| Using Unlisted for 24-48 hours | Unclear if algorithm starts |
| Misleading title/thumbnail | High CTR + low retention = penalty |
| Ignoring first 150 characters of description | Most visible content ignored |
| Adding 50+ tags | YouTube ignores excess |
| Publishing at random times | Misses peak audience |

---

## Shorts Algorithm Signals Reference

| Signal | Weight | Direction |
|--------|--------|-----------|
| Completion rate | 🔴 Dominant | Higher = more distribution |
| Replay / loop rate | 🔴 Very High | Loops = quality signal |
| Swipe-away rate | 🔴 Very High | Strongest negative signal |
| Shares | 🟠 High | Viral potential indicator |
| Likes | 🟠 High | Engagement signal |
| Comments | 🟡 Medium | Engagement signal |
| Subscribe after watching | 🟡 Medium | Channel quality signal |
| Audio page engagement | 🟡 Medium | Discovery flywheel for music |

---

## Shorts Content Format Performance Reference

| Format | Completion Rate | Replay Potential | Best For |
|--------|----------------|------------------|----------|
| Hook/Chorus clip | Very High | Very High (loop-friendly) | Release day, discovery |
| Lyric highlight | High | Medium | Shareability, fan engagement |
| Behind-the-scenes | Medium-High | Low | Artist connection, pre-release |
| Visual teaser | Medium | Low | Pre-release hype |
| Before/After (demo→final) | High | High | Satisfying transformation |
| Live performance | Medium-High | Medium | Authenticity, post-release |
| Fan reaction / duet bait | Variable | Low | Community building |

---

## Shorts Release Cadence Template

| Day | Short Type | Goal |
|-----|-----------|------|
| -3 | Visual teaser | Build curiosity |
| -1 | Hook/chorus clip | Reveal the sound |
| 0 | Full MV release (long-form) | Main event |
| +1 | Behind-the-scenes | Sustain interest |
| +3 | Lyric highlight | Shareability wave |
| +7 | Live/acoustic or fan reaction | Long-tail engagement |

---

## Shorts Safe Zone Reference

```
┌──────────────────────┐
│   ⚠️ TOP 15%         │ ← Channel name, search bar overlay
│   (avoid text here)  │
│                      │
│  ┌──────────────┐    │
│  │              │    │
│  │  ✅ SAFE     │    │
│  │    ZONE      │    │
│  │              │    │
│  └──────────────┘    │
│                      │
│   ⚠️ BOTTOM 25%      │ ← Title, description, like/comment/share buttons
│   (avoid text here)  │
└──────────────────────┘
```

---

## Shorts Title Templates for Music

| Format | Template | Example |
|--------|----------|---------|
| Hook clip | `[Performer] – [Song]` | AURORA – Cure For Me |
| BTS | `How [Performer] recorded [Song] 🎙️` | How Billie recorded LUNCH 🎙️ |
| Lyric | `"[Lyric Line]" — [Performer]` | "Running up that hill" — Kate Bush |
| Teaser | `[Performer] – [Song] drops Friday 👀` | Dua Lipa – Illusion drops Friday 👀 |
| Live | `[Performer] – [Song] LIVE 🎤` | Hozier – Too Sweet LIVE 🎤 |
| Challenge | `Can you sing this? [Performer] – [Song]` | Can you sing this? SZA – Saturn |
