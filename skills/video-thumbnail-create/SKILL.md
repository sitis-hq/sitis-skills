---
description: Generate high-CTR video thumbnails optimized for clicks and watch time. Use when asked to "create youtube thumbnail", "make video thumbnail", "design thumbnail for youtube", "generate thumbnail", or "create clickable thumbnail".
---

# Requirements Document

## Introduction

This document defines requirements for the "Video Thumbnail Creation" skill - an AI-powered thumbnail generation system optimized for CTR, watch time, and platform-specific engagement. The skill enables generation of high-performing video thumbnails for YouTube and other video platforms using AI image generation tools.

Scientific foundation: Thumbnails are processed by the brain 60,000x faster than text. Research shows faces in thumbnails boost CTR by 20-30%, high-contrast colors increase engagement by 617K+ views on average, and visual simplicity (max 3 elements) prevents 23% CTR loss. 70%+ of video traffic comes from mobile devices, making mobile-first design critical.

## Glossary

- **CTR**: Click-Through Rate - percentage of impressions that result in clicks
- **Safe Zone**: Central area of thumbnail where critical elements should be placed to avoid platform UI overlays
- **Rule of Thirds**: Compositional guideline dividing frame into 9 equal parts; key elements placed on intersection points
- **Focal Point**: Single dominant visual element that draws viewer attention first
- **Hero Shot**: Primary subject positioned as the main visual focus
- **Before-After**: Split composition showing transformation, increases CTR by 35% for tutorials
- **Timestamp Overlay**: YouTube's video duration indicator in bottom-right corner
- **Impression**: Single instance of thumbnail being displayed to a viewer

## Requirements

### Requirement 1: Face Dominance

**User Story:** As a content creator, I want thumbnails with prominent faces, so that my videos achieve 20-30% higher CTR through human connection.

#### Acceptance Criteria

1. THE thumbnail SHALL include face covering minimum 40% of thumbnail area
2. THE face SHALL have clear direct eye contact with viewer
3. THE face SHALL be positioned on rule-of-thirds gridlines (left or right third)
4. THE face SHALL display expressive emotion appropriate to content
5. WHEN sad emotion THEN expect 2.3M average views (highest performing)
6. WHEN happy emotion THEN aligns with 25.3% of top-performing thumbnails
7. THE System SHALL NOT generate faces smaller than 40% of frame area
8. THE System SHALL NOT generate faces without clear eye contact

### Requirement 2: Color Contrast

**User Story:** As a content creator, I want high-contrast bold colors, so that my thumbnails stand out in feeds and achieve 20-30% CTR boost.

#### Acceptance Criteria

1. THE thumbnail SHALL use high-contrast bold color combinations
2. THE thumbnail SHALL use proven combinations: red/blue, yellow/purple, orange/teal, yellow on black
3. THE thumbnail SHALL be colorful (88% of top thumbnails are colorful, +617K views vs desaturated)
4. THE System SHALL NOT generate muted or desaturated color palettes
5. THE System SHALL NOT generate low-contrast color combinations

### Requirement 3: Visual Simplicity

**User Story:** As a content creator, I want clean simple compositions, so that viewers instantly understand my thumbnail without 23% CTR loss from complexity.

#### Acceptance Criteria

1. THE thumbnail SHALL contain maximum 3 distinct visual elements
2. THE thumbnail SHALL have single clear focal point
3. THE thumbnail SHALL have clean uncluttered composition
4. THE System SHALL NOT generate thumbnails with more than 3 visual elements
5. THE System SHALL NOT generate thumbnails without clear focal point
6. THE System SHALL NOT generate cluttered or busy compositions

### Requirement 4: Text Rules

**User Story:** As a content creator, I want optimal text usage, so that my message is clear without reducing CTR.

#### Acceptance Criteria

1. THE thumbnail text SHALL be 0-3 words (optimal range)
2. THE thumbnail text SHALL be under 12 characters for best performance
3. THE thumbnail text SHALL use bold sans-serif fonts (Montserrat, Oswald, Impact)
4. THE thumbnail text SHALL use font weight 700 or higher
5. THE thumbnail text SHALL be minimum 24px for mobile readability
6. THE thumbnail text SHALL NOT be placed in bottom-right corner (timestamp overlay)
7. THE thumbnail text SHALL NOT be placed in top-right corner (menu icon overlay)
8. THE System SHALL NOT generate text over 7 words

### Requirement 5: Mobile-First Design

**User Story:** As a content creator, I want mobile-optimized thumbnails, so that my content performs well for 70%+ of traffic from mobile devices.

#### Acceptance Criteria

1. THE thumbnail SHALL be tested at ~120px wide (mobile preview size)
2. THE thumbnail SHALL keep critical elements within desktop safe zone: center 1100×620px
3. THE thumbnail SHALL keep critical elements within mobile safe zone: center 960×540px
4. THE thumbnail SHALL avoid bottom-right corner (timestamp overlay)
5. THE thumbnail SHALL avoid top-right corner (menu icon overlay)
6. THE System SHALL NOT generate desktop-only designs ignoring mobile traffic

### Requirement 6: Niche-Specific Optimization

**User Story:** As a content creator, I want thumbnails optimized for my specific content niche, so that my thumbnails match audience expectations and maximize engagement.

#### Acceptance Criteria - Gaming

1. WHEN Gaming niche THEN use dramatic action moments with character close-ups
2. WHEN Gaming niche THEN use intense focused expressions
3. WHEN Gaming niche THEN use neon colors (blue, orange) with dark backgrounds
4. WHEN Gaming niche THEN use high energy aesthetic

#### Acceptance Criteria - Tutorial / How-To

1. WHEN Tutorial niche THEN use before-after compositions (35% higher CTR)
2. WHEN Tutorial niche THEN show clear visible transformation
3. WHEN Tutorial niche THEN use arrows or circles highlighting key element
4. WHEN Tutorial niche THEN use clean white or light backgrounds

#### Acceptance Criteria - Vlog / Lifestyle

1. WHEN Vlog niche THEN use authentic expressive face covering 40%+ of frame
2. WHEN Vlog niche THEN use relatable genuine emotion
3. WHEN Vlog niche THEN use warm natural golden lighting
4. WHEN Vlog niche THEN use lifestyle context in blurred background

#### Acceptance Criteria - Tech Review

1. WHEN Tech Review niche THEN use sleek product as hero shot
2. WHEN Tech Review niche THEN use minimal clean aesthetic
3. WHEN Tech Review niche THEN use professional studio lighting
4. WHEN Tech Review niche THEN use subtle gradient backgrounds

#### Acceptance Criteria - Educational / Explainer

1. WHEN Educational niche THEN use curious or surprised expression
2. WHEN Educational niche THEN use visual metaphor for concept
3. WHEN Educational niche THEN use bold contrasting colors (blue/orange)
4. WHEN Educational niche THEN use clean minimal background

#### Acceptance Criteria - Music Video

1. WHEN Music Video niche THEN use dramatic artist portrait
2. WHEN Music Video niche THEN use genre-matching aesthetic
3. WHEN Music Video niche THEN use moody dramatic lighting (purple, blue)
4. WHEN Music Video niche THEN use emotional expression matching song mood

#### Acceptance Criteria - Reaction / Commentary

1. WHEN Reaction niche THEN use exaggerated genuine emotion
2. WHEN Reaction niche THEN use face filling 50%+ of frame
3. WHEN Reaction niche THEN use bright contrasting background (yellow)
4. WHEN Reaction niche THEN use minimal distractions

### Requirement 7: Technical Specifications

**User Story:** As a content creator, I want correct technical specifications, so that my thumbnails display properly on all platforms.

#### Acceptance Criteria

1. THE thumbnail SHALL use 16:9 aspect ratio
2. THE thumbnail SHALL use the largest 16:9 size the generator supports — 2560×1440 (minimum 1280×720)
3. THE thumbnail SHALL be under 50MB file size
4. THE thumbnail SHALL use PNG format for text/graphics or JPG for photos
5. WHEN generating THEN use `--size "16:9"` (there is no `--resolution` for images — passing it is rejected)

### Requirement 8: Error Handling

**User Story:** As a user, I want clear feedback when generation fails.

#### Acceptance Criteria

1. IF generation fails THEN present error to user with description
2. THE System SHALL NOT auto-retry without explicit user approval
3. WHEN error occurs THEN offer retry option to user

---

## Prompt Templates

### Gaming
```
Dramatic close-up of gamer face with intense focused expression covering 50% of frame, direct eye contact with viewer, neon blue and orange lighting, dark background with bright accents, high contrast gaming aesthetic, single focal point, clean composition, 16:9 aspect ratio --size "16:9"
```

### Tutorial / How-To
```
Split composition showing dramatic before-after transformation, bright yellow arrow pointing to result, clean white background, single clear focal point, high contrast, face with surprised expression on left third, eye contact with viewer, maximum 3 visual elements, 16:9 aspect ratio --size "16:9"
```

### Vlog / Lifestyle
```
Expressive surprised face close-up covering 50% of frame, warm golden hour lighting, blurred lifestyle background, direct eye contact with viewer, authentic genuine emotion, positioned on right third, single focal point, high contrast, clean composition, 16:9 aspect ratio --size "16:9"
```

### Tech Review
```
Sleek tech product hero shot on dark gradient background, professional studio lighting, minimal clean composition, high contrast, single focal point, subtle reflections, premium aesthetic, clean uncluttered frame, 16:9 aspect ratio --size "16:9"
```

### Educational / Explainer
```
Curious expression face close-up with raised eyebrow covering 40% of frame, bold blue and orange contrast, clean minimal background, single visual element representing concept, direct eye contact with viewer, high contrast, positioned on left third, 16:9 aspect ratio --size "16:9"
```

### Music Video
```
Dramatic artist portrait with moody purple and blue lighting, intense emotional expression matching song mood, dark cinematic background, high contrast, face covering 40% of frame, direct eye contact with viewer, single focal point, music video aesthetic, 16:9 aspect ratio --size "16:9"
```

### Reaction / Commentary
```
Shocked expression face filling 50% of frame, bright yellow background, wide eyes with direct eye contact, genuine exaggerated emotion, ultra high contrast, minimal distractions, positioned on right third, single focal point, clean composition, 16:9 aspect ratio --size "16:9"
```

---

## Negative Prompts (Always Include)

### Universal Negative Prompts
```
low quality, blurry, cluttered composition, more than 3 elements, no focal point, muted colors, desaturated, low contrast, small face, text in bottom right corner, text in top right corner, busy background, multiple focal points, text over 7 words, desktop-only design, complex composition
```

### Gaming-Specific Negative Prompts
```
static pose, neutral expression, bright cheerful lighting, pastel colors, minimal energy
```

### Tutorial-Specific Negative Prompts
```
no transformation visible, unclear before-after, missing arrows or highlights, dark background
```

### Vlog-Specific Negative Prompts
```
fake emotion, cold lighting, studio background, formal aesthetic
```

### Tech Review-Specific Negative Prompts
```
cluttered background, poor lighting, multiple products, busy composition
```

---

## CTR Benchmarks Reference

| Performance Level | CTR Range | Action |
|-------------------|-----------|--------|
| Needs optimization | <3% | Redesign required |
| Average | 3-4% | Room for improvement |
| Solid | 4-6% | Good performance |
| Exceptional | 7%+ | High performer |
| Top-tier | 9-10%+ | Elite performance |

---

## Technical Specifications Reference

| Specification | Value |
|---------------|-------|
| Resolution | 2560×1440 (`--size "16:9"`; minimum 1280×720) |
| Aspect ratio | 16:9 |
| File size | Up to 50MB |
| Format | PNG (text/graphics), JPG (photos) |
| Desktop safe zone | Center 1100×620px |
| Mobile safe zone | Center 960×540px |

---

## Prompt Construction Formula

```
[EMOTION] [SUBJECT] + [COMPOSITION] + [LIGHTING] + [COLORS] + [STYLE KEYWORDS]
```

### Mandatory Keywords (Always Include)
- "single focal point"
- "high contrast"
- "eye contact with viewer" (if face present)
- "clean composition"
- "16:9 aspect ratio"
- `--size "16:9"`

---

## Anti-Patterns Reference

| Anti-Pattern | Impact |
|--------------|--------|
| More than 3 visual elements | 23% CTR drop |
| Text over 7 words | Underperforms across all categories |
| Muted/desaturated colors | 617K fewer views |
| No clear focal point | Attention fragments |
| Misleading imagery | Algorithm penalizes (high CTR + low retention) |
| Small faces (<40% of frame) | 20-30% CTR loss |
| Desktop-only design | Ignores 70% of traffic |
