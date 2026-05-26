# Model Inventory

Sounder can use model inventory from three optional sources:

1. Client/runtime context injected by the agent client.
2. Models or candidate lists named in the current user prompt.
3. `MODEL_INVENTORY.md` in the Sounder skill root.

All three sources are optional. When more than one exists, compose them into one
candidate pool for the current decision. Only restrict the pool when the user
explicitly asks for a restriction, such as "only use A and B" or "restrict to
client models."

## Source Priority

- Client/runtime context is the best signal for models the current client can select directly.
- Prompt-level inventory is additive by default and restrictive only when the user explicitly says so.
- `MODEL_INVENTORY.md` is persistent local configuration and may add models available through external providers, such as a user-configured OpenRouter API key.

If sources conflict, prefer explicit prompt restrictions for the current task,
prefer runtime context for direct client-selectable models, and use
`MODEL_INVENTORY.md` for externally available models, ordering, and notes.

When recommending a model from `MODEL_INVENTORY.md` that is not present in the
runtime inventory, call out the assumed provider or access path if the file
names one. If no access path is named, ask the user to confirm the model is
available before treating it as directly usable.

## Root Inventory Format

Use Markdown so the file is easy to maintain without special tooling. List model
names in smallest-to-largest reliable order:

```md
# Model Inventory

## Models

- compact-model
- standard-model
- advanced-model

## Defaults

- Default model: standard-model
- Subagent model overrides supported: yes
- External providers: OpenRouter

## Notes

- compact-model: good for extraction, classification, simple rewrites.
- standard-model: good default for normal coding and planning.
- advanced-model: use for ambiguous, long-context, or high-judgment tasks.
- openrouter/example-model: provider OpenRouter, 128k context, low cost, moderate latency.
```

The exact headings are flexible. Extract model names, ordering, default model,
override support, provider/access path, aliases, context window, cost, latency,
and useful notes from the file when present.

## Availability Labels

- `direct`: the current client/runtime can select the model directly.
- `external`: the model is available through configured provider notes, such as OpenRouter.
- `unconfirmed`: the model is listed but no access path is clear.
- `unknown`: no inventory exists.

Sounder can recommend external models for assignment and estimation, but the
client/runtime or a separate spawn skill is responsible for executing any
provider-specific subagent spawning.

## Missing Inventory

When no inventory is available, do not invent exact model names.

For ordinary model sizing, ask the user for available models and rough
smallest-to-largest ordering. If the user provides inventory and the installed
skill location is writable, create or update `MODEL_INVENTORY.md` from the
user's answer. If writes are not possible, return the Markdown the user can
place in that file.

For subagent decisions, a missing inventory does not block delegation. Recommend
`model: inherit/default` unless the task clearly needs an override, and classify
the required capability tier as compact, standard, or advanced.
