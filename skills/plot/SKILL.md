---
name: plot
description: Write layered project specs (concept → umbrella → feature triplets) for any codebase. Interview-driven, strict stage gates, XML .spec files in docs/ tree. Use when starting a new project, adding a feature slice, or extending existing specs.
license: Complete terms in LICENSE.txt
---

Spec-writing workflow for any project. Produces XML `.spec` files in a `docs/`
tree by interviewing you one question at a time and refusing to advance until
each layer is approved.

## When To Use Plot

- Starting a new project and need to define scope, architecture, and test
  strategy before writing code.
- Adding a feature slice to a project that already has umbrella specs.
- Reviewing or extending existing specs for cross-link correctness.

Do not use Plot to document finished code after the fact without running the
full interview loop.

## The Layered Workflow

Plot always inspects `docs/` first to determine which stage applies.

### Stage 1 — Concept

**Trigger**: no `docs/concept.spec` exists.

Read `references/interview-questions.md` § Concept. Draft `docs/concept.spec`
using `references/concept.template.spec`. Show the file path and wait for
explicit approval.

**Gate**: user must approve `docs/concept.spec` before Stage 2 begins.

### Stage 2 — Umbrellas

**Trigger**: `docs/concept.spec` exists but at least one of `docs/functional.spec`,
`docs/technical.spec`, or `docs/test.spec` is missing.

Write the missing specs in order: functional first, then technical, then test.
Each spec cross-references the ones before it. Each spec requires individual
approval before the next is drafted.

Templates: `references/functional.umbrella.template.spec`,
`references/technical.umbrella.template.spec`,
`references/test.umbrella.template.spec`.

**Gate**: all three umbrella specs approved before Stage 3 begins.

### Stage 3 — Feature Slice

**Trigger**: all three umbrella specs exist.

Ask which feature area from `concept.spec`'s `<feature_areas_for_atomic_specs>`
(or a new one) to slice next. Write `docs/features/<slug>/functional.spec`,
then `technical.spec`, then `test.spec` — each requiring approval before the
next is drafted.

Templates: `references/feature.functional.template.spec`,
`references/feature.technical.template.spec`,
`references/feature.test.template.spec`.

After each approved feature triplet, update the `<cross_references>` block in
the relevant umbrella specs and the `<acceptance_matrix>` in the umbrella
`test.spec`.

**Gate**: full triplet approved before starting the next slice.

### Gate Overrides

A user may skip a gate explicitly (e.g., "skip ahead, I already have the
concept"). Note the override in conversation. Do not record it in any spec file.

## Interview Loop

Each spec type runs the same loop:

1. **Read parent specs.** Umbrella specs → read `concept.spec`. Feature specs
   → read the relevant umbrella specs. Skip questions whose answers are already
   derivable from a parent spec.
2. **Ask interview questions** from `references/interview-questions.md` for
   that spec type — one at a time unless several are obviously batchable.
3. **Draft the spec** into the target path using the matching template.
4. **Show the file path** and ask for review. Do not progress until the user
   explicitly approves.

## Layout & Naming

```
docs/
  concept.spec
  functional.spec           ← extends="concept.spec"
  technical.spec            ← extends="concept.spec"
  test.spec                 ← extends="concept.spec"
  features/
    <slug>/
      functional.spec       ← extends="../../functional.spec"
      technical.spec        ← extends="../../technical.spec"
      test.spec             ← extends="../../test.spec"
```

- Extension: `.spec` (not `.xml`).
- All spec files are well-formed XML.
- Root element is `<spec>` with `name`, `status`, and `extends` attributes
  (except concept, which has no `extends`).
- Feature slugs are kebab-case, matching the element name from
  `<feature_areas_for_atomic_specs>`.

## Defaults

When the interview reaches `<principles>`, `<architecture>`, or
`<testing_strategy>`, propose these defaults and let the user accept or
override:

- Functional programming over imperative mutation.
- Screaming architecture (directory and file names use business language, not
  generic technical labels).
- Vertical slicing (each feature area is a coherent, independently deliverable
  slice).
- Test-driven development (acceptance criteria and tests drive implementation).
- Interface-first design (public contracts are defined before implementation).
- Tests and interfaces as navigation surface (an agent should understand the
  system from tests and port interfaces alone, without reading implementation).

These are proposals. The user's overrides take precedence and are written into
the spec.

## Cross-Linking In One Glance

| Link type | Attribute | Example |
|---|---|---|
| Spec inheritance | `extends="..."` | `extends="../../functional.spec"` |
| Feature AC rolls up to umbrella | `rolls_up_to="AC-FUN-NN"` | on feature `<ac>` |
| Test case covers use case + AC | `covers="UC-FEAT-NN AC-FEAT-NN"` | on `<test_case>` |
| Umbrella references feature spec | `<ref feature="..." path="..."/>` | in `<cross_references>` |
| Umbrella AC maps to tests | `<row ac="AC-FUN-NN" tests="TC-FEAT-NN,..."/>` | in `<acceptance_matrix>` |

Full ID conventions and tag vocabulary: `references/style-guide.md`.

## Non-Goals

- Plot does not write implementation code.
- Plot does not run tests or validate runtime behavior.
- Plot does not enforce a specific language, framework, or runtime.
- Plot does not produce specs without following the interview loop (unless the
  user explicitly overrides a gate).
