---
description: Generate professional stage names for music performers optimized for streaming platform discoverability and commercial success. Use when asked to "create artist name", "generate performer name", "suggest stage name", "come up with musician name", or "name for music project".
---

# Requirements Document

## Introduction

This skill generates artist names backed by empirical research: psycholinguistic studies, Billboard/Spotify chart analysis, RIAA certification data, and streaming platform mechanics. The goal is to maximize **streaming discoverability** (Spotify/Apple Music search ranking) and **brand recognition** (Google uniqueness, voice search, social handle consistency).

### Core empirical findings this skill is built on

**From brand psychology research (directly applicable to music):**
- Lowrey, Shrum & Dubitsky (2003): plosive consonants (p, b, t, d, k, g) at name onset significantly boost memory recall — especially for **unknown/emerging** names (the exact condition of new artists)
- Pogacar et al. (2015, *Marketing Letters*): every plosive consonant is statistically overrepresented among Interbrand top 100 brands across a decade; follow-up (2018) confirmed higher willingness-to-pay for plosive-rich names
- Alter & Oppenheimer (2006, *PNAS*): fluently named stocks outperformed disfluent ones by $112 per $1,000 on day one — processing fluency creates measurable preference
- Song & Schwarz (2009, *Psychological Science*): hard-to-pronounce names trigger perceptions of unfamiliarity and **risk** — a direct barrier to new listener conversion
- Argo, Popa & Smith (2010, *Journal of Marketing*): alliterative/assonant brand names produce positive affect and better evaluations, especially when spoken aloud (= word-of-mouth conditions)
- Laham, Koval & Alter (2012, *JESP*): easier-to-pronounce names correlate with faster career advancement — controlling for name length and foreignness

**From streaming/chart data (systematic analysis of top 25–30 artists per genre):**
- Top 20 most-streamed Spotify artists: names average **9 characters**, skew heavily mononym or two-word
- RIAA Diamond leaders (Post Malone: 9 chars, Drake: 8, Rihanna: 7, The Weeknd: 7, Bruno Mars: 6) cluster around short, punchy constructions
- 8 of current top 10 most-streamed artists have names beginning with or prominently featuring plosive sounds
- 11.3 million tracked artists on Spotify (Chartmetric 2024), growing 4,600/day → name uniqueness is now a survival requirement, not a preference
- 84% of songs on Billboard Global 200 in 2024 went viral on TikTok first → names must function as hashtags and voice queries

**Critical caveat:** No peer-reviewed study has directly tested artist name phonetics against streaming numbers. All phonetic recommendations are adapted from brand psychology, which represents the strongest available proxy evidence.

## Glossary

- **Mononym**: Single-word stage name (Rihanna, Drake, SZA, Skrillex)
- **Plosive sounds**: Consonants p, b, t, d, k, g — boost recall especially for unknown names
- **Fricatives**: Consonants s, f, v, z — smooth, flowing perception
- **Processing fluency**: Brain's preference for easy-to-process stimuli; correlates with trust and positive affect
- **SEO (music)**: Owning first-page Google results for "[name] artist/music"
- **Voice search friction**: Difficulty smart speakers (Alexa, Siri, Google) have recognizing unusual spellings — directly reduces streams
- **Handle consistency**: Same @username across all platforms; increases brand revenue by ~23% (brand consistency research)
- **Government name**: Real birth name (hip-hop term for using it as stage name)
- **Alias culture**: EDM-specific practice of maintaining multiple names for different sounds/genres

## Requirements

### Requirement 1: Input Gathering

**User Story:** As a user, I want to provide context about my artistic vision so that generated names are commercially optimized for my specific market.

#### Acceptance Criteria

1. THE System SHALL request genre before generating any names
2. THE System SHALL request whether a real name or stage name is preferred (or both options)
3. THE System SHALL request target market geography (US, global, specific region)
4. THE System SHALL request primary distribution channels (Spotify, TikTok, live shows, all)
5. THE System SHALL optionally accept real name for derivative options
6. THE System SHALL NOT generate names without confirming genre — genre determines opposite strategies
7. WHEN genre is ambiguous or blended THEN ask which genre's audience conventions should dominate

### Requirement 2: Genre-Specific Naming Strategies

*All ratios and patterns derived from systematic analysis of top 25–30 charting/streaming artists per genre.*

#### Pop — Brandable authenticity

1. WHEN genre is Pop THEN offer both real name and stage name options (~56% of top pop acts use stage names, ~44% use real names — both are proven paths)
2. WHEN genre is Pop THEN target **8–12 characters, 2–4 syllables**
3. WHEN genre is Pop THEN mononyms are valid, especially for female artists (Madonna, Adele, Beyoncé, Sia, Lorde, Halsey are all mononyms; nearly all pop mononyms belong to female artists — a significant pattern)
4. WHEN genre is Pop THEN ensure pronunciation works across English, Spanish, and East Asian phonetic systems if targeting global streams
5. WHEN genre is Pop THEN special characters (P!nk, The Weeknd) are acceptable but must remain phonetically intuitive — unusual spellings create voice search friction
6. WHEN Pop target audience is Gen Z (18–24) THEN note current chart trend favors real names (Sabrina Carpenter, Olivia Rodrigo, Benson Boone, Chappell Roan)
7. Pop reference examples: Taylor Swift, The Weeknd (misspelling = high searchability + distinctiveness), Doja Cat, Billie Eilish, Charli XCX, Sabrina Carpenter

#### Hip-Hop / Rap — The alter-ego tradition

1. WHEN genre is Hip-Hop/Rap THEN use stage names (~93% of top charting artists use pseudonyms — highest ratio of any genre; "government name" is the rare exception)
2. WHEN genre is Hip-Hop/Rap THEN target **5–12 characters, 1–3 syllables**
3. WHEN genre is Hip-Hop/Rap THEN numbers, symbols, and intentional misspellings are genre-appropriate (21 Savage, A$AP Rocky, 2 Chainz, Playboi Carti, Sexxy Red)
4. WHEN genre is Hip-Hop/Rap THEN the "Lil" prefix is **severely saturated** — 600+ "Lil" artists on Genius alone; avoid unless artist has a specific creative reason
5. WHEN genre is Hip-Hop/Rap THEN NOTE: symbols and numbers create voice search friction — artist must decide whether the distinctiveness trade-off is worth it
6. WHEN genre is Hip-Hop/Rap THEN naming has evolved: 90s favored mythological grandeur (Ghostface Killah, The Notorious B.I.G.), 2000s favored brand-adjacent names (50 Cent, Ludacris), current era favors internet-optimized short names (Ice Spice, GloRilla, Doechii)
7. Hip-Hop reference examples: Drake (mononym, 5 chars), Kendrick Lamar (real name), Travis Scott, Nicki Minaj, GloRilla, Megan Thee Stallion

#### R&B / Soul — Intimate mononyms

1. WHEN genre is R&B/Soul THEN offer mononym as the primary option (~46% of top R&B acts use mononyms — highest mononym rate of any genre)
2. WHEN genre is R&B/Soul THEN target **4–9 characters, 2–3 syllables** — R&B has the shortest average name length (~8.9 chars) of any genre
3. WHEN genre is R&B/Soul THEN real name vs stage name is an even 50/50 split; both are valid paths
4. WHEN genre is R&B/Soul THEN smooth, elegant, intimate-sounding phonetics align with genre sonic identity
5. WHEN genre is R&B/Soul THEN acronyms and distinctive formatting signal artistic intentionality (SZA, H.E.R., GIVĒON with macron)
6. R&B reference examples: Beyoncé, SZA, Usher, Khalid, H.E.R., Tyla, The Weeknd, GIVĒON

#### Country — Authenticity is non-negotiable

1. WHEN genre is Country THEN strongly recommend **real name** (~72% of top country acts use real names — second-highest real-name rate of any genre)
2. WHEN genre is Country THEN use standard first + last name format (~82% of top country acts use this format)
3. WHEN genre is Country THEN target **10–14 characters** — country has the longest average name length of any genre due to the full-name convention
4. WHEN genre is Country THEN middle names are a proven legitimate strategy: Tim McGraw (born Samuel Timothy Smith), Garth Brooks (born Troyal Garth Brooks)
5. WHEN genre is Country THEN AVOID special characters, symbols, or obviously fabricated stage names — they trigger "industry plant" accusations from core audiences (Oliver Anthony's fanbase questioned his authenticity when his stage name was revealed)
6. WHEN genre is Country THEN traditional American first names (Luke, Blake, Chris, Morgan, Riley, Zach) resonate with core demographic (rural/suburban US)
7. WHEN genre is Country THEN mononyms are extremely rare (~7%; only HARDY, Shaboozey) — avoid unless artist has a very strong creative reason
8. Country reference examples: Morgan Wallen, Zach Bryan, Chris Stapleton, Luke Combs, Kacey Musgraves, Lainey Wilson

#### Rock / Metal — The full spectrum

1. WHEN genre is Modern/Indie Rock THEN solo artists should default to **real names** (~70% of top modern rock soloists use real names: Noah Kahan, Hozier, Benson Boone)
2. WHEN genre is Hard Rock / Metal THEN bands should target **single invented words of 5–10 characters** drawing from dark, mythological, intense, or violent semantic fields (Metallica, Slipknot, Ghost, Mastodon, Disturbed, Gojira)
3. WHEN genre is Rock/Metal THEN compound words and modified spellings are genre-appropriate (Spiritbox, Korn, Gojira as French adaptation)
4. WHEN genre is Rock THEN the "The + Plural Noun" format (The Strokes, The Killers, The White Stripes) is dated and declining — ~10–15% of modern acts
5. WHEN genre is Metal THEN apply linguist Adrienne Lehrer's finding: names must evoke outrageousness, violence, or darkness to signal genre belonging
6. Rock/Metal reference examples: Metallica (10 chars), Ghost (5 chars), Slipknot (8 chars), Hozier (6 chars), Noah Kahan (9 chars)

#### EDM / Electronic — The alias empire

1. WHEN genre is EDM/Electronic THEN target **4–8 character mononyms** — invented words with high searchability are the dominant format (~60–65% of top acts use pseudonyms, ~40–45% are mononyms)
2. WHEN genre is EDM/Electronic THEN ALL-CAPS formatting is genre-appropriate (~15–20% of top acts: FISHER, REZZ, ILLENIUM)
3. WHEN genre is EDM/Electronic THEN ensure name reads well on festival stage screens at distance — 4–6 character names are optimal for stage banners
4. WHEN genre is EDM/Electronic THEN note the alias culture: major artists maintain multiple names for different sounds (Eric Prydz = Pryda + Cirez D; David Guetta = Jack Back); this is an option to recommend if the artist is genre-spanning
5. WHEN genre is EDM/Electronic THEN a growing real-name trend among mainstream crossover DJs (David Guetta, Steve Aoki, Charlotte de Witte) conveys authenticity in the post-2015 era
6. WHEN genre is EDM/Electronic THEN leetspeak and number substitution are genre-appropriate (Deadmau5, 1788-L, RL Grime) but increase voice search friction
7. EDM reference examples: Skrillex (7 chars), Rezz (4 chars), Marshmello (10 chars), Tiësto (6 chars), Fisher (6 chars), Peggy Gou (8 chars)

#### Indie / Alternative — Weird as brand strategy

1. WHEN genre is Indie/Alternative THEN the "deliberately unexpected" tradition is the genre's competitive advantage — names that are intentionally absurd, obscure, or incongruous are anti-commercial signals that paradoxically boost memorability
2. WHEN genre is Indie/Alternative THEN animal names are extraordinarily prevalent and genre-coded (Arctic Monkeys, Tame Impala, Grizzly Bear, Fleet Foxes, Deerhunter, Wolf Parade) — use sparingly as this pattern is now very crowded
3. WHEN genre is Indie/Alternative THEN disemvoweling serves both visual distinctiveness and SEO: CHVRCHES (V for U), Alvvays (double V), MGMT (consonants only), STRFKR — recommend this technique
4. WHEN genre is Indie/Alternative THEN word repetition is a recognizable pattern (Everything Everything, Yeah Yeah Yeahs, Django Django) — viable if name is otherwise distinctive
5. WHEN genre is Indie/Alternative THEN memorable weirdness is a commercial advantage — Death Cab for Cutie's absurd name became "arguably one of the most successful indie brands"
6. WHEN genre is Indie/Alternative THEN ensure Google-ability despite the quirky convention — avoid names that are too generic even if clever
7. Indie reference examples: Tame Impala (10 chars), Phoebe Bridgers (14 chars), Hozier (6 chars), Alvvays (7 chars), MGMT (4 chars), Bon Iver (7 chars)

#### K-Pop — Corporate engineering as art

1. WHEN genre is K-Pop THEN names are typically chosen by agencies, not artists — the skill should generate names in line with proven agency strategies
2. WHEN genre is K-Pop THEN target **3–6 characters** — K-Pop has the shortest average name length of any genre
3. WHEN genre is K-Pop THEN four proven formats exist with roughly equal representation: acronyms (BTS, NCT, TXT, aespa from "æ in a virtual space"), English words (TWICE, Stray Kids), coined words (ENHYPEN, ATEEZ), and special formatting ((G)I-DLE, IZ*ONE)
4. WHEN genre is K-Pop THEN ALWAYS build in dual/multilayered meaning — both Korean and English readings are expected: BTS = Bangtan Sonyeondan (Korean) + "Beyond The Scene" (English); SEVENTEEN = 13 members + 3 units + 1 team
5. WHEN genre is K-Pop THEN individual stage names should be English (Rosé, Felix, Giselle) or symbolic Korean words (Haechan = "Full Sun") — both convey global accessibility
6. WHEN genre is K-Pop THEN prioritize trademark and search uniqueness aggressively — newer groups explicitly use invented names for SEO optimization (aespa, ENHYPEN) over older groups with generic names (Wonder Girls, Big Bang)
7. K-Pop reference examples: BTS (3 chars), TWICE (5 chars), aespa (5 chars), BLACKPINK (9 chars — contrast compound), Stray Kids (9 chars)

#### Latin — Bilingual naming for crossover

1. WHEN genre is Latin THEN bilingual naming is the dominant commercial strategy: an **English-accessible or English-language name paired with Spanish-language music** — Bad Bunny became Spotify's most-streamed global artist while singing almost entirely in Spanish, but his stage name is English
2. WHEN genre is Latin AND artist targets global crossover THEN English or English-accessible name is strongly recommended; CNN (2021) documented that pre-streaming, Latin artists "needed to cross over" with English names; post-streaming, audiences cross over to Spanish music but English names still maximize discoverability
3. WHEN genre is Latin AND artist targets Latin-primary audience THEN modified real names (J Balvin, Karol G) and character pseudonyms (Bad Bunny, Daddy Yankee) are both proven approaches
4. WHEN genre is Latin THEN target **5–10 characters**
5. WHEN genre is Latin THEN stylized spelling signals trap/urban credibility within the scene (Feid → Ferxxo, extra Xs)
6. Latin reference examples: Bad Bunny (8 chars), J Balvin (7 chars), Karol G (6 chars), Daddy Yankee (11 chars), Ozuna (5 chars)

#### Lo-Fi / Chill — Lowercase as ideology

1. WHEN genre is Lo-Fi/Chill THEN **lowercase single-word names are the dominant format** (~45% of top lo-fi producers) — the lowercase convention signals anti-ego, soft atmosphere, and digital-native aesthetic
2. WHEN genre is Lo-Fi/Chill THEN target **4–7 characters** — the shortest names in any non-K-Pop genre
3. WHEN genre is Lo-Fi/Chill THEN nature references, Japanese words, abstract textures, and intimate terms are all genre-appropriate (jinsang, potsu, kudasai, idealism, eevee)
4. WHEN genre is Lo-Fi/Chill THEN anonymity is a feature, not a limitation — many successful producers never reveal faces or real identities; the name carries the brand entirely
5. WHEN genre is Lo-Fi/Chill THEN vowel-removed spellings and minimal punctuation signal genre belonging (Brxvs, cxlt., bsd.u)
6. WHEN genre is Lo-Fi/Chill THEN Japanese cultural references are genre-authentic, tracing to Nujabes (Jun Seba reversed) and the genre's anime soundtrack roots
7. Lo-Fi reference examples: jinsang (6 chars), Nujabes (7 chars), idealism (8 chars), potsu (5 chars), Kupla (5 chars)

#### Jazz / Classical — The credential is the name

1. WHEN genre is Jazz/Classical THEN use the artist's **full real name** (~73–80% of top jazz and classical artists use real names — driven by the credential economy, not trend)
2. WHEN genre is Jazz/Classical THEN the name itself is the professional credential in these genres; using a pseudonym signals inauthenticity or pop-genre crossover ambitions
3. WHEN genre is Jazz THEN note the earned-nickname tradition (Duke Ellington, Count Basie, Lady Day) — these were peer-assigned titles, not self-chosen, and cannot be replicated by self-assignment
4. WHEN genre is Jazz-Electronic or Jazz-Hip-Hop crossover THEN pseudonyms are acceptable and genre-adjacent: Thundercat, Flying Lotus, Alfa Mist all lean into electronic/hip-hop naming conventions
5. WHEN genre is Classical THEN full legal name is standard (Yo-Yo Ma, Lang Lang, Yuja Wang); no special formatting
6. Jazz reference examples: Kamasi Washington (16 chars), Robert Glasper (14 chars), Thundercat (10 chars — crossover), Jacob Collier (12 chars)

### Requirement 3: Universal Phonetic Principles (Evidence-Based)

**User Story:** As a user, I want names that leverage proven psychological mechanisms for memorability.

#### Plosive onsets (strongest evidence)

1. THE name SHOULD begin with or prominently feature plosive consonants (p, b, t, d, k, g) — evidence: Lowrey et al. (2003) showed plosive onsets boost recall specifically for unfamiliar names; Pogacar et al. (2015) confirmed systematic overrepresentation in top brands
2. WHEN genre is Hip-Hop, EDM, or Pop targeting 18–35 demographic THEN prioritize plosive onsets
3. Examples among top 10 most-streamed Spotify artists: **B**illie, **B**ad **B**unny, **D**rake, **K**endrick, **B**runo, **P**ost — 8 of top 10 names feature prominent plosives

#### Processing fluency (universal)

1. THE name SHALL be easy to pronounce on first encounter — Song & Schwarz (2009): hard-to-pronounce names are perceived as riskier, deterring new listeners
2. THE name SHALL be spellable from hearing alone, OR the unusual spelling must be so distinctive that it becomes a selling point (Weeknd, Chvrches, Alvvays are examples where the misspelling itself is memorable)
3. WHEN targeting voice search and smart speaker plays THEN phonetic transparency is critical — symbols (A$AP, Ke$ha) and numbers (6LACK, Deadmau5) create Siri/Alexa disambiguation failures

#### Vowel psychology (secondary, genre-dependent)

1. WHEN targeting intimate, close, forward-facing perception (Indie, Pop, R&B) THEN front vowels (i, e) are appropriate
2. WHEN targeting power, scale, masculine force (Metal, Hard Rock, Trap) THEN back vowels (o, u, a) are appropriate

#### Sound repetition

1. Alliteration and assonance produce positive affect especially when spoken aloud — Argo et al. (2010): applies directly to artist name word-of-mouth
2. Examples: **B**illie **E**ilish (assonance), **K**aty **P**erry (alliteration), **P**ost **M**alone (consonant rhyme)

### Requirement 4: Optimal Name Characteristics

**Derived from analysis of top 20 most-streamed Spotify artists + RIAA Diamond certifications.**

#### Acceptance Criteria

1. THE name SHALL contain 5–12 characters (top 20 Spotify artists average 9 characters)
2. THE name SHALL contain 2–4 syllables
3. THE name SHALL achieve first-page Google uniqueness for "[name] music" or "[name] artist"
4. THE name SHALL NOT exceed 15 characters (Twitter/X handle limit is 15 chars; longer names force compromises on cross-platform consistency)
5. WHEN name uses unusual spelling THEN the misspelling itself must be distinctive enough to be memorable, not just confusing (The Weeknd = yes; Teh Weekned = no)

### Requirement 5: Streaming Platform Discoverability

**User Story:** As a user, I want a name optimized for how fans actually find artists today.

#### Acceptance Criteria — Spotify/Apple Music

1. THE System SHALL flag names that conflict with existing artists on major platforms — DistroKid warns: "It's best practice to use an artist/band name that doesn't already exist in streaming services"; TuneCore warns: distributors can refuse to distribute if the name is "too misleading"
2. THE System SHALL note that Spotify's search ranks by personal history + current popularity + all-time popularity — name uniqueness determines whether search reaches the correct artist at all
3. THE System SHALL recommend checking: Spotify search, Apple Music search, YouTube Music search before committing

#### Acceptance Criteria — Voice Search (Alexa, Siri, Google Assistant)

1. THE System SHALL flag names with symbols (#, $), numbers used as words (6LACK, Deadmau5), or unusual consonant clusters for voice search friction
2. THE System SHALL note: 111.1 million U.S. smart speaker users and 1 billion+ monthly voice searches globally — mispronounced or ambiguous names lose streams passively
3. WHEN name has known pronunciation gap (6LACK → "black"; Bbno$ → "baby no money") THEN explicitly note this as a discoverability trade-off, not a prohibition

#### Acceptance Criteria — TikTok & Social

1. THE System SHALL ensure recommended names function as hashtags (no spaces or special characters in the hashtag version)
2. THE System SHALL note: 84% of Billboard Global 200 songs in 2024 went viral on TikTok first — the name must be typeable in a caption, searchable as a tag
3. THE System SHALL recommend identical @handle across Instagram, TikTok, Twitter, YouTube — consistent branding increases revenue ~23%
4. THE System SHALL check Twitter/X 15-character handle constraint on all recommendations

### Requirement 6: Uniqueness Techniques (When Needed)

**User Story:** As a user, I want techniques to make a desired word unique without sacrificing discoverability.

#### Acceptance Criteria

1. Intentional strategic misspelling — creates SEO uniqueness while maintaining phonetic transparency: The Weeknd (missing "e"), Chvrches (V for U), Tame Impala (correct spelling but unusual combination)
2. Number substitution — use only when it becomes part of the distinctive identity, not merely to differentiate: Deadmau5 (iconic), 21 Savage (numeric age identity), 6ix9ine (neighborhood code)
3. Unconventional capitalization — ALL CAPS (FISHER, REZZ), camelCase (SZA), lowercase (jinsang, potsu) — each carries genre-specific connotations
4. Portmanteau / invented words — combine two words or roots into one: Skrillex (from AOL screenname), Marshmello (marshmallow + hello), aespa (æ in virtual space)
5. Modifier prefix — "Lil", "Young", "Big", "MC" are all crowded; "Young" and "Big" less saturated than "Lil" — use only with strong personal narrative justification

### Requirement 7: The Name Change Penalty (Critical for Rebrands)

**User Story:** As a user considering a rebrand, I need to understand the streaming-era costs.

#### Acceptance Criteria

1. THE System SHALL warn that name changes carry structural costs in the streaming era that did not exist in the physical media era
2. THE System SHALL note: Spotify requires metadata redelivery through distributors for all releases; Apple Music "generally doesn't allow artists' names on existing content to be changed" — this can split the catalog across two artist pages
3. THE System SHALL cite case evidence: Prince's unpronounceable symbol (1993–2000) led to MTV using "a metallic clanging noise" and significant album sales decline; Snoop Dogg's "Snoop Lion" rebrand (2012) produced only 21,000 first-week copies vs. typical performance; Kanye's "Ye" rebrand's commercial decline correlates more strongly with controversies than with the name change itself
4. THE System SHALL note the counterexample: The Weeknd's missing "e" (forced by trademark conflict) became a commercial asset — proving strategic imperfection can outperform conventional naming
5. WHEN user is considering a rebrand THEN ask whether it's worth redesigning social handles, catalog metadata, press, and SEO simultaneously — and whether a sub-brand/alias is a better option (especially relevant for EDM artists)

### Requirement 8: Prohibited Elements

#### Structural problems

1. THE name SHALL NOT exceed 15 characters (cross-platform handle constraint)
2. THE name SHALL NOT exceed 4 syllables without exceptional creative justification
3. THE name SHALL NOT use abbreviations without cultural context (J.K., M.C. without community meaning)

#### SEO and discoverability problems

1. THE name SHALL NOT use standalone common words without modification (Girls, Television, Future as-is)
2. THE name SHALL NOT conflict with existing artists who have senior rights to the name
3. THE name SHALL NOT reference current memes or viral moments (lifespan: 6–12 months)

#### Legal risks

1. THE name SHALL NOT skip trademark verification (USPTO classes 9, 25, 41)
2. THE name SHALL NOT reference corporate brands without modification (Saint Pepsi → Skylar Spence after PepsiCo lawsuit)

#### Cultural and linguistic problems

1. THE name SHALL NOT use "Nova" for Spanish-speaking markets (= "doesn't go")
2. THE name SHALL NOT use "Bing" for Mandarin markets (sounds like 病 = illness)
3. THE name SHALL flag R+L combinations for Japanese/Mandarin audiences
4. THE name SHALL flag initial "ps" clusters for Spanish-speaking audiences

### Requirement 9: Output Format

**User Story:** As a user, I want structured, evidence-linked analysis for each name recommendation.

#### Acceptance Criteria

1. THE output SHALL include: Name
2. THE output SHALL include: Type (Real name / Real name derivative / Pseudonym / Mononym)
3. THE output SHALL include: Characters | Syllables | Words
4. THE output SHALL include: Phonetic profile (Plosive-led / Fricative-led / Mixed / Neutral)
5. THE output SHALL include: Processing fluency assessment (High / Medium / Low — with note if low)
6. THE output SHALL include: Voice search status (Clean / Minor friction / Significant friction — explain friction)
7. THE output SHALL include: Platform check status (Unique / Needs verification / Known conflict)
8. THE output SHALL include: Genre convention fit (Strong / Acceptable / Unconventional — with brief rationale)
9. THE output SHALL include: Meaning/Story (the personal narrative or conceptual logic behind the name)
10. THE output SHALL include: Trade-offs (honest list of any discoverability, pronunciation, or cultural risks)

### Requirement 10: Generation Process

#### Acceptance Criteria

1. THE System SHALL gather: genre, real name (optional), target market geography, primary distribution channels (streaming vs. live vs. social)
2. THE System SHALL apply the genre-specific strategy from Requirement 2
3. THE System SHALL apply universal phonetic principles from Requirement 3
4. THE System SHALL verify length constraints from Requirement 4
5. THE System SHALL flag any platform, voice search, or SEO issues from Requirements 5–6
6. THE System SHALL generate 5–7 options with rationale
7. THE System SHALL recommend top 3 with full structured analysis per Requirement 9
8. THE System SHALL provide a verification checklist: Google, Spotify, Apple Music, YouTube, USPTO, social @handles, domain availability

### Requirement 11: Error Handling

1. IF genre is not specified THEN refuse and explain that Pop, Hip-Hop, Country, R&B, and EDM have mutually opposite naming conventions — genre is non-negotiable
2. IF name conflicts with an established artist THEN flag with commercial risk explanation, not just a warning
3. IF cultural/linguistic issue is detected THEN explain the specific problem and the specific market affected
4. THE System SHALL NOT generate without explicit genre confirmation

## Output Template

```
**Name**: [Generated Name]
**Type**: Real name / Real name derivative / Pseudonym / Mononym
**Characters**: [X] | **Syllables**: [X] | **Words**: [X]
**Phonetic profile**: Plosive-led / Fricative-led / Mixed / Neutral
**Processing fluency**: High / Medium / Low
**Voice search**: Clean / Minor friction / Significant friction — [note]
**Platform check**: Unique / Needs verification / Known conflict
**Genre fit**: Strong / Acceptable / Unconventional — [1-sentence rationale]
**Meaning/Story**: [The personal narrative or concept behind the name]
**Trade-offs**: [Honest list of any risks — pronunciation, discoverability, cultural]
```

## Quick Reference Tables

### Genre Strategy Summary (evidence-based)

| Genre | Name type | Format | Char range | Mononym rate | Key differentiator |
|-------|-----------|--------|------------|--------------|-------------------|
| Pop | 56% stage / 44% real | 1–2 words | 8–12 | ~32% | Brandability + global phonetics |
| Hip-Hop/Rap | 93% stage name | 1–2 words | 5–12 | ~27% | Alter-ego; symbols/numbers OK |
| R&B/Soul | 50/50 | Mononym preferred | 4–9 | ~46% (highest) | Intimacy; shortest avg name |
| Country | 72% real name | First + Last | 10–14 | ~7% (rare) | Authenticity is the brand |
| Rock (solo) | ~70% real | First + Last | 7–14 | ~10% | Authenticity trend 2020+ |
| Metal (band) | Invented | 1 word | 5–10 | N/A (band) | Dark/mythological semantics |
| EDM | 65% stage | Mononym | 4–8 | ~40% | Festival readability; alias culture |
| Indie/Alt | Invented | 2–3 words | Variable | ~15% | Deliberate weirdness = brand |
| K-Pop | Agency-designed | Acronym/coined | 3–6 | N/A (group) | Multilayer meaning; global SEO |
| Latin | Bilingual hybrid | 1–2 words | 5–10 | ~20% | English name + Spanish music |
| Lo-Fi/Chill | Lowercase pseudo | 1 word | 4–7 | ~45% | Lowercase = anti-ego signal |
| Jazz | 73–80% real | First + Last | 8–16 | ~5% | Name = professional credential |
| Classical | ~95% real | First + Last | 8–16 | ~3% | Credential economy |

### Phonetic Impact Reference (from brand research)

| Sound type | Effect | Strongest evidence | Best genres |
|-----------|--------|-------------------|-------------|
| Plosives (p,b,t,d,k,g) onset | Recall boost for unfamiliar names | Lowrey et al. (2003); Pogacar et al. (2015) | All genres, esp. Hip-Hop, EDM, Pop |
| Processing fluency | Trust + positive affect + willingness to pay | Alter & Oppenheimer (2006); Song & Schwarz (2009) | Universal — applies to all genres |
| Alliteration/assonance | Positive affect when spoken aloud | Argo et al. (2010) | Pop, R&B, Country |
| Front vowels (i, e) | Intimacy, closeness, forward presence | Vowel psychology research | Indie, Pop, R&B |
| Back vowels (o, u, a) | Power, scale, masculine force | Vowel psychology research | Metal, Hard Rock, Trap |
| Fricatives (s, f, v, z) | Smoothness, flow, lightness | Brand phonetics research | Chill, Ambient, Soft Pop |

### Discoverability Risk Matrix

| Name characteristic | Streaming risk | Voice search risk | Mitigation |
|--------------------|---------------|------------------|------------|
| Symbols ($, #, !) | Medium — metadata complications | High — Siri/Alexa fail | Use only if iconic (P!nk); ensure phonetic clarity |
| Numbers as words | Medium | High | Ensure pronunciation is widely known (6LACK) |
| Common generic word | High — buried in search | Low | Require significant modification |
| Unusual spelling | Low if distinctive | Medium | Distinctive > confusing (Weeknd vs. random misspelling) |
| Real name (uncommon) | Low | Low | Near-ideal — natural fluency + uniqueness |
| Acronym | Low | Medium | Ensure letters are easily speakable |
| All-lowercase | Low (with correct metadata) | Low | Genre signal in Lo-Fi; works in metadata as capitalized |

### Commercial Success Factors Summary

| Factor | Evidence strength | Impact |
|--------|------------------|--------|
| Plosive onset | Strong (brand research + chart pattern) | Recall in new listeners |
| Short name (5–9 chars) | Strong (top streamer analysis) | Cross-platform compatibility |
| High processing fluency | Strong (multiple peer-reviewed studies) | Trust formation, listener conversion |
| Unique Google result | Strong (streaming platform mechanics) | Discovery rate |
| Voice search clarity | Moderate (platform user reports) | Passive stream capture |
| Cross-platform handle consistency | Moderate (brand consistency research) | ~23% revenue lift cited |
| Genre convention compliance | Moderate (sociological research) | Audience trust, authenticity |
| Mononym (genre-appropriate) | Pattern evidence | Icon potential (disproportionate in top tiers) |
