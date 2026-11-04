---
name: logbook
description: Operate against a logbook MCP server with the correct task lifecycle, need-info reply cycle, hook scaffolding, and one-task-at-a-time workflow. Use this skill when the user asks to work with logbook tasks, status transitions, hook setup, or session startup behavior, or invokes `/logbook` to review tasks waiting on them.
license: Complete terms in LICENSE.txt
---

# Logbook

Use this skill when working with a logbook MCP server. The server already exposes
tool schemas; this skill defines the operating rules and lifecycle contract.

## When Invoked Directly As `/logbook`

1. Find the board: the current repo's `.logbook/`. If there is none and the
   folder holds several repos, list the boards found and ask which one. If there
   are none, say so and suggest `logbook init`; never run it unasked.
2. List `need_info`, `blocked` and `pending_review` tasks, each with its last
   comment, and ask the user to answer, unblock or approve. Apply their decision
   with `task.update` (reply via `comment.replyToCommentId`, then the status).
   Never move `pending_review` to `done` without the user's explicit approval.
3. If nothing is waiting, follow Start Of Session (`task.current`, then the
   oldest suitable `todo`). With no task, say the board is clear and offer to
   show the backlog; do not promote backlog tasks unasked.
4. Work the task to its definition of done, then move it to `pending_review`
   with a comment: what changed, how it was checked, what is left. Stop after
   one task unless asked.
5. Do not commit or push unless the user asks.

## Start Of Session

Run this only when Logbook is intentionally being used for task work, status
transitions, hook setup, or session startup. Do not auto-start a Logbook task for
inspection-only requests.

1. Call `task.current` before starting task work.
2. If it returns a task, read `title`, `description`, and `definition_of_done`;
   continue that task and do not list or start another.
3. If it returns nothing, call `task.list` with `{ "status": "todo" }`.
4. Start exactly one suitable task only after applying this selection order:
   user-requested task, matching project or milestone, clearest
   `definition_of_done`, lower estimation, oldest created or updated task.
5. If multiple candidates existed, note briefly why the task was selected.
6. If no suitable task exists, report that no actionable Logbook task is
   available. Do not create one unless the user asks or discovered work clearly
   needs tracking.

## Server Availability

- If Logbook MCP tools are absent, use the CLI when `logbook` is installed:
  `logbook task:list --status "*"`, `logbook task:update ...`. Each command
  prints one JSON envelope; check `ok`. Details:
  https://github.com/bosun-sh/logbook#cli
- Never pass `--help` to a subcommand: it runs the command instead.
- If neither MCP nor CLI is available, do not simulate lifecycle changes; tell
  the user and continue only with read-only local assessment.
- Never claim task status changed unless the response had `ok: true`.

## Tool Use Rules

- Always check `ok` before reading `data` from any MCP response.
- On `ok: false`, surface `error.message` and stop that call path.
- Do not duplicate tool input schemas in this skill.
- Use `task.update` for lifecycle transitions.
- Use `task.edit` only for metadata changes such as `title`, `description`,
  `definition_of_done`, or `estimation`.

## One Task At A Time

- Only one task may be `in_progress` for the session.
- Before starting a different task, move the current one to `need_info`,
  `blocked`, or `pending_review`, or provide the required justification comment.

## Status Transitions

| From | To | Comment required? | Notes |
|------|----|-------------------|-------|
| `backlog` | `todo` | No | Grooming only |
| `todo` | `in_progress` | No | Sets `in_progress_since` |
| `in_progress` | `need_info` | Yes | Blocking question for the user |
| `need_info` | `in_progress` | Yes | Answer every open question |
| `in_progress` | `blocked` | Yes | External blocker, not a question |
| `blocked` | `in_progress` | Yes | Describe how the blocker was resolved |
| `in_progress` | `pending_review` | No | Triggers reviewer spawn |
| `pending_review` | `in_progress` | Yes | Reviewer issues only; never self-approve |
| `pending_review` | `done` | Yes | Reviewer approval only |

## Need-Info Cycle

When a task is in `need_info`:

1. Read every comment with `kind: "need_info"` that has no reply.
2. Answer all open questions.
3. Call `task.update` with `new_status: "in_progress"` and a comment whose `reply`
   field contains the answers.

Never return to `in_progress` with an empty or placeholder reply.

## Review Flow

When `definition_of_done` is satisfied:

1. Call `task.update` with `new_status: "pending_review"`.
2. Do not mark the task `done` yourself.
3. Wait for the reviewer to either return the task to `in_progress` with issues or
   move it to `done`.

## Creating Tasks

Use `task.create` when you discover work that is not yet tracked. Supply a
specific, verifiable `definition_of_done`, plus matching `project` and
`milestone` values for the current work context. Use a Fibonacci estimation value
(`1`, `2`, `3`, `5`, `8`, or `13`) when setting or revising effort.

## Hook Scaffolding

Hooks live at:

```text
.logbook/hooks/<id>/
├── config.json
└── script.ts
```

`config.json` must define:

- `id`
- `event`
- `command`
- Optional `condition`
- Optional `timeoutMs`

The supported event today is `task.status_changed`. Hook scripts receive:

- `LOGBOOK_TASK_ID`
- `LOGBOOK_OLD_STATUS`
- `LOGBOOK_NEW_STATUS`
- `LOGBOOK_SESSION_ID`
- `LOGBOOK_TASKS_FILE`

Guard against missing values and exit `0` when the hook should skip work.

Hook IDs must be lowercase slug IDs with no path separators and no `..`. Before
creating `.logbook/hooks/<id>/`, check whether the directory, `config.json`, or
`script.ts` already exists. Do not overwrite existing hook files without
explicit user approval.

Generated hook scripts must be minimal, idempotent, and environment-guarded.
`config.json` commands should target the local hook script path and avoid
destructive shell chains. Validate with `hook.run` when available; otherwise
inspect the config and script shape only.

### Minimal Script Shape

```typescript
#!/usr/bin/env bun
const taskId = process.env["LOGBOOK_TASK_ID"] ?? ""
if (taskId === "") process.exit(0)

process.exit(0)
```

## Tool Discovery And Naming

The MCP server's exposed tool list and schemas are authoritative. Prefer live
tool discovery over static names, and do not duplicate MCP input schemas in this
skill.

Expected capabilities include current task lookup, task listing, lifecycle
updates, task metadata edits, task creation, hook listing, and hook execution.
If an expected tool is missing or renamed, stop that call path and report the
missing capability instead of guessing a replacement.

## Non-Goals

- Do not document MCP input schemas.
- Do not document Linear or GitHub sync internals.
- Do not document CLI flags; link to the logbook README instead.
