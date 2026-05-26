# Project Orientation

Use this reference before changing an existing Ohtools repo or when the task
does not clearly name a workflow.

## Inspect First

- Identify the package manager and scripts in `package.json`.
- Inspect lockfiles, workspace config, README, and existing scripts before using
  commands from this reference.
- Find the app entry. Common paths are `src/ohtools.ts`, `src/app.ts`, or a
  package/example-specific app module. The CLI expects `--app <path>`.
- Check whether the default export or named `app` is an `Ohtools` builder, a
  built registry wrapper, or another local composition helper.
- Map tools, groups, plugins, adapters, schemas, tests, docs, examples, and
  scaffold templates before editing.
- Record public contracts: tool IDs, group IDs, plugin names, JSON Schema input
  and output shapes, adapter IDs, CLI scripts, generated docs, and package
  exports.

## Authority Order

Live repo state beats this reference. Prefer existing package scripts, local
binaries, lockfiles, workspace config, README, and source code over example
commands here. If repo scripts disagree with skill docs, use the repo scripts
and report the mismatch as a docs update candidate.

## Migrating Existing Non-Ohtools Tools

Do not replace a working non-Ohtools CLI or MCP service unless the user asks for
migration. For explicit migrations, preserve command names, flags, MCP tool
names, input/output contracts, exit behavior, and error semantics first. Wrap
existing behavior behind `defineTool`, add Ohtools adapters incrementally, and
treat behavior changes as explicit migrations that need tests and docs.

## Expected Shape

An Ohtools project usually keeps app composition thin:

```ts
import { Ohtools } from "@bosun-sh/ohtools";
import { mcpAdapter } from "@bosun-sh/ohtools/adapters/mcp";
import { supportPlugin } from "./plugins/support";

export default new Ohtools({ name: "support-tools" })
  .use(supportPlugin)
  .adapter(mcpAdapter());
```

Larger apps should keep domain services and data access outside tool
definitions, then pass services through runtime layers or small factories.

## Ownership Cues

- `.agents/skills/ohtools/` is repo-local agent guidance. Keep it aligned with
  the app, but do not treat it as runtime code.
- `packages/ohtools/templates/*` owns scaffold output in the Ohtools package.
- `examples/*` should remain runnable and should demonstrate public APIs only.
- Docs should describe supported commands and imports from the current package.

Avoid hidden dynamic discovery as the default design. Static tool, group, and
plugin definitions produce better IDs, graph output, docs, validation, and
agent planning.
