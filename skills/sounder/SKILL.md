---
name: sounder
description: Estimate the smallest reliable LLM for a task, prompt, spec, or subagent. Use when a user wants to size a task for model capability, compare available models, assign work to an agent, decide whether to spawn a subagent, choose a worker/explorer/default agent for delegated work, or choose the least capable model that can still complete the work with acceptable quality.
---

# Sounder

Estimate task difficulty against the available model set, then choose the smallest model or subagent assignment that is still likely to succeed.

## Inputs

- Accept either pasted text, a task prompt, a spec, or a file path.
- Treat user-supplied candidate models and client-available models as the same pool when both exist.
- If only one source exists, use that source as the model inventory.
- When evaluating a subagent, treat the delegated subtask as the unit being estimated, not the whole parent task.
- Do not force a file format. Read whatever the user gives and extract the task requirements from it.

## Workflow

1. Identify the task shape.
   - Determine whether the work is generation, extraction, transformation, reasoning, planning, coding, or multi-step agentic work.
   - Note output length, required precision, tool use, delegation boundaries, and whether the task has hidden dependencies.

2. Estimate difficulty.
   - Prefer larger models for ambiguous goals, multi-constraint work, long-context synthesis, or tasks that require planning across steps.
   - Prefer smaller models for bounded extraction, simple rewrites, classification, templated output, or short deterministic edits.
   - Treat hallucination risk, requirement density, and quality sensitivity as first-class signals.

3. Rank the available models.
   - Use only models that are actually available to the client or explicitly supplied by the user.
   - Prefer the smallest model that clears the reliability bar for the task.
   - Break ties by lower token cost, shorter latency, and narrower capability than the next larger option.
   - If two models look close, choose the safer one unless the task is clearly low risk.

4. Escalate when needed.
   - Move up a tier when the task is underspecified, the output will be user-facing and high stakes, or the model would need to simulate too much hidden state.
   - Do not over-optimize into a smaller model if that likely causes retries, rework, or degraded quality.

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

- Return one recommended model as the primary answer.
- Include a short rationale that names the key decision factors.
- For subagent decisions, return `spawn: yes/no`, the recommended role, the recommended model only if an override is justified, and a one-sentence rationale.
- Include a compact delegation prompt when it would prevent ambiguity.
- Optionally include a brief fallback order if the user asked for comparison.
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
- If the model inventory is missing, say so and infer from the client context only when that context is available.
- If the task is outside the available model set, recommend the smallest model that is at least close enough, and call out the gap.
