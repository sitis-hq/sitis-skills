---
name: spotify-pitch
description: Draft the Spotify for Artists pitch description for an upcoming release, and know Spotify's rules a pitch depends on. Use when a step drafts or redrafts a pitch description (at most 500 characters) from the song's lyrics, subgenre and genre. The description is the owner's to approve; this skill writes the draft only.
---

# Spotify pitch

## When it is used

- **Create Music Release — "Distribute single to DistroKid"**: drafts the description of the release
  that holds the pitch reservation, for the owner to approve. Pitch a Song on Spotify drafts nothing:
  it uses the approved text or does not pitch.

## Inputs

1. **The approved lyrics** — the song's lyric file from Create Music Release's "Create text content".
   Required: a description is grounded in what the song actually says. Without them, do not draft.
2. **The subgenre** — `audio:<Spec id>:subgenre` in Create Music Release's memory, chosen at the start of
   "Generate audio".
3. **The genre** — `MUSIC_PRIMARY_GENRE`; the song's language — `MUSIC_LYRICS_LANGUAGE`.
4. The song's title as approved (the release record's `title`).

## The description

- **At most 500 characters** (Spotify's limit). Count before showing it.
- **Written complete in one pass.** Spotify lets a pitch be edited until release day, but does not
  promise editors see the change.
- **Grounded in the lyrics**: the song's concrete story, an image or two, its mood — not an abstract
  blurb. Never paste lyric lines wholesale; one short phrase may be quoted when it carries the song.
- **Genre and vibe**, anchored on the subgenre and `MUSIC_PRIMARY_GENRE`, in the words an editor files by
  (instrumentation, tempo feel, mood).
- **One or two playlist directions** it fits — the kind of editorial playlist (mood, moment, scene),
  never a promise of a specific playlist.
- **Neutral editorial tone.** No hype ("the next big hit"), no links, no hashtags, no emojis, no streaming
  numbers that are not true and checkable.
- **English**, whatever the song's language; name the song's language when it is not English.
- What editors ask for, per Spotify: the story behind the song, its genre and vibe, the playlists it
  suits; "more detail gives your song a better chance" (references/pitch-timing-research.md, section 5).

**Output**: the text alone, then its character count on a separate line for the step to check. A
redraft changes the angle (another image, another playlist direction), not only the wording.

## Spotify's rules a pitch depends on

These are rules, not timings. When and how fast a distributor delivers, or Spotify lists a release,
is never estimated here or in a recipe: a recipe observes it.

- **A pitch needs the release in the Upcoming tab** of Spotify for Artists with a "Pitch a song" link.
- **One pitch at a time**: the next pitch is possible once the pitched song is out. A released song
  cannot be pitched.
- **The description takes at most 500 characters**; Spotify lets it be edited until release day but
  does not promise editors see the change, so it is written complete once.
- **A distributor's paid pitching service** blocks the artist's own pitch for that release. Do not
  enable it for a release we pitch ourselves.
- **What a pitch reliably buys**: the song chosen for followers' Release Radar, and a pin in "This Is"
  for up to 28 days. An editorial playlist is a bonus.

`references/pitch-timing-research.md` collects artists' reports and Spotify's help pages (October
2026). Its timing anecdotes are **background, not used for planning**: the recipes compute only their
own rules (youtube-skills CONTRACT.md, rule 17).
