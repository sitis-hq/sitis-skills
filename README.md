# Sitis skills

Agent skills delivered to a run as **attachments** of a spec unit (project, template or
task-template). Each directory under `skills/` is one skill: `SKILL.md` plus whatever it needs
beside it. The runtime clones this repository into a worker-local mirror, checks out the pinned
sha and materialises the selected skills into the per-run `.claude/skills/<name>/`, which is the
only path the Skill tool reads.

Layout is the contract:

```
skills/<name>/SKILL.md
```

`<name>` is the directory name — it becomes the skill name in the run, so it must be stable.
`SKILL.md` front matter carries `description` (shown when picking the skill) and `allowed-tools`.

## Pinning

An attachment records a sha, never a moving ref: two runs of the same unit must see the same
skill. Pushing to this repository therefore changes nothing by itself — the attachment has to be
re-pinned to the new sha.

## Current dependency on the host image

These skills call CLIs that today ship inside the worker image (`ai-generator` for generation,
`ai-integration` for delivering results back to the chat, `media-commands` for editing). The
generation half is being moved out: the capability will arrive as its own attachment instead of
being baked into the image, and the skills will be rewritten onto it. Until that lands, a run
without those binaries on `PATH` will fail at the first Bash call, so this repository is not yet
self-sufficient.
