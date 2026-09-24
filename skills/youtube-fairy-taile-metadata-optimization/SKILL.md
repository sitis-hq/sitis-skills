---
description: Optimize YouTube metadata for bilingual children's fairy tale channels (Russian + English). Use when asked to "optimize video metadata", "write YouTube title", "create video description", "generate tags for fairy tale", "prepare metadata for kids video", or "optimize fairy tale upload".
---

# Requirements Document

## Introduction

This document defines requirements for the "YouTube Fairy Tale Metadata Optimization" skill — a metadata generation system for bilingual (Russian/English) children's animated fairy tale channels targeting preschoolers (ages 3–6). The skill enables creation of algorithm-optimized titles, descriptions, tags, and thumbnail briefs for Made for Kids content.

Scientific foundation: Made for Kids content disables personalized recommendations, comments, end screens, and notifications under COPPA. This makes the title-thumbnail combination the single most important factor driving clicks and algorithmic promotion. Front-loading primary keywords improves YouTube search rankings by up to 20%. Captioned videos earn 7.32% more views. 74% of Shorts views come from non-subscribers. Channels using both Shorts and long-form grow 41% faster.

## Glossary

- **Made for Kids**: YouTube designation required for content targeting children under 13, disabling personalization and engagement features
- **COPPA**: Children's Online Privacy Protection Act — US law requiring Made for Kids designation for child-directed content
- **CTR**: Click-Through Rate — percentage of impressions that result in clicks
- **MLA**: Multi-Language Audio — YouTube feature allowing dubbed audio tracks on a single video
- **Front-loading**: Placing the most important keyword at the beginning of a title
- **LSI Keywords**: Latent Semantic Indexing keywords — semantically related terms that reinforce topic relevance
- **RPM**: Revenue Per Mille — earnings per 1,000 views
- **Session Time**: Total continuous watch time a viewer spends on YouTube after clicking a video
- **Compilation**: Long-form video (30–60+ min) combining multiple individual stories
- **Series Playlist**: YouTube playlist type that signals intended sequential viewing order

## Requirements

### Requirement 1: Channel Architecture

**User Story:** As a bilingual content creator, I want separate Russian and English channels with proper configuration, so that the algorithm builds clear audience profiles for each language.

#### Acceptance Criteria

1. THE system SHALL recommend two separate channels — one Russian, one English
2. THE Russian channel name SHALL be in Russian (e.g., "Волшебные Сказки — Мультфильмы для Детей")
3. THE English channel name SHALL be in English (e.g., "Enchanted Tales — Bedtime Stories for Kids")
4. EACH channel SHALL set the correct default language in YouTube Studio
5. EACH video SHALL have the audio language set correctly (strongest algorithm signal)
6. EACH channel SHALL add translated titles/descriptions in the secondary language via YouTube Studio multi-language feature
7. EACH channel SHALL cross-link the other channel in Featured Channels, About page, and video descriptions
8. BOTH channels SHALL use consistent branding (same logo, color palette, character designs) with localized text
9. THE system SHALL recommend adding MLA dubbed audio tracks as a supplement, not a replacement for separate channels

### Requirement 2: Title Optimization — English Channel

**User Story:** As a content creator, I want English titles optimized for YouTube search and suggested traffic, so that my fairy tale videos reach the maximum audience.

#### Acceptance Criteria

1. THE title SHALL be 50–60 characters maximum (YouTube truncates beyond ~60 characters)
2. THE title SHALL front-load the story name as the first words
3. THE title SHALL include a content-type keyword after the story name (e.g., "Bedtime Story for Kids", "Animated Fairy Tale", "Fairy Tale for Children")
4. THE title MAY include one emoji maximum for long-form content (🌙 preferred for bedtime)
5. THE title MAY include emojis freely for Shorts content
6. THE title SHALL use pipe separator `|` or dash `—` to separate story name from keyword phrase
7. THE title MAY include age marker "Ages 3-6" when character budget allows
8. THE title SHALL NOT use excessive capitalization (flagged as clickbait)
9. THE title SHALL NOT use sensational or misleading language
10. THE title SHALL NOT exceed 2 emojis (triggers "deceptive kids content" classifiers)
11. THE title SHALL accurately represent the video content

#### English Title Formulas

| Formula | Example |
|---------|---------|
| `[Story Name] \| Bedtime Story for Kids` | Little Red Riding Hood \| Bedtime Story for Kids |
| `[Story Name] — Animated Fairy Tale \| Ages 3-6` | Cinderella — Animated Fairy Tale \| Ages 3-6 |
| `[Story Name] 🌙 [Content Type] for Children` | Three Little Pigs 🌙 Fairy Tale for Children |
| `[Story Name] \| Kids Animated Story` | Goldilocks \| Kids Animated Story |

#### Priority English Keywords

- bedtime stories for kids
- fairy tales for children
- animated stories for preschoolers
- kids fairy tales
- children's stories
- classic fairy tales
- stories for kids age 3-6

### Requirement 3: Title Optimization — Russian Channel

**User Story:** As a content creator, I want Russian titles optimized for YouTube search in the Russian-speaking market, so that my fairy tale videos reach Russian-speaking families.

#### Acceptance Criteria

1. THE title SHALL be 50–60 characters maximum
2. THE title SHALL front-load the story name (Название) as the first words
3. THE title SHALL use pipe-separated keyword stacking (more aggressive than English convention)
4. THE title SHALL include content-type keywords: "Сказка на ночь для детей", "Мультфильм для детей", "Аудиосказка для детей", "Добрые сказки"
5. THE title MAY include one emoji maximum for long-form (🌙 preferred)
6. THE title SHALL NOT use excessive capitalization
7. THE title SHALL NOT use misleading language
8. THE title SHALL accurately represent the video content

#### Russian Title Formulas

| Formula | Example |
|---------|---------|
| `[Название] \| Сказка на ночь для детей` | Красная Шапочка \| Сказка на ночь для детей |
| `[Название] — Мультфильм для детей \| Добрые сказки` | Золушка — Мультфильм для детей \| Добрые сказки |
| `[Название] 🌙 Аудиосказка для детей на ночь` | Колобок 🌙 Аудиосказка для детей на ночь |
| `[Название] \| Сказки для малышей` | Теремок \| Сказки для малышей |

#### Priority Russian Keywords

- сказка на ночь для детей
- мультфильм для детей
- аудиосказка для детей
- сказки для малышей
- добрый мультик перед сном
- детские сказки
- сказки перед сном
- мультфильм для детей 3-6 лет

### Requirement 4: Description Optimization

**User Story:** As a content creator, I want structured descriptions that feed the algorithm and serve parents, so that my videos rank higher and provide useful information.

#### Acceptance Criteria

1. THE description SHALL be 200–300 words total
2. THE first 100–150 characters SHALL contain the primary keyword phrase (visible before "Show more")
3. THE description SHALL include the primary keyword in the first sentence
4. THE description SHALL repeat the primary keyword 2–3 times naturally throughout
5. THE description SHALL include 3–5 secondary/LSI keywords woven naturally
6. THE description SHALL include timestamps/chapters (enables Google "Key Moments" rich results)
7. THE description SHALL include playlist links to related fairy tales
8. THE description SHALL include a brief channel description with publishing schedule
9. THE description SHALL include exactly 3 hashtags (displayed above video title)
10. THE description SHALL NOT exceed 15 total hashtags (YouTube ignores all if exceeded)
11. THE description SHALL NOT keyword-stuff (penalized, especially for kids' content)
12. KEYWORDS in the description SHALL also be spoken in the video audio (YouTube cross-references)

#### English Hashtag Sets

| Theme | Hashtags |
|-------|----------|
| Bedtime | #BedtimeStories #FairyTalesForKids #AnimatedStories |
| Classic Tales | #ClassicFairyTales #KidsStories #AnimatedFairyTales |
| Compilations | #BedtimeStories #KidsCompilation #FairyTalesForKids |

#### Russian Hashtag Sets

| Theme | Hashtags |
|-------|----------|
| Bedtime | #СказкиНаНочь #СказкиДляДетей #МультикиДляДетей |
| Classic Tales | #ДетскиеСказки #МультфильмыДляДетей #СказкиДляМалышей |
| Compilations | #СборникСказок #СказкиДляДетей #ДобрыеМультики |

### Requirement 5: Description Templates

**User Story:** As a content creator, I want ready-to-use description templates, so that I can quickly generate consistent, optimized descriptions.

#### English Description Template

```
🌙 [Story Name] — Animated Bedtime Story for Kids (Ages 3-6)

Join [Main Character] on [brief adventure hook] in this beautifully animated fairy tale! A classic bedtime story perfect for preschoolers, retold with gentle narration and colorful animation.

📖 [2-3 sentence plot summary with secondary keywords woven in naturally. Mention "fairy tale", "animated story", "children" etc.]

⏰ Timestamps:
0:00 – Introduction
[0:30] – [Scene description]
[2:15] – [Scene description]
[4:00] – [Scene description]
[5:30] – Happy ending & moral

🌟 More Bedtime Stories: ▶ [Related Story 1] [link] ▶ [Related Story 2] [link] ▶ Full Playlist [link]

📌 We create gentle, animated fairy tales for preschoolers ages 3-6. New stories every [schedule]! Subscribe for magical bedtime adventures.

#[Hashtag1] #[Hashtag2] #[Hashtag3]
```

#### Russian Description Template

```
🌙 [Название] — Сказка на ночь для детей | Мультфильм для малышей от 3 до 6 лет

[Главный герой] отправляется в [краткое описание приключения] в этом добром мультфильме! Красивая анимированная сказка перед сном для самых маленьких.

📖 [2-3 предложения с пересказом сюжета и вплетёнными ключевыми словами: "сказка", "мультфильм для детей", "добрый мультик" и т.д.]

⏰ Таймкоды:
0:00 – Начало
[0:30] – [Описание сцены]
[2:15] – [Описание сцены]
[4:00] – [Описание сцены]
[5:30] – Счастливый конец

🌟 Ещё сказки на ночь: ▶ [Сказка 1] [ссылка] ▶ [Сказка 2] [ссылка] ▶ Весь плейлист [ссылка]

📌 Мы создаём добрые мультфильмы-сказки для малышей от 3 до 6 лет. Новые сказки каждую [расписание]! Подписывайтесь!

#[Хештег1] #[Хештег2] #[Хештег3]
```

### Requirement 6: Tag Optimization

**User Story:** As a content creator, I want bilingual tags that maximize discoverability across languages, so that my videos appear in both Russian and English search results.

#### Acceptance Criteria

1. THE system SHALL generate 10–15 highly relevant tags per video
2. THE tags SHALL stay within the 500-character limit
3. THE tags SHALL prioritize the primary channel language first
4. THE tags SHALL include secondary language tags after primary language tags
5. THE tags SHALL include common misspellings of story names
6. THE tags SHALL include the channel name as the last tag
7. THE system SHALL NOT generate irrelevant or misleading tags

#### English Channel Tag Template (for a given story)

```
bedtime stories for kids, [Story Name], fairy tales for children, animated bedtime story, fairy tale for preschoolers, kids fairy tales, children's stories, stories for kids age 3-6, animated fairy tales, classic fairy tales, [Story Name Russian], сказки для детей, [Channel Name]
```

#### Russian Channel Tag Template (for a given story)

```
сказки на ночь для детей, [Название], сказки для детей, мультфильм для малышей, сказка на ночь, детские сказки, [Название] мультик, сказки перед сном, мультфильм для детей 3-6 лет, добрые мультики для детей, аудиосказка, [Story Name English], bedtime stories for kids, fairy tales for children, [Channel Name]
```

### Requirement 7: Thumbnail Brief Generation

**User Story:** As a content creator, I want thumbnail design briefs optimized for kids' content CTR, so that my thumbnails drive maximum clicks in suggested traffic.

#### Acceptance Criteria

1. THE thumbnail SHALL be 1280 × 720 pixels (16:9), under 2MB, PNG format
2. THE thumbnail SHALL feature two or more characters interacting with clear emotional expressions
3. THE thumbnail SHALL use bright primary colors (purple/violet for magic, bright yellow for cheer, sky blue for trust)
4. THE thumbnail SHALL include the channel logo
5. THE thumbnail SHALL use minimal or zero text (children can't read; 3–5 large words maximum if text is used)
6. THE thumbnail SHALL maintain consistent visual branding across all videos
7. THE thumbnail SHALL NOT use exaggerated "shock face" expressions (flagged as deceptive kids content)
8. THE thumbnail SHALL NOT use thin lines or fine details that disappear at small sizes
9. WHEN bedtime content THEN use softer palette: deep purples, blues, warm golds, moon/stars imagery
10. THE system SHALL recommend A/B testing via YouTube's "Test & Compare" feature

### Requirement 8: Shorts Metadata

**User Story:** As a content creator, I want optimized metadata for Shorts teasers, so that Shorts serve as my primary discovery engine.

#### Acceptance Criteria

1. THE Short SHALL be 30–60 seconds, extracted from full stories
2. THE Short title MAY include emojis freely (Shorts with emojis get +49% views)
3. THE Short title SHALL front-load the story name
4. THE Short description SHALL mention the full-length video title and channel name (links in Shorts descriptions are NOT clickable — use text references instead)
5. THE Short description MAY include premiere date for upcoming content (e.g., "Full story — Friday on our channel")
6. THE Short SHALL target high completion rate and replays (strongest Shorts algorithm signals)
6. THE Short content SHALL be visually striking scene highlights, character introductions, or teaser clips

#### English Shorts Title Formulas

| Formula | Example |
|---------|---------|
| `[Story Name] 🐺✨ #BedtimeStories #FairyTales` | Little Red Riding Hood 🐺✨ #BedtimeStories #FairyTales |
| `Will [Character] escape? 😱 [Story Name]` | Will Hansel escape? 😱 Hansel and Gretel |

#### Russian Shorts Title Formulas

| Formula | Example |
|---------|---------|
| `[Название] 🐺✨ #СказкиДляДетей #Мультики` | Красная Шапочка 🐺✨ #СказкиДляДетей #Мультики |
| `Что будет дальше? 😱 [Название]` | Что будет дальше? 😱 Колобок |

### Requirement 9: Playlist Organization

**User Story:** As a content creator, I want structured playlists that compound watch time, so that session time increases and videos rank higher.

#### Acceptance Criteria

1. THE system SHALL recommend themed playlists for each channel
2. THE playlists SHALL use YouTube's "Series Playlists" feature for sequential viewing order
3. LINKS in descriptions SHALL point to the first video in a playlist (not the playlist page) to trigger autoplay
4. EACH playlist title SHALL include a relevant keyword

#### Recommended Playlist Structure — English

| Playlist | Title |
|----------|-------|
| Bedtime | 🌙 Bedtime Stories for Kids |
| Princess | 🏰 Princess & Castle Fairy Tales |
| Animals | 🐻 Animal Fairy Tales for Children |
| Classics | 📚 Classic Fairy Tales — Animated |
| Compilations | 📺 Long Compilations (30+ min) |
| Popular | ⭐ Most Popular Stories |

#### Recommended Playlist Structure — Russian

| Playlist | Title |
|----------|-------|
| Bedtime | 🌙 Сказки на ночь для детей |
| Princess | 🏰 Сказки про принцесс |
| Animals | 🐻 Сказки про животных для малышей |
| Classics | 📚 Классические сказки — Мультфильмы |
| Compilations | 📺 Сборники сказок (30+ мин) |
| Popular | ⭐ Самые популярные сказки |

### Requirement 10: Captions and Subtitles

**User Story:** As a content creator, I want manual bilingual captions on every video, so that my videos gain SEO value and reach wider audiences.

#### Acceptance Criteria

1. EACH video SHALL have manually edited subtitles in the primary channel language
2. EACH video SHALL have translated subtitles in the secondary language
3. THE system SHALL NOT rely on auto-generated captions (frequent errors with children's voices and fairy tale vocabulary)
4. KEYWORDS from the description SHALL appear in the spoken audio and captions (YouTube cross-references)
5. A 10-minute video contains ~1,300 spoken words of indexable text — captions are a significant SEO asset

### Requirement 11: Upload Scheduling

**User Story:** As a content creator, I want optimal upload timing, so that my videos are processed and ready during peak viewing hours.

#### Acceptance Criteria

1. THE system SHALL recommend uploading 1–2 hours before peak viewing times
2. WHEN targeting Russian audience THEN peak times are 6–8 AM and 5–7 PM Moscow time
3. WHEN targeting English/US audience THEN peak times are 7–9 AM and 5–7 PM Eastern
4. WEEKEND mornings are especially strong for preschool content
5. THE system SHALL recommend 2–3 long-form uploads per week plus 3–5 Shorts
6. THE system SHALL recommend ramping up content output October 15 – December 15 (peak ad rates)

### Requirement 12: Category and YouTube Kids Eligibility

**User Story:** As a content creator, I want my videos categorized correctly and eligible for YouTube Kids, so that I access the dedicated preschool audience pipeline.

#### Acceptance Criteria

1. THE video category SHALL be "Film & Animation"
2. THE video SHALL be marked "Made for Kids"
3. THE content SHALL be 100% safe — no scary elements, violence, clickbait, keyword stuffing, or excessive commercial focus
4. THE content SHALL have clear storylines targeting the Preschool tier (ages 4 and under)
5. THE system SHALL recommend building visual CTAs into the video itself (show related thumbnails at the end) since end screens are disabled
6. THE system SHALL recommend ending each story with a teaser for the next one
7. THE system SHALL recommend referencing playlists verbally and in descriptions

### Requirement 13: Compilation Metadata

**User Story:** As a content creator, I want optimized metadata for compilation videos, so that compilations drive maximum watch time.

#### Acceptance Criteria

1. THE compilation SHALL be 30–60+ minutes
2. THE compilation title SHALL include "Compilation" / "Сборник" and story count or duration
3. THE compilation description SHALL include timestamps for each individual story
4. THE compilation SHALL be added to the compilations playlist

#### English Compilation Title Formulas

| Formula | Example |
|---------|---------|
| `[Theme] Fairy Tales \| 1 Hour Compilation for Kids` | Classic Fairy Tales \| 1 Hour Compilation for Kids |
| `Bedtime Stories Collection 🌙 [N] Stories for Children` | Bedtime Stories Collection 🌙 5 Stories for Children |

#### Russian Compilation Title Formulas

| Formula | Example |
|---------|---------|
| `[Тема] \| Сборник сказок для детей — 1 час` | Классические сказки \| Сборник сказок для детей — 1 час |
| `Сказки на ночь 🌙 Сборник [N] сказок для малышей` | Сказки на ночь 🌙 Сборник 5 сказок для малышей |

### Requirement 14: Error Handling

**User Story:** As a user, I want clear feedback when metadata generation encounters issues.

#### Acceptance Criteria

1. IF story name is not provided THEN ask the user for the story name before generating
2. IF target language is ambiguous THEN generate metadata for both channels
3. IF title exceeds 60 characters THEN warn the user and suggest a shorter alternative
4. IF tags exceed 500 characters THEN trim least important tags and notify the user
5. IF description exceeds 300 words THEN trim and notify the user

---

## Video Length Reference

| Content Type | Optimal Length | Notes |
|--------------|---------------|-------|
| Individual fairy tale | 5–10 minutes | Preschooler attention span |
| Compilation | 30–60+ minutes | Drives massive watch time |
| Shorts teaser | 30–60 seconds | Discovery engine |
| 24/7 Livestream | Continuous | Consider once enough material exists |

## CTR Benchmarks

| Metric | Range | Notes |
|--------|-------|-------|
| Normal YouTube CTR | 2–10% | YouTube stated range |
| Kids' content with loyal audience | >10% possible | More targeted impressions |
| New channel starting CTR | Lower end | Improves as algorithm identifies audience |

## Monetization Context

| Metric | Value |
|--------|-------|
| Kids' content RPM | $0.25–$1.00 per 1,000 views |
| Compared to non-kids | 60–95% lower |
| Peak ad rates | October 15 – December 15 |

## Competitor Patterns Reference

| Channel | Title Pattern | Key Tactic |
|---------|--------------|------------|
| Masha and the Bear | `Show Name — Episode Title (Серия #)` | 14 language channels, 3D character thumbnails |
| CoComelon | `Song Name \| + More Nursery Rhymes & Kids Songs` | Short titles, channel brand appended |
| Лалабук | `Терапевтическая сказка на ночь \| Успокаивающий мультик перед сном «Title»` | Emotional descriptors, therapeutic positioning |
| Kids Diana Show | Per-language channel names | 20+ language channels, consistent branding |

## Universal Metadata Checklist

| Check | Requirement |
|-------|-------------|
| ✓ | Title under 60 characters with front-loaded story name |
| ✓ | Primary keyword in first 100–150 characters of description |
| ✓ | 200–300 word description with timestamps |
| ✓ | Exactly 3 hashtags displayed above title |
| ✓ | 10–15 bilingual tags within 500 characters |
| ✓ | Manual captions in both languages |
| ✓ | Category set to "Film & Animation" |
| ✓ | Marked "Made for Kids" |
| ✓ | Audio language set correctly |
| ✓ | Translated title/description added via multi-language feature |
| ✓ | Playlist links in description |
| ✓ | Thumbnail: 1280×720, PNG, bright colors, expressive characters, logo |
| ✗ | Title over 60 characters |
| ✗ | More than 2 emojis in long-form title |
| ✗ | More than 15 hashtags in description |
| ✗ | Keyword stuffing |
| ✗ | Exaggerated shock-face thumbnails |
| ✗ | Auto-generated captions without manual editing |
