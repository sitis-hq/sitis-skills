---
description: Generate professional AI avatars optimized for CTR, trust perception, and gender-specific charisma. Use when asked to "create avatar", "generate profile photo", "make headshot", "design profile picture", or "create user avatar".
---

# Requirements Document

## Introduction

This document defines requirements for the "User Avatar Generation" skill - an AI-powered professional avatar generation system optimized for CTR, trust perception, and gender-specific charismatic appeal. The skill enables generation of context-appropriate profile photos for various platforms using AI image generation tools.

Scientific foundation: First impressions form in 100 milliseconds (Willis & Todorov, 2006). Optimized profile photos deliver 21x more views on LinkedIn, 38% higher engagement on Instagram, and 95% more conversions in e-commerce. PhotoFeeler research on 60,000+ ratings confirms gender-specific optimization increases perceived competence, likability, and influence.

## Glossary

- **Duchenne Smile**: A genuine smile involving both mouth and eye muscles (eye crinkles), increases likability by +1.35
- **Squinch**: Slight lower eyelid tension conveying confidence, increases influence perception by +0.37
- **fWHR**: Facial Width-to-Height Ratio - key metric for male dominance perception; higher fWHR correlates with leadership perception
- **Butterfly Lighting**: Light source directly above camera at 45° down, creates symmetrical shadow under nose; optimal for feminine portraits
- **Rembrandt Lighting**: Light source at 45° side angle, creates triangle of light on far cheek; optimal for masculine portraits
- **CTR**: Click-Through Rate
- **Uncanny Valley**: Phenomenon where humanoid objects imperfectly resembling humans provoke unease
- **Key-to-Fill Ratio**: Contrast ratio between main light and fill light; higher = more dramatic shadows

## Requirements

### Requirement 1: Context-Specific Avatar Generation

**User Story:** As a user, I want to generate avatars optimized for my specific use case, so that my profile photo maximizes engagement for my target audience.

#### Acceptance Criteria

1. THE System SHALL support contexts: Corporate/LinkedIn, Creative Professional, Tech/Startup, Music Artist/Performer, Social Media Influencer, E-commerce/Trust-Critical
2. THE System SHALL support gender specification: Male, Female, or Neutral/Universal
3. THE System SHALL support cultural targeting: Western, Asian, or Universal
4. WHEN generating Corporate avatar THEN use professional studio lighting, formal attire, confident expression, neutral/warm background
5. WHEN generating Creative Professional avatar THEN use artistic lighting, personality-forward styling, warm tones
6. WHEN generating Tech/Startup avatar THEN use modern minimalist aesthetic, casual-professional balance, clean backgrounds
7. WHEN generating Music Artist avatar THEN use dramatic lighting, high contrast, genre-appropriate styling
8. WHEN generating Social Media avatar THEN use bright genuine smile, warm golden hour lighting, vibrant colors
9. WHEN generating E-commerce avatar THEN maximize trustworthiness with warm smile, direct eye contact, professional attire

### Requirement 2: Gender-Specific Face Characteristics

**User Story:** As a user, I want scientifically-optimized facial characteristics appropriate for my gender, so that my avatar maximizes charisma, trust, and likability.

#### Acceptance Criteria - Universal (All Genders)

1. THE avatar SHALL include Duchenne smile (teeth visible, eye crinkles) - increases likability +1.35
2. THE avatar SHALL include slight squinch (lower lid tension) - increases influence +0.37
3. THE avatar SHALL include direct eye contact with camera
4. THE avatar SHALL include natural facial symmetry with subtle asymmetry for realism
5. THE System SHALL NOT generate avatars with sunglasses (-0.36 likability), extreme close-ups, dark photos, oversaturated colors, or fake smiles

#### Acceptance Criteria - Male Avatars

1. THE male avatar SHALL include defined jawline with mature masculine features
2. THE male avatar SHALL include moderate fWHR (facial width-to-height ratio) for leadership perception
3. THE male avatar SHALL include confident expression without aggression
4. THE male avatar SHALL NOT include baby-face features (reduces competence perception)
5. THE male avatar SHALL NOT include extreme masculine features (reduces trustworthiness)
6. WHEN Western audience THEN emphasize angular features, defined jaw, healthy skin tone
7. WHEN Asian audience THEN use refined features, V-shaped face line, flawless porcelain skin

#### Acceptance Criteria - Female Avatars

1. THE female avatar SHALL include soft feminine features with high cheekbones
2. THE female avatar SHALL include large eyes relative to face size
3. THE female avatar SHALL include full lips and refined features
4. THE female avatar SHALL include soft rounded facial contours
5. THE female avatar SHALL include warm genuine smile with eye engagement
6. WHEN Western audience THEN natural healthy skin tone, expressive features
7. WHEN Asian audience THEN V-shaped face, porcelain skin, delicate refined features

### Requirement 3: Gender-Specific Pose and Body Language

**User Story:** As a user, I want optimal pose and body language for my gender, so that my avatar projects appropriate confidence and approachability.

#### Acceptance Criteria - Male Avatars

1. THE male avatar SHALL use head level position or very slight downward tilt
2. THE male avatar SHALL use minimal or no lateral head tilt (more authoritative)
3. THE male avatar SHALL use shoulders facing camera directly or slight angle
4. THE male avatar SHALL project confident open body language
5. THE male avatar SHALL NOT use head tilted back (perceived as confrontational)

#### Acceptance Criteria - Female Avatars

1. THE female avatar SHALL use slight chin-down tilt (makes eyes appear larger, more feminine)
2. THE female avatar MAY include slight lateral head tilt (increases approachability)
3. THE female avatar SHALL use 45-degree body angle to camera (more dynamic, visually slimming)
4. THE female avatar SHALL project confident warmth without excessive submission
5. THE female avatar SHALL NOT use head tilted back (unfeminine angle per research)

### Requirement 4: Composition Rules

**User Story:** As a user, I want optimal composition, so that my avatar performs well across platforms.

#### Acceptance Criteria

1. THE avatar SHALL have face coverage ~85% of frame with tight head crop and minimal shoulders visible (full face only reduces likability -0.21)
2. THE avatar SHALL use tight head crop framing — face must dominate the frame, shoulders barely visible at bottom edge
3. THE avatar SHALL use eye level or slightly above camera angle
4. THE avatar SHALL use neutral or warm background tones (+35% CTR)
5. THE avatar SHALL use 1:1 aspect ratio
6. THE avatar SHALL NOT use full body framing (reduces competence -0.29, influence -0.29)
7. THE avatar SHALL optimize for "golden proportions": eye-mouth distance ~36% face length, inter-eye distance ~46% face width

### Requirement 5: Gender-Specific Lighting Guidelines

**User Story:** As a user, I want lighting appropriate for my gender and context, so that it conveys the right impression.

#### Acceptance Criteria - Male Avatars

1. WHEN Corporate/Professional THEN use Rembrandt lighting (45° side angle, triangle on far cheek)
2. THE male avatar SHALL use 3:1 to 4:1 key-to-fill lighting ratio (defined shadows)
3. WHEN dramatic effect needed THEN may increase to 8:1 ratio
4. THE male avatar lighting SHALL emphasize facial structure and jawline
5. THE male avatar MAY use slightly cooler color temperature (3500-4500K)

#### Acceptance Criteria - Female Avatars

1. WHEN Corporate/Professional THEN use Butterfly lighting (directly above at 45° down)
2. THE female avatar SHALL use 2:1 to 3:1 key-to-fill lighting ratio (soft shadows)
3. THE female avatar lighting SHALL create even, symmetrical illumination
4. THE female avatar SHALL use warm color temperature (3000-3500K)
5. THE female avatar lighting SHALL emphasize cheekbones and soft features

#### Acceptance Criteria - Universal

1. WHEN soft natural lighting THEN generate most trustworthy appearance (universal default)
2. WHEN golden hour lighting THEN generate warm, approachable appearance (social, creative)
3. WHEN dramatic rim lighting THEN generate artistic, memorable appearance (artists)
4. THE System SHALL NOT generate avatars with harsh shadows on face
5. THE System SHALL NOT generate flat, shadowless lighting (lacks dimension)

### Requirement 6: Gender-Specific Attire and Colors

**User Story:** As a user, I want attire and colors optimized for professional perception by gender.

#### Acceptance Criteria - Male Avatars

1. WHEN Corporate THEN use navy blue (#000080, #202A44) or charcoal gray (#36454F) suit
2. WHEN Corporate THEN use crisp white or light blue dress shirt
3. THE male avatar SHALL NOT use orange clothing (25% associate with unprofessionalism per CareerBuilder)
4. WHEN Tech/Startup THEN use quality casual button-up in blue, gray, or deep green
5. THE male avatar colors SHALL convey: blue=trust/teamwork, black=leadership, gray=logic

#### Acceptance Criteria - Female Avatars

1. WHEN Corporate THEN use jewel tones: emerald (#2E5A4C), burgundy (#800020), deep blue (#000080), plum
2. THE female avatar SHALL use modest professional neckline (low necklines reduce competence perception per Howlett 2015)
3. THE female avatar SHALL use tailored, well-fitted professional attire
4. THE female avatar SHALL NOT use orange or neon bright colors
5. WHEN Creative THEN may use warmer tones and personality-forward styling

#### Acceptance Criteria - Universal

1. THE avatar SHALL avoid busy patterns and thin stripes (moiré effect)
2. THE avatar SHALL use solid colors or subtle textures
3. THE avatar attire SHALL match industry expectations

### Requirement 7: Platform-Specific Output

**User Story:** As a user, I want correct sizing for my target platform.

#### Acceptance Criteria

1. WHEN LinkedIn THEN generate 640×640 minimum, face 85%
2. WHEN YouTube THEN generate 800×800, high contrast, center-weighted
3. WHEN Instagram THEN generate 320×320, circular crop optimized
4. WHEN Spotify THEN generate 750×750, no text overlay
5. WHEN Apple Music THEN generate 2400×2400, strict quality
6. WHEN Universal THEN generate 2400×2400 PNG, 1:1 ratio

### Requirement 8: Realism (Uncanny Valley Avoidance)

**User Story:** As a user, I want realistic natural avatars without uncanny valley effect.

#### Acceptance Criteria

1. THE avatar SHALL include natural skin texture with visible pores
2. THE avatar SHALL include subtle skin imperfections (context-appropriate)
3. THE avatar SHALL include detailed glossy eyes with natural reflections
4. THE avatar SHALL include natural facial asymmetry
5. THE System SHALL NOT generate plastic/waxy skin, dead eyes, oversized eyes, or airbrushed perfection
6. WHEN Asian audience THEN skin may be smoother but must retain realistic texture

### Requirement 9: Cultural Adaptation

**User Story:** As a user, I want my avatar optimized for my target cultural audience.

#### Acceptance Criteria - Western Audience

1. THE avatar SHALL include warm expressive smile (75% of Western professional photos include smile)
2. THE avatar SHALL use natural healthy skin tone with warmth
3. THE male avatar SHALL emphasize defined angular features
4. THE female avatar SHALL balance warmth with competence signals

#### Acceptance Criteria - Asian Audience

1. THE avatar MAY use more neutral/subtle expression (31% smile rate in Asian professional photos)
2. THE avatar SHALL emphasize flawless, porcelain skin quality
3. THE male avatar SHALL use refined, elegant features (kkot-minam aesthetic acceptable)
4. THE female avatar SHALL emphasize V-shaped face, large eyes, delicate features
5. THE avatar SHALL use formal conservative attire emphasis

#### Acceptance Criteria - Universal/Global

1. THE avatar SHALL use symmetrical features (universal attractiveness signal)
2. THE avatar SHALL use clean, healthy skin
3. THE avatar SHALL use direct eye contact
4. THE avatar SHALL use professional, well-groomed appearance

### Requirement 10: Trust Psychology Compliance

**User Story:** As a user, I want my avatar to pass trust psychology checks.

#### Acceptance Criteria

1. THE avatar SHALL pass mandatory checklist: Duchenne smile, direct eye contact, slight squinch, head/shoulders framing, appropriate lighting, appropriate attire, natural skin
2. THE System SHALL reject trust-reducing elements: sunglasses, extreme framing, underexposed photos, oversaturated colors, busy backgrounds, fake smiles, perfect AI skin
3. THE avatar SHALL optimize for PhotoFeeler metrics: Competence, Likability, Influence

### Requirement 11: Error Handling

**User Story:** As a user, I want clear feedback when generation fails.

#### Acceptance Criteria

1. IF generation fails THEN present error to user with description
2. THE System SHALL NOT auto-retry without explicit user approval
3. WHEN error occurs THEN offer retry option to user

---

## Prompt Templates

### Corporate/LinkedIn - Male
```
Professional corporate headshot of a man, tight head crop with face filling 85% of frame, minimal shoulders visible, eye level camera angle, direct eye contact, Duchenne smile with visible teeth and eye crinkles, slight squinch, defined jawline with mature masculine features, moderate fWHR, confident expression, head level position, navy blue suit with crisp white dress shirt, Rembrandt lighting with 4:1 key-to-fill ratio creating triangle of light on far cheek, neutral charcoal gray background, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, Canon EOS R5, 85mm f/1.4, sharp focus --ar 1:1 --style raw
```

### Corporate/LinkedIn - Female
```
Professional corporate headshot of a woman, tight head crop with face filling 85% of frame, minimal shoulders visible, 45-degree body angle to camera, eye level camera angle, direct eye contact, warm Duchenne smile with visible teeth and eye crinkles, slight squinch, soft feminine features with high cheekbones, chin slightly lowered, burgundy or deep blue tailored blazer with modest professional neckline, butterfly lighting with 2:1 key-to-fill ratio creating soft even illumination, warm color temperature 3200K, neutral warm background, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, Canon EOS R5, 85mm f/1.4, sharp focus --ar 1:1 --style raw
```

### Creative Professional - Male
```
Creative professional portrait of a man, tight head crop with face filling 85% of frame, minimal shoulders visible, eye level camera angle, direct eye contact, Duchenne smile with visible teeth and eye crinkles, slight squinch, defined masculine features, confident relaxed expression, casual smart attire in charcoal or deep blue, warm Rembrandt lighting with 3:1 ratio, no harsh shadows on face, soft bokeh background with warm tones, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, artistic but professional, 85mm lens --ar 1:1 --style raw
```

### Creative Professional - Female
```
Creative professional portrait of a woman, tight head crop with face filling 85% of frame, minimal shoulders visible, 45-degree body angle, eye level camera angle, direct eye contact, warm genuine Duchenne smile with eye crinkles, soft feminine features with high cheekbones, slight head tilt, emerald or plum creative professional attire, warm golden hour style lighting with soft diffusion, no harsh shadows on face, soft bokeh background with warm tones, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, artistic and approachable, 85mm lens --ar 1:1 --style raw
```

### Tech/Startup - Male
```
Modern tech professional headshot of a man, tight head crop with face filling 85% of frame, minimal shoulders visible, eye level camera angle, direct eye contact, Duchenne smile with visible teeth and eye crinkles, slight squinch, friendly confident expression, defined but approachable features, casual quality button-up shirt in blue or gray, soft natural lighting with subtle Rembrandt influence, no harsh shadows on face, clean minimal white or light gray background, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, Silicon Valley aesthetic --ar 1:1 --style raw
```

### Tech/Startup - Female
```
Modern tech professional headshot of a woman, tight head crop with face filling 85% of frame, minimal shoulders visible, slight body angle, eye level camera angle, direct eye contact, bright genuine Duchenne smile with eye crinkles, soft feminine features, friendly approachable expression, quality casual blouse in teal or soft blue, soft diffused natural lighting, no harsh shadows on face, clean minimal white or light gray background, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, modern tech aesthetic --ar 1:1 --style raw
```

### Music Artist - Male
```
Artist portrait of a man, tight head crop with face filling 85% of frame, minimal shoulders visible, eye level camera angle, direct eye contact, Duchenne smile with eye crinkles or intense confident expression, slight squinch, strong defined features, expressive confident pose, dramatic Rembrandt lighting with 6:1 ratio, no harsh shadows obscuring features, dark moody background with subtle color accent, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, cinematic quality, personality-forward --ar 1:1 --style raw
```

### Music Artist - Female
```
Artist portrait of a woman, tight head crop with face filling 85% of frame, minimal shoulders visible, dynamic body angle, eye level camera angle, direct eye contact, expressive confident expression with Duchenne smile or artistic intensity, striking feminine features, dramatic butterfly lighting with rim accent, dark moody background with subtle color accent, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, cinematic quality, personality-forward, high fashion influence --ar 1:1 --style raw
```

### Social Media - Male
```
Engaging social media portrait of a man, tight head crop with face filling 85% of frame, minimal shoulders visible, eye level camera angle, direct eye contact, bright Duchenne smile with visible teeth and eye crinkles, slight squinch, friendly approachable masculine features, casual stylish attire, warm golden hour lighting, no harsh shadows on face, soft colorful background, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, high contrast for thumbnail visibility, approachable and relatable energy --ar 1:1 --style raw
```

### Social Media - Female
```
Engaging social media portrait of a woman, tight head crop with face filling 85% of frame, minimal shoulders visible, 45-degree body angle, eye level camera angle, direct eye contact, bright warm Duchenne smile with visible teeth and eye crinkles, soft feminine features with warm expression, slight natural head tilt, colorful casual stylish attire, warm golden hour lighting with soft glow, no harsh shadows on face, soft vibrant background, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, high contrast for thumbnail visibility, approachable and relatable energy --ar 1:1 --style raw
```

### E-commerce - Male
```
Trustworthy professional portrait of a man, tight head crop with face filling 85% of frame, minimal shoulders visible, eye level camera angle, direct eye contact, warm Duchenne smile with visible teeth and eye crinkles, slight squinch, reliable mature features, professional attire in navy or charcoal, soft natural lighting with Rembrandt influence, no harsh shadows on face, clean neutral background, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, confidence without arrogance, approachable expert aesthetic --ar 1:1 --style raw
```

### E-commerce - Female
```
Trustworthy professional portrait of a woman, tight head crop with face filling 85% of frame, minimal shoulders visible, slight body angle, eye level camera angle, direct eye contact, warm genuine Duchenne smile with visible teeth and eye crinkles, soft trustworthy feminine features, professional attire in jewel tones with modest neckline, soft butterfly lighting with warm temperature, no harsh shadows on face, clean neutral background, natural skin texture with visible pores, subtle skin imperfections, glossy eyes with natural reflections, natural facial asymmetry, confidence and warmth, approachable expert aesthetic --ar 1:1 --style raw
```

### Corporate - Asian Market - Male
```
Professional corporate headshot of a man, tight head crop with face filling 85% of frame, minimal shoulders visible, eye level camera angle, direct eye contact, subtle confident expression with slight smile, refined elegant masculine features, V-shaped face line, immaculate grooming, formal dark navy suit with white dress shirt, soft diffused studio lighting with minimal shadows, clean neutral background, flawless porcelain skin with subtle realistic texture, glossy eyes with natural reflections, formal conservative aesthetic, 85mm f/1.4, sharp focus --ar 1:1 --style raw
```

### Corporate - Asian Market - Female
```
Professional corporate headshot of a woman, tight head crop with face filling 85% of frame, minimal shoulders visible, slight body angle, eye level camera angle, direct eye contact, elegant subtle smile, refined delicate feminine features, V-shaped face, large expressive eyes, formal professional attire in deep blue or burgundy with conservative neckline, soft even butterfly lighting, clean neutral background, flawless porcelain skin with subtle realistic texture, glossy eyes with natural reflections, elegant sophisticated aesthetic, 85mm f/1.4, sharp focus --ar 1:1 --style raw
```

---

## Negative Prompts (Always Include)

### Universal Negative Prompts
```
worst quality, low quality, blurry, bad anatomy, poorly drawn face, extra eyes, oversized eyes, deformed, plastic skin, waxy skin, dead eyes, vacant expression, asymmetric ears, double face, flawless skin, perfect features, airbrushed, sunglasses, eyes obscured, full body shot, extreme close-up, busy background, orange clothing, neon colors, too much headroom, small face in frame, distant framing, wide shot, half body shot
```

### Additional Male-Specific Negative Prompts
```
baby face, childish features, round soft face, head tilted back, excessive head tilt, feminine features, weak jawline, overly aggressive expression, menacing look
```

### Additional Female-Specific Negative Prompts
```
harsh hard lighting, high contrast shadows, head tilted back, chin up angle, low neckline, revealing clothing, heavy contour makeup, masculine angular features, stern expression
```

### Asian Market Additional Negative Prompts
```
heavy tan, dark skin tone, excessive visible pores, acne, freckles prominent, heavy western contouring, overly casual attire
```

---

## PhotoFeeler Metrics Reference

| Element | Competence | Likability | Influence |
|---------|------------|------------|-----------|
| Open smile with teeth | +0.33 | **+1.35** | +0.22 |
| Formal dark attire | +0.94 | — | **+1.29** |
| Squinch (eye squint) | +0.33 | +0.22 | +0.37 |
| Defined jawline (male) | +0.24 | +0.18 | +0.18 |
| Sunglasses | — | **-0.36** | — |
| Full body in frame | -0.29 | — | -0.29 |
| Face-only extreme closeup | — | -0.21 | — |

---

## Gender-Lighting Quick Reference

| Gender | Primary Pattern | Key:Fill Ratio | Color Temp | Shadow Style |
|--------|----------------|----------------|------------|--------------|
| Male | Rembrandt | 3:1 to 4:1 | 3500-4500K | Defined, sculpting |
| Female | Butterfly | 2:1 to 3:1 | 3000-3500K | Soft, minimal |
| Neutral | Loop/Natural | 2:1 to 3:1 | 3200-3800K | Moderate |

---

## Cultural Adaptation Quick Reference

| Aspect | Western | Asian | Universal |
|--------|---------|-------|-----------|
| Smile | Warm, expressive (75%) | Subtle, elegant (31%) | Natural, genuine |
| Skin | Natural with warmth | Porcelain, flawless | Healthy, clear |
| Male features | Angular, defined jaw | Refined, V-shape | Balanced, mature |
| Female features | Expressive, warm | Delicate, V-shape | Soft, feminine |
| Attire | Industry-appropriate | Formal, conservative | Professional |
| Expression | Dynamic, personality | Reserved, elegant | Confident, approachable |
