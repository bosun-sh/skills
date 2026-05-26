---
name: sounder
description: Estimate the smallest reliable LLM for a task, prompt, spec, or subagent. Use when a user wants to size a task for model capability, compare available models, assign work to an agent, decide whether to spawn a subagent, choose a worker/explorer/default agent for delegated work, or choose the least capable model that can still complete the work with acceptable quality.
---

# Sounder

Estimate task difficulty against the available model set, then choose the smallest model or subagent assignment that is still likely to succeed.

For model inventory formats and examples, read `references/model-inventory.md`
when the available models are not obvious from client/runtime context or the
user prompt.

## Inputs

- Accept either pasted text, a task prompt, a spec, or a file path.
- Build the model inventory from all available optional sources: client/runtime context, user prompt, and `MODEL_INVENTORY.md` in the skill root.
- Treat client/runtime inventory as the best signal for models the current client can select directly.
- Treat user prompt inventory as additive unless the user explicitly restricts the candidate pool.
- Treat `MODEL_INVENTORY.md` as persistent local configuration that may add models available through external providers, not canonical bundled reference material.
- When evaluating a subagent, treat the delegated subtask as the unit being estimated, not the whole parent task.
- Do not force a file format. Read whatever the user gives and extract the task requirements from it.

## Model Inventory

Use every available inventory source and merge them into one candidate pool.
Distinguish directly selectable client models from models available through
configured external providers. Only restrict the pool when the user explicitly
says to, such as "only use A and B" or "restrict to client models."

Track the inventory source and availability in the recommendation:

- `inventory_source`: `runtime`, `prompt`, `file`, any `+` combination, or `none`.
- `availability: direct` when the current client/runtime can select the model directly.
- `availability: external` when the model is available through configured provider notes.
- `availability: unconfirmed` when a model is listed but no access path is clear.
- `availability: unknown` when no inventory exists.
- `provider` is optional. Use it for external models with a named access path such as OpenRouter, Anthropic, OpenAI, or a local runtime.

If no inventory is available:

- Ask the user for the available models and rough smallest-to-largest ordering when a named model recommendation is required.
- If the user provides inventory but does not ask to save it, use it only for the current recommendation.
- Do not create or update `MODEL_INVENTORY.md` unless the user explicitly asks to persist inventory.
- If the user asks to save inventory and the installed skill location is writable, update `MODEL_INVENTORY.md`; otherwise provide exact Markdown the user can place there.
- For subagent decisions that do not require an explicit model override, recommend inherited/default model selection and classify the needed tier instead of inventing model names.

## Workflow

1. Identify the task shape.
   - Determine whether the work is generation, extraction, transformation, reasoning, planning, coding, or multi-step agentic work.
   - Note output length, required precision, tool use, delegation boundaries, and whether the task has hidden dependencies.

2. Estimate difficulty.
   - Prefer larger models for ambiguous goals, multi-constraint work, long-context synthesis, or tasks that require planning across steps.
   - Prefer smaller models for bounded extraction, simple rewrites, classification, templated output, or short deterministic edits.
   - Treat hallucination risk, requirement density, and quality sensitivity as first-class signals.

3. Rank the available models.
   - Use only models found in client/runtime context, the user prompt, or `MODEL_INVENTORY.md`.
   - Prefer the smallest model that clears the reliability bar for the task.
   - Break ties by lower token cost, shorter latency, and narrower capability than the next larger option.
   - If two models look close, choose the safer one unless the task is clearly low risk.

4. Escalate when needed.
   - Move up a tier when the task is underspecified, the output will be user-facing and high stakes, or the model would need to simulate too much hidden state.
   - Do not over-optimize into a smaller model if that likely causes retries, rework, or degraded quality.

## Capability Tiers

- `compact`: extraction, classification, simple rewrites, templated output, and localized low-risk edits.
- `standard`: normal coding, bounded planning, moderate synthesis, and multi-file but well-scoped work.
- `advanced`: ambiguous goals, long-context synthesis, high-judgment decisions, high-stakes output, and brittle multi-step agentic work.

## Subagent Spawn

Use Sounder before spawning a subagent when delegation is under consideration.

- Recommend `spawn: no` when the task is the immediate critical path, too coupled to local context, too vague to delegate, or faster to handle locally.
- Recommend `spawn: yes` when the subtask is bounded, self-contained, materially advances the work, and can run without blocking the immediate local step.
- Classify the agent role by work type:
  - `explorer` for specific codebase questions or bounded read-only investigation.
  - `worker` for concrete implementation with a clear ownership area and expected changed files.
  - `default` for general delegated work that is neither specialized exploration nor a bounded code patch.
- Prefer inherited/default model selection for spawned agents unless there is a clear task-specific reason to override.
- Recommend a smaller model override only for low-risk, well-scoped subtasks that are easy to validate.
- Recommend a larger model override when the delegated task is ambiguous, long-context, high-judgment, or likely to fail on a smaller model.
- For worker agents, include ownership boundaries and remind the caller that parallel agents may edit the codebase, so the worker must not revert unrelated changes.

## Output

- For ordinary model sizing, use exactly:
  - `model: <name or inherit/default>`
  - `tier: compact|standard|advanced`
  - `availability: direct|external|unconfirmed|unknown`
  - `inventory_source: runtime|prompt|file|runtime+prompt|runtime+file|prompt+file|runtime+prompt+file|none`
  - `rationale: <one sentence>`
- For subagent decisions, use exactly:
  - `spawn: yes|no`
  - `role: explorer|worker|default`
  - `model: inherit/default|<name>`
  - `tier: compact|standard|advanced`
  - `availability: direct|external|unconfirmed|unknown`
  - `inventory_source: <sources>`
  - `rationale: <one sentence>`
- Add optional fields only when useful, and never emit empty optional fields:
  - `provider: <name>` when `availability: external` or the access path is known.
  - `prompt: <delegation prompt>` only when `spawn: yes` and it prevents ambiguity.
  - `fallback_order: <models>` only when the user asks for comparison or fallback.
  - `notes: <brief caveat>` only for access gaps, missing inventory, or unsupported model override.
- Return one recommended model when inventory is available.
- If inventory is unavailable, return the required capability tier and whether to use inherited/default selection.
- Keep the answer compact; this skill exists to reduce token usage while still making a reliable recommendation.

## Decision Rule

- Choose the smallest model that can handle the task without obvious quality risk.
- Prefer reliability over compression when the task includes:
  - multiple moving parts,
  - ambiguous requirements,
  - long or brittle context,
  - external tool coordination,
  - or a need for careful judgment.
- Prefer compact models when the task is:
  - short,
  - localized,
  - strongly constrained,
  - or easy to validate automatically.
- If the evidence is mixed, choose the next larger model.

## Notes

- Avoid generic “best model” answers unless the user explicitly asks for an open-ended recommendation.
- If the model inventory is missing, say so and ask for it when an exact model name is needed.
- If the task is outside the available model set, recommend the smallest model that is at least close enough, and call out the gap.
