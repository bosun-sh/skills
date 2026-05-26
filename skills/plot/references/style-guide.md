# Plot Style Guide

Source of truth for XML tag vocabulary, ID conventions, cross-link rules, and
writing tone. All `.spec` files must conform to this guide.

Canonical working example of a complete spec tree:
`/Users/jiramirez/code/personal/bosun.sh/modules/chest/chore-initial-specs/docs/`

---

## XML Tag Vocabulary

### concept.spec

| Tag | Purpose |
|---|---|
| `<context>` | Children: `<problem>` (pain narrative) and `<solution>` (one-paragraph fix). |
| `<goals>` | Numbered list of project success outcomes. |
| `<non_goals>` | Numbered list of explicit exclusions for this version. |
| `<principles>` | Numbered list of design principles. Machine-verifiable phrasing preferred. |
| `<technical_decisions>` | Named child elements per decision area (e.g., `<storage>`, `<interfaces>`). Each includes a Rationale subsection. |
| `<core_entities>` | Named child elements per domain concept. Each describes required semantics as a numbered list. |
| `<architecture>` | Children: `<overview>` (prose) and `<layers>` (named child elements per layer). |
| `<feature_areas_for_atomic_specs>` | Named child elements per feature area. Each describes what the slice defines. |
| `<public_contract_expectations>` | Numbered list of invariants that must hold on all public APIs or tools. |
| `<acceptance_criteria>` | Numbered list of project-level acceptance criteria (plain text items, not `<ac>` elements). |
| `<testing_strategy>` | Numbered list of test level descriptions. |

### functional.spec (umbrella)

| Tag | Purpose |
|---|---|
| `<purpose>` | One-paragraph summary of what the system does functionally. |
| `<actors>` | `<actor id="...">` elements — each names the actor and lists what workflows they trigger. |
| `<surfaces>` | `<surface id="...">` elements — each describes an access surface (MCP, CLI, HTTP API, UI). |
| `<workflows>` | `<workflow id="...">` elements — each has `<trigger>`, `<preconditions>`, `<steps>`, `<postconditions>`, `<failure_modes>`. |
| `<inputs_outputs>` | `<row workflow="..." input="..." output="..."/>` elements — compact input/output summary per workflow. |
| `<error_scenarios>` | `<scenario id="...">` elements — each describes an observable error condition and what the message must include. |
| `<acceptance_criteria>` | `<ac id="AC-FUN-NN" concept_ac="N">` elements — each maps to a concept-level AC number. |
| `<glossary>` | `<term name="...">` elements with precise domain definitions. |
| `<cross_references>` | `<ref feature="..." path="..."/>` elements — links to feature specs. Updated per approved slice. |

### technical.spec (umbrella)

| Tag | Purpose |
|---|---|
| `<architecture_overview>` | Layer rules as a numbered list of import constraints per layer. |
| `<source_layout>` | `<file path="...">` elements — each names a source file and its single responsibility. |
| `<runtime>` | Children: `<engine>`, `<language>`, `<effect>`, `<cancellation>`, `<dependencies>`. |
| `<storage_conventions>` | Children: `<root>`, `<files>` (with `<file>` children), `<write_policy>`, `<diagnostics>`. |
| `<domain_types>` | `<interface name="...">` elements listing typed fields. |
| `<ports>` | `<port name="...">` elements with method signatures (port interface definitions). |
| `<tool_registry>` | Authoritative list of tool IDs, groups, actions, and the composition expression. Feature specs reference these IDs; they do not create new ones. |
| `<json_schema_conventions>` | Numbered list of JSON Schema rules for tool input/output. |
| `<error_taxonomy>` | `<error code="ERR-PROJ-NN" domain="...">` elements with descriptions. |
| `<configuration>` | `<env_var name="..." default="..." required="...">` elements. |
| `<cross_references>` | `<ref feature="..." path="..."/>` elements. Updated per approved slice. |

### test.spec (umbrella)

| Tag | Purpose |
|---|---|
| `<test_pyramid>` | `<level name="...">` elements — each describes a test level, its scope, and exclusions. |
| `<runners_and_layout>` | Children: `<runner>`, `<unit_tests>`, `<integration_tests>`, `<e2e_tests>`, `<coverage_targets>`. |
| `<fixtures>` | `<fixture path="...">` elements — each describes fixture directory contents. |
| `<naming_conventions>` | Children: `<test_ids>`, `<feat_codes>`, `<describe_blocks>`, `<it_blocks>`. |
| `<test_doubles>` | Describes fake/stub port implementations. Children: `<name>`, `<location>`, `<behavior>`, `<scripted_responses>`. |
| `<acceptance_matrix>` | `<row ac="AC-FUN-NN" tests="TC-FEAT-NN,..."/>` elements — maps each umbrella AC to its covering tests. Updated per approved slice. |
| `<commands>` | `<command purpose="...">` elements with test runner invocations. |
| `<cross_references>` | `<ref feature="..." path="..."/>` elements. Updated per approved slice. |

### feature functional.spec

| Tag | Purpose |
|---|---|
| `<summary>` | One-paragraph description of the feature slice. |
| `<use_cases>` | `<use_case id="UC-FEAT-NN" actor="..." surface="...">` elements — each has `<goal>`, `<preconditions>`, `<inputs>`, `<steps>`, `<outputs>`, `<postconditions>`. |
| `<error_scenarios>` | `<scenario id="ES-FEAT-NN" ref="ERR-PROJ-NN">` elements — each has `<trigger>` and `<observable>`. |
| `<acceptance_criteria>` | `<ac id="AC-FEAT-NN" rolls_up_to="AC-FUN-NN">` elements. |
| `<out_of_scope>` | Free-form prose listing what this slice explicitly excludes. |

### feature technical.spec

| Tag | Purpose |
|---|---|
| `<slice_layout>` | `<file path="...">` elements for source files owned by this slice. |
| `<domain_types>` | New or extended types introduced by this slice. |
| `<ports_used>` | Prose listing which port methods this slice invokes. |
| `<touchpoints>` | Files or resources read and written; schemas used. (Also seen as `<yaml_touchpoints>` in storage-heavy slices.) |
| `<tools>` | `<tool id="..." api="..." group="...">` elements — each has `<description>`, `<input_schema>`, `<output_schema>`, `<errors>`, `<handler_contract>`. |
| `<plugin_composition>` | How this slice's tools are wired into the composition root. |
| `<effects>` | Prose listing every external effect (fs, network, process execution). |
| `<observability>` | Logger calls for success, warning, and error paths. |

### feature test.spec

| Tag | Purpose |
|---|---|
| `<fixtures_used>` | Which fixture directories this slice's tests rely on. |
| `<test_cases>` | `<test_case id="TC-FEAT-NN" level="..." covers="UC-FEAT-NN AC-FEAT-NN">` elements — each has `<given>`, `<input>`, `<when>`, `<expected_output>`, `<expected_errors>`. |
| `<coverage_matrix>` | `<row uc="UC-FEAT-NN" tests="TC-FEAT-NN,..."/>` elements — maps each use case to its covering tests. |

---

## ID Conventions

| ID type | Pattern | Scope | Example |
|---|---|---|---|
| Umbrella functional AC | `AC-FUN-NN` | functional umbrella | `AC-FUN-01` |
| Feature AC | `AC-<FEAT>-NN` | feature slice | `AC-INIT-01` |
| Use case | `UC-<FEAT>-NN` | feature slice | `UC-INIT-01` |
| Test case | `TC-<FEAT>-NN` | feature slice | `TC-INIT-01` |
| Error scenario | `ES-<FEAT>-NN` | feature slice | `ES-INIT-01` |
| Error code | `ERR-<PROJ>-NN` | project-wide | `ERR-CHEST-01` |
| Actor | kebab-case text | functional umbrella | `planning-agent` |
| Surface | kebab-case text | functional umbrella | `mcp`, `cli`, `api` |
| Workflow | kebab-case text | functional umbrella | `initialize` |

- `NN` is a zero-padded two-digit sequence number within its scope (01, 02, …).
- `<FEAT>` is a short uppercase code (2–5 chars) defined in the umbrella
  `test.spec`'s `<naming_conventions><feat_codes>`.
- `<PROJ>` is a short uppercase project code (e.g., `CHEST`, `MYAPP`).
- Sequence numbers are local to their scope. Two different feature slices can
  both have `AC-FEAT-01` if their `<FEAT>` codes differ.

---

## The `extends` Chain

```
docs/concept.spec                            ← no extends
docs/functional.spec   extends="concept.spec"
docs/technical.spec    extends="concept.spec"
docs/test.spec         extends="concept.spec"
docs/features/<slug>/functional.spec   extends="../../functional.spec"
docs/features/<slug>/technical.spec    extends="../../technical.spec"
docs/features/<slug>/test.spec         extends="../../test.spec"
```

The `extends` attribute is on the root `<spec>` element. It is a relative path
from the spec file's own location to its parent spec. A spec must not be
written before its parent exists — Plot's stage gates enforce this.

---

## `rolls_up_to` and `covers`

- **`rolls_up_to="AC-FUN-NN"`** on a feature `<ac>` element: satisfying this
  feature AC also satisfies the named umbrella AC.
- **`covers="UC-FEAT-NN AC-FEAT-NN"`** on a `<test_case>` element: this test
  case covers the named use case(s) and acceptance criterion(/ia).

Both attributes accept space-separated ID lists when multiple apply.

A test case should cover at least one use case AND at least one AC. If it
covers only an error scenario, reference the `ES-FEAT-NN` ID in the
`covers` attribute instead.

---

## `<cross_references>` and `<acceptance_matrix>`

Umbrella specs include a `<cross_references>` block at the end:

```xml
<cross_references>
  <ref feature="<slug>" path="features/<slug>/functional.spec"/>
  ...
</cross_references>
```

The umbrella `test.spec`'s `<acceptance_matrix>` maps each umbrella AC to the
test cases that satisfy it:

```xml
<acceptance_matrix>
  <row ac="AC-FUN-01" tests="TC-FEAT-01,TC-FEAT-02"/>
  ...
</acceptance_matrix>
```

Both blocks are updated each time a new feature slice is approved and added to
the tree.

---

## Writing Tone

1. Use numbered lists in `<goals>`, `<non_goals>`, `<principles>`,
   `<acceptance_criteria>` (concept), and `<steps>` sections.
2. Use present tense throughout. "The system validates input" — not "will
   validate."
3. Phrase acceptance criteria so they are machine-verifiable where possible.
   Avoid "the system handles errors gracefully." Prefer "the system returns
   `ERR-PROJ-NN` with file path and line number when YAML cannot be parsed."
4. Use domain language. "governance store" not "the database"; "planning agent"
   not "the user."
5. Keep `<summary>` and `<purpose>` to one paragraph. Put detail in child
   sections.
6. Use "must" for requirements, "may" for permissions, "does not" for
   non-goals. Avoid "will," "would," and "shall" in normative sections.
7. `<steps>` are numbered and imperative: "1. Resolve the target path."
8. `<failure_modes>` are declarative: "File absent. File not parseable as YAML."
