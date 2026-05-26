# Bosun Skills

This repository contains agent skills developed for Bosun.

Skills live under `skills/`, with one directory per skill. Each skill is a
self-contained package of instructions, references, and optional assets that an
agent can load when the user's task matches that skill's purpose.

## Installation

Install any skill into your Claude Code project using `npx`:

```bash
npx skills add https://github.com/bosun-sh/skills.git --skill <skill-name>
```

For example:

```bash
npx skills add https://github.com/bosun-sh/skills.git --skill logbook
npx skills add https://github.com/bosun-sh/skills.git --skill plot
npx skills add https://github.com/bosun-sh/skills.git --skill ohtools
```

## Skills

| Skill | Purpose |
| --- | --- |
| `skills/logbook` | Guidance for working with logbook tasks, lifecycle transitions, hooks, and session startup behavior. |
| `skills/plot` | Guidance for writing layered project specs using the concept, umbrella, and feature workflow. |
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

This repo currently contains three skills: `skills/logbook`, `skills/plot`, and `skills/ohtools`.
