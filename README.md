# Bosun Skills

This repository contains agent skills developed for Bosun.

Skills live under `skills/`, with one directory per skill. Each skill is a
self-contained package of instructions, references, and optional assets that an
agent can load when the user's task matches that skill's purpose.

## Skills

| Skill | Purpose |
| --- | --- |
| `skills/ohtools` | Guidance for creating, extending, reviewing, and releasing Ohtools apps, CLI tools, MCP adapters, and plugins. |

## Repository Layout

```text
skills/
  <skill-name>/
    SKILL.md
    LICENSE.txt
    references/
```

Every skill should include:

- `SKILL.md`: the entry point with the skill name, description, license pointer,
  usage rules, and links to any deeper references.
- `LICENSE.txt`: the license terms for the skill.
- `references/`: supporting material that should be loaded only when relevant to
  the task.

## Adding A Skill

1. Create a new directory under `skills/`.
2. Add a concise `SKILL.md` that tells an agent when to use the skill and what to
   read first.
3. Keep detailed workflow notes in `references/` instead of overloading
   `SKILL.md`.
4. Include a `LICENSE.txt`.
5. Keep the skill focused on Bosun workflows, products, and engineering
   conventions.

## Current Status

This repo currently contains one skill: `skills/ohtools`.
