# Sitis skills

Agent skills attached to Sitis recipes, recipe steps and projects. Each directory under `skills/` is
one skill: `SKILL.md` plus whatever it needs beside it.

YouTube channel operations live in their own repository,
[`sitis-hq/youtube-skills`](https://github.com/sitis-hq/youtube-skills). This one keeps the skills of
music releases that are not about YouTube, and general content skills such as image prompting.

## How a run receives a skill

An attachment pins a source and a commit. The run receives that commit's **whole tree** as a plugin
view that lists only the skills chosen for the step, so a skill may use files elsewhere in the
repository by a path relative to its own directory. Nothing in the repository is executed when a skill
is installed.

`<name>` — the directory name — is the name the skill is called by in a run, so it stays stable.

## Changing this repository

- **Only new commits on `main`. Never rewrite history** (force-push, squash, re-create the repository,
  change its URL). Attachments pin commits; a commit that can no longer be fetched leaves every copy
  pinned to it without its skills, silently.
- Pushing changes nothing by itself: a copy moves to a new commit only when its pin is raised on the
  shelf and the copy adopts it.
- Removing or renaming a skill is safe for copies pinned to an older commit. Before raising their
  pin, move them off the skill — a recipe's text that names a skill breaks with the rename too.

## Skills

| Skill | Used by |
| --- | --- |
| `music-lyrics-generate` | Create Music Release — "Create text content" |
| `photorealistic-image-generation` | Create Music Release — "Create cover images", "Create music story shorts" |
| `music-mix-assemble` | Create Music Mix — the assembly step (planned) |
