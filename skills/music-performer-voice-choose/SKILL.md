---
description: Choose optimal performer voice type for music generation based on genre, mood, and production context. Use when asked to "choose voice", "select singer type", "pick vocal style", "recommend voice for genre", or "what voice for this song".
---

# Requirements Document

## Introduction

This document defines requirements for the "Music Performer Voice Choose" skill - an AI-powered voice type selection system optimized for genre authenticity, emotional impact, and production compatibility. The skill enables intelligent voice recommendations for music generation based on scientific research and industry standards.

Scientific foundation: Research by Bruder, Poeppel & Larrouy-Maestri (2024) demonstrates that acoustic parameters explain only 1.6% of listener preferences, while perceptual characteristics explain 43%. Key predictors include pitch accuracy, resonance, soft attack, and moderate vibrato. This confirms that genre fit and authenticity matter more than technical range.

## Glossary

- **Lyric Voice**: Light, flexible voice suited for melodic passages with agility
- **Dramatic Voice**: Powerful, rich voice with strong projection and intensity
- **Spinto Voice**: Voice between lyric and dramatic, capable of both delicacy and power
- **Tessitura**: The most comfortable and frequently used range of a voice
- **Belt**: Powerful chest-dominant singing in higher range, common in pop and musical theater
- **Mixed Voice**: Blend of chest and head voice for smooth transitions across range
- **Falsetto**: Light, airy head voice register, typically in male singers
- **Melisma**: Singing multiple notes on a single syllable (vocal runs)
- **Twang**: Bright, nasal resonance characteristic of country music
- **Vocal Fry**: Low, creaky register used for emotional effect in indie/alternative
- **Coloratura**: Agile, ornamental singing with rapid passages and trills
- **Bel Canto**: Classical Italian singing technique emphasizing beauty of tone

## Requirements

### Requirement 1: Genre-Based Voice Selection

**User Story:** As a music producer, I want voice recommendations based on genre, so that the vocal style matches listener expectations and industry standards.

#### Acceptance Criteria - Pop

1. WHEN genre is Pop AND gender is Female THEN recommend lyric mezzo-soprano (Beyoncé, Adele, Dua Lipa style)
2. WHEN genre is Pop AND gender is Male THEN recommend light-lyric tenor (Ed Sheeran, The Weeknd, Bruno Mars style)
3. THE Pop voice SHALL include falsetto capability
4. THE Pop voice SHALL include mixed voice technique
5. THE Pop voice SHALL include melisma capability for vocal runs
6. THE Pop voice prompt SHALL be: `"Warm lyric mezzo-soprano with smooth belt capability, radio-friendly pop delivery"` (female) or `"Warm light-lyric tenor with falsetto capability, radio-friendly pop delivery"` (male)

#### Acceptance Criteria - Electronic / EDM

1. WHEN genre is Electronic/EDM AND gender is Female THEN recommend soprano or light mezzo-soprano (Ellie Goulding, MØ style)
2. WHEN genre is Electronic/EDM AND gender is Male THEN recommend tenor with falsetto capability
3. THE Electronic voice SHALL include long sustained note capability
4. THE Electronic voice SHALL include clean tone that cuts through dense mix
5. THE Electronic voice SHALL include ethereal quality
6. THE Electronic voice prompt SHALL be: `"Airy soprano voice with ethereal quality, clean tone for electronic production"`

#### Acceptance Criteria - Rock / Metal

1. WHEN genre is Rock/Metal AND gender is Female THEN recommend dramatic mezzo-soprano with power
2. WHEN genre is Rock/Metal AND gender is Male THEN recommend dramatic baritone (Dave Grohl, James Hetfield style)
3. THE Rock voice SHALL include scream capability
4. THE Rock voice SHALL include growl technique
5. THE Rock voice SHALL include belt and raspy delivery
6. THE Rock voice prompt SHALL be: `"Powerful dramatic baritone with gritty rasp, capable of intense belt and controlled scream"`

#### Acceptance Criteria - Indie / Alternative

1. WHEN genre is Indie/Alternative AND gender is Female THEN recommend lyric mezzo-soprano (Florence Welch style)
2. WHEN genre is Indie/Alternative AND gender is Male THEN recommend lyric baritone or tenor (Hozier, Alex Turner style)
3. THE Indie voice SHALL include falsetto capability
4. THE Indie voice SHALL include whisper and breathy "indie voice" quality
5. THE Indie voice SHALL include subtle vibrato
6. THE Indie voice prompt SHALL be: `"Intimate lyric baritone with breathy quality, authentic indie delivery with subtle vibrato"`

#### Acceptance Criteria - Hip-Hop / Rap

1. WHEN genre is Hip-Hop/Rap AND gender is Female THEN recommend mezzo with strong chest voice (Megan Thee Stallion style)
2. WHEN genre is Hip-Hop/Rap AND gender is Male THEN recommend baritone/tenor hybrid (Drake, Kendrick style)
3. THE Hip-Hop voice SHALL include autotune compatibility
4. THE Hip-Hop voice SHALL include vocal persona versatility
5. THE Hip-Hop voice SHALL include melodic rap capability
6. THE Hip-Hop voice prompt SHALL be: `"Versatile baritone with melodic capability, smooth autotune-ready tone for modern hip-hop"`

#### Acceptance Criteria - Lo-Fi / Chill

1. WHEN genre is Lo-Fi/Chill AND gender is Female THEN recommend mezzo-soprano or soprano (Clairo, Kali Uchis style)
2. WHEN genre is Lo-Fi/Chill AND gender is Male THEN recommend tenor or lyric baritone (Frank Ocean, Daniel Caesar style)
3. THE Lo-Fi voice SHALL include intimate delivery quality
4. THE Lo-Fi voice SHALL include breathy texture
5. THE Lo-Fi voice SHALL include emotional vulnerability
6. THE Lo-Fi voice prompt SHALL be: `"Warm intimate tenor with bedroom recording quality, vulnerable emotional delivery"`

#### Acceptance Criteria - Jazz

1. WHEN genre is Jazz AND gender is Female THEN recommend contralto or mezzo-soprano (Diana Krall style)
2. WHEN genre is Jazz AND gender is Male THEN recommend lyric baritone (Gregory Porter style)
3. THE Jazz voice SHALL include strong chest voice
4. THE Jazz voice SHALL include improvisation capability
5. THE Jazz voice SHALL include intimate mic technique
6. THE Jazz voice prompt SHALL be: `"Rich contralto with warm chest resonance, sophisticated jazz phrasing and subtle improvisation"`

#### Acceptance Criteria - Classical / Opera

1. WHEN genre is Classical/Opera AND gender is Female THEN recommend lyric soprano (Anna Netrebko style)
2. WHEN genre is Classical/Opera AND gender is Male THEN recommend spinto or bel canto tenor (Jonas Kaufmann style)
3. THE Classical voice SHALL include bel canto technique
4. THE Classical voice SHALL include coloratura capability
5. THE Classical voice SHALL include acoustic projection without amplification
6. THE Classical voice prompt SHALL be: `"Powerful lyric soprano with classical training, pure bel canto technique and controlled vibrato"`

#### Acceptance Criteria - Modern Country

1. WHEN genre is Modern Country AND gender is Female THEN recommend soprano with strong belt (Carrie Underwood style)
2. WHEN genre is Modern Country AND gender is Male THEN recommend warm baritone (Luke Combs, Morgan Wallen style)
3. THE Modern Country voice SHALL include twang capability
4. THE Modern Country voice SHALL include belt technique
5. THE Modern Country voice SHALL include radio-friendly delivery
6. THE Modern Country voice prompt SHALL be: `"Warm creamy baritone with authentic twang, powerful belt for modern country radio"`

#### Acceptance Criteria - Outlaw / Traditional Country

1. WHEN genre is Outlaw/Traditional Country AND gender is Female THEN recommend mezzo-soprano with character
2. WHEN genre is Outlaw/Traditional Country AND gender is Male THEN recommend dramatic baritone or bass-baritone (Chris Stapleton, Colter Wall style)
3. THE Outlaw Country voice SHALL include rasp and growl
4. THE Outlaw Country voice SHALL include storytelling delivery
5. THE Outlaw Country voice SHALL include raw emotional quality
6. THE Outlaw Country voice prompt SHALL be: `"Deep gravelly dramatic baritone with authentic rasp, raw emotional storytelling quality"`

#### Acceptance Criteria - Americana / Indie Country

1. WHEN genre is Americana/Indie Country AND gender is Female THEN recommend mezzo-soprano with dynamic range (Brandi Carlile style)
2. WHEN genre is Americana/Indie Country AND gender is Male THEN recommend tenor or lyric baritone (Jason Isbell, Tyler Childers style)
3. THE Americana voice SHALL include emotional delivery
4. THE Americana voice SHALL include natural vibrato
5. THE Americana voice SHALL include vocal fry capability
6. THE Americana voice prompt SHALL be: `"Expressive lyric baritone with natural vibrato, authentic Americana emotional delivery"`

### Requirement 2: Mood-Based Voice Adjustment

**User Story:** As a music producer, I want voice recommendations adjusted for mood, so that the vocal delivery matches the emotional intent of the track.

#### Acceptance Criteria

1. WHEN mood is Upbeat/Dance THEN prioritize light, agile voices with energy
2. WHEN mood is Ballad/Emotional THEN prioritize voices with belt capability and emotional depth
3. WHEN mood is Aggressive THEN prioritize dramatic voices with rasp and power
4. WHEN mood is Melodic THEN prioritize voices with smooth transitions and range
5. WHEN mood is Euphoric THEN prioritize airy, soaring voices
6. WHEN mood is Dark/Moody THEN prioritize voices with falsetto and lower register depth
7. THE System SHALL combine genre and mood criteria for optimal recommendation

### Requirement 3: Voice Type Range Compliance

**User Story:** As a music producer, I want voice recommendations within proper vocal ranges, so that the generated vocals are technically accurate.

#### Acceptance Criteria

1. THE soprano voice SHALL have range C4–C6
2. THE mezzo-soprano voice SHALL have range A3–A5
3. THE contralto voice SHALL have range F3–F5
4. THE tenor voice SHALL have range C3–C5
5. THE baritone voice SHALL have range A2–A4
6. THE bass-baritone voice SHALL have range F2–F4
7. THE System SHALL NOT recommend voice types outside their natural range for the song's tessitura

### Requirement 4: Production Context Consideration

**User Story:** As a music producer, I want voice recommendations that consider production context, so that the voice sits well in the final mix.

#### Acceptance Criteria

1. WHEN production is Dense/Layered THEN recommend voices with clear tone that cuts through mix
2. WHEN production is Minimal/Sparse THEN recommend voices with rich texture and character
3. WHEN production is Lo-Fi/Bedroom THEN recommend intimate voices with natural imperfections
4. WHEN production is Polished/Commercial THEN recommend clean, radio-ready voices
5. THE System SHALL consider frequency spectrum occupation when recommending voice type

### Requirement 5: Critical Selection Rules

**User Story:** As a music producer, I want consistent selection criteria, so that recommendations are reliable and predictable.

#### Acceptance Criteria

1. THE System SHALL prioritize genre match over vocal range
2. THE System SHALL prioritize unique timbre over wide range (recognizability over range)
3. THE System SHALL ensure voice can deliver required techniques for the genre
4. THE System SHALL prioritize emotional authenticity over technical perfection
5. THE System SHALL consider how voice sits in the mix (production context)
6. THE System SHALL NOT recommend voices incompatible with genre expectations

### Requirement 6: User Confirmation

**User Story:** As a music producer, I want to confirm voice selection before proceeding, so that I maintain creative control.

#### Acceptance Criteria

1. THE System SHALL present voice recommendation with reasoning
2. THE System SHALL NOT auto-select without user approval when multiple valid options exist
3. WHEN presenting recommendation THEN include voice type, example artists, key techniques, and prompt template
4. THE System SHALL offer alternative options when available

### Requirement 7: Error Handling

**User Story:** As a music producer, I want clear feedback when selection fails, so that I can adjust my requirements.

#### Acceptance Criteria

1. IF genre is not recognized THEN request clarification from user
2. IF conflicting requirements exist THEN present options with trade-offs
3. THE System SHALL NOT guess when critical information is missing
4. WHEN error occurs THEN offer guidance on valid options

---

## Voice Type Reference Table

| Voice Type | Range | Best Genres |
|------------|-------|-------------|
| Soprano | C4–C6 | Pop, EDM, Classical, Modern Country |
| Mezzo-soprano | A3–A5 | Pop, Rock, Indie, Jazz, Lo-Fi |
| Contralto | F3–F5 | Jazz, Blues, Americana |
| Tenor | C3–C5 | Pop, EDM, Indie, Lo-Fi, Classical |
| Baritone | A2–A4 | Rock, Country, Jazz, Hip-Hop, Indie |
| Bass-baritone | F2–F4 | Outlaw Country, Traditional |

---

## Genre-Mood Decision Matrix

| If Genre Is... | And Mood Is... | Recommend |
|----------------|----------------|-----------|
| Pop | Upbeat/Dance | Light tenor / Mezzo-soprano |
| Pop | Ballad/Emotional | Lyric tenor / Mezzo with belt |
| Rock | Aggressive | Dramatic baritone with rasp |
| Rock | Melodic | Tenor with belt capability |
| Country | Traditional | Warm baritone with twang |
| Country | Modern/Pop | Baritone or soprano with belt |
| Hip-Hop | Melodic | Tenor/baritone hybrid |
| Hip-Hop | Hard/Aggressive | Low baritone with chest voice |
| Electronic | Euphoric | Airy soprano |
| Electronic | Dark/Moody | Mezzo or tenor with falsetto |
| Jazz | Intimate | Contralto or lyric baritone |
| Jazz | Upbeat/Swing | Mezzo-soprano or tenor |
| Indie | Melancholic | Lyric baritone with vocal fry |
| Indie | Ethereal | Soprano with falsetto |

---

## Prompt Templates by Genre

### Pop - Female
```
Warm lyric mezzo-soprano with smooth belt capability, radio-friendly pop delivery, capable of falsetto transitions and melismatic runs, clear tone with emotional depth
```

### Pop - Male
```
Warm light-lyric tenor with falsetto capability, radio-friendly pop delivery, smooth mixed voice transitions, capable of emotional ballad delivery and upbeat energy
```

### Electronic/EDM - Female
```
Airy soprano voice with ethereal quality, clean tone for electronic production, capable of long sustained notes, cuts through dense mix with clarity
```

### Electronic/EDM - Male
```
Clean tenor with ethereal falsetto capability, smooth tone for electronic production, capable of sustained phrases, modern EDM vocal delivery
```

### Rock/Metal - Female
```
Powerful dramatic mezzo-soprano with gritty edge, capable of intense belt and controlled scream, raw emotional delivery with rock authenticity
```

### Rock/Metal - Male
```
Powerful dramatic baritone with gritty rasp, capable of intense belt and controlled scream, raw rock delivery with emotional intensity
```

### Indie/Alternative - Female
```
Intimate lyric mezzo-soprano with breathy quality, authentic indie delivery with subtle vibrato, capable of whisper to belt dynamics, emotional vulnerability
```

### Indie/Alternative - Male
```
Intimate lyric baritone with breathy quality, authentic indie delivery with subtle vibrato, capable of falsetto and vocal fry, emotional authenticity
```

### Hip-Hop/Rap - Female
```
Versatile mezzo with strong chest voice, smooth autotune-ready tone for modern hip-hop, capable of melodic hooks and rhythmic delivery
```

### Hip-Hop/Rap - Male
```
Versatile baritone with melodic capability, smooth autotune-ready tone for modern hip-hop, capable of melodic rap and rhythmic flow
```

### Lo-Fi/Chill - Female
```
Warm intimate mezzo-soprano with bedroom recording quality, vulnerable emotional delivery, breathy texture with natural imperfections
```

### Lo-Fi/Chill - Male
```
Warm intimate tenor with bedroom recording quality, vulnerable emotional delivery, breathy texture with natural imperfections, lo-fi aesthetic
```

### Jazz - Female
```
Rich contralto with warm chest resonance, sophisticated jazz phrasing and subtle improvisation, intimate mic technique, classic jazz delivery
```

### Jazz - Male
```
Rich lyric baritone with warm chest resonance, sophisticated jazz phrasing and subtle improvisation, intimate mic technique, classic jazz delivery
```

### Classical/Opera - Female
```
Powerful lyric soprano with classical training, pure bel canto technique and controlled vibrato, capable of coloratura passages, acoustic projection
```

### Classical/Opera - Male
```
Powerful spinto tenor with classical training, pure bel canto technique and controlled vibrato, capable of dramatic passages, acoustic projection
```

### Modern Country - Female
```
Bright soprano with authentic twang, powerful belt for modern country radio, capable of emotional ballad delivery and upbeat energy
```

### Modern Country - Male
```
Warm creamy baritone with authentic twang, powerful belt for modern country radio, capable of emotional storytelling and radio-friendly delivery
```

### Outlaw/Traditional Country - Female
```
Character mezzo-soprano with authentic rasp, raw emotional storytelling quality, capable of growl and intimate delivery, traditional country authenticity
```

### Outlaw/Traditional Country - Male
```
Deep gravelly dramatic baritone with authentic rasp, raw emotional storytelling quality, capable of growl and intimate delivery, outlaw country authenticity
```

### Americana/Indie Country - Female
```
Expressive mezzo-soprano with natural vibrato, authentic Americana emotional delivery, capable of dynamic range from whisper to belt
```

### Americana/Indie Country - Male
```
Expressive lyric baritone with natural vibrato, authentic Americana emotional delivery, capable of vocal fry and emotional intensity
```

---

## Scientific Research Reference

Based on Bruder, Poeppel & Larrouy-Maestri (2024):

| Factor | Variance Explained |
|--------|-------------------|
| Acoustic parameters | 1.6% |
| Perceptual characteristics | 43% |

Key predictors of listener preference:
- Pitch accuracy
- Resonance quality
- Soft attack
- Moderate vibrato

Conclusion: No universal "ideal voice" exists — genre fit and authenticity matter most.
