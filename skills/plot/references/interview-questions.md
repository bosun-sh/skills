# Interview Questions

Question bank for the Plot interview loop. Sections are organized by spec type.
Each question names the XML tag or section it populates.

Plot asks these one at a time (or batches obviously related sub-questions).
Before each question, Plot reads the parent spec(s) and skips questions whose
answers are already derivable from what's there.

---

## Concept

Feeds `docs/concept.spec`. No parent spec to read.

### `<context>`
1. What problem is this project solving? Who feels the pain, and how does it
   manifest?
2. What is the proposed solution in one or two sentences?

### `<goals>`
3. What are the 3–5 outcomes that would make this project a clear success?

### `<non_goals>`
4. What is explicitly out of scope for this version?

### `<principles>`
5. What design principles should every implementation decision defer to?

   *(Plot will propose: functional programming, screaming architecture, vertical
   slicing, TDD, interface-first design, tests-and-interfaces as navigation
   surface. Confirm or override.)*

### `<technical_decisions>`
6. What key infrastructure or technology choices have already been made
   (storage mechanism, runtime, framework, language)?
7. For each decision area, what is the rationale?

### `<core_entities>`
8. What are the primary domain concepts or entities? For each, what semantics
   are required?

### `<architecture>`
9. What are the architectural layers? What are the strict import rules between
   them?

   *(Plot will propose screaming architecture defaults — layers named after
   business concepts — unless you override.)*

### `<feature_areas_for_atomic_specs>`
10. What discrete feature areas should each get their own
    functional/technical/test spec triplet? Name each with a kebab-case slug.

### `<public_contract_expectations>`
11. What invariants must always hold on the system's public API or tool
    contracts?

### `<acceptance_criteria>`
12. What are the top-level acceptance criteria for the whole project?

### `<testing_strategy>`
13. What test levels are required (unit, integration, e2e, contract)? What
    does each cover?

    *(Plot will propose TDD defaults. Confirm or override.)*

---

## Umbrella Functional

Feeds `docs/functional.spec`. Plot reads `concept.spec` first and skips
questions already answered there.

### `<purpose>`
1. Summarize in one paragraph what the system does from a functional
   perspective.

### `<actors>`
2. Who or what interacts with this system? For each actor, list the workflows
   they trigger.

### `<surfaces>`
3. Through what surfaces does the system expose its behavior (CLI, MCP, HTTP
   API, UI, SDK)?

### `<workflows>`
4. For each major workflow: what triggers it, what are its preconditions, what
   are its steps, what does success look like, and what are the failure modes?

### `<inputs_outputs>`
5. For each workflow, what is the input shape and output shape? (Compact
   summary form.)

### `<error_scenarios>`
6. What observable error conditions must the system produce? What must each
   error message or response include?

### `<acceptance_criteria>`
7. Translate each concept-level acceptance criterion into a functional,
   testable statement. Each AC must reference its concept-level AC number in
   the `concept_ac` attribute.

### `<glossary>`
8. Are there domain terms that need precise definitions?

---

## Umbrella Technical

Feeds `docs/technical.spec`. Plot reads `concept.spec` and `functional.spec`
first.

### `<architecture_overview>`
1. Confirm or refine the layer rules from the concept spec. What are the
   strict import boundaries between layers?

### `<source_layout>`
2. What source files will exist at the start of the project? What is each
   file's single responsibility?

### `<runtime>`
3. What runtime, language, and key dependencies are used? Are Effect-style
   error propagation or cancellation patterns required?

### `<storage_conventions>`
4. What files or data stores does the system own? What naming, path
   resolution, and write-policy rules apply?

### `<domain_types>`
5. List the core domain interfaces and their fields.

### `<ports>`
6. What are the port interfaces (external services, storage, execution
   boundaries)? What are their method signatures?

### `<tool_registry>`
7. If the system exposes agent-callable tools (MCP, CLI): what are the
   authoritative tool IDs, groups, and composition structure?

### `<error_taxonomy>`
8. What error codes exist? What domain and layer does each belong to?

### `<configuration>`
9. What environment variables or config options exist? What are their defaults?

---

## Umbrella Test

Feeds `docs/test.spec`. Plot reads `concept.spec`, `functional.spec`, and
`technical.spec` first.

### `<test_pyramid>`
1. What test levels are needed? For each level, what is in scope, what is
   excluded, and what is the speed expectation?

### `<runners_and_layout>`
2. What test runner is used? Where do unit, integration, and e2e tests live?
   What are the coverage targets per level?

### `<fixtures>`
3. What fixture directories are needed? What files does each contain and why?

### `<naming_conventions>`
4. Confirm the test ID format (`TC-<FEAT>-NN`), feature codes, describe-block
   pattern, and it-block pattern.

### `<test_doubles>`
5. What fake or stub implementations of ports are needed? Where do they live
   and how do they work?

### `<commands>`
6. What commands run each test level? What command verifies the tool registry
   or public API shape?

*Note: `<acceptance_matrix>` is filled in incrementally as feature specs are
approved. Plot adds rows to it after each approved feature triplet.*

---

## Feature Functional

Feeds `docs/features/<slug>/functional.spec`. Plot reads the umbrella
`functional.spec` first.

### `<summary>`
1. Describe this feature slice in one paragraph. What does it do, who uses it,
   and what value does it deliver?

### `<use_cases>`
2. List the use cases for this slice. For each: actor, surface, goal,
   preconditions, steps, outputs, postconditions.

### `<error_scenarios>`
3. What error conditions specific to this slice produce observable structured
   output? For each: what triggers it, and what must the observable output
   contain?

### `<acceptance_criteria>`
4. Write the ACs for this slice. Each must declare `rolls_up_to` pointing at
   an umbrella `AC-FUN-NN`.

### `<out_of_scope>`
5. What related behaviors are explicitly excluded from this slice?

---

## Feature Technical

Feeds `docs/features/<slug>/technical.spec`. Plot reads the umbrella
`technical.spec` and this feature's `functional.spec` first.

### `<slice_layout>`
1. What source files does this slice own? What is each file's single
   responsibility?

### `<domain_types>`
2. Does this slice introduce or extend any domain types?

### `<ports_used>`
3. Which port methods does this slice invoke?

### `<touchpoints>`
4. What files or external resources does this slice read and write? Which
   schemas or contracts apply?

### `<tools>`
5. What tool definitions does this slice contribute? For each: ID, group,
   description, input schema, output schema, error references, handler
   contract.

### `<plugin_composition>`
6. How are this slice's tools wired into the composition root?

### `<effects>`
7. List every external effect this slice causes (file system, network, process
   execution, LLM call).

### `<observability>`
8. What logger calls are required for success, warning, and error paths?

---

## Feature Test

Feeds `docs/features/<slug>/test.spec`. Plot reads the umbrella `test.spec`,
this feature's `functional.spec`, and this feature's `technical.spec` first.

### `<fixtures_used>`
1. Which fixture directories does this slice's tests rely on? Does this slice
   need new fixtures?

### `<test_cases>`
2. For each use case and each AC in the feature functional spec, write a test
   case. Each must declare `covers` pointing at one or more use case and AC
   IDs.

### `<coverage_matrix>`
3. Map each use case in this slice to the test cases that cover it.
