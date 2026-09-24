---
description: Generate professional voiceover cover art optimized for streaming and video platforms. Use when asked to "create voiceover cover", "make narration cover", "design story artwork", "generate audiobook cover", or "create artwork for voiceover".
---

# Requirements Document

## Introduction

This document defines requirements for the "Voiceover Cover Art Generation" skill - an AI-powered cover art generation system optimized for voiceover content including fairy tales, stories, narrations, audiobooks, and spoken word releases. The skill enables generation of professional artwork using AI image generation tools.

Scientific foundation: Cover artwork influences click-through behavior within 0.3 seconds (eye-tracking studies). Thumbnail visibility at 64×64 pixels is critical - the majority of content discovery happens in feed/playlist contexts where covers appear at minimal sizes. Genre-appropriate visuals increase engagement rates significantly.

## Glossary

- **Thumbnail Test**: Verification that artwork remains recognizable and impactful at 64×64 pixel display size
- **Safe Zone**: Central 80% of image where critical visual elements must be placed to avoid platform cropping
- **Color Temperature**: Warm (reds, oranges) vs cool (blues, purples) color palette dominance
- **Focal Point**: Single dominant visual element that draws viewer attention
- **Negative Space**: Empty areas that provide visual breathing room and improve readability
- **Key Light**: Primary light source defining the main illumination direction
- **Rim Light**: Edge lighting that separates subject from background
- **Scene Atmosphere**: Overall mood conveyed through lighting, color, and composition

## Requirements

### Requirement 1: Platform-Specific Output

**User Story:** As a narrator, I want cover art sized correctly for my target platform, so that my artwork displays optimally everywhere.

#### Acceptance Criteria

1. WHEN Spotify THEN generate 3000×3000 pixels, JPEG/PNG, no text overlay in image
2. WHEN Apple Music THEN generate 3000×3000 pixels minimum, strict quality requirements
3. WHEN YouTube THEN generate 1280×720 for video, 800×800 for audio
4. WHEN SoundCloud THEN generate 800×800 pixels minimum
5. WHEN Universal/Default THEN generate 3000×3000 PNG, 1:1 ratio, sRGB color space
6. THE artwork SHALL place all critical elements within central 80% safe zone
7. THE artwork SHALL NOT include text (platforms display title/narrator separately)

### Requirement 2: Thumbnail Visibility

**User Story:** As a narrator, I want my cover art to be recognizable in feeds, so that listeners can identify my content at any size.

#### Acceptance Criteria

1. THE artwork SHALL be recognizable at 64×64 pixel thumbnail size
2. THE artwork SHALL use high contrast between foreground and background
3. THE artwork SHALL have single clear focal point
4. THE artwork SHALL NOT use fine details that disappear at small sizes
5. THE artwork SHALL NOT use thin lines or small text elements
6. THE artwork SHALL NOT use low contrast color combinations
7. THE artwork SHALL NOT use cluttered compositions with multiple competing elements

### Requirement 3: Content-Specific Visual Style - Fairy Tales

**User Story:** As a storyteller, I want cover art that matches fairy tale aesthetics, so that my audience immediately recognizes the content type.

#### Acceptance Criteria

1. THE fairy tale artwork SHALL use enchanted, magical atmosphere
2. THE fairy tale artwork SHALL use rich saturated colors (deep blues, emerald greens, golden yellows)
3. THE fairy tale artwork SHALL use painterly or illustrated aesthetic
4. THE fairy tale artwork MAY include fantasy elements (enchanted forests, castles, magical creatures)
5. THE fairy tale artwork SHALL convey: wonder, magic, adventure
6. WHEN children's fairy tale THEN use bright warm colors, friendly characters, soft rounded shapes
7. WHEN dark fairy tale THEN use deep moody tones, mysterious atmosphere, dramatic shadows

### Requirement 4: Content-Specific Visual Style - Stories/Fiction

**User Story:** As a narrator, I want cover art that matches the story genre, so that my audience understands the content mood.

#### Acceptance Criteria

1. THE fiction artwork SHALL reflect the story's primary mood and setting
2. THE fiction artwork SHALL use cinematic composition with depth
3. THE fiction artwork MAY include key scene or symbolic element from the story
4. THE fiction artwork SHALL convey the emotional tone of the narrative
5. WHEN thriller/mystery THEN use dark tones, dramatic shadows, suspenseful atmosphere
6. WHEN romance THEN use warm soft lighting, intimate composition, rich warm colors
7. WHEN sci-fi THEN use futuristic elements, cool blue/purple palette, technological aesthetic
8. WHEN horror THEN use dark oppressive atmosphere, high contrast, unsettling imagery

### Requirement 5: Content-Specific Visual Style - Audiobooks

**User Story:** As an audiobook narrator, I want professional cover art, so that my content looks polished on distribution platforms.

#### Acceptance Criteria

1. THE audiobook artwork SHALL use refined, professional aesthetic
2. THE audiobook artwork SHALL use sophisticated color palette appropriate to genre
3. THE audiobook artwork SHALL use clean composition with strong focal point
4. THE audiobook artwork MAY include symbolic imagery representing the book's theme
5. THE audiobook artwork SHALL convey: quality, professionalism, narrative depth
6. WHEN non-fiction THEN use clean minimalist design, authoritative aesthetic
7. WHEN literary fiction THEN use artistic, contemplative imagery with emotional depth

### Requirement 6: Content-Specific Visual Style - Meditation/Relaxation

**User Story:** As a narrator, I want calming cover art for meditation content, so that my audience feels the peaceful mood immediately.

#### Acceptance Criteria

1. THE meditation artwork SHALL use serene, tranquil atmosphere
2. THE meditation artwork SHALL use soft muted colors (soft blues, lavenders, sage greens, warm creams)
3. THE meditation artwork SHALL use gentle diffused lighting
4. THE meditation artwork MAY include nature elements (water, sky, mountains, forests)
5. THE meditation artwork SHALL convey: peace, calm, mindfulness
6. THE meditation artwork SHALL NOT use harsh contrasts or aggressive imagery
7. THE meditation artwork SHALL use minimal composition with generous negative space

### Requirement 7: Content-Specific Visual Style - Educational/Podcast

**User Story:** As a narrator, I want engaging cover art for educational content, so that my audience finds it approachable and professional.

#### Acceptance Criteria

1. THE educational artwork SHALL use clean, modern aesthetic
2. THE educational artwork SHALL use bold contrasting colors for visibility
3. THE educational artwork SHALL use simple iconic imagery related to the topic
4. THE educational artwork SHALL convey: clarity, knowledge, approachability
5. WHEN science/tech THEN use clean geometric elements, blue/teal palette
6. WHEN history THEN use warm vintage tones, period-appropriate imagery
7. WHEN self-help THEN use uplifting warm colors, aspirational imagery

### Requirement 8: Color Psychology Application

**User Story:** As a narrator, I want colors that evoke the right emotions, so that my cover art creates the intended mood.

#### Acceptance Criteria

1. WHEN adventurous/exciting mood THEN use warm golds, deep reds, rich greens
2. WHEN melancholic/introspective mood THEN use dark blue, purple, muted tones
3. WHEN scary/suspenseful mood THEN use dark red, black, high contrast
4. WHEN calm/peaceful mood THEN use soft blue, green, pastels
5. WHEN magical/whimsical mood THEN use deep purple, gold, emerald, starlight accents
6. WHEN warm/comforting mood THEN use amber, soft orange, warm brown
7. WHEN mysterious mood THEN use deep purple, midnight blue, subtle lighting

### Requirement 9: Composition Rules

**User Story:** As a narrator, I want professional composition, so that my cover art looks polished and intentional.

#### Acceptance Criteria

1. THE artwork SHALL use single dominant focal point
2. THE artwork SHALL use rule of thirds or centered composition
3. THE artwork SHALL maintain visual hierarchy (one element dominates)
4. THE artwork SHALL use adequate negative space for visual breathing room
5. THE artwork SHALL NOT use competing focal points
6. THE artwork SHALL NOT use edge-to-edge busy compositions
7. THE artwork SHALL NOT place critical elements in outer 10% (crop danger zone)

### Requirement 10: Lighting Guidelines

**User Story:** As a narrator, I want appropriate lighting for my content type, so that my cover art has the right atmosphere.

#### Acceptance Criteria

1. WHEN dramatic narrative THEN use high contrast lighting with deep shadows
2. WHEN warm/comforting story THEN use golden hour or warm artificial lighting
3. WHEN mysterious/dark content THEN use blue-tinted or moonlight aesthetic
4. WHEN magical/fantasy content THEN use ethereal glow, magical light sources
5. WHEN calm/meditation THEN use soft diffused natural lighting
6. THE artwork SHALL NOT use flat, shadowless lighting (lacks dimension)
7. THE artwork SHALL NOT use lighting that obscures focal point

### Requirement 11: Realism and Quality Standards

**User Story:** As a narrator, I want high-quality artwork, so that my cover looks professional.

#### Acceptance Criteria

1. THE artwork SHALL maintain consistent lighting direction throughout
2. THE artwork SHALL use realistic proportions and anatomy (if featuring people)
3. THE artwork SHALL have sharp focus on focal point
4. THE artwork SHALL use appropriate depth of field
5. THE System SHALL NOT generate artifacts, distortions, or AI glitches
6. THE System SHALL NOT generate extra limbs, deformed faces, or anatomical errors
7. THE System SHALL NOT generate text or legible words in image

### Requirement 12: Error Handling

**User Story:** As a user, I want clear feedback when generation fails.

#### Acceptance Criteria

1. IF generation fails THEN present error to user with description
2. THE System SHALL NOT auto-retry without explicit user approval
3. WHEN error occurs THEN offer retry option to user


---

## Prompt Templates

### Fairy Tale - Children's
```
Enchanted fairy tale cover art, magical illustrated scene, bright warm colors with golden accents, friendly fantasy landscape, soft rounded shapes, whimsical magical atmosphere, storybook illustration style, rich emerald greens and warm golds, single clear focal point, gentle magical lighting, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Fairy Tale - Dark/Classic
```
Dark fairy tale cover art, moody enchanted forest scene, deep blues and emerald greens with golden accents, mysterious magical atmosphere, painterly illustration style, dramatic shadows with ethereal light sources, gothic fairy tale aesthetic, single powerful focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Story - Thriller/Mystery
```
Suspenseful narrative cover art, dramatic cinematic composition, dark moody tones with sharp accent lighting, mysterious atmosphere, deep shadows, noir aesthetic, single focal point with tension, high contrast, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Story - Romance
```
Romantic narrative cover art, warm intimate atmosphere, soft golden lighting, rich warm color palette with rose and amber tones, dreamy soft focus background, emotional depth, elegant composition, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Story - Adventure/Fantasy
```
Epic adventure cover art, dramatic fantasy landscape, rich saturated colors with golden light, cinematic depth and scale, magical atmospheric elements, bold composition, powerful focal point, dramatic lighting with warm and cool contrast, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Story - Horror
```
Dark horror narrative cover art, oppressive atmospheric scene, deep blacks with cold accent lighting, unsettling composition, high contrast dramatic shadows, eerie fog or mist, single disturbing focal point, dread atmosphere, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Audiobook - Non-Fiction
```
Clean professional audiobook cover art, minimalist modern design, bold contrasting colors, simple iconic symbolic element, authoritative sophisticated aesthetic, clean negative space, single strong focal point, professional quality, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Audiobook - Literary Fiction
```
Artistic literary cover art, contemplative atmospheric scene, muted sophisticated color palette, emotional depth, painterly quality, thoughtful composition with negative space, single evocative focal point, refined aesthetic, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Meditation/Relaxation
```
Serene meditation cover art, tranquil natural scene, soft muted colors lavender sage and warm cream, gentle diffused lighting, minimal peaceful composition, generous negative space, calm water or sky elements, single serene focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Educational/Science
```
Modern educational cover art, clean geometric design, bold blue and teal palette, simple iconic element representing topic, professional minimalist aesthetic, high contrast for visibility, single clear focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Educational/History
```
Historical narrative cover art, warm vintage tones with sepia undertones, period-appropriate atmospheric scene, cinematic lighting, rich amber and brown palette, authentic historical feel, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Children's Story
```
Bright cheerful children's cover art, colorful illustrated scene, friendly characters, warm saturated colors, playful composition, soft rounded shapes, inviting joyful atmosphere, storybook illustration quality, single clear focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

---

## Negative Prompts (Always Include)

### Universal Negative Prompts
```
text, words, letters, typography, watermark, signature, logo, worst quality, low quality, blurry, pixelated, artifacts, distortion, deformed, extra limbs, bad anatomy, poorly drawn, cluttered composition, multiple focal points, busy background, low contrast, thin lines, fine details, small elements
```

### Portrait/Character-Based Artwork Additional Negative Prompts
```
extra fingers, missing fingers, deformed hands, asymmetric eyes, crossed eyes, bad teeth, unnatural skin, plastic skin, oversaturated skin, dead eyes, vacant expression
```

### Scene/Landscape Artwork Additional Negative Prompts
```
inconsistent perspective, muddy colors, unclear focal point, chaotic composition, unrealistic scale
```

---

## Content-Color Quick Reference

| Content Type | Primary Colors | Mood | Lighting Style |
|-------------|---------------|------|----------------|
| Fairy Tale (Children's) | Gold, Emerald, Warm Blue | Magical, Joyful | Warm, Ethereal Glow |
| Fairy Tale (Dark) | Deep Blue, Emerald, Gold | Mysterious, Enchanted | Moonlight, Ethereal |
| Thriller/Mystery | Dark Grey, Black, Sharp Accent | Suspenseful, Tense | Noir, High Contrast |
| Romance | Rose, Amber, Warm Gold | Intimate, Emotional | Golden Hour, Soft |
| Adventure/Fantasy | Rich Gold, Deep Blue, Emerald | Epic, Exciting | Dramatic, Cinematic |
| Horror | Black, Cold Blue, Dark Red | Dread, Unsettling | Cold, Harsh Shadows |
| Audiobook (Non-Fiction) | Bold Contrasting, Clean | Professional, Clear | Clean, Even |
| Audiobook (Literary) | Muted Sophisticated | Contemplative, Deep | Atmospheric, Subtle |
| Meditation | Lavender, Sage, Warm Cream | Peaceful, Calm | Soft, Diffused |
| Educational (Science) | Blue, Teal, White | Clear, Modern | Clean, Bright |
| Educational (History) | Amber, Brown, Sepia | Authentic, Rich | Warm, Vintage |
| Children's Story | Bright Saturated, Warm | Playful, Inviting | Bright, Friendly |

---

## Thumbnail Visibility Checklist

| Check | Requirement |
|-------|-------------|
| ✓ | Single clear focal point visible at 64×64 |
| ✓ | High contrast between subject and background |
| ✓ | No fine details that disappear at small size |
| ✓ | Bold shapes and silhouettes |
| ✓ | Color palette distinguishable at thumbnail |
| ✗ | Thin lines or intricate patterns |
| ✗ | Multiple competing elements |
| ✗ | Low contrast color combinations |
| ✗ | Text or small symbols |

---

## Platform Specifications Reference

| Platform | Size | Format | Notes |
|----------|------|--------|-------|
| Spotify | 3000×3000 | JPEG/PNG | No text in image |
| Apple Music | 3000×3000 | JPEG/PNG | Strict quality review |
| YouTube | 1280×720 / 800×800 | JPEG/PNG | High contrast recommended |
| SoundCloud | 800×800 | JPEG/PNG | Square crop |
| Universal | 3000×3000 | PNG | sRGB, 1:1 ratio |
