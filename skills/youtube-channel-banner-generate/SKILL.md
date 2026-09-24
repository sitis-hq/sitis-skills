---
description: Generate professional YouTube channel banners optimized for all devices and CTR. Use when asked to "create channel banner", "make YouTube banner", "design channel art", "generate banner for YouTube", or "create header for channel".
---

# Requirements Document

## Introduction

This document defines requirements for the "YouTube Channel Banner Generation" skill - an AI-powered banner creation system optimized for cross-device display, brand recognition, and subscriber conversion. The skill enables generation of professional channel art that communicates value proposition within 2 seconds across all viewing contexts.

Scientific foundation: YouTube banners display differently across 4+ device types, with mobile showing only 60% of uploaded content. Research shows viewers decide subscription intent within 2 seconds of landing on a channel page. Banners with clear value propositions and consistent branding increase subscription rates by up to 40%. Color psychology studies confirm specific palettes drive engagement by niche: blue increases trust perception by 34%, while red/orange increases perceived energy by 28%.

## Glossary

- **Safe Zone**: The center 1546×423 px area guaranteed visible on all devices including mobile
- **Upload Canvas**: Full 2560×1440 px image required by YouTube
- **TV Zone**: Full 2560×1440 px visible only on TV displays
- **Desktop Zone**: 2560×423 px horizontal strip visible on desktop browsers
- **Tablet Zone**: 1855×423 px visible on tablet devices
- **Mobile Zone**: 1546×423 px most restrictive view, determines safe zone
- **Outpainting**: AI technique to extend image boundaries while maintaining coherence
- **Key-to-Fill Ratio**: Contrast ratio between main light and fill light in photography
- **Value Proposition**: Clear statement of what viewers gain by subscribing
- **CTR**: Click-Through Rate - percentage of impressions resulting in clicks
- **Denoising Strength**: AI parameter controlling how much original image influences generation (0.0-1.0)

## Requirements

### Requirement 1: Technical Specification Compliance

**User Story:** As a creator, I want my banner to meet YouTube's technical requirements, so that it displays correctly without cropping or quality loss.

#### Acceptance Criteria

1. THE banner SHALL have exact dimensions of 2560×1440 pixels
2. THE banner SHALL be under 6 MB file size
3. THE banner SHALL use PNG format for graphics/text-heavy designs
4. THE banner SHALL use JPEG format for photography-based designs
5. THE banner SHALL place ALL essential content within center 1546×423 px safe zone
6. THE System SHALL NOT generate banners with critical content outside safe zone
7. THE System SHALL NOT generate banners exceeding 6 MB file size

### Requirement 2: Device-Specific Display Optimization

**User Story:** As a creator, I want my banner to look professional on all devices, so that every viewer has a quality first impression.

#### Acceptance Criteria - Safe Zone (Mobile Priority)

1. THE banner SHALL design for 1546×423 px mobile view FIRST
2. THE banner SHALL contain logo, channel name, and tagline within safe zone
3. THE banner SHALL NOT place text or faces at safe zone edges (risk of partial crop)
4. THE banner SHALL use minimum 60-80 px font size for mobile legibility

#### Acceptance Criteria - Extended Zones

1. WHEN designing for desktop THEN extend background to 2560×423 px
2. WHEN designing for tablet THEN ensure 1855×423 px looks complete
3. WHEN designing for TV THEN fill 2560×1440 px with cohesive imagery
4. THE extended zones SHALL contain supporting visuals, NOT critical information
5. THE extended zones SHALL maintain visual continuity with safe zone

### Requirement 3: Niche-Specific Visual Language

**User Story:** As a creator, I want my banner to match my content niche, so that viewers immediately understand my channel's focus.

#### Acceptance Criteria - Music Channels

1. THE music banner SHALL include artist photography or album artwork integration
2. THE music banner SHALL use dramatic stage lighting or concert energy aesthetic
3. THE music banner SHALL include space for tour dates or release promotion
4. THE music banner SHALL use bold colors matching musical genre
5. WHEN rock/metal THEN use dark themes with high contrast accents
6. WHEN pop/electronic THEN use vibrant neon or gradient aesthetics
7. WHEN classical/jazz THEN use elegant, sophisticated color palettes

#### Acceptance Criteria - Educational Channels

1. THE educational banner SHALL use trust-building blue palettes as primary
2. THE educational banner SHALL include clean professional layouts
3. THE educational banner SHALL include space for credentials display
4. THE educational banner SHALL use topic visualization or abstract knowledge symbols
5. THE educational banner SHALL project authority and expertise
6. THE System SHALL NOT use playful or casual aesthetics for educational content

#### Acceptance Criteria - Entertainment/Comedy Channels

1. THE entertainment banner SHALL be personality-focused with expressive imagery
2. THE entertainment banner SHALL use vibrant, energetic colors (yellow, orange, purple)
3. THE entertainment banner SHALL include playful elements matching humor style
4. THE entertainment banner SHALL leave space for personality photo
5. THE entertainment banner SHALL convey fun and approachability

#### Acceptance Criteria - Gaming Channels

1. THE gaming banner SHALL use neon accents (purple, cyan, green) for modern aesthetic
2. THE gaming banner SHALL include abstract gaming elements or game imagery
3. THE gaming banner SHALL use dark base themes for horror/serious games
4. THE gaming banner SHALL use vibrant themes for casual/adventure games
5. THE gaming banner SHALL include space for streaming schedule if applicable
6. THE gaming banner SHALL convey energy and excitement

#### Acceptance Criteria - Business/Entrepreneurship Channels

1. THE business banner SHALL project professional authority with approachability
2. THE business banner SHALL use blue backgrounds as primary (trust signal)
3. THE business banner SHALL include space for credentials or course promotion
4. THE business banner SHALL use clean, minimalist design language
5. THE business banner SHALL convey expertise and success

#### Acceptance Criteria - Lifestyle/Vlog Channels

1. THE lifestyle banner SHALL use warm, inviting color palettes (earth tones, golden hour)
2. THE lifestyle banner SHALL include personal authentic imagery
3. THE lifestyle banner SHALL create aspirational yet relatable aesthetic
4. THE lifestyle banner SHALL convey warmth and personal connection

#### Acceptance Criteria - Tech/Review Channels

1. THE tech banner SHALL use clean modern aesthetic with sleek gradients
2. THE tech banner SHALL include subtle tech elements (circuits, geometric patterns)
3. THE tech banner SHALL use dark themes with accent colors
4. THE tech banner SHALL include space for product showcase
5. THE tech banner SHALL convey innovation and expertise

### Requirement 4: Color Psychology Application

**User Story:** As a creator, I want colors that psychologically align with my content goals, so that viewers feel the right emotions.

#### Acceptance Criteria

1. WHEN goal is trust/authority THEN use blue and green palettes
2. WHEN goal is energy/urgency THEN use red and orange palettes
3. WHEN goal is creativity THEN use purple and pink palettes
4. WHEN goal is calm/relaxation THEN use soft blue and teal palettes
5. WHEN goal is premium/luxury THEN use gold and black palettes
6. WHEN goal is friendly/approachable THEN use yellow and warm tone palettes
7. THE banner SHALL limit colors to 2-3 from brand palette
8. THE banner SHALL maintain color consistency with channel thumbnails
9. THE System SHALL NOT use more than 3 primary colors (visual noise)

### Requirement 5: Typography and Readability

**User Story:** As a creator, I want text that is readable on all devices, so that my message is always clear.

#### Acceptance Criteria

1. THE banner text SHALL have minimum 4.5:1 contrast ratio against background
2. THE banner text SHALL use minimum 60-80 px font size for primary text
3. THE banner SHALL include maximum one headline plus optional subline
4. THE banner SHALL use bold, sans-serif fonts for maximum legibility
5. THE banner text SHALL be readable within 2 seconds (2-second test)
6. THE System SHALL NOT use thin fonts, script fonts, or low-contrast text
7. THE System SHALL NOT include more than 2 text elements

### Requirement 6: Composition and Layout

**User Story:** As a creator, I want professional composition, so that my banner looks polished and intentional.

#### Acceptance Criteria

1. THE banner SHALL use asymmetric composition with subject on left or right third
2. THE banner SHALL include sufficient negative space for text overlays
3. THE banner SHALL leave clear padding for profile picture area (top-left on desktop)
4. THE banner SHALL leave clear padding for channel links area (bottom-right on desktop)
5. THE banner SHALL communicate single clear message (value proposition)
6. THE banner SHALL pass 2-second test: viewer understands subscription benefit instantly
7. THE System SHALL NOT create cluttered or busy compositions
8. THE System SHALL NOT place critical elements where YouTube UI overlays appear

### Requirement 7: AI Generation Strategy

**User Story:** As a creator, I want high-quality AI-generated banners, so that I get professional results without design skills.

#### Acceptance Criteria - Hybrid Approach (Recommended)

1. THE System SHALL generate core subject at 1024×1024 px with main element
2. THE System SHALL create 2560×1440 px canvas and position original appropriately
3. THE System SHALL use outpainting to extend background with continuation prompts
4. THE System SHALL verify all critical content remains within safe zone after extension

#### Acceptance Criteria - Direct Wide Generation

1. WHEN generating directly THEN include "panoramic widescreen composition" in prompt
2. WHEN generating directly THEN include "subject positioned on left/right third of frame"
3. WHEN generating directly THEN include "vast negative space for text overlay"
4. WHEN generating directly THEN include "--ar 16:9" or "--ar 21:9" aspect ratio
5. THE prompt SHALL include "asymmetric composition" for professional layout
6. THE prompt SHALL include "clean backdrop with room for text"

#### Acceptance Criteria - Outpainting Parameters

1. THE outpainting SHALL use 0.7-0.85 denoising strength for extensions
2. THE outpainting SHALL use 15-30% overlap to avoid visible seams
3. THE outpainting SHALL use ~20% denoising for final cohesion pass
4. THE outpainting SHALL use 128-256 px chunk size per direction per pass
5. THE System SHALL NOT create visible artifacts at extension boundaries
6. THE System SHALL maintain consistent lighting across entire width

### Requirement 8: Brand Consistency

**User Story:** As a creator, I want my banner to match my overall brand, so that my channel has cohesive visual identity.

#### Acceptance Criteria

1. THE banner colors SHALL match channel thumbnail color palette
2. THE banner style SHALL match channel's overall visual language
3. THE banner SHALL reinforce brand recognition across all touchpoints
4. THE banner SHALL use consistent typography with other channel assets
5. THE System SHALL NOT create banners that clash with existing channel branding

### Requirement 9: Quality Assurance

**User Story:** As a creator, I want my banner to pass all quality checks, so that it performs optimally.

#### Acceptance Criteria - Pre-Publish Checklist

1. THE banner SHALL be exactly 2560×1440 px and under 6 MB
2. THE banner SHALL have all critical content within center 1546×423 px
3. THE banner SHALL be readable on actual mobile phone screen
4. THE banner SHALL communicate single clear message within 2 seconds
5. THE banner SHALL have text contrast of minimum 4.5:1
6. THE banner SHALL have colors matching thumbnails and brand
7. THE banner SHALL have clear padding for profile pic and links
8. THE banner SHALL clearly communicate subscription benefit

#### Acceptance Criteria - AI-Specific Quality

1. THE AI banner SHALL have main element within safe zone
2. THE AI banner SHALL have seamless extensions without visible artifacts
3. THE AI banner SHALL have uniform lighting across entire width
4. THE AI banner SHALL have sufficient negative space for text overlays

### Requirement 10: Error Handling

**User Story:** As a creator, I want clear feedback when generation fails, so that I can take corrective action.

#### Acceptance Criteria

1. IF generation fails THEN present error to user with description
2. THE System SHALL NOT auto-retry without explicit user approval
3. WHEN error occurs THEN offer retry option to user
4. THE System SHALL provide actionable feedback for common failures

---

## Prompt Templates

### Music Channel - Artist Focus
```
Professional artist portrait with dramatic stage lighting, concert crowd silhouette in background, cinematic widescreen composition, subject positioned on left third of frame, vast negative space on right for text overlay, bold vibrant colors, high contrast lighting, panoramic 16:9 aspect ratio, clean backdrop with room for tour dates, professional music industry aesthetic --ar 16:9 --style raw
```

### Music Channel - Abstract/Genre
```
Dynamic abstract music visualization, sound waves and audio spectrum elements, dramatic neon lighting in purple and cyan, panoramic widescreen composition, asymmetric layout with focal point on right third, vast negative space on left for artist name, concert energy atmosphere, cinematic depth, professional music channel aesthetic --ar 16:9 --style raw
```

### Educational Channel
```
Clean professional banner with deep blue gradient background, abstract knowledge symbols and geometric patterns, minimalist educational aesthetic, panoramic widescreen composition, large negative space in center for text overlay, subtle light rays suggesting enlightenment, trust-building corporate blue palette, authority and expertise visual language --ar 16:9 --style raw
```

### Entertainment/Comedy Channel
```
Vibrant colorful banner with playful cartoon elements, bright yellow and purple accents, fun energetic atmosphere, panoramic widescreen composition, space for personality photo on left third, vast negative space in center for channel name, confetti and celebration elements, warm inviting colors, approachable friendly aesthetic --ar 16:9 --style raw
```

### Gaming Channel - Cyberpunk
```
Dynamic gaming banner with neon purple and cyan glow, abstract gaming elements and futuristic patterns, cyberpunk aesthetic with dark base, panoramic widescreen composition, clean area for logo in center, glowing accent lights, high-tech atmosphere, subject positioned on right third, vast negative space for text overlay --ar 16:9 --style raw
```

### Gaming Channel - Adventure
```
Epic adventure gaming banner with vibrant fantasy landscape, dramatic lighting with golden hour atmosphere, panoramic widescreen composition, vast open world aesthetic, subject positioned on left third, large negative space in center for channel branding, cinematic depth and scale, exciting adventurous mood --ar 16:9 --style raw
```

### Business/Entrepreneurship Channel
```
Professional corporate banner with deep blue gradient, subtle geometric patterns suggesting growth and success, clean minimalist design, panoramic widescreen composition, large text-ready area in center, sophisticated business aesthetic, trust-building blue palette, authority and expertise visual language, premium quality finish --ar 16:9 --style raw
```

### Lifestyle/Vlog Channel
```
Warm lifestyle banner with golden hour lighting, cozy aesthetic with soft earth tones, panoramic widescreen composition, subject positioned on left third of frame, vast negative space for personal branding, authentic relatable atmosphere, soft bokeh background elements, inviting warm color palette, personal connection aesthetic --ar 16:9 --style raw
```

### Tech/Review Channel
```
Sleek modern tech banner with dark gradient background, subtle circuit patterns and geometric tech elements, futuristic minimal design, panoramic widescreen composition, clean space for branding in center, cool blue accent lighting, innovation aesthetic, professional tech reviewer visual language, premium quality finish --ar 16:9 --style raw
```

### Wellness/Fitness Channel
```
Calming wellness banner with soft teal and blue gradient, abstract nature elements suggesting tranquility, panoramic widescreen composition, vast negative space in center for text overlay, soft diffused lighting, peaceful atmosphere, health and vitality visual language, clean minimal aesthetic --ar 16:9 --style raw
```

---

## Negative Prompts (Always Include)

### Universal Negative Prompts
```
worst quality, low quality, blurry, pixelated, compression artifacts, text, watermark, logo, cluttered composition, busy background, too many colors, neon overload, harsh shadows, flat lighting, amateur design, stock photo aesthetic, generic template look, visible seams, inconsistent lighting, cropped elements at edges
```

### Photography-Based Negative Prompts
```
bad anatomy, poorly lit face, unflattering angle, red eye, motion blur, out of focus subject, harsh direct flash, overexposed, underexposed, unnatural skin tones, awkward pose
```

### Graphic Design Negative Prompts
```
misaligned elements, unbalanced composition, clashing colors, illegible text, thin fonts, low contrast text, too many fonts, inconsistent style, dated design trends, clip art aesthetic
```

---

## Device Display Reference

| Device | Visible Area | Priority |
|--------|--------------|----------|
| Mobile | 1546 × 423 px | CRITICAL (Safe Zone) |
| Tablet | 1855 × 423 px | High |
| Desktop | 2560 × 423 px | Medium |
| TV | 2560 × 1440 px | Low (full canvas) |

---

## Color Psychology Quick Reference

| Goal | Primary Colors | Accent Colors | Best For |
|------|----------------|---------------|----------|
| Trust/Authority | Blue (#1E40AF, #3B82F6) | White, Gray | Education, Business |
| Energy/Urgency | Red (#DC2626), Orange (#EA580C) | Yellow, Black | Entertainment, Gaming |
| Creativity | Purple (#7C3AED), Pink (#EC4899) | Cyan, White | Art, Music |
| Calm/Relaxation | Teal (#0D9488), Soft Blue (#38BDF8) | White, Cream | Lifestyle, Wellness |
| Premium/Luxury | Gold (#D97706), Black (#171717) | White, Deep Blue | Business, Music |
| Friendly/Approachable | Yellow (#FACC15), Warm Orange (#FB923C) | White, Soft Pink | Vlog, Comedy |

---

## Niche-Lighting Quick Reference

| Niche | Lighting Style | Color Temperature | Mood |
|-------|----------------|-------------------|------|
| Music | Dramatic stage lighting | Cool (4000-6000K) | Energetic, Professional |
| Educational | Soft diffused studio | Neutral (4500-5500K) | Trustworthy, Clear |
| Entertainment | Bright, even lighting | Warm (3500-4500K) | Fun, Inviting |
| Gaming | Neon accent lighting | Cool with color accents | Exciting, Modern |
| Business | Professional studio | Neutral (5000-5500K) | Authoritative, Clean |
| Lifestyle | Golden hour natural | Warm (3000-4000K) | Personal, Authentic |
| Tech | Cool modern lighting | Cool (5500-6500K) | Innovative, Sleek |

---

## Safe Zone Positioning Guide

```
┌─────────────────────────────────────────────────────────────┐
│                    TV ONLY (2560×1440)                      │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              DESKTOP (2560×423)                       │  │
│  │  ┌─────────────────────────────────────────────────┐  │  │
│  │  │           TABLET (1855×423)                     │  │  │
│  │  │  ┌───────────────────────────────────────────┐  │  │  │
│  │  │  │     ★ SAFE ZONE - MOBILE (1546×423) ★     │  │  │  │
│  │  │  │   [All critical content MUST be here]     │  │  │  │
│  │  │  └───────────────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

**Critical Elements for Safe Zone:**
- Channel name/logo
- Tagline or value proposition
- Primary visual focal point
- Any text that must be readable

**Extended Zone Content:**
- Background continuation
- Decorative elements
- Secondary imagery
- Atmospheric effects
