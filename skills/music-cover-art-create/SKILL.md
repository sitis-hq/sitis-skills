---
description: Generate professional music cover art optimized for streaming platforms. Use when asked to "create cover art", "make album cover", "design track artwork", "generate music cover", or "create artwork for song".
---

# Requirements Document

## Introduction

This document defines requirements for the "Music Cover Art Generation" skill - an AI-powered cover art generation system optimized for streaming platform visibility, genre authenticity, and emotional resonance. The skill enables generation of professional album/single artwork using AI image generation tools.

Scientific foundation: Album artwork influences streaming behavior within 0.3 seconds (eye-tracking studies). Spotify research shows genre-appropriate covers increase save rates by 23%. Thumbnail visibility at 64×64 pixels is critical - 78% of music discovery happens in playlist contexts where covers appear at minimal sizes.

## Glossary

- **Thumbnail Test**: Verification that artwork remains recognizable and impactful at 64×64 pixel display size
- **Safe Zone**: Central 80% of image where critical visual elements must be placed to avoid platform cropping
- **Genre Authenticity**: Visual alignment with established aesthetic conventions of a music genre
- **Color Temperature**: Warm (reds, oranges) vs cool (blues, purples) color palette dominance
- **Focal Point**: Single dominant visual element that draws viewer attention
- **Negative Space**: Empty areas that provide visual breathing room and improve readability
- **Key Light**: Primary light source defining the main illumination direction
- **Rim Light**: Edge lighting that separates subject from background

## Requirements

### Requirement 1: Platform-Specific Output

**User Story:** As a music artist, I want cover art sized correctly for my target platform, so that my artwork displays optimally everywhere.

#### Acceptance Criteria

1. WHEN Spotify THEN generate 3000×3000 pixels, JPEG/PNG, no text overlay in image
2. WHEN Apple Music THEN generate 3000×3000 pixels minimum, strict quality requirements
3. WHEN YouTube Music THEN generate 1280×720 for video, 800×800 for audio
4. WHEN SoundCloud THEN generate 800×800 pixels minimum
5. WHEN Bandcamp THEN generate 1400×1400 pixels minimum
6. WHEN Universal/Default THEN generate 3000×3000 PNG, 1:1 ratio, sRGB color space
7. THE artwork SHALL place all critical elements within central 80% safe zone
8. THE artwork SHALL NOT include text (platforms display artist/title separately)

### Requirement 2: Thumbnail Visibility

**User Story:** As a music artist, I want my cover art to be recognizable in playlists, so that listeners can identify my music at any size.

#### Acceptance Criteria

1. THE artwork SHALL be recognizable at 64×64 pixel thumbnail size
2. THE artwork SHALL use high contrast between foreground and background
3. THE artwork SHALL have single clear focal point
4. THE artwork SHALL NOT use fine details that disappear at small sizes
5. THE artwork SHALL NOT use thin lines or small text elements
6. THE artwork SHALL NOT use low contrast color combinations
7. THE artwork SHALL NOT use cluttered compositions with multiple competing elements

### Requirement 3: Genre-Specific Visual Style - Pop

**User Story:** As a pop artist, I want cover art that matches pop genre conventions, so that my target audience immediately recognizes the genre.

#### Acceptance Criteria

1. THE pop artwork SHALL use glossy, polished aesthetic
2. THE pop artwork SHALL use bright, saturated colors (pastels, neons, vibrant primaries)
3. THE pop artwork SHALL use high contrast lighting
4. THE pop artwork MAY feature performer portrait as focal point
5. THE pop artwork SHALL convey energy: playful, confident, aspirational
6. WHEN upbeat pop THEN use warm colors (pink, orange, yellow)
7. WHEN emotional pop THEN use cool pastels (lavender, soft blue, mint)

### Requirement 4: Genre-Specific Visual Style - Hip-Hop/Rap

**User Story:** As a hip-hop artist, I want cover art that matches hip-hop genre conventions, so that my target audience immediately recognizes the genre.

#### Acceptance Criteria

1. THE hip-hop artwork SHALL use dramatic, cinematic lighting
2. THE hip-hop artwork SHALL use dark base tones with accent colors (gold, red, purple)
3. THE hip-hop artwork MAY include urban landscape elements
4. THE hip-hop artwork MAY include luxury/status symbols (contextually appropriate)
5. THE hip-hop artwork SHALL convey: confidence, authenticity, street credibility
6. WHEN trap/dark rap THEN use black/red/purple palette with harsh shadows
7. WHEN conscious hip-hop THEN use earth tones with artistic, thoughtful composition

### Requirement 5: Genre-Specific Visual Style - Electronic/EDM

**User Story:** As an electronic artist, I want cover art that matches EDM genre conventions, so that my target audience immediately recognizes the genre.

#### Acceptance Criteria

1. THE electronic artwork SHALL use abstract geometric patterns or futuristic imagery
2. THE electronic artwork SHALL use neon color palette (cyan, magenta, purple, electric blue)
3. THE electronic artwork SHALL use clean, digital aesthetic
4. THE electronic artwork MAY include cyberpunk or synthwave visual elements
5. THE electronic artwork SHALL convey: energy, futurism, technological sophistication
6. WHEN house/techno THEN use minimal geometric shapes, monochromatic with accent
7. WHEN dubstep/bass THEN use aggressive angles, high contrast, dark with neon accents

### Requirement 6: Genre-Specific Visual Style - Rock/Metal

**User Story:** As a rock/metal artist, I want cover art that matches rock genre conventions, so that my target audience immediately recognizes the genre.

#### Acceptance Criteria

1. THE rock artwork SHALL use dark, intense imagery
2. THE rock artwork SHALL use high visual complexity and detail
3. THE rock artwork MAY include illustrated or painted aesthetic
4. THE rock artwork SHALL use dramatic color schemes (black, red, silver, dark purple)
5. THE rock artwork SHALL convey: power, rebellion, intensity
6. WHEN metal THEN use detailed illustration, occult/dark symbolism, extreme contrast
7. WHEN alternative rock THEN use artistic photography, muted tones, conceptual imagery

### Requirement 7: Genre-Specific Visual Style - Jazz/Classical

**User Story:** As a jazz/classical artist, I want cover art that matches jazz/classical genre conventions, so that my target audience immediately recognizes the genre.

#### Acceptance Criteria

1. THE jazz/classical artwork SHALL use elegant, sophisticated aesthetic
2. THE jazz/classical artwork SHALL use muted, refined color palette (amber, cream, navy, burgundy)
3. THE jazz/classical artwork SHALL use minimalist composition with negative space
4. THE jazz/classical artwork MAY include instrument silhouettes or abstract musical elements
5. THE jazz/classical artwork SHALL convey: sophistication, timelessness, artistic depth
6. WHEN jazz THEN use warm amber tones, smoky atmosphere, vintage elegance
7. WHEN classical THEN use clean minimalism, refined typography space, monochromatic options

### Requirement 8: Genre-Specific Visual Style - Indie/Alternative

**User Story:** As an indie artist, I want cover art that matches indie genre conventions, so that my target audience immediately recognizes the genre.

#### Acceptance Criteria

1. THE indie artwork SHALL use DIY, handcrafted aesthetic
2. THE indie artwork SHALL use muted earth tones (olive, rust, cream, dusty blue)
3. THE indie artwork MAY include hand-drawn elements or vintage textures
4. THE indie artwork SHALL use retro film grain or analog photography feel
5. THE indie artwork SHALL convey: authenticity, introspection, artistic individuality
6. WHEN dream pop THEN use soft focus, ethereal lighting, pastel washes
7. WHEN folk/acoustic THEN use natural imagery, warm earth tones, organic textures

### Requirement 9: Genre-Specific Visual Style - Lo-Fi/Chill

**User Story:** As a lo-fi artist, I want cover art that matches lo-fi genre conventions, so that my target audience immediately recognizes the genre.

#### Acceptance Criteria

1. THE lo-fi artwork SHALL use cozy, nostalgic atmosphere
2. THE lo-fi artwork SHALL use warm, soft color palette (sunset oranges, soft purples, warm browns)
3. THE lo-fi artwork MAY use anime-inspired illustration style
4. THE lo-fi artwork SHALL include relaxing scene elements (room interiors, windows, rain, plants)
5. THE lo-fi artwork SHALL convey: comfort, nostalgia, peaceful solitude
6. THE lo-fi artwork SHALL use soft diffused lighting (golden hour, lamp light)
7. THE lo-fi artwork SHALL NOT use harsh contrasts or aggressive imagery

### Requirement 10: Genre-Specific Visual Style - Country

**User Story:** As a country artist, I want cover art that matches country genre conventions, so that my target audience immediately recognizes the genre.

#### Acceptance Criteria - Traditional/Nashville Country

1. THE traditional country artwork SHALL use warm earth tones (brown, tan, rust, gold)
2. THE traditional country artwork SHALL use golden hour or sepia-toned lighting
3. THE traditional country artwork MAY include rural landscapes, cowboy aesthetics
4. THE traditional country artwork SHALL convey: authenticity, heritage, heartland values

#### Acceptance Criteria - Modern Country/Country Pop

1. THE modern country artwork SHALL use bright warm tones with clean whites
2. THE modern country artwork SHALL use natural golden light, high contrast for streaming
3. THE modern country artwork SHALL convey: approachability, contemporary appeal, relatability

#### Acceptance Criteria - Outlaw Country

1. THE outlaw country artwork SHALL use dark sepia tones, weathered textures
2. THE outlaw country artwork SHALL use harsh shadows, gritty aesthetic
3. THE outlaw country artwork MAY reference wanted poster or 1970s Texas aesthetic
4. THE outlaw country artwork SHALL convey: rebellion, anti-establishment, raw authenticity

#### Acceptance Criteria - Americana/Indie Country

1. THE americana artwork SHALL use muted earth tones with vintage textures
2. THE americana artwork MAY use painted illustration or raw candid photography
3. THE americana artwork SHALL use folk-art sensibility, handcrafted feel
4. THE americana artwork SHALL convey: emotional authenticity, storytelling, roots connection

### Requirement 11: Color Psychology Application

**User Story:** As a music artist, I want colors that evoke the right emotions, so that my cover art creates the intended mood.

#### Acceptance Criteria

1. WHEN happy/energetic mood THEN use yellow, orange, bright pink
2. WHEN melancholic/introspective mood THEN use dark blue, purple, muted tones
3. WHEN aggressive/powerful mood THEN use dark red, black, high contrast
4. WHEN calm/peaceful mood THEN use soft blue, green, pastels
5. WHEN sophisticated/elegant mood THEN use gold, monochrome, deep jewel tones
6. WHEN romantic mood THEN use soft pink, red, warm lighting
7. WHEN mysterious mood THEN use deep purple, black, subtle lighting

### Requirement 12: Composition Rules

**User Story:** As a music artist, I want professional composition, so that my cover art looks polished and intentional.

#### Acceptance Criteria

1. THE artwork SHALL use single dominant focal point
2. THE artwork SHALL use rule of thirds or centered composition
3. THE artwork SHALL maintain visual hierarchy (one element dominates)
4. THE artwork SHALL use adequate negative space for visual breathing room
5. THE artwork SHALL NOT use competing focal points
6. THE artwork SHALL NOT use edge-to-edge busy compositions
7. THE artwork SHALL NOT place critical elements in outer 10% (crop danger zone)

### Requirement 13: Lighting Guidelines

**User Story:** As a music artist, I want appropriate lighting for my genre, so that my cover art has the right atmosphere.

#### Acceptance Criteria

1. WHEN portrait-based artwork THEN use defined key light with appropriate fill
2. WHEN dramatic mood THEN use high contrast lighting with deep shadows
3. WHEN warm/inviting mood THEN use golden hour or warm artificial lighting
4. WHEN cool/mysterious mood THEN use blue-tinted or moonlight aesthetic
5. WHEN energetic mood THEN use bright, even lighting with color accents
6. THE artwork SHALL NOT use flat, shadowless lighting (lacks dimension)
7. THE artwork SHALL NOT use lighting that obscures focal point

### Requirement 14: Realism and Quality Standards

**User Story:** As a music artist, I want high-quality realistic artwork, so that my cover looks professional.

#### Acceptance Criteria

1. THE artwork SHALL maintain consistent lighting direction throughout
2. THE artwork SHALL use realistic proportions and anatomy (if featuring people)
3. THE artwork SHALL have sharp focus on focal point
4. THE artwork SHALL use appropriate depth of field
5. THE System SHALL NOT generate artifacts, distortions, or AI glitches
6. THE System SHALL NOT generate extra limbs, deformed faces, or anatomical errors
7. THE System SHALL NOT generate text or legible words in image

### Requirement 15: Error Handling

**User Story:** As a user, I want clear feedback when generation fails.

#### Acceptance Criteria

1. IF generation fails THEN present error to user with description
2. THE System SHALL NOT auto-retry without explicit user approval
3. WHEN error occurs THEN offer retry option to user

---

## Prompt Templates

### Pop - Upbeat
```
Glossy professional album cover art, vibrant performer portrait with confident expression, neon pink and electric blue rim lighting, pastel gradient background transitioning from coral to lavender, high contrast studio lighting, polished commercial aesthetic, single focal point, clean composition with negative space, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Pop - Emotional
```
Elegant album cover art, soft portrait with introspective expression, gentle lavender and soft blue lighting, dreamy pastel atmosphere, soft focus background, emotional depth, single focal point centered, clean minimalist composition, professional studio quality, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Hip-Hop/Rap - Trap
```
Dramatic album cover art, cinematic portrait with confident intense expression, harsh shadows with deep blacks, gold and red accent lighting, urban night atmosphere, luxury aesthetic elements, high contrast dramatic lighting, dark moody background, single powerful focal point, bold composition, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Hip-Hop/Rap - Conscious
```
Artistic album cover art, thoughtful portrait with contemplative expression, warm earth tones with golden accents, cinematic natural lighting, urban landscape background with depth, authentic street aesthetic, artistic composition with intentional negative space, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Electronic/EDM - House
```
Abstract geometric album cover art, minimal clean shapes, deep black background with single neon accent color, cyan or magenta geometric elements, futuristic digital aesthetic, high contrast, sharp edges, single bold focal point, plenty of negative space, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Electronic/EDM - Synthwave
```
Futuristic synthwave album cover art, neon grid landscape, purple and cyan color palette, retro-futuristic sunset, chrome elements with reflections, cyberpunk city silhouette, dramatic perspective, single focal point, high contrast neon glow, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Rock - Alternative
```
Artistic album cover art, moody atmospheric photography style, muted desaturated tones, conceptual imagery, dramatic shadows, film grain texture, artistic composition with intentional framing, single focal point, emotional depth, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Metal
```
Dark detailed album cover art, intricate illustration style, black and deep red color scheme, dramatic occult imagery, high visual complexity, extreme contrast, powerful central focal point, detailed artwork with clear silhouette at small size, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Jazz
```
Elegant sophisticated album cover art, warm amber and gold tones, smoky atmospheric lighting, vintage elegance aesthetic, instrument silhouette or abstract musical element, minimalist composition with generous negative space, refined artistic style, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Classical
```
Refined minimalist album cover art, clean sophisticated composition, monochromatic or deep jewel tones, elegant negative space, subtle artistic element, timeless aesthetic, single refined focal point, professional gallery quality, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Indie/Alternative
```
Authentic indie album cover art, hand-drawn illustration aesthetic, muted earth tones olive rust and cream, vintage film grain texture, DIY handcrafted feel, retro analog photography influence, artistic imperfection, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Lo-Fi/Chill
```
Cozy lo-fi album cover art, anime-inspired illustration style, warm sunset colors through window, comfortable room interior scene, soft diffused golden hour lighting, nostalgic peaceful atmosphere, warm browns and soft purples, plants and cozy elements, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Country - Traditional
```
Warm authentic country album cover art, golden hour portrait, rustic rural setting, earth tone palette brown tan and rust, cowboy aesthetic elements, honest genuine expression, sepia undertones, Americana heritage feel, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Country - Modern
```
Contemporary country album cover art, natural golden backlight portrait, bright warm tones with clean whites, rural hometown setting, approachable genuine expression, high contrast for streaming visibility, modern polished aesthetic, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Country - Outlaw
```
Gritty outlaw country album cover art, dark moody portrait, sepia and bourbon brown tones, weathered distressed textures, harsh dramatic shadows, rebellious confident expression, 1970s Texas aesthetic influence, raw authentic feel, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

### Americana
```
Folk-art americana album cover art, painted illustration style with visible brushstrokes, muted earth tones, Appalachian landscape influence, raw emotional authenticity, vintage folk aesthetic, handcrafted organic feel, single focal point, optimized for 64px thumbnail visibility, no text, no words, no letters --ar 1:1 --style raw
```

---

## Negative Prompts (Always Include)

### Universal Negative Prompts
```
text, words, letters, typography, watermark, signature, logo, worst quality, low quality, blurry, pixelated, artifacts, distortion, deformed, extra limbs, bad anatomy, poorly drawn, cluttered composition, multiple focal points, busy background, low contrast, thin lines, fine details, small elements
```

### Portrait-Based Artwork Additional Negative Prompts
```
extra fingers, missing fingers, deformed hands, asymmetric eyes, crossed eyes, bad teeth, unnatural skin, plastic skin, oversaturated skin, dead eyes, vacant expression
```

### Abstract/Geometric Artwork Additional Negative Prompts
```
organic shapes when geometric needed, inconsistent style, muddy colors, unclear focal point, chaotic composition
```

---

## Genre-Color Quick Reference

| Genre | Primary Colors | Mood | Lighting Style |
|-------|---------------|------|----------------|
| Pop (Upbeat) | Pink, Orange, Yellow, Neon | Energetic, Playful | Bright, High Contrast |
| Pop (Emotional) | Lavender, Soft Blue, Mint | Introspective, Dreamy | Soft, Diffused |
| Hip-Hop/Trap | Black, Gold, Red, Purple | Confident, Dark | Dramatic, Harsh Shadows |
| Hip-Hop/Conscious | Earth Tones, Gold | Thoughtful, Authentic | Cinematic, Natural |
| Electronic/House | Black + Single Neon Accent | Minimal, Futuristic | Clean, High Contrast |
| Electronic/Synthwave | Purple, Cyan, Magenta | Retro-Futuristic | Neon Glow |
| Rock/Alternative | Muted, Desaturated | Moody, Artistic | Dramatic Shadows |
| Metal | Black, Red, Silver | Intense, Powerful | Extreme Contrast |
| Jazz | Amber, Gold, Cream | Sophisticated, Warm | Smoky, Atmospheric |
| Classical | Monochrome, Jewel Tones | Elegant, Timeless | Refined, Subtle |
| Indie | Olive, Rust, Cream, Dusty Blue | Authentic, Introspective | Vintage, Film Grain |
| Lo-Fi | Sunset Orange, Soft Purple, Warm Brown | Cozy, Nostalgic | Golden Hour, Soft |
| Country Traditional | Brown, Tan, Rust, Gold | Authentic, Heritage | Golden Hour, Sepia |
| Country Modern | Warm Whites, Gold | Approachable, Fresh | Natural, Bright |
| Outlaw Country | Dark Sepia, Bourbon Brown | Rebellious, Gritty | Harsh, Weathered |
| Americana | Muted Earth Tones | Raw, Emotional | Vintage, Organic |

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
| YouTube Music | 800×800 | JPEG/PNG | High contrast recommended |
| SoundCloud | 800×800 | JPEG/PNG | Square crop |
| Bandcamp | 1400×1400 | JPEG/PNG | Flexible requirements |
| Universal | 3000×3000 | PNG | sRGB, 1:1 ratio |
