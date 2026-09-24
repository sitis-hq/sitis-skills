---
description: Generate illustrated avatars for children's fairy tale authors optimized for global audience trust, parent confidence, child engagement, and cross-platform consistency. Use when asked to "create author avatar for children's books", "generate fairy tale author profile picture", "make avatar for kids book writer", "design children's author illustration", "create storyteller avatar", or "avatar for children's literature author".
---

# Requirements Document

## Introduction

This document defines requirements for the "Children's Author Avatar Generation" skill — an AI-powered illustrated avatar generation system optimized for parent trust perception, child emotional engagement, cross-cultural safety, and multi-platform consistency. The skill enables generation of warm, handmade-style illustrated avatars for children's fairy tale authors that function as effective brand assets from Amazon to TikTok.

Scientific foundation: First impressions form in 100 milliseconds (Willis & Todorov, 2006). Fiske, Cuddy & Glick (2007) showed people evaluate strangers on warmth (primary) and competence (secondary) — for children's authors, warmth must dominate. LinkedIn data confirms profiles with photos receive 21x more views. Bente et al. (2014) found avatar trust effect amplifies when other trust signals are weak — critical for new authors without ratings. Boyatzis & Varghese (1994) showed children 5-6 positively react to bright warm colors and negatively to dark tones. Frontiers in Psychology (2023) eye-tracking study on 108 children aged 4-7 confirmed preference for medium-high brightness with moderate saturation. 65% of successful children's books in 2024 featured handmade aesthetics (Neolemon, 2025). The mere exposure effect (Zajonc, 1968) proves consistent visual identity across platforms builds trust through repetition.

## Glossary

- **Handmade Aesthetic**: Visual style conveying human artistry — watercolor, mixed-media, hand-drawn — as opposed to digital perfection; 65% of top children's books 2024 use this approach
- **Watercolor Style**: Fluid, translucent painting technique ideal for fairy tales; conveys warmth, dreaminess, and artistry (Beatrix Potter tradition)
- **Mixed-Media Style**: Combination of techniques (watercolor + ink + collage) creating rich textured illustrations (Eric Carle tradition)
- **Mascot Companion**: A fairy tale creature appearing alongside the author avatar — builds franchise potential and child engagement (Mo Willems' Pigeon, Pete the Cat model)
- **Color Signature**: 2-3 consistent brand colors used across all platforms for instant recognition
- **Circular Safe Zone**: Central 80% of avatar area where all key elements must fit — critical for YouTube, TikTok, Instagram circular crop
- **Warmth Perception**: Primary trust axis (Fiske et al., 2007) — evaluated before competence; avatar must radiate friendliness, safety, kindness
- **Mere Exposure Effect**: Zajonc (1968) — repeated exposure to consistent visual identity increases positive attitude, even unconsciously
- **Bouba/Kiki Effect**: Cross-cultural association of rounded shapes with warmth and angular shapes with sharpness — applies to visual avatar design
- **Cultural Neutrality**: Design approach avoiding symbols, animals, or colors with negative connotations in major world cultures

## Requirements

### Requirement 1: Input Gathering

**User Story:** As a children's fairy tale author, I want to provide context about my creative vision and brand, so that the generated avatar aligns with my books' world, target audience, and authorial persona.

#### Acceptance Criteria

1. THE System SHALL request author persona type: warm storyteller, wise mentor, playful trickster, mysterious narrator, gentle dreamer
2. THE System SHALL request target age group: 0-3 toddlers, 4-7 picture books, 8-12 middle grade, mixed/all ages
3. THE System SHALL request primary art style preference: watercolor, mixed-media/collage, hand-drawn/sketch, soft digital illustration
4. THE System SHALL request gender presentation: feminine, masculine, neutral/androgynous
5. THE System SHALL request color signature preference or allow system to recommend based on research
6. THE System SHALL request mascot companion preference: type of creature (rabbit, butterfly, owl, cat, fantasy creature, none) or allow system to recommend
7. THE System SHALL request target markets: global/universal, Western, Eastern European/Russian, Asian, Latin American
8. THE System SHALL request book style reference if available (existing illustrations, mood boards, color palettes)
9. THE System SHALL request platform priority: Amazon/ЛитРес (square), YouTube/TikTok/Instagram (circular crop), universal
10. THE System SHALL NOT auto-generate without confirming at minimum: persona type, gender presentation, and art style


### Requirement 2: Art Style Selection

**User Story:** As a children's fairy tale author, I want my avatar in a handmade artistic style that matches my books' illustrations, so that parents perceive artistry and children feel warmth.

#### Acceptance Criteria

1. THE avatar SHALL use a handmade aesthetic — visible artistic process, "hand of the master" feel
2. THE avatar SHALL NOT use photorealistic style — children's authors benefit from illustrated branding over photography
3. THE avatar SHALL NOT use 3D render style — lacks warmth, risks Uncanny Valley
4. THE avatar SHALL NOT use flat/corporate minimalist style — too cold for fairy tales

#### Acceptance Criteria — Watercolor Style (Default for Fairy Tales)

1. WHEN watercolor style THEN use fluid translucent washes, soft edges, visible paper texture
2. WHEN watercolor style THEN convey dreaminess, gentleness, and bedtime-story quality
3. WHEN watercolor style THEN use wet-on-wet technique appearance for soft color transitions
4. WHEN watercolor style THEN reference tradition: Beatrix Potter, Quentin Blake softened

#### Acceptance Criteria — Mixed-Media / Collage Style

1. WHEN mixed-media style THEN combine watercolor + ink outlines + paper texture layers
2. WHEN mixed-media style THEN convey playfulness, creativity, and tactile richness
3. WHEN mixed-media style THEN reference tradition: Eric Carle, Ezra Jack Keats

#### Acceptance Criteria — Hand-Drawn / Sketch Style

1. WHEN hand-drawn style THEN use visible pencil/ink lines, crosshatching, doodle energy
2. WHEN hand-drawn style THEN convey spontaneity, humor, and creative energy
3. WHEN hand-drawn style THEN reference tradition: Quentin Blake, Shel Silverstein
4. WHEN hand-drawn style THEN ensure professional quality — rough ≠ sloppy

#### Acceptance Criteria — Soft Digital Illustration

1. WHEN soft digital style THEN mimic hand-painted quality with digital tools
2. WHEN soft digital style THEN use visible brush strokes, texture overlays, imperfect edges
3. WHEN soft digital style THEN avoid plastic/vector perfection — must feel human-made
4. WHEN soft digital style THEN reference tradition: Oliver Jeffers, Jon Klassen


### Requirement 3: Color Signature System

**User Story:** As a children's fairy tale author, I want a scientifically-grounded color palette that attracts children and reassures parents across cultures, so that my avatar works globally.

#### Acceptance Criteria — Color Science

1. THE avatar SHALL use 2-3 primary brand colors + 1 accent color consistently
2. THE avatar SHALL use medium-high brightness with moderate saturation (children's preference per Frontiers in Psychology 2023 eye-tracking study)
3. THE avatar SHALL NOT use dark dominant tones (brown, black, gray) — children react negatively (Boyatzis & Varghese, 1994)
4. THE avatar SHALL NOT use oversaturated neon colors — perceived as cheap/untrustworthy by parents

#### Acceptance Criteria — Recommended Global-Safe Palettes

1. WHEN "Enchanted Forest" palette THEN use: warm teal (#4A9B8E), golden amber (#E8A849), soft cream (#FFF5E1), coral accent (#E87461)
2. WHEN "Starlight Dreams" palette THEN use: soft lavender-blue (#7B9ACC), warm gold (#D4A843), ivory (#FFF8F0), rose accent (#D4727A)
3. WHEN "Meadow Tales" palette THEN use: sage green (#7BAF6E), warm honey (#D4A24E), soft peach (#FFE5D4), sky blue accent (#6BA3C7)
4. WHEN "Ocean Stories" palette THEN use: warm ocean blue (#5B8DB8), sandy gold (#D4B86A), soft white (#FFF9F2), coral accent (#E8836B)
5. WHEN custom palette THEN validate against cultural safety rules below

#### Acceptance Criteria — Cross-Cultural Color Safety

1. THE avatar SHALL NOT use white as dominant color — mourning in China, Japan, India, Korea
2. THE avatar SHALL NOT use pure yellow as dominant color — mourning in Egypt and parts of Latin America
3. THE avatar SHALL NOT use purple/violet as dominant color — mourning in Brazil, India, Thailand
4. THE avatar SHALL NOT use black as dominant color — negative associations for children universally
5. THE avatar MAY use green carefully — sacred in Islam (respectful context required), "green hat" = infidelity in China
6. THE avatar MAY use red as accent — love in West, luck in China, but mourning in parts of Africa
7. THE safe global primaries ARE: warm blues, golden yellows, nature greens, coral/salmon tones


### Requirement 4: Author Figure Design

**User Story:** As a children's fairy tale author, I want my illustrated avatar to convey warmth, creativity, and trustworthiness, so that parents feel safe and children feel invited.

#### Acceptance Criteria — Universal

1. THE author figure SHALL have a warm genuine smile — open, inviting, Duchenne-like (eye crinkles even in illustration)
2. THE author figure SHALL have kind, expressive eyes with direct "eye contact" toward viewer
3. THE author figure SHALL convey approachability — soft rounded features preferred over angular (bouba/kiki effect)
4. THE author figure SHALL include fairy tale context elements: books, quill pen, magical sparkles, stars, leaves, lantern, reading glasses on nose
5. THE author figure SHALL occupy 60-70% of frame — enough presence with room for magical environment
6. THE author figure SHALL NOT look threatening, stern, or cold
7. THE author figure SHALL NOT be photorealistic — stylized illustration matching book art style

#### Acceptance Criteria — Feminine Presentation

1. WHEN feminine THEN use soft rounded features, warm expressive eyes, gentle smile
2. WHEN feminine THEN may include: flowing hair with fairy tale elements woven in (flowers, stars, leaves), cozy shawl or cardigan, reading glasses
3. WHEN feminine THEN convey: wise grandmother / kind fairy godmother / gentle storyteller archetype

#### Acceptance Criteria — Masculine Presentation

1. WHEN masculine THEN use friendly rounded features, warm eyes, approachable smile
2. WHEN masculine THEN may include: cozy sweater or vest, reading glasses, book in hand, gentle beard or mustache
3. WHEN masculine THEN convey: kind grandfather / friendly wizard / warm storyteller archetype

#### Acceptance Criteria — Neutral/Androgynous Presentation

1. WHEN neutral THEN use soft features without strong gender markers
2. WHEN neutral THEN focus on storyteller attributes: books, magical elements, cozy attire
3. WHEN neutral THEN convey: ageless storyteller / magical narrator archetype


### Requirement 5: Mascot Companion Design

**User Story:** As a children's fairy tale author, I want an optional mascot companion in my avatar, so that I build franchise potential and create an emotional anchor for children.

#### Acceptance Criteria — General

1. THE mascot SHALL be a secondary element — author figure remains primary focus
2. THE mascot SHALL be positioned near the author (on shoulder, peeking from behind, sitting on book, flying nearby)
3. THE mascot SHALL match the art style of the author figure exactly
4. THE mascot SHALL have expressive, friendly features — large eyes, warm expression
5. THE mascot SHALL be simple enough to be recognizable at 98px display size
6. THE mascot MAY be used independently for content, merch, and social media posts

#### Acceptance Criteria — Culturally Safe Mascot Choices

1. THE System SHALL recommend universally safe animals: rabbits, butterflies, birds (songbirds), cats, bears (teddy-style), hedgehogs, squirrels
2. THE System SHALL recommend safe fantasy creatures: star spirits, tiny fairies, friendly dragons (stylized/cute), magical fireflies, enchanted flowers with faces
3. THE System SHALL warn about culturally sensitive animals:
   - Owls — wisdom in West, bad omen in Middle East and parts of Asia
   - Pigs — popular in Western fairy tales, taboo in Islamic cultures
   - Dogs — beloved in West, considered unclean in some Islamic traditions
   - Snakes — wisdom in some cultures, evil in others
4. THE System SHALL warn about culturally loaded fantasy creatures:
   - Dragons — villains in West, noble in East Asia (design must be clearly cute/friendly to avoid confusion)
5. WHEN global audience THEN prefer: rabbits, butterflies, cats, star spirits, magical fireflies
6. WHEN Russian/Eastern European audience THEN also safe: hedgehogs (Ёжик), bears (Мишка), foxes (Лисичка)


### Requirement 6: Composition & Framing Rules

**User Story:** As a children's fairy tale author, I want optimal composition that works across all platforms, so that my avatar is recognizable from Amazon square to TikTok circle at 98px.

#### Acceptance Criteria

1. THE avatar SHALL use 1:1 square aspect ratio as master format
2. THE avatar SHALL place all key elements (face, mascot, core magical details) within central 80% circle — safe zone for circular crop
3. THE avatar SHALL be recognizable and readable at 98px display size (YouTube comment minimum)
4. THE avatar SHALL use soft, warm background — gradient, bokeh, or simple fairy tale environment (starry sky, forest glow, cozy room)
5. THE avatar SHALL NOT use busy detailed backgrounds that compete with the author figure
6. THE avatar SHALL NOT place critical elements in corners (will be cropped in circular display)
7. THE avatar SHALL include subtle magical atmosphere: soft glow, floating sparkles, gentle light rays, fairy dust
8. THE avatar background SHALL use colors from the chosen color signature palette

### Requirement 7: Platform-Specific Output

**User Story:** As a children's fairy tale author, I want correct sizing for all my publishing and social platforms.

#### Acceptance Criteria

1. THE master file SHALL be 2000×2000 pixels minimum
2. WHEN Amazon Author Central / ЛитРес THEN square display, minimum 300×300 px, JPG/PNG
3. WHEN YouTube THEN 800×800 px upload, displays at 98×98 px minimum, circular crop, high contrast required
4. WHEN TikTok THEN 720×720 px, displays at 200×200 px, circular crop
5. WHEN Instagram THEN 720×720 px, displays at 110×110 px, circular crop
6. WHEN website/blog THEN 400×400+ px, variable display
7. WHEN universal (default) THEN generate 2000×2000 PNG, 1:1 ratio, optimized for both square and circular crop
8. THE System SHALL test: is the author's face and mascot clearly distinguishable at 98px? If not — simplify the design


### Requirement 8: Persona-Specific Optimization

**User Story:** As a children's fairy tale author, I want my avatar to reflect my authorial persona, so that the visual identity tells the first story before the book is opened.

#### Acceptance Criteria

1. WHEN "warm storyteller" THEN use: soft warm lighting, cozy environment (armchair, fireplace glow, blanket), gentle smile, book in hand or lap, warm color palette, mascot curled up nearby
2. WHEN "wise mentor" THEN use: gentle authority, reading glasses, surrounded by books and scrolls, soft magical glow, slightly elevated perspective, mascot looking up at author with admiration
3. WHEN "playful trickster" THEN use: mischievous warm smile, dynamic pose, colorful chaotic elements (flying books, scattered stars, paint splashes), bright saturated palette, mascot in playful action
4. WHEN "mysterious narrator" THEN use: enigmatic gentle smile, moonlit or twilight atmosphere, cloak or hood (soft, not threatening), glowing book or lantern, deeper jewel-tone palette, mascot peeking from shadows
5. WHEN "gentle dreamer" THEN use: soft dreamy expression, eyes slightly upward, floating/ethereal elements (clouds, stars, bubbles), pastel palette, mascot floating or sleeping nearby

### Requirement 9: Age-Group Visual Optimization

**User Story:** As a children's fairy tale author, I want my avatar optimized for my target readers' age group, so that it resonates with both children and their parents.

#### Acceptance Criteria

1. WHEN 0-3 (toddlers/board books) THEN maximize softness: ultra-round shapes, pastel colors, maximum warmth, simple composition, large friendly face, very simple mascot
2. WHEN 4-7 (picture books) THEN balance warmth with wonder: bright colors, magical details, expressive face, playful mascot interaction, fairy tale environment visible
3. WHEN 8-12 (middle grade) THEN allow more complexity: richer details, deeper colors, more atmospheric environment, mascot with personality, hint of adventure/mystery
4. WHEN mixed/all ages THEN optimize for 4-7 sweet spot while maintaining sophistication for parents — the "Beatrix Potter balance"


### Requirement 10: Cultural Adaptation

**User Story:** As a children's fairy tale author targeting specific markets, I want my avatar adapted for cultural expectations, so that it resonates locally while remaining globally safe.

#### Acceptance Criteria — Universal/Global (Default)

1. THE avatar SHALL use nature-based fairy tale elements (trees, stars, moon, flowers) — positive across all cultures
2. THE avatar SHALL avoid culture-specific clothing, symbols, or architectural elements
3. THE avatar SHALL use the global-safe color palette (warm blues, golden yellows, nature greens, coral accents)
4. THE avatar SHALL use a fantasy/fairy tale creature as mascot rather than culturally loaded real animals

#### Acceptance Criteria — Western Markets

1. WHEN Western THEN may include: classic fairy tale elements (castles in background, enchanted forests), warmer expressive smile, slightly more saturated colors
2. WHEN Western THEN safe mascots: any from universal list + owls, foxes

#### Acceptance Criteria — Russian/Eastern European Markets

1. WHEN Russian/Eastern European THEN may include: rich illustrative tradition elements (detailed nature, birch trees, folk patterns as subtle accents), gуашь/watercolor aesthetic in tradition of Сутеев, Васнецов, Конашевич
2. WHEN Russian/Eastern European THEN safe mascots: hedgehogs (Ёжик), bears (Мишка), foxes (Лисичка), cats (Котик), hares (Зайчик)
3. WHEN Russian/Eastern European THEN use richer, more detailed illustration style — this market values visible artistic mastery

#### Acceptance Criteria — Asian Markets

1. WHEN Asian THEN use cleaner, less visually cluttered composition (PMC/NIH research: Asian preference for visual simplicity)
2. WHEN Asian THEN may use softer, more delicate line work
3. WHEN Asian THEN avoid: number 4 in any form, white as dominant color, green hats
4. WHEN Asian THEN safe mascots: rabbits (Moon Rabbit tradition), cats (Maneki-neko positive association), butterflies, birds

#### Acceptance Criteria — Latin American Markets

1. WHEN Latin American THEN may use warmer, more vibrant color palette
2. WHEN Latin American THEN avoid: yellow as dominant color, skull imagery
3. WHEN Latin American THEN safe mascots: butterflies (mariposas), birds (colibríes), rabbits

### Requirement 11: Trust & Anti-AI Perception

**User Story:** As a children's fairy tale author, I want my avatar to be perceived as authentically human-created, so that I avoid the anti-AI backlash in children's publishing.

#### Acceptance Criteria

1. THE avatar SHALL include visible artistic imperfections: slightly uneven lines, natural color bleeding, paper texture, brush stroke variations
2. THE avatar SHALL NOT have pixel-perfect symmetry — subtle asymmetry signals human creation
3. THE avatar SHALL NOT have the "AI sheen" — overly smooth gradients, plastic-looking surfaces, generic perfection
4. THE avatar SHALL include texture elements: paper grain, watercolor blooms, ink splatter, pencil marks (style-appropriate)
5. THE avatar SHALL feel like it could be a page from the author's own book
6. THE System SHALL recommend: commission a human illustrator for final production avatar; use AI-generated version as concept/reference only


### Requirement 12: Prohibited Elements

**User Story:** As a children's fairy tale author, I want to avoid visual elements that reduce trust, alienate audiences, or damage my brand.

#### Acceptance Criteria — Visual Prohibitions

1. THE avatar SHALL NOT use dark, threatening, or horror-adjacent imagery
2. THE avatar SHALL NOT use photorealistic human faces (uncanny valley risk in illustrated context)
3. THE avatar SHALL NOT use corporate/business attire (suit, tie) — wrong genre signal
4. THE avatar SHALL NOT use sunglasses or anything obscuring the eyes — reduces trust
5. THE avatar SHALL NOT use busy patterns or excessive detail that becomes noise at small sizes
6. THE avatar SHALL NOT use text or typography within the avatar image
7. THE avatar SHALL NOT use trademarked or copyrighted characters or visual elements

#### Acceptance Criteria — Style Prohibitions

1. THE avatar SHALL NOT use anime/manga style as primary (niche perception in Western and Middle Eastern markets)
2. THE avatar SHALL NOT use hyper-realistic digital painting (conflicts with handmade aesthetic requirement)
3. THE avatar SHALL NOT use vector/flat design (too corporate for fairy tales)
4. THE avatar SHALL NOT use grunge, distressed, or dark artistic treatments
5. THE avatar SHALL NOT use excessive filters or post-processing effects

#### Acceptance Criteria — Cultural Prohibitions

1. THE avatar SHALL NOT use religious symbols of any tradition
2. THE avatar SHALL NOT use national flags or political symbols
3. THE avatar SHALL NOT use culturally appropriated elements (indigenous patterns, sacred symbols)
4. THE avatar SHALL NOT use gender stereotypes beyond gentle archetypal warmth

### Requirement 13: Error Handling

**User Story:** As a user, I want clear feedback when generation fails or cannot proceed.

#### Acceptance Criteria

1. IF generation fails THEN present error to user with description
2. THE System SHALL NOT auto-retry without explicit user approval
3. WHEN error occurs THEN offer retry option to user
4. IF persona type and art style are not specified THEN refuse generation and request minimum inputs
5. IF cultural conflict is detected in color/mascot choice THEN warn with specific explanation and affected market

---

## Prompt Templates

### Watercolor — Warm Storyteller — Feminine
```
Warm watercolor illustration of a kind feminine storyteller, portrait style, face occupying 65% of frame, soft rounded features, warm genuine smile with eye crinkles, kind expressive eyes looking directly at viewer, reading glasses perched on nose, cozy knitted shawl in warm teal, flowing hair with tiny golden stars woven in, holding an open glowing book, small friendly [MASCOT] sitting on her shoulder, soft golden ambient light, floating fairy dust particles, watercolor paper texture visible, wet-on-wet color transitions, color palette: warm teal and golden amber and soft cream with coral accents, dreamy fairy tale atmosphere, Beatrix Potter meets modern children's book illustration, visible brush strokes, natural color bleeding at edges, handmade artistic quality --ar 1:1 --style raw
```

### Watercolor — Warm Storyteller — Masculine
```
Warm watercolor illustration of a kind masculine storyteller, portrait style, face occupying 65% of frame, friendly rounded features, warm genuine smile with eye crinkles, kind expressive eyes looking directly at viewer, gentle short beard, cozy knitted sweater in warm teal, reading glasses, holding an open glowing book on his lap, small friendly [MASCOT] peeking from behind his shoulder, soft golden ambient light, floating fairy dust particles, watercolor paper texture visible, wet-on-wet color transitions, color palette: warm teal and golden amber and soft cream with coral accents, cozy fireside fairy tale atmosphere, handmade artistic quality, visible brush strokes, natural color bleeding --ar 1:1 --style raw
```

### Watercolor — Wise Mentor — Feminine
```
Warm watercolor illustration of a wise feminine mentor figure, portrait style, face occupying 65% of frame, gentle authoritative expression, warm knowing smile, kind wise eyes with reading glasses, silver-streaked hair in soft updo with tiny flowers, elegant shawl in sage green, surrounded by floating old books and scrolls, small [MASCOT] looking up at her admiringly, soft magical glow emanating from an ancient book, color palette: sage green and warm honey and soft peach with sky blue accents, library-meets-enchanted-garden atmosphere, watercolor paper texture, visible artistic brushwork, Beatrix Potter tradition --ar 1:1 --style raw
```

### Watercolor — Wise Mentor — Masculine
```
Warm watercolor illustration of a wise masculine mentor figure, portrait style, face occupying 65% of frame, gentle authoritative expression, warm knowing smile, kind wise eyes behind round reading glasses, distinguished silver hair, cozy vest over soft shirt in sage green tones, surrounded by floating old books and scrolls, small [MASCOT] perched on a stack of books nearby, soft magical glow from an ancient tome, color palette: sage green and warm honey and soft peach with sky blue accents, cozy study-meets-enchanted-library atmosphere, watercolor paper texture, visible artistic brushwork --ar 1:1 --style raw
```


### Watercolor — Playful Trickster — Feminine
```
Warm watercolor illustration of a playful feminine trickster storyteller, portrait style, face occupying 65% of frame, mischievous warm smile, bright sparkling eyes looking directly at viewer, colorful messy hair with paint splashes and tiny stars, paint-stained apron over bright coral top, dynamic slightly tilted pose, flying open books and scattered stars around her, small [MASCOT] in playful mid-leap pose, bright saturated watercolor splashes in background, color palette: warm teal and golden amber and coral with bright accents, joyful chaotic creative energy, visible paint drips and watercolor blooms, handmade artistic quality --ar 1:1 --style raw
```

### Watercolor — Playful Trickster — Masculine
```
Warm watercolor illustration of a playful masculine trickster storyteller, portrait style, face occupying 65% of frame, mischievous warm grin, bright sparkling eyes looking directly at viewer, tousled hair with ink spots, paint-stained rolled-up sleeves, colorful vest with mismatched buttons, dynamic slightly tilted pose, flying open books and scattered stars around him, small [MASCOT] in playful mid-leap pose, bright saturated watercolor splashes in background, color palette: warm teal and golden amber and coral with bright accents, joyful creative chaos, visible paint drips and watercolor blooms --ar 1:1 --style raw
```

### Watercolor — Mysterious Narrator — Feminine
```
Warm watercolor illustration of an enigmatic feminine narrator, portrait style, face occupying 65% of frame, gentle mysterious smile, deep knowing eyes looking directly at viewer, dark flowing hair with tiny glowing stars, soft hooded cloak in deep lavender-blue, holding a glowing lantern that illuminates her face warmly, small [MASCOT] peeking from cloak folds with glowing eyes, moonlit twilight atmosphere, floating fireflies, color palette: soft lavender-blue and warm gold and ivory with rose accents, enchanted twilight forest background softly blurred, watercolor wet-on-wet technique, mysterious but warm and inviting not threatening --ar 1:1 --style raw
```

### Watercolor — Mysterious Narrator — Masculine
```
Warm watercolor illustration of an enigmatic masculine narrator, portrait style, face occupying 65% of frame, gentle mysterious smile, deep knowing eyes looking directly at viewer behind round spectacles, distinguished features with gentle expression, soft hooded traveling cloak in deep lavender-blue, holding a glowing ancient book that illuminates his face warmly, small [MASCOT] peeking from cloak with curious expression, moonlit twilight atmosphere, floating fireflies, color palette: soft lavender-blue and warm gold and ivory with rose accents, enchanted twilight path background softly blurred, watercolor technique, mysterious but warm --ar 1:1 --style raw
```

### Watercolor — Gentle Dreamer — Feminine
```
Warm watercolor illustration of a gentle feminine dreamer storyteller, portrait style, face occupying 65% of frame, soft dreamy expression, eyes gazing slightly upward with wonder, delicate features, flowing hair dissolving into clouds and stars at the edges, soft flowing dress in pastel tones, floating among gentle clouds and golden stars, small [MASCOT] sleeping peacefully on a tiny cloud nearby, ethereal soft-focus atmosphere, color palette: soft lavender-blue and warm gold and ivory with gentle rose, everything slightly floating and weightless, ultra-soft watercolor washes, dreamlike quality, lullaby atmosphere --ar 1:1 --style raw
```

### Watercolor — Gentle Dreamer — Masculine
```
Warm watercolor illustration of a gentle masculine dreamer storyteller, portrait style, face occupying 65% of frame, soft dreamy expression, eyes gazing slightly upward with wonder, gentle features, soft tousled hair, cozy oversized cardigan in pastel tones, sitting on a crescent moon with an open book, small [MASCOT] sleeping peacefully in his lap, surrounded by floating golden stars and gentle clouds, color palette: soft lavender-blue and warm gold and ivory with gentle rose, everything slightly floating and weightless, ultra-soft watercolor washes, dreamlike lullaby atmosphere --ar 1:1 --style raw
```


### Mixed-Media — Warm Storyteller — Feminine
```
Mixed-media children's book illustration of a kind feminine storyteller, portrait style, face occupying 65% of frame, warm genuine smile with eye crinkles, kind expressive eyes, collage paper texture layers, ink outlines with watercolor fills, torn paper edges visible, cozy patterned cardigan in warm teal with fabric texture collage, holding a colorful handmade book, small [MASCOT] made of collage paper pieces sitting nearby, layered paper background with stamped patterns, color palette: warm teal and golden amber and soft cream with coral accents, Eric Carle meets Ezra Jack Keats aesthetic, visible glue edges and paper layers, tactile handmade quality --ar 1:1 --style raw
```

### Mixed-Media — Warm Storyteller — Masculine
```
Mixed-media children's book illustration of a kind masculine storyteller, portrait style, face occupying 65% of frame, warm genuine smile, friendly expressive eyes, collage paper texture layers, ink outlines with watercolor fills, torn paper edges, cozy patterned sweater in warm teal with fabric texture collage, book open on his knee, small [MASCOT] made of collage paper pieces on his shoulder, layered paper background with stamped patterns, color palette: warm teal and golden amber and soft cream with coral accents, tactile handmade collage quality, visible paper layers and ink lines --ar 1:1 --style raw
```

### Hand-Drawn — Playful Trickster — Feminine
```
Hand-drawn ink and watercolor wash illustration of a playful feminine trickster storyteller, portrait style, face occupying 65% of frame, mischievous warm smile, bright expressive eyes, loose confident ink line work, crosshatching for shadows, watercolor wash accents, wild expressive hair with doodle stars and swirls, casual creative outfit with ink splatter details, surrounded by doodle-style flying books and sparkles, small [MASCOT] drawn in matching sketchy style mid-bounce, color palette: warm teal and golden amber and coral accents on cream paper, Quentin Blake energy with warmth, visible pencil underdrawing, spontaneous artistic quality --ar 1:1 --style raw
```

### Hand-Drawn — Playful Trickster — Masculine
```
Hand-drawn ink and watercolor wash illustration of a playful masculine trickster storyteller, portrait style, face occupying 65% of frame, mischievous warm grin, bright expressive eyes, loose confident ink line work, crosshatching for shadows, watercolor wash accents, tousled hair with doodle stars, casual rolled-up sleeves with ink stains, surrounded by doodle-style flying books and sparkles, small [MASCOT] drawn in matching sketchy style mid-leap, color palette: warm teal and golden amber and coral accents on cream paper, Quentin Blake meets Shel Silverstein energy, visible pencil marks, spontaneous quality --ar 1:1 --style raw
```

### Soft Digital — Warm Storyteller — Feminine (Russian/Eastern European Market)
```
Richly detailed digital illustration in Russian children's book tradition, portrait style of a kind feminine storyteller, face occupying 65% of frame, warm genuine smile, kind wise eyes, soft rounded features, cozy embroidered shawl with subtle folk pattern accents in warm teal, braided hair with tiny wildflowers, holding an ornate fairy tale book with golden edges, small [MASCOT] nestled in her arms, background of soft birch trees and wildflower meadow in gentle focus, golden hour warm light, color palette: warm teal and golden amber and soft cream with coral accents, Сутеев meets modern illustration quality, rich but not cluttered, visible digital brush strokes mimicking gouache, warm handmade feel --ar 1:1 --style raw
```

### Soft Digital — Warm Storyteller — Masculine (Russian/Eastern European Market)
```
Richly detailed digital illustration in Russian children's book tradition, portrait style of a kind masculine storyteller, face occupying 65% of frame, warm genuine smile, kind wise eyes behind round glasses, gentle features with soft beard, cozy knitted sweater with subtle folk pattern in warm teal, sitting by a window with birch trees visible, holding an ornate fairy tale book, small [MASCOT] sitting on the windowsill looking at him, golden hour warm light streaming in, color palette: warm teal and golden amber and soft cream with coral accents, rich illustrative tradition, visible digital brush strokes mimicking gouache, warm handmade feel --ar 1:1 --style raw
```


---

## Negative Prompts (Always Include)

### Universal Negative Prompts for Children's Author Avatars
```
worst quality, low quality, blurry, bad anatomy, poorly drawn face, extra eyes, oversized eyes, deformed, plastic skin, waxy skin, dead eyes, vacant expression, photorealistic, 3D render, vector art, flat design, corporate style, anime style, manga style, dark mood, horror, threatening, scary, aggressive expression, stern face, frown, sunglasses, eyes obscured, full body shot, extreme close-up, busy background, cluttered composition, text in image, watermark, logo, neon colors, oversaturated, black dominant, white dominant, purple dominant, corporate attire, suit and tie, business formal, AI-generated look, perfect symmetry, plastic smooth gradients, generic stock photo feel, dark shadows on face, harsh lighting
```

### Additional Watercolor-Specific Negative Prompts
```
digital perfection, vector clean lines, pixel-perfect edges, smooth gradients without texture, no paper texture, plastic appearance, uniform flat color fills, mechanical precision
```

### Additional Mixed-Media-Specific Negative Prompts
```
clean digital art, smooth surfaces, no texture layers, uniform appearance, single-technique look, no paper edges visible
```

### Additional Hand-Drawn-Specific Negative Prompts
```
clean vector lines, perfect curves, digital smoothness, no pencil marks, no ink variation, mechanical line weight, sterile appearance
```

---

## Mascot Substitution Guide

Replace `[MASCOT]` in prompt templates with one of the following based on user choice:

| Mascot | Prompt Substitution | Global Safety |
|--------|-------------------|---------------|
| Rabbit | `cute fluffy rabbit with big expressive eyes` | ✓ Universal |
| Butterfly | `colorful magical butterfly with glowing wings` | ✓ Universal |
| Cat | `small friendly cat with warm expressive eyes` | ✓ Universal (minor caution: some cultures) |
| Songbird | `tiny colorful songbird with bright eyes` | ✓ Universal |
| Bear (teddy) | `small cute teddy bear with button eyes` | ✓ Universal |
| Hedgehog | `tiny friendly hedgehog with curious expression` | ✓ Universal (strong in Russian market) |
| Squirrel | `small fluffy squirrel with bushy tail` | ✓ Universal |
| Star spirit | `tiny glowing star spirit with a friendly face` | ✓ Universal (fantasy) |
| Firefly | `magical glowing firefly with warm golden light` | ✓ Universal (fantasy) |
| Fairy | `tiny friendly fairy with translucent wings` | ✓ Universal (fantasy) |
| Fox | `small friendly fox with warm amber eyes` | ⚠️ Trickster connotation in some cultures |
| Owl | `small wise owl with big round eyes` | ⚠️ Bad omen in Middle East/parts of Asia |
| Dragon (cute) | `tiny cute baby dragon with big innocent eyes` | ⚠️ Villain in West, noble in East Asia |

---

## Color Palette Quick Reference

| Palette Name | Primary 1 | Primary 2 | Base | Accent | Best For |
|-------------|-----------|-----------|------|--------|----------|
| Enchanted Forest | Warm teal #4A9B8E | Golden amber #E8A849 | Soft cream #FFF5E1 | Coral #E87461 | Warm storyteller, nature themes |
| Starlight Dreams | Lavender-blue #7B9ACC | Warm gold #D4A843 | Ivory #FFF8F0 | Rose #D4727A | Gentle dreamer, mysterious narrator |
| Meadow Tales | Sage green #7BAF6E | Warm honey #D4A24E | Soft peach #FFE5D4 | Sky blue #6BA3C7 | Wise mentor, nature themes |
| Ocean Stories | Warm ocean blue #5B8DB8 | Sandy gold #D4B86A | Soft white #FFF9F2 | Coral #E8836B | Adventure, playful trickster |

---

## Persona-Visual Mapping Quick Reference

| Persona | Lighting | Environment | Expression | Mascot Behavior | Color Intensity |
|---------|----------|-------------|------------|-----------------|-----------------|
| Warm Storyteller | Soft golden glow | Cozy fireside / armchair | Gentle warm smile | Curled up / nestled | Medium-warm |
| Wise Mentor | Soft magical glow | Library / book-filled | Knowing gentle smile | Looking up admiringly | Medium |
| Playful Trickster | Bright dynamic | Creative chaos | Mischievous grin | Mid-leap / playful | High-saturated |
| Mysterious Narrator | Moonlit twilight | Enchanted forest / path | Enigmatic gentle smile | Peeking from shadows | Deep jewel tones |
| Gentle Dreamer | Ethereal soft | Clouds / stars / floating | Dreamy upward gaze | Sleeping / floating | Soft pastels |

---

## Age Group Visual Optimization Quick Reference

| Age Group | Shape Language | Color Saturation | Detail Level | Composition | Mascot Style |
|-----------|--------------|------------------|--------------|-------------|--------------|
| 0-3 (toddlers) | Ultra-round, soft | Soft pastels | Minimal, simple | Very clean, large face | Simple, round, cute |
| 4-7 (picture books) | Round with some variety | Medium-bright | Moderate, magical details | Balanced, room for wonder | Expressive, interactive |
| 8-12 (middle grade) | More varied, some angles | Richer, deeper | Rich, atmospheric | Complex, environmental | Personality-driven |
| Mixed/all ages | Round-dominant, gentle variety | Medium, warm | Moderate with key details | Balanced (4-7 sweet spot) | Friendly, clear |

---

## Platform Technical Requirements

| Platform | Upload Size | Display Size | Crop Shape | Format | Key Consideration |
|----------|------------|-------------|------------|--------|-------------------|
| Master file | 2000×2000 px | — | — | PNG | Source for all derivatives |
| Amazon Author Central | min 300×300 px | varies | Square | JPG/PNG | Trust-critical, book buyers |
| ЛитРес | ~300×300+ px | varies | Square | JPG/PNG | "Page with photo = more trust" |
| YouTube | 800×800 px | 98×98 px min | Circle | JPG/PNG | Test at 98px — must be readable |
| TikTok | 720×720 px | 200×200 px | Circle | JPG/PNG | High contrast for small display |
| Instagram | 720×720 px | 110×110 px | Circle | JPG/PNG | Must work at tiny size |
| Website/blog | 400×400+ px | varies | Varies | JPG/PNG | Flexible, can show more detail |

---

## Cross-Cultural Color Safety Quick Reference

| Color | Safe Regions | Caution Regions | Risk |
|-------|-------------|-----------------|------|
| Warm blue | ✓ Global | — | None — universally trusted |
| Golden yellow | ✓ Most regions | ⚠️ Egypt, parts of Latin America (mourning) | Low if not dominant |
| Nature green | ✓ Most regions | ⚠️ Islam (sacred, respectful use), China (green hat = infidelity) | Low with awareness |
| Coral/salmon | ✓ Global | — | None — universally warm |
| White (dominant) | ✓ West | ✗ China, Japan, India, Korea (mourning) | High as dominant |
| Purple (dominant) | ✓ West | ✗ Brazil, India, Thailand (mourning) | High as dominant |
| Black (dominant) | — | ✗ Global for children (negative associations) | High |
| Red (dominant) | ✓ China (luck) | ⚠️ Parts of Africa (mourning) | Medium |

---

## Generation Workflow

1. Gather inputs (persona, gender, art style, colors, mascot, market, age group, platform)
2. Select appropriate prompt template based on art style + persona + gender
3. Substitute `[MASCOT]` with chosen mascot description from substitution guide
4. Adjust color references if custom palette chosen (validate cultural safety)
5. Adjust detail level and composition based on age group
6. Adjust cultural elements based on target market
7. Add universal negative prompts + style-specific negative prompts
8. Generate avatar
9. Validate: readable at 98px? Key elements in central 80% circle? Handmade feel? Warm and inviting?
10. Present to user with platform adaptation recommendations

---

## Brand Consistency Reminder

The avatar is one element of a three-asset brand system:

1. **Primary** — This illustrated avatar (all social platforms, author pages)
2. **Secondary** — Mascot character standalone (content, merch, children's engagement)
3. **Tertiary** — Professional photograph (press kits, interviews, adult contexts)

All three assets should share the same color signature. The illustrated avatar and mascot must share the same art style. Consistency across all platforms activates the mere exposure effect — 7+ contacts build trust → recognition → loyalty.