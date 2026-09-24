---
description: Generate literary pseudonyms for children's book authors optimized for global audience, phonetic memorability, and trust perception. Use when asked to "create pen name", "generate pseudonym", "choose author name", "literary pseudonym for children's books", "pen name for kids literature", or "author name for fairy tales".
---

# Requirements Document

## Introduction

This document defines requirements for the "Children's Literature Pseudonym Generation" skill — an AI-powered literary pseudonym generation system optimized for global pronounceability, phonetic memorability, trust perception, and bookshelf discoverability. The skill enables generation of author names that maximize recognition across cultures, convey warmth and safety appropriate for children's literature, and function as effective brands in both physical and digital book markets.

Scientific foundation: Processing fluency research (Alter & Oppenheimer, 2009) demonstrates that easily processed stimuli are systematically rated as more truthful, pleasant, and valuable. Laham et al. (2012) showed people form more positive impressions of easily pronounceable names. The bouba/kiki effect (Ramachandran & Hubbard, 2001) confirms 95-98% cross-cultural association of soft sonorants (/m/, /n/, /l/) with warmth and rounded shapes — ideal for children's literature. The von Restorff effect (1933) explains why moderately unusual names outperform both common and exotic names in recall. Successful children's pseudonyms (Dr. Seuss, Lewis Carroll, Lemony Snicket, Корней Чуковский) consistently leverage alliteration, cognitive dissonance, and sensory imagery as mnemonic devices.

## Glossary

- **Processing Fluency**: Subjective ease with which the brain processes information; higher fluency = more trust, liking, and perceived value
- **Bouba/Kiki Effect**: Cross-cultural sound symbolism where rounded sounds (/m/, /n/, /l/ + /a/, /o/) feel warm/soft and angular sounds (/k/, /t/ + /i/, /e/) feel sharp/energetic
- **Von Restorff Effect**: Moderately unusual items are remembered significantly better than both common and extremely unusual items
- **Cognitive Dissonance Hook**: Combining incongruent elements (e.g., "Dr." + playful surname) to create memorable tension
- **CV Syllable**: Consonant + Vowel pattern — the only syllable structure permitted in all world languages
- **CVCV Pattern**: Two CV syllables — ideal template for cross-cultural pronounceability
- **Universal Consonants**: /m/, /n/, /p/, /t/, /k/, /s/, /l/, /h/, /b/, /d/ — present in 90%+ of world languages
- **Universal Vowels**: /a/, /e/, /i/, /o/, /u/ — the five-vowel system shared by Spanish, Italian, Japanese, Swahili, and dozens of other languages
- **Sonorants**: Consonants /m/, /n/, /l/ — perceived as warm, soft, safe (preferred for children's literature)
- **Plosives**: Consonants /k/, /t/, /p/, /b/, /d/ — perceived as sharp, energetic, memorable (useful in initial position)
- **Alliteration**: Repetition of initial consonant sounds (Lewis Carroll, Korney Chukovsky)
- **Tailgating**: Choosing a surname that places the book alphabetically near a bestselling author in the same genre
- **DBA/FBN**: "Doing Business As" / "Fictitious Business Name" — legal registration for receiving payments under a pseudonym

## Requirements

### Requirement 1: Input Gathering

**User Story:** As an author, I want to provide context about my creative vision, so that generated pseudonyms align with my genre, audience, and personal story.

#### Acceptance Criteria

1. THE System SHALL request target age group (0-3 toddlers, 4-7 picture books, 8-12 middle grade, mixed)
2. THE System SHALL request subgenre (fairy tales, educational, adventure, fantasy, humor, poetry, bedtime stories)
3. THE System SHALL request real name (optional) for derivative pseudonyms
4. THE System SHALL request primary target markets/languages (for phonetic optimization)
5. THE System SHALL request author persona (warm storyteller, wise mentor, playful trickster, mysterious narrator)
6. THE System SHALL request gender presentation preference (masculine, feminine, neutral/initials, no preference)
7. THE System SHALL request any personal elements to incorporate (family names, meaningful words, cultural roots)
8. THE System SHALL NOT auto-generate pseudonyms without confirming at minimum: age group, subgenre, and target markets

### Requirement 2: Phonetic Science Compliance — Universal Pronounceability

**User Story:** As an author targeting a global audience, I want a name pronounceable by children and adults across languages, so that my pseudonym works in Tokyo, Mexico City, Berlin, and Moscow alike.

#### Acceptance Criteria — Safe Sounds

1. THE pseudonym SHALL use only universal consonants: /m/, /n/, /p/, /t/, /k/, /s/, /l/, /h/, /b/, /d/
2. THE pseudonym SHALL use only universal vowels: /a/, /e/, /i/, /o/, /u/
3. THE pseudonym SHALL NOT contain "th" (/θ/, /ð/) — exists in only ~8% of world languages
4. THE pseudonym SHALL NOT contain English "r" — varies radically across languages (uvular in French, alveolar in Spanish, retroflex in Chinese, conflated with "l" in Japanese)
5. THE pseudonym SHALL NOT contain "v" — not distinguished from other sounds in many languages (German "v" = "f"; Vicks → Wicks in Germany)
6. THE pseudonym SHALL avoid consonant clusters (str-, spl-, -nk, -xt) — impossible in Japanese, Chinese, Arabic, and most African languages

#### Acceptance Criteria — Syllable Structure

1. THE pseudonym SHALL prefer CV (consonant + vowel) or CVCV syllable patterns
2. THE pseudonym SHALL contain 2-3 syllables per word (4-7 letters per word)
3. THE pseudonym total length SHALL be 2-4 syllables for the full name
4. THE pseudonym SHALL be testable: a 5-year-old should be able to repeat it after hearing it once

#### Acceptance Criteria — Warm Sound Profile (Children's Literature Specific)

1. THE pseudonym SHALL prioritize sonorants (/m/, /n/, /l/) and open vowels (/a/, /o/) for warmth and safety perception (bouba effect)
2. THE pseudonym MAY use a plosive (/k/, /t/, /p/, /b/) in initial position for memorability, followed by warm sounds
3. THE pseudonym SHALL create an overall "round" sound profile — soft, inviting, non-threatening
4. THE pseudonym SHALL NOT create an overall "angular" sound profile unless the author persona is deliberately edgy (e.g., dark fairy tales)

### Requirement 3: Mnemonic Hook Strategies

**User Story:** As an author, I want my pseudonym to be instantly memorable, so that children and parents recall it after a single encounter.

#### Acceptance Criteria

1. THE pseudonym SHALL employ at least one mnemonic device from the following:
   - Alliteration: repeated initial sounds (Lewis Carroll, Korney Chukovsky)
   - Assonance: repeated vowel sounds within the name
   - Cognitive dissonance: incongruent elements creating memorable tension (Dr. Seuss — authority + playfulness)
   - Sensory imagery: name evokes taste, texture, color, or sound (Lemony — citrus, bright, slightly sour)
   - Rhythmic pattern: name has a natural musical cadence (dactylic, trochaic)
   - Rhyme or near-rhyme between name elements
2. THE pseudonym SHALL NOT rely solely on being "unusual" — it must have a structural hook
3. THE pseudonym SHALL be evaluated for its "story potential" — can the name itself suggest a character or narrative?

### Requirement 4: Format Strategies

**User Story:** As an author, I want the optimal name format for my market positioning, so that my pseudonym follows proven conventions in children's literature.

#### Acceptance Criteria — Initials + Surname Format

1. WHEN gender neutrality is strategically important THEN use initials + surname format
2. THE initials format has deep tradition in children's literature: J.K. Rowling, C.S. Lewis, A.A. Milne, E.B. White, P.L. Travers, R.L. Stine, K.A. Applegate
3. THE initials format adds perceived literary seriousness
4. THE System SHALL warn: middle initials may be forgotten during search (SEO risk per Gordon Miller)
5. WHEN using initials THEN limit to 2 initials maximum (first + middle or first + first)

#### Acceptance Criteria — Full Pseudonym Format

1. WHEN maximum memorability is the goal THEN use full first name + surname
2. THE full name format allows stronger phonetic hooks (alliteration, rhythm)
3. THE full name format is better for building author-as-character persona (Lemony Snicket model)

#### Acceptance Criteria — Title + Name Format

1. WHEN authority + playfulness is desired THEN consider title prefix (Dr., Professor, Captain)
2. THE title format creates cognitive dissonance — a proven mnemonic device (Dr. Seuss)
3. THE title format works best when the surname is short and playful

#### Acceptance Criteria — Mononim (Single Name)

1. WHEN iconic simplicity is desired THEN consider single-name format
2. THE mononim SHALL be 2-3 syllables, 5-8 characters
3. THE mononim is higher risk (harder to achieve uniqueness) but higher reward (iconic if successful)

### Requirement 5: Cultural Safety Verification

**User Story:** As an author targeting a global audience, I want my pseudonym free of unintended meanings, so that it doesn't cause embarrassment or offense in any major market.

#### Acceptance Criteria

1. THE System SHALL check the pseudonym and its parts against unintended meanings in at minimum: Chinese (tonal homophone check), Japanese, Arabic, German, French, Spanish, Portuguese, Hindi, Korean, Thai
2. THE System SHALL flag known cultural traps:
   - "Mist" = manure in German
   - "Puff" = brothel in German slang
   - "Pinto" = vulgar term in Brazilian Portuguese
   - "Bite" = vulgar slang in French
   - Number 4 = death in Chinese, Japanese, Korean
   - Visual similarity to Arabic calligraphy of "Allah" = religious offense
   - Names from indigenous cultures = cultural appropriation risk
3. THE System SHALL flag any phonetic similarity to profanity, slurs, or taboo words in major languages
4. THE System SHALL verify the name does not belong to a real public figure (living or recently deceased)
5. THE System SHALL verify the name does not belong to a well-known fictional character that would cause confusion

### Requirement 6: Discoverability & Digital Branding

**User Story:** As an author, I want a pseudonym that dominates search results and is available across platforms, so that readers can easily find me.

#### Acceptance Criteria — Search Uniqueness

1. THE System SHALL recommend Google search verification: "[name] author" — no competitors on page 1
2. THE System SHALL recommend Amazon Books search — name must be unique among authors
3. THE System SHALL recommend Goodreads search — no existing author with same name
4. THE System SHALL recommend WorldCat search — no existing author in library catalogs
5. IF the name returns existing results for another person THEN flag as conflict and suggest alternatives

#### Acceptance Criteria — Digital Presence

1. THE System SHALL recommend domain check (.com priority) via registrar
2. THE System SHALL recommend social handle check via Namechk.com: identical @name on Instagram, TikTok, YouTube, Facebook, Twitter/X
3. THE System SHALL recommend securing domain and handles BEFORE any public announcement
4. THE pseudonym SHALL be easily typeable — no special characters, diacritics, or unusual spellings that complicate URL entry

#### Acceptance Criteria — Bookshelf Positioning

1. THE System SHALL note whether the surname falls in the first third of the alphabet (A-I) for physical bookshelf advantage
2. THE System MAY suggest "tailgating" — choosing a surname that places the book near a bestselling children's author alphabetically
3. THE System SHALL present alphabet position as informational, not mandatory — digital discoverability outweighs physical shelf position

### Requirement 7: Legal Considerations

**User Story:** As an author, I want to understand the legal implications of my pseudonym, so that I protect my intellectual property and income.

#### Acceptance Criteria

1. THE System SHALL inform: pseudonymous works have copyright protection of 95 years from publication (vs. 70 years after death for real-name works) unless real name is registered with Copyright Office
2. THE System SHALL recommend registering DBA/FBN if receiving payments under pseudonym
3. THE System SHALL recommend filing copyright under both real name and pseudonym for maximum protection term
4. THE System SHALL recommend trademark registration (relevant classes) if planning a series
5. THE System SHALL recommend consulting a publishing attorney for multi-market rights

### Requirement 8: Age-Group Specific Optimization

**User Story:** As an author, I want my pseudonym optimized for my target age group, so that it resonates with both children and their parents/guardians.

#### Acceptance Criteria

1. WHEN target is 0-3 (toddlers/board books) THEN maximize softness: sonorants, open vowels, 2 syllables, extremely simple structure
2. WHEN target is 4-7 (picture books) THEN balance warmth with playfulness: allow one plosive for energy, 2-3 syllables, name should be "fun to say"
3. WHEN target is 8-12 (middle grade) THEN allow more complexity: cognitive dissonance hooks, slightly longer names, mysterious or adventurous tone acceptable
4. WHEN target is mixed/all ages THEN optimize for the youngest viable reader while maintaining sophistication for parents — the "Dr. Seuss sweet spot"

### Requirement 9: Persona Alignment

**User Story:** As an author, I want my pseudonym to reflect my authorial persona, so that the name itself tells the first story before the book is opened.

#### Acceptance Criteria

1. WHEN persona is "warm storyteller" THEN use sonorants, open vowels, gentle rhythm, names evoking comfort (fireside, nature, home)
2. WHEN persona is "wise mentor" THEN use title prefix or dignified structure, balanced rhythm, names evoking knowledge and calm authority
3. WHEN persona is "playful trickster" THEN use cognitive dissonance, unexpected combinations, sensory words, names that make children giggle
4. WHEN persona is "mysterious narrator" THEN use slightly unusual phonetic combinations, names with narrative potential (Lemony Snicket model), names that invite curiosity
5. THE pseudonym SHALL be evaluated: "Does this name sound like someone who would write the kind of books I write?"

### Requirement 10: Prohibited Elements

**User Story:** As an author, I want to avoid naming pitfalls, so that my pseudonym doesn't limit my career or alienate readers.

#### Acceptance Criteria — Phonetic Errors

1. THE pseudonym SHALL NOT contain sounds absent in major world languages ("th", variable "r", "v")
2. THE pseudonym SHALL NOT contain consonant clusters impossible in Japanese, Chinese, Arabic
3. THE pseudonym SHALL NOT exceed 4 syllables total (will be shortened or misremembered)
4. THE pseudonym SHALL NOT be unpronounceable by a 5-year-old native speaker of any major language

#### Acceptance Criteria — Branding Errors

1. THE pseudonym SHALL NOT be a common dictionary word without modification (will be unsearchable)
2. THE pseudonym SHALL NOT conflict with existing children's book authors
3. THE pseudonym SHALL NOT conflict with existing brands, franchises, or fictional characters
4. THE pseudonym SHALL NOT reference current trends or memes (expire in 6-12 months)
5. THE pseudonym SHALL NOT use special characters or diacritics that complicate digital search

#### Acceptance Criteria — Tone Errors

1. THE pseudonym SHALL NOT sound threatening, aggressive, or dark (unless specifically writing dark fairy tales for older children)
2. THE pseudonym SHALL NOT sound overly corporate or clinical
3. THE pseudonym SHALL NOT sound condescending or infantilizing
4. THE pseudonym SHALL NOT appropriate names from indigenous or marginalized cultures without authentic connection

### Requirement 11: Output Format

**User Story:** As an author, I want structured analysis for each pseudonym option, so that I can make an informed decision.

#### Acceptance Criteria

1. THE output SHALL include the pseudonym
2. THE output SHALL include format type (Full Name / Initials + Surname / Title + Name / Mononim)
3. THE output SHALL include character count and syllable count
4. THE output SHALL include phonetic profile (Sonorant-dominant / Plosive-accented / Mixed)
5. THE output SHALL include sound warmth assessment (Warm ☀️ / Balanced ⚖️ / Sharp ⚡)
6. THE output SHALL include mnemonic hook used (Alliteration / Assonance / Cognitive Dissonance / Sensory / Rhythmic / Rhyme)
7. THE output SHALL include universal pronounceability assessment (✓ Universal / ⚠️ Minor issues / ✗ Problematic)
8. THE output SHALL include cultural safety status (✓ Clear / ⚠️ Needs verification / ✗ Conflict detected)
9. THE output SHALL include SEO/uniqueness assessment (✓ Likely unique / ⚠️ Needs verification / ✗ Conflict)
10. THE output SHALL include alphabet position (A-I advantage / J-R neutral / S-Z disadvantage)
11. THE output SHALL include persona fit explanation
12. THE output SHALL include "story of the name" — what narrative or feeling the name evokes

### Requirement 12: Generation Process

**User Story:** As an author, I want a systematic generation process, so that I receive well-researched pseudonym options.

#### Acceptance Criteria

1. THE System SHALL gather input (age group, subgenre, real name, markets, persona, gender preference, personal elements)
2. THE System SHALL determine optimal format strategy based on inputs
3. THE System SHALL generate candidate names applying phonetic science (universal sounds, CV structure, warm profile)
4. THE System SHALL apply mnemonic hooks to each candidate
5. THE System SHALL verify cultural safety for each candidate
6. THE System SHALL assess discoverability for each candidate
7. THE System SHALL generate 5-7 options with full analysis
8. THE System SHALL recommend top 3 with detailed rationale
9. THE System SHALL provide a verification checklist (Google, Amazon, Goodreads, domain, social handles, cultural check with native speakers, child pronunciation test)

### Requirement 13: Child Pronunciation Test Protocol

**User Story:** As an author, I want a practical way to validate my pseudonym with real children, so that I know it works for my actual audience.

#### Acceptance Criteria

1. THE System SHALL recommend testing with children aged 4-10 from at least 3 different language backgrounds
2. THE test protocol: say the name once, wait 5 seconds, ask the child to repeat it
3. Success criteria: child reproduces the name recognizably on first attempt
4. THE System SHALL recommend testing with at least 5 children per language group
5. THE System SHALL note: this is the most honest and important test — if children can't say it, the name fails regardless of all other criteria

### Requirement 14: Error Handling

**User Story:** As an author, I want clear feedback when generation cannot proceed.

#### Acceptance Criteria

1. IF age group and subgenre are not specified THEN refuse generation and request minimum inputs
2. IF a generated name conflicts with an existing author THEN flag and suggest alternatives
3. IF cultural issue is detected THEN warn with specific explanation and affected market
4. IF all generated names fail uniqueness checks THEN explain the constraint and offer to adjust parameters
5. THE System SHALL NOT auto-generate without explicit user confirmation of creative direction

---

## Output Template

```
**Pseudonym**: [Generated Name]
**Format**: Full Name / Initials + Surname / Title + Name / Mononim
**Characters**: [X] | **Syllables**: [X]
**Phonetic profile**: Sonorant-dominant / Plosive-accented / Mixed
**Sound warmth**: Warm ☀️ / Balanced ⚖️ / Sharp ⚡
**Mnemonic hook**: [Alliteration / Assonance / Cognitive Dissonance / Sensory / Rhythmic / Rhyme]
**Pronounceability**: ✓ Universal / ⚠️ Minor issues / ✗ Problematic
**Cultural safety**: ✓ Clear / ⚠️ Needs verification / ✗ Conflict detected
**SEO/Uniqueness**: ✓ Likely unique / ⚠️ Needs verification / ✗ Conflict
**Alphabet position**: [A-I ✓ / J-R ~ / S-Z ✗]
**Persona fit**: [How the name matches the author's persona]
**Story of the name**: [What narrative, feeling, or image the name evokes — the "first fairy tale"]
```

---

## Quick Reference Tables

### Universal Safe Sounds for Children's Literature

| Category | Sounds | Effect | Priority |
|----------|--------|--------|----------|
| Sonorants | /m/, /n/, /l/ | Warmth, softness, safety | ★★★ Primary |
| Voiceless plosives | /p/, /t/, /k/ | Memorability, energy | ★★ Initial position |
| Voiced plosives | /b/, /d/ | Gentle strength | ★★ Supporting |
| Fricatives | /s/, /h/ | Lightness, whisper | ★ Accent |
| Open vowels | /a/, /o/ | Warmth, roundness | ★★★ Primary |
| Mid vowels | /e/ | Brightness | ★★ Supporting |
| Close vowels | /i/, /u/ | Precision, depth | ★ Accent |

### Dangerous Sounds to Avoid

| Sound | Problem | Affected Languages |
|-------|---------|-------------------|
| "th" (/θ/, /ð/) | Exists in only ~8% of languages | Most non-English |
| English "r" | Varies radically across languages | Japanese, Chinese, French, Spanish |
| "v" | Confused with "f" or "b" | German, Spanish, Japanese, Arabic |
| Consonant clusters (str-, spl-) | Impossible in many languages | Japanese, Chinese, Arabic, most African |
| "zh", "j" (English) | Highly variable | Most non-English |

### Mnemonic Hook Reference (Children's Literature Examples)

| Hook Type | Mechanism | Famous Example | Effect |
|-----------|-----------|----------------|--------|
| Alliteration | Repeated initial sound | Lewis Carroll | Lyrical, literary |
| Cognitive dissonance | Incongruent elements | Dr. Seuss | Playful authority |
| Sensory imagery | Name evokes sensation | Lemony Snicket | Vivid, tactile |
| Name splitting | Personal name transformed | Корней Чуковский | Rebirth, identity |
| Rhyme/assonance | Internal sound echo | Dr. Seuss / Mother Goose | Musical, childlike |
| Rhythmic pattern | Natural cadence | Roald Dahl (trochee) | Easy to chant |

### Format Strategy by Context

| Format | Best For | Tradition | Risk Level |
|--------|----------|-----------|------------|
| Initials + Surname | Gender neutrality, literary gravitas | J.K., C.S., A.A., E.B., P.L. | Low |
| Full First + Surname | Maximum memorability, persona building | Lemony Snicket, Lewis Carroll | Medium |
| Title + Name | Authority + playfulness | Dr. Seuss | Medium |
| Mononim | Iconic simplicity | — (rare in children's lit) | High |

### Age Group Sound Optimization

| Age Group | Optimal Sounds | Syllables | Tone |
|-----------|---------------|-----------|------|
| 0-3 (toddlers) | Maximum sonorants + open vowels | 2 | Ultra-soft, lullaby |
| 4-7 (picture books) | Sonorants + one plosive accent | 2-3 | Warm + playful |
| 8-12 (middle grade) | Balanced, allow complexity | 2-4 | Intriguing, adventurous |
| Mixed/all ages | Sonorants + plosive initial | 2-3 | Warm + memorable |

### Persona-Sound Mapping

| Persona | Primary Sounds | Structure | Example Pattern |
|---------|---------------|-----------|-----------------|
| Warm storyteller | /m/, /n/, /l/ + /a/, /o/ | Gentle CVCV | "Mona Lale" |
| Wise mentor | /t/, /s/ + /a/, /e/ | Title + balanced | "Dr. Tane" |
| Playful trickster | Plosive + sonorant contrast | Dissonant combo | "Captain Miko" |
| Mysterious narrator | /s/, /n/ + /i/, /u/ | Unusual but pronounceable | "Suni Kale" |

### Verification Checklist

| Step | Action | Tool/Method |
|------|--------|-------------|
| 1 | Google "[name] author" | Google Search |
| 2 | Search Amazon Books | amazon.com |
| 3 | Search Goodreads | goodreads.com |
| 4 | Search WorldCat | worldcat.org |
| 5 | Check domain (.com) | Domain registrar |
| 6 | Check social handles | Namechk.com |
| 7 | Cultural meaning check | Native speakers (5+ languages) |
| 8 | Child pronunciation test | 5+ children aged 4-10, 3+ language groups |
| 9 | Trademark search | USPTO / local trademark office |
| 10 | Legal registration | DBA/FBN + copyright filing |
