---
description: Generate professional song lyrics optimized for commercial success and genre authenticity. Use when asked to "write lyrics", "generate lyrics", "create song text", "write a song", "write verses", or "create lyrics for track".
---

# Requirements Document

## Introduction

This document defines requirements for the "Music Lyrics Generation" skill — an AI-powered lyric writing system grounded in evidence-based parameters for commercial success, genre authenticity, and emotional resonance. The skill enables generation of professional song lyrics calibrated to specific genres, moods, and structural conventions.

Scientific foundation: Large-scale NLP studies (Parada-Cabaleiro et al., 2024, *Scientific Reports*, 353,320 songs; Varnum et al., 2021, *PLOS ONE*, 14,661 Billboard songs) demonstrate that lyrical simplicity correlates with chart performance, and more compressible (repetitive) songs reach higher chart positions (z = 2.30, p = .02). Yet topically atypical songs outperform by one chart position per 16% increase in differentiation (Berger & Packard, 2018, *Psychological Science*). The central principle: conform to genre conventions on most parameters, then deviate meaningfully on one or two.

## Glossary

- **Processing Fluency**: Ease with which lyrics are cognitively processed — driven by rhyme, repetition, familiar structures, and simple vocabulary
- **Optimal Distinctiveness**: Conforming to genre conventions on most parameters while deviating meaningfully on one or two for memorability
- **Hook**: The most memorable, repeatable lyrical phrase — typically the title, placed in the chorus
- **Rhyme Density**: Number of rhymes per line — highest in hip-hop (up to 3.04/line), lowest in lo-fi/indie
- **Lexical Diversity**: Ratio of unique words to total words — inversely correlated with commercial success in most genres
- **Compression Ratio**: How much a lyric can be compressed via repetition — top-10 songs compress ~50%
- **Syllabic Mirroring**: Matching syllable counts and stress patterns across corresponding lines in different verses
- **Refrain-Anchor Line**: A recurring line that grounds the listener during extended narrative or imagery passages
- **Inverted-U Curve**: Berlyne's model — liking peaks at moderate familiarity/complexity, declines at extremes
- **AABA Form**: 32-bar jazz standard structure — two A sections, contrasting B (bridge), final A
- **Riserchorus**: EDM structure blending rising sonic intensity with a lyrical-melodic hook before the drop
- **Onomatopoeic Hook**: A hook built on sound-imitative words that function simultaneously as rhythm, texture, and meaning (e.g., "click-clack" for train wheels)
- **Character-as-Hook**: Using a vivid character name or persona as the primary hook — the name itself becomes the memorable element (e.g., "Cactus Jack")
- **Mantra Hook**: A short phrase repeated with meditative intensity, gaining emotional weight through repetition rather than variation (e.g., "Ride on, ride on")
- **Phonetic Texture**: The deliberate arrangement of consonant and vowel sounds within a line for rhythmic and sonic effect — alliteration, assonance, consonance, and plosive/fricative patterning
- **Kinetic Imagery**: Imagery built on physical movement and sensory action rather than static description — every line implies motion, sound, or tactile sensation
- **Show Don't Tell**: Conveying emotion through concrete sensory details and actions rather than naming the emotion directly ("dust on my brim, rust on my badge" vs. "I was a worn-out outlaw")
- **Narrative Arc**: The emotional and dramatic trajectory within a lyric — setup (verse 1) → development (verse 2) → climax (bridge) → resolution (final chorus/outro)

## Requirements

### Requirement 1: Genre Detection and Parameter Calibration

**User Story:** As a songwriter, I want lyrics calibrated to my target genre, so that the output matches audience expectations and commercial conventions.

#### Acceptance Criteria

1. WHEN genre is specified THEN apply all genre-specific parameters from the Genre Parameter Matrix
2. WHEN genre is NOT specified THEN ask the user before generating
3. WHEN subgenre is specified (e.g., "trap", "bedroom pop", "outlaw country") THEN apply subgenre-specific overrides
4. THE system SHALL calibrate all 10 parameters simultaneously: rhyme scheme, song structure, lyrical themes, vocabulary complexity, repetition level, syllable count, emotional valence, authenticity markers, point of view, title/hook placement
5. WHEN cross-genre fusion is requested THEN use the primary genre as base and selectively incorporate secondary genre elements

### Requirement 2: Rhyme Scheme Application

**User Story:** As a songwriter, I want genre-appropriate rhyme patterns, so that my lyrics sound natural within the target genre.

#### Acceptance Criteria

1. WHEN Pop THEN use ABAB as primary scheme, slant/near rhymes preferred over perfect rhymes, different schemes between verse and chorus for contrast
2. WHEN Hip-Hop/Rap THEN use high rhyme density (2–3 rhymes per line), multisyllabic rhymes, internal rhymes at 46%+ of total rhymes, moderate complexity (avoid extremes)
3. WHEN Rock/Metal THEN use ABAB or AABB with end rhyme predominating, less internal rhyme than hip-hop
4. WHEN Indie/Alternative THEN use slant rhyme, assonance, near-rhyme; abandon strict rhyme when prose-like flow serves the lyric better
5. WHEN Electronic/EDM THEN use minimal formal rhyme; phrase repetition replaces rhyme as primary sonic pattern; simple AABB or ABAB when rhymed lyrics are present
6. WHEN Lo-Fi/Chill THEN use basic ABAB or AABB with relaxed, non-rigorous approach; rhyme should feel incidental
7. WHEN Jazz THEN use highly crafted AABB or ABAB with sophisticated internal rhymes, multi-syllabic rhymes, wit and precision
8. WHEN Classical/Opera THEN use formal poetic rhyme schemes determined by the text's literary tradition
9. WHEN Modern Country THEN use XAXA predominantly (lines 2 and 4 rhyme), perfect and identity rhyme, increasing internal rhymes
10. WHEN Outlaw/Traditional Country THEN use ABAB or ABCB ballad forms, more tolerance for near-rhyme and narrative flow
11. WHEN Americana/Indie Country THEN use the most varied schemes — near-rhyme, slant rhyme, unrhymed passages all acceptable

### Requirement 3: Song Structure

**User Story:** As a songwriter, I want properly structured lyrics, so that the song follows genre conventions and flows naturally.

#### Acceptance Criteria

1. WHEN Pop THEN use ABABCB (verse-chorus-verse-chorus-bridge-chorus) as default; chorus within first 50 seconds; limit to 3–4 individual sections; target ~3:00 song length
2. WHEN Hip-Hop/Rap THEN use Intro → Hook → Verse (12–16 bars) → Hook → Verse → Hook → Outro; first chorus at ~38 seconds; verses may shrink to 8–12 bars in modern style
3. WHEN Rock/Metal THEN use standard VCVCBC; guitar solo position at bridge; progressive subgenres allow extended/through-composed structures
4. WHEN Indie/Alternative THEN allow atypical structures — through-composed, absent choruses, extended tracks, dynamic shifts; structural freedom is a core aesthetic value
5. WHEN Electronic/EDM THEN use Verse → Riser → Drop structure; compound AAA forms (three rotations); lyrics minimal — single phrases looping as sonic elements
6. WHEN Lo-Fi/Chill THEN use simple verse-chorus or looping patterns; short songs (2–3 minutes); no bridges or pre-choruses
7. WHEN Jazz THEN use 32-bar AABA as default; also ABAC, ABAB, 12-bar blues; different lyrics over each A section melody
8. WHEN Classical/Opera THEN use recitative (plot-driving) and aria (emotional expression) modes; strophic, through-composed, or modified strophic for Lieder
9. WHEN Modern Country THEN use Verse-Chorus-Verse-Chorus-Bridge-Chorus (58% of #1 hits); title within 60 seconds; "you" within 18 seconds
10. WHEN Outlaw/Traditional Country THEN use simpler verse-verse-chorus or verse-with-refrain; longer songs acceptable; narrative progression over chorus repetition
11. WHEN Americana/Indie Country THEN use the most varied structures — folk forms, refrain-anchor lines, through-composed narrative poems set to music

### Requirement 4: Lyrical Themes

**User Story:** As a songwriter, I want thematically appropriate content, so that my lyrics resonate with the target audience.

#### Acceptance Criteria

1. WHEN Pop THEN center on love/relationships (60–73% of hits), self-empowerment, or sensuality; universal and relatable
2. WHEN Hip-Hop/Rap THEN draw from introspective themes (26.3% and rising), complex emotional patterns (28.3%), material wealth, social commentary; substance references common
3. WHEN Rock/Metal THEN use rebellion, personal freedom, existential questions, longing for intensity; metal: religion, dystopia, darkness, battle; power metal: fantasy, mythology
4. WHEN Indie/Alternative THEN use self-discovery, alienation, existential contemplation, identity, disillusionment; literary influences; heavy metaphor and symbolism
5. WHEN Electronic/EDM THEN use love, freedom, euphoria, escape, togetherness, the night/dance floor; abstract and universal over specific narrative
6. WHEN Lo-Fi/Chill THEN use anxiety, depression, mental health, loneliness, unrequited love, vulnerability, nostalgia; gentle emotional expression
7. WHEN Jazz THEN use love, heartbreak, nostalgia, joy, celebration; universal emotions with timeless quality; escapist rather than political
8. WHEN Classical/Opera THEN use mythology, love and death, political intrigue, sacrifice, the supernatural, nature, spiritual yearning
9. WHEN Modern Country THEN use story + hook + payoff; small-town life, trucks, drinking, romance, Friday nights; every lyric points toward title payoff
10. WHEN Outlaw/Traditional Country THEN use drinking as coping, heartbreak, defiance, redemption, working-class struggles, life on the road, anti-establishment
11. WHEN Americana/Indie Country THEN use the broadest range — social justice, personal reflection, class consciousness, regional specificity; songs as "weathered postcards from specific places"
12. WHEN user specifies a theme THEN adapt the theme to genre conventions while maintaining the user's intent

### Requirement 5: Vocabulary Complexity

**User Story:** As a songwriter, I want the right vocabulary level for my genre, so that the lyrics feel authentic and accessible to the target audience.

#### Acceptance Criteria

1. WHEN Pop THEN target grade 2.9 reading level; conversational register; sound over meaning — pick the word that sounds appealing
2. WHEN Hip-Hop/Rap THEN calibrate to subgenre: commercial trap uses minimal vocabulary; conscious/lyrical rap uses high vocabulary; moderate complexity correlates best with chart success
3. WHEN Rock/Metal THEN use moderate-high vocabulary; metal has least repetitive lyrics of all genres; ~52% lexical diversity benchmark
4. WHEN Indie/Alternative THEN use moderate-high vocabulary reflecting literary aspirations; sardonic wordplay, cryptic imagery, surrealist elements acceptable
5. WHEN Electronic/EDM THEN use minimal vocabulary when present; abstract and non-lexical vocalizations ("oh," "yeah") may replace semantic content
6. WHEN Lo-Fi/Chill THEN use minimal to moderate; simple conversational vocabulary focused on emotional honesty; lyrics as texture
7. WHEN Jazz THEN use the highest vocabulary sophistication — urbane, witty, economy with elegance; wordplay and double entendres
8. WHEN Classical/Opera THEN use the highest literary register; poetic and archaic vocabulary acceptable; word painting central
9. WHEN Modern Country THEN target grade 3.3 reading level; multi-syllable words and place names raise the level; conversational naturalness required
10. WHEN Outlaw/Traditional Country THEN use higher vocabulary than modern country; poetic sophistication (Kristofferson/Van Zandt standard)
11. WHEN Americana/Indie Country THEN use the highest vocabulary of any country subgenre; dense imagery, multiple interpretive layers; solo-writer model preserves richness

### Requirement 6: Repetition and Hook Engineering

**User Story:** As a songwriter, I want the right level of repetition for my genre, so that the lyrics are memorable without being monotonous.

#### Acceptance Criteria

1. WHEN Pop THEN use very high repetition; 3+ chorus occurrences; title as repetitive hook; "glue hook" (same lyric across different sections)
2. WHEN Hip-Hop/Rap THEN use hook-driven structure; simple memorable phrase in chorus; 8–12 bar verses with longer melodic hooks; title repeated 10+ times in commercial style
3. WHEN Rock/Metal THEN use low repetition (metal is lowest of all genres); guitar riff may serve as primary hook over lyrical phrase
4. WHEN Indie/Alternative THEN use low repetition; hooks may be melodic/textural/atmospheric rather than lyrical; absent chorus is a valid aesthetic choice
5. WHEN Electronic/EDM THEN use extreme sonic repetition; single phrases loop as sonic elements; the drop replaces chorus as primary hook
6. WHEN Lo-Fi/Chill THEN use moderate textual repetition; repetition creates sustained mood state; understated hooks
7. WHEN Jazz THEN use moderate structured repetition via AABA form; different lyrics over each A section; title as first or last line of A sections
8. WHEN Modern Country THEN use high repetition (~61%+ compression); more writers = more repetition; 3–5 chorus appearances
9. WHEN Outlaw/Traditional Country THEN use low repetition (~45%); narrative progression over chorus repetition; emphasis on storytelling
10. WHEN Americana/Indie Country THEN use low repetition (~45–50%); strong refrain-anchor lines without excessive repetition; lyrical density prioritized
11. THE hook SHALL be the most memorable phrase in the lyric
12. THE title SHALL appear in the hook/chorus unless genre conventions dictate otherwise (indie, Americana)

### Requirement 7: Syllable Count and Rhythmic Patterning

**User Story:** As a songwriter, I want natural rhythmic phrasing, so that the lyrics are singable and fit the musical meter.

#### Acceptance Criteria

1. WHEN Pop THEN use 6–10 syllables per line; common patterns 8-8-8-8 or 6-8-6-8; stressed syllable alignment across verses; iambic patterns dominate
2. WHEN Hip-Hop/Rap THEN use 10–13 syllables per line typical; ~4.5 syllables per second pace; rhythmic density varies by subgenre and delivery speed
3. WHEN Rock/Metal THEN use 7–10 for standard rock, 9–12+ for progressive; death metal/thrash: rapid syllable delivery; doom: stretched syllables
4. WHEN Indie/Alternative THEN allow highly variable counts; irregular phrasing, enjambment, unconventional stress patterns valued over regularity
5. WHEN Electronic/EDM THEN use short punchy phrases (4–8 syllables) aligned to BPM grid; vocal chops reduce lyrics to percussive elements
6. WHEN Lo-Fi/Chill THEN use sparse, short phrases; relaxed behind-the-beat delivery
7. WHEN Jazz THEN match syllables to melodic phrasing with precision; 8-bar phrase structure creates natural frameworks
8. WHEN Modern Country THEN use 7–9 syllables per line; natural speech rhythms; the "you wouldn't say it that way" test for naturalness
9. WHEN Outlaw/Traditional Country THEN use a strict 7–10 syllable cap per line — no "narrative stretch" exceptions. Lines exceeding 10 syllables MUST be re-written. Storytelling density SHALL be achieved through image compression (cutting articles, prepositions, weak verbs), not syllable inflation. Chorus B-lines (lines 2 and 4) SHOULD be 1–2 syllables shorter than A-lines to create syncopated breathing room for the vocalist
10. WHEN Americana/Indie Country THEN use variable narrative-driven counts; dense imagery may push counts higher
11. Line 1 of Verse 1 MUST match the stress pattern of Line 1 of Verse 2 (syllabic mirroring)
12. THE system SHALL apply Phonetic Texture techniques to create sonic richness beyond rhyme:
    - **Alliteration**: Repeated initial consonants within a line or couplet ("coal dust on tongue, heart steady and slow") — use for emphasis and rhythmic drive
    - **Assonance**: Repeated vowel sounds across words ("spurs strike a spark on the midnight road") — use for melodic flow and internal musicality
    - **Consonance**: Repeated consonant sounds in non-initial positions ("boot-heel, hoof-heel — one turning wheel") — use for percussive texture
    - **Plosive clusters** (b, d, g, k, p, t): Create rhythmic punch — best for uptempo, aggressive, or rhythmic passages
    - **Fricative/sibilant clusters** (f, s, sh, v, z): Create flowing, atmospheric texture — best for slow, contemplative, or mysterious passages
13. WHEN a line serves as a rhythmic anchor (pre-chorus, hook transition) THEN phonetic texture SHALL be maximized — sound pattern matters as much as meaning in these positions

### Requirement 8: Emotional Valence

**User Story:** As a songwriter, I want the right emotional tone for my genre and mood, so that the lyrics create the intended feeling.

#### Acceptance Criteria

1. WHEN Pop THEN trend toward mixed valence; Spotify data shows higher valence correlates with popularity (+7.3%); sorrowful endings score higher (peak-end rule)
2. WHEN Hip-Hop/Rap THEN note inverted trend: positive content now correlates with success (r = 0.29 in 2010s); highest emotional variance of any genre
3. WHEN Rock/Metal THEN use insecurity, loneliness, fearlessness, freedom, social condemnation; metal is lowest happiness valence; rock is the only genre where anger has not increased
4. WHEN Indie/Alternative THEN use melancholic but nuanced; emotional complexity and bittersweet sentiments; ambiguity is a feature
5. WHEN Electronic/EDM THEN use euphoric and escapist; positive energetic content; physical engagement over emotional depth
6. WHEN Lo-Fi/Chill THEN use melancholic to cozy; negative emotions expressed gently; vulnerability without intensity
7. WHEN Jazz THEN use positive to bittersweet; "sadness with levity, sorrow without becoming beleaguered"
8. WHEN Classical/Opera THEN use the widest emotional range — ecstatic joy to devastating grief, often within a single work
9. WHEN Modern Country THEN use positive sentiments predominantly; range from celebratory anthems to heartbreak ballads; nostalgia and pride
10. WHEN Outlaw/Traditional Country THEN use darker than modern country; honesty and vulnerability; anti-hero narrator sympathetic but flawed
11. WHEN Americana/Indie Country THEN use wide range with emphasis on nuanced, complex emotional states; bittersweet and contemplative
12. WHEN user specifies mood THEN calibrate valence to match while respecting genre norms

### Requirement 9: Authenticity Markers

**User Story:** As a songwriter, I want genre-authentic language and style, so that the lyrics feel genuine to the target audience.

#### Acceptance Criteria

1. WHEN Pop THEN use conversational register, emotional directness, phonesthetic devices (alliteration, assonance), relatable first-person narratives
2. WHEN Hip-Hop/Rap THEN use AAVE features (y'all, non-standard grammar, code-switching), regional dialect markers, perceived lived experience; no artist self-identifies as "commercial"
3. WHEN Rock/Metal THEN use raw emotional expression, rejection of commercial polish, confessional tone, anti-establishment stance; metal demands genre-specific vocabulary (darkness, defiance)
4. WHEN Indie/Alternative THEN use lo-fi aesthetic signals, vocal imperfections implied in phrasing, DIY ethos, specificity (real places, names, cultural artifacts), literary quality
5. WHEN Electronic/EDM THEN use chantable universal phrases, festival-ready dynamics, producer identity over vocal personality
6. WHEN Lo-Fi/Chill THEN use DIY production signals in lyrical style, anti-corporate sincerity, internet culture references, intimate confessional tone
7. WHEN Jazz THEN use musical sophistication, lyrical wit, interpretive nuance, connection to Great American Songbook tradition
8. WHEN Classical/Opera THEN use fidelity to literary tradition, proper language conventions, dramatic coherence, word-music unity
9. WHEN Modern Country THEN use "ain't," "y'all," contractions, dropped g's ("huntin'"), regional vocabulary ("tall boy," "holler," "backroad"), whiskey over beer, long Southern place names
10. WHEN Outlaw/Traditional Country THEN use self-written feel, stripped-down language, rejection of Nashville formula, autobiographical rootedness, genre-blending influences
11. WHEN Americana/Indie Country THEN use regional specificity (Appalachian vocabulary, specific settings), literary quality as authenticity marker, solo-writer voice

### Requirement 10: Point of View

**User Story:** As a songwriter, I want the right narrative perspective, so that the lyrics connect with listeners effectively.

#### Acceptance Criteria

1. WHEN Pop THEN use first person/direct address (I/you) as default; verses in looser perspective, choruses tighten to direct I/you address
2. WHEN Hip-Hop/Rap THEN use first person dominant; direct address to rivals/listeners/love interests; "boast" and "narrative" as primary modes
3. WHEN Rock/Metal THEN use first person for personal struggle/defiance; third person for mythological/historical storytelling (power metal, progressive)
4. WHEN Indie/Alternative THEN use deeply first-person/introspective; highly particular rather than universally relatable; confessional songwriting central
5. WHEN Electronic/EDM THEN use first person or collective "we" for communal experience; abstract "we" creates dance floor unity; many tracks need no POV
6. WHEN Lo-Fi/Chill THEN use first-person confessional, intimate; personal vulnerability and emotional honesty
7. WHEN Jazz THEN use first-person romantic/reflective; the performer's relationship to the lyric matters as much as the lyric itself
8. WHEN Classical/Opera THEN use multiple character perspectives (dialogue, soliloquy, ensemble); first-person lyric voice for Lieder
9. WHEN Modern Country THEN use first person + direct address ("you"); "you" within 18 seconds; first-person anthem mode over narrative storytelling
10. WHEN Outlaw/Traditional Country THEN use first-person confessional and third-person narrative in roughly equal measure; narrator as flawed outsider
11. WHEN Americana/Indie Country THEN use all POVs freely; third-person narrative more common; character-driven perspectives that may or may not be autobiographical

### Requirement 11: Title and Hook Placement

**User Story:** As a songwriter, I want strategic title/hook placement, so that the song is memorable and follows genre expectations.

#### Acceptance Criteria

1. WHEN Pop THEN place first chorus at ~0:42 (19% into song); title as primary hook in chorus repeated 3+ times; consider chorus-first opening (42% of modern hits)
2. WHEN Hip-Hop/Rap THEN place first hook at ~38 seconds; title repeated 10+ times in commercial style; simple repetitive hook as primary commercial driver
3. WHEN Rock/Metal THEN place title in chorus; allow instrumental hooks to carry songs; less formulaic placement than pop
4. WHEN Indie/Alternative THEN allow flexible/non-formulaic placement; title may appear once, not at all, or be unrelated to lyrics; hooks may be buried
5. WHEN Electronic/EDM THEN place title/hook in riser section before drop; drop itself is the primary hook (sonic, not lyrical); minimal title repetition
6. WHEN Lo-Fi/Chill THEN use non-formulaic placement; hook may be melodic phrase or production texture; understated chorus without emphatic repetition
7. WHEN Jazz THEN place title as first or last line of each A section in AABA; consistent structural anchor
8. WHEN Modern Country THEN place title in chorus, first use within 60 seconds; "write to the hook" — every lyric builds toward title payoff
9. WHEN Outlaw/Traditional Country THEN use refrain or title line, less rigidly placed; title may appear as last line of each verse; hook serves the story
10. WHEN Americana/Indie Country THEN use flexible placement; refrain-anchor lines carry title; memorable moment may be an image or narrative turn rather than repeated title

### Requirement 12: Cross-Genre Universal Rules

**User Story:** As a songwriter, I want lyrics that follow proven universal principles, so that the output is commercially viable regardless of genre.

#### Acceptance Criteria

1. THE lyrics SHALL apply the optimal distinctiveness principle: conform to genre conventions on most parameters, deviate meaningfully on one or two
2. THE lyrics SHALL prioritize processing fluency through rhyme, repetition, and familiar structures calibrated to genre
3. THE lyrics SHALL NOT exceed the vocabulary complexity ceiling for the target genre
4. THE lyrics SHALL use first-person pronouns as default unless genre or user specifies otherwise
5. THE lyrics SHALL front-load the hook/title according to genre timing conventions
6. THE lyrics SHALL maintain syllabic mirroring across corresponding verse lines
7. THE lyrics SHALL NOT include filler lines that don't serve the narrative, mood, or hook
8. THE lyrics SHALL be singable — no awkward consonant clusters, unnatural stress patterns, or tongue-twister phrases unless stylistically intentional
9. THE lyrics SHALL default to "Show, Don't Tell" — convey emotions and situations through concrete sensory details and actions rather than naming them directly. Abstract emotional statements ("I'm broken", "I feel lost", "love hurts") SHALL be replaced with physical, observable correlates unless the genre explicitly favors directness (Pop, EDM)
10. THE lyrics SHALL build a coherent image system — related images and metaphors that reinforce each other across the song, creating a unified sensory world rather than disconnected metaphors
11. THE lyrics SHALL avoid AI-vocalist singability hazards — these confuse synthetic vocal models (Suno, Udio, etc.) and produce mushy, off-rhythm delivery:
    - **Triple-negative clusters**: NO line may contain three or more negation words in sequence (e.g. "I don't sign no line for no Crown Vic" — `don't / no / no`). Two negatives max per line, and only when vernacular-justified
    - **Mid-line em-dashes (`—`) and inline direct speech**: AI vocalists ignore typographic cues and slur the cesura. Use line breaks or new sections instead of em-dashes mid-line. Direct speech inside a line (`Told him: "Son, you don't make law..."`) SHALL be rewritten as narration or moved to a dedicated line
    - **Heavy mid-line comma stacking**: more than one comma per line forces the vocalist to guess phrasing. Restructure to one cesura max per line
    - **Adjacent unstressed function words (3+)**: clusters like "for no Crown Vic", "on the dam I made", "than it ever did stand" pile weak syllables and break iambic flow. Replace with stressed-syllable substitutes or compress

### Requirement 13: Output Format

**User Story:** As a songwriter, I want clearly formatted lyrics, so that I can immediately use them.

#### Acceptance Criteria

1. THE output SHALL label each section (Verse 1, Chorus, Verse 2, Bridge, etc.)
2. THE output SHALL use blank lines between sections
3. THE output SHALL indicate repeated sections with notation (e.g., [Chorus repeats])
4. WHEN the user requests it THEN include annotations explaining structural choices, rhyme patterns, or genre-specific decisions
5. THE output SHALL specify the target genre and any subgenre at the top
6. IF the user provides a melody, tempo, or key THEN note how the lyrics align rhythmically

### Requirement 14: Error Handling and Clarification

**User Story:** As a user, I want clear feedback when my request needs refinement.

#### Acceptance Criteria

1. IF genre is ambiguous or missing THEN ask the user to specify before generating
2. IF the user requests conflicting parameters (e.g., "high vocabulary pop" or "simple Americana") THEN acknowledge the tension and propose a resolution
3. IF the requested theme is outside genre norms THEN generate but note the deviation and its potential impact
4. THE system SHALL NOT auto-generate without sufficient context (minimum: genre OR mood + theme)

### Requirement 15: Hook Typology

**User Story:** As a songwriter, I want to choose the right type of hook for my song, so that the memorability mechanism matches the genre, theme, and emotional intent.

#### Acceptance Criteria

1. THE system SHALL select a hook type from the following typology based on genre and theme:
   - **Title-Repetition Hook**: The title phrase repeated verbatim in the chorus. Default for Pop, Modern Country, Hip-Hop. Most commercially proven.
   - **Onomatopoeic Hook**: A sound-imitative word or phrase that doubles as rhythm and meaning (e.g., train wheels = "click-clack", gunshot = "bang", heartbeat = "boom-boom"). Best for: narrative-driven genres, cinematic themes, songs with strong physical settings. Creates instant sensory anchoring.
   - **Character-as-Hook**: A vivid character name or persona that IS the hook — the name carries personality, imagery, and story in a single phrase. Best for: country, hip-hop, novelty, character-driven narratives. The name must be phonetically memorable and visually evocative.
   - **Mantra Hook**: A short phrase (2–5 words) repeated with increasing emotional intensity, gaining weight through repetition rather than variation. Best for: Americana, folk, anthemic rock, spiritual/meditative themes. Works through rhythmic hypnosis.
   - **Phonetic Hook**: A phrase where the sound pattern (alliteration, assonance, consonance) is more memorable than the semantic content. Best for: pop, EDM, any genre where singability > meaning.
   - **Contrast Hook**: A phrase that works by juxtaposing contradictory ideas or images ("lonely crowd", "beautiful disaster"). Best for: indie, alternative, singer-songwriter.
   - **Question Hook**: A provocative or unanswered question that lodges in the listener's mind. Best for: pop, R&B, hip-hop.
2. WHEN the song theme involves strong physical setting or action THEN prefer Onomatopoeic or Mantra hooks over Title-Repetition
3. WHEN the song is character-driven THEN consider Character-as-Hook — the name must pass the "bar test" (can someone shout it across a bar and it sounds right?)
4. THE system MAY combine hook types (e.g., Onomatopoeic + Mantra: "click-clack, keep it rolling")
5. THE hook type SHALL be consistent with the genre's hook priority level from the Genre Parameter Matrix

### Requirement 16: Sensory and Cinematic Writing

**User Story:** As a songwriter, I want vivid, sensory lyrics that create mental images, so that listeners experience the song rather than just hear it.

#### Acceptance Criteria

1. THE system SHALL prefer concrete sensory details over abstract statements — "Show, Don't Tell" as default mode
2. EVERY verse SHALL contain at least 2 lines engaging different senses (sight, sound, touch, taste, smell)
3. THE system SHALL use Kinetic Imagery — lines that imply movement, physical action, or spatial change — especially in narrative genres (country, rock, hip-hop storytelling)
4. WHEN writing emotion THEN express it through physical correlates, not labels:
   - INSTEAD OF "I'm lonely" → "Empty chair, cold coffee, clock ticks on the wall"
   - INSTEAD OF "I'm angry" → "Knuckles white around the wheel, jaw set like a vice"
   - INSTEAD OF "I'm free" → "Wind pulls the hat off my head and I let it go"
5. THE system SHALL build a coherent image system per song — related images that reinforce each other across verses (e.g., train imagery: rails, coal dust, sparks, steel, smoke — all connected)
6. WHEN the genre is Pop or EDM THEN sensory density may be lower — prioritize phonetic hooks and emotional directness over dense imagery
7. WHEN the genre is Outlaw Country, Americana, Rock, or Indie THEN sensory density SHALL be high — every line earns its place through specificity
8. THE system SHALL avoid cliché sensory images ("tears like rain", "heart on fire", "broken wings") — prefer fresh, specific images rooted in the song's world

### Requirement 17: Narrative Arc and Emotional Architecture

**User Story:** As a songwriter, I want lyrics with emotional progression, so that the song builds toward a satisfying climax rather than staying flat.

#### Acceptance Criteria

1. WHEN the song has 2+ verses and a bridge THEN the lyrics SHALL follow a narrative arc:
   - **Verse 1 (Setup)**: Establish the world, character, or situation — ground the listener in specifics
   - **Verse 2 (Development)**: Raise the stakes, deepen the conflict, reveal new information, or shift perspective
   - **Bridge (Climax)**: Deliver the emotional peak — a confession, revelation, perspective shift, or moment of truth. The bridge SHALL contain the most emotionally charged or philosophically resonant lines
   - **Final Chorus (Resolution)**: The same words as earlier choruses, but now carrying accumulated meaning from the bridge
2. THE bridge SHALL shift at least one element: perspective (I → we, present → past), emotional register (defiance → vulnerability), or level of abstraction (concrete → philosophical)
3. WHEN writing a narrative song THEN each verse SHALL advance the story — no verse may simply restate or rephrase another verse's content
4. THE emotional trajectory SHALL follow one of these proven patterns:
   - **Ascending**: Quiet start → building intensity → emotional peak at bridge → powerful final chorus
   - **Descending/Reflective**: Energetic/defiant start → gradual vulnerability → quiet, honest bridge → resolved final chorus
   - **Circular**: Return to the opening image or phrase in the outro, but with transformed meaning
5. WHEN the song has no bridge (simple verse-chorus) THEN the final verse SHALL still introduce a shift — a twist, a new detail, or a change in emotional temperature
6. THE outro (if present) SHALL create a sense of resolution or deliberate open-endedness — never simply fade out lyrically

---

## Genre Parameter Matrix — Quick Reference

| Genre | Rhyme | Structure | Vocabulary | Repetition | Syllables/Line | Hook Priority | POV |
|---|---|---|---|---|---|---|---|
| Pop | ABAB, slant | ABABCB | Grade 2.9 | Very high | 6–10 | Critical | I/you |
| Hip-Hop/Rap | Dense, internal | Hook-Verse-Hook | Varies (inverse) | High (increasing) | 10–13 | Critical | 1st person |
| Rock/Metal | ABAB/AABB | VCVCBC | Moderate-high | Low (metal lowest) | 7–12+ | Moderate | 1st/3rd |
| Indie/Alternative | Slant/free | Atypical/free | Moderate-high | Low | Variable | Low | 1st introspective |
| Electronic/EDM | Minimal | Verse-Riser-Drop | Minimal | Extreme (sonic) | 4–8 | Drop > lyrics | We/abstract |
| Lo-Fi/Chill | Basic/relaxed | Simple/looping | Minimal | Moderate | Sparse | Low | 1st confessional |
| Jazz | Crafted AABB/ABAB | 32-bar AABA | Highest (pop) | Structured | Melodic-driven | Moderate | 1st romantic |
| Classical/Opera | Formal poetic | Aria/recitative | Highest (overall) | Through motif | Text-governed | N/A | Multiple |
| Modern Country | XAXA | VCVCBC | Grade 3.3 | High (61%+) | 7–9 | Critical | I/you |
| Outlaw/Traditional | ABAB/ABCB | Verse-refrain | Higher | Low (~45%) | 7–10 strict | Moderate | 1st/3rd equal |
| Americana/Indie Country | Most varied | Most varied | Grade 14.5 | Low (~45–50%) | Variable | Low-moderate | All POVs |

---

## Emotional Valence Quick Reference

| Genre | Dominant Valence | Key Emotions |
|---|---|---|
| Pop | Mixed trending negative, but positive correlates with popularity | Playful, confident, aspirational, heartbreak |
| Hip-Hop/Rap | Highest variance; positive now correlates with success | Confidence, introspection, complex emotional patterns |
| Rock/Metal | Negative (metal lowest happiness); anger stable | Insecurity, loneliness, fearlessness, freedom, defiance |
| Indie/Alternative | Melancholic, nuanced | Bittersweet, alienation, existential contemplation |
| Electronic/EDM | Euphoric, escapist | Energy, freedom, togetherness, transcendence |
| Lo-Fi/Chill | Melancholic to cozy | Anxiety, nostalgia, vulnerability, comfort |
| Jazz | Positive to bittersweet | Romance, nostalgia, joy, sophisticated sadness |
| Classical/Opera | Widest range | Ecstatic joy to devastating grief |
| Modern Country | Predominantly positive | Nostalgia, pride, celebration, heartbreak |
| Outlaw/Traditional | Darker, honest | Defiance, redemption, loneliness, vulnerability |
| Americana/Indie Country | Nuanced, complex | Bittersweet, contemplative, specific emotional states |

---

## Authenticity Markers Quick Reference

| Genre | Key Markers |
|---|---|
| Pop | Conversational register, emotional directness, phonesthetic devices, universal relatability |
| Hip-Hop/Rap | AAVE, regional dialect, code-switching, perceived lived experience, specific cultural references |
| Rock/Metal | Raw expression, anti-establishment, confessional tone, genre vocabulary (darkness, defiance) |
| Indie/Alternative | Specificity (real places/names), literary quality, DIY ethos, artistic imperfection |
| Electronic/EDM | Chantable phrases, festival-ready, producer-centric, communal language |
| Lo-Fi/Chill | DIY sincerity, internet culture, intimate confession, anti-corporate tone |
| Jazz | Wit, sophistication, interpretive nuance, Great American Songbook tradition |
| Classical/Opera | Literary fidelity, dramatic coherence, word-music unity, proper diction |
| Modern Country | "Ain't," "y'all," dropped g's, regional vocab, whiskey, long Southern place names, "got" |
| Outlaw/Traditional | Self-written feel, anti-Nashville, autobiographical, stripped-down, genre-blending |
| Americana/Indie Country | Regional specificity, literary density, solo-writer voice, multiple interpretive layers |
