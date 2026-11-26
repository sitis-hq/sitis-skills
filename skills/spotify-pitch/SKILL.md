---
name: spotify-pitch
description: Draft the Spotify for Artists pitch description for an upcoming release, and know the timing facts a pitch depends on. Use when a step drafts or redrafts a pitch description (at most 500 characters) from the song's lyrics, subgenre and genre, or when it judges whether and when a release can still be pitched. The description is the owner's to approve; this skill writes the draft only.
---

# Spotify pitch

## When it is used

- **Create Music Release — "Distribute single to DistroKid"**: drafts the description of a release the
  owner allowed to be pitched (`pitch_ok`), for the owner to approve before the submit.
- **Pitch a Song on Spotify**: a run the owner started (Run) may redraft it at the owner's request. A
  scheduled run never drafts: it uses the approved text or does not pitch.

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

## Timing facts a recipe plans by

From `references/pitch-timing-research.md` (artists' reports and Spotify's help pages, October 2026):

- **A pitch is possible only once the release shows in the Upcoming tab** of Spotify for Artists — after
  the distributor delivers it. Delivery, review and the profile steps take one to three weeks; this
  chain, not editors' taste, is where pitches are lost.
- **Pitch on the day the release appears in Upcoming.** Target: 3–4 weeks before release. 7 days before
  release is Spotify's minimum for Release Radar, an emergency floor, not a plan.
- **Ship to the distributor 4–6 weeks before release** for a pitched release (a new, unclaimed profile:
  6–7 weeks).
- **One pitch at a time**: the next pitch is possible once the pitched song is out. A released song
  cannot be pitched.
- **Two future releases delivered at once** — one artist reports he then could not pitch one of them.
  An anecdote, not a rule; worth watching when several releases are in Upcoming together.
- **A distributor's paid pitching service** blocks the artist's own pitch for that release and, when its
  curators decline, uses the attempt up. Do not enable it for a release we pitch ourselves.
- **What a pitch reliably buys**: the song chosen for followers' Release Radar, and a pin in "This Is"
  for up to 28 days. An editorial playlist is a bonus, often personalised and modest.
