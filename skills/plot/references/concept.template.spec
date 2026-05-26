<spec name="[PROJECT] Concept Specification" status="initial">

  <context>
    <problem>
      <!-- What problem does this project solve? Who feels the pain and how? -->
    </problem>

    <solution>
      <!-- One or two sentences describing the proposed solution. -->
    </solution>
  </context>

  <goals>
    <!-- Numbered list of 3–5 project success outcomes. -->
    1.
    2.
    3.
  </goals>

  <non_goals>
    <!-- Numbered list of explicit exclusions for this version. -->
    1.
    2.
  </non_goals>

  <principles>
    <!-- Numbered list of design principles. Machine-verifiable phrasing preferred.
         Plot will propose: functional programming, screaming architecture,
         vertical slicing, TDD, interface-first, tests-and-interfaces as
         navigation surface. Confirm or override. -->
    1.
    2.
    3.
  </principles>

  <technical_decisions>
    <!-- One named child element per decision area. Include a Rationale subsection. -->

    <storage>
      <!-- How and where data is persisted.

           Rationale:

           1.
           2. -->
    </storage>

    <interfaces>
      <!-- How the system exposes behavior to agents and humans.

           Rationale:

           1.
           2. -->
    </interfaces>
  </technical_decisions>

  <core_entities>
    <!-- One named child element per domain concept.
         Each element describes required semantics as a numbered list. -->

    <entity_name>
      Required semantics:

      1.
      2.
    </entity_name>
  </core_entities>

  <architecture>
    <overview>
      <!-- High-level architecture style. Screaming architecture means directory
           and file names use business language, not generic technical labels.
           Vertical slicing means each feature area is a coherent, independently
           deliverable slice. -->
    </overview>

    <layers>
      <!-- One named child element per architectural layer.
           State what the layer owns and what it must not import. -->

      <domain>
        <!-- The domain layer owns [core concepts] and [validation rules].

             It must not import [infrastructure, adapters, external SDKs]. -->
      </domain>

      <infrastructure>
        <!-- The infrastructure layer owns [storage, external service adapters].

             It must not import [ohtools, LLM SDKs, ...]. -->
      </infrastructure>

      <tools>
        <!-- The tools/adapters layer owns [MCP/CLI definitions, public contracts].

             It must not contain domain logic. -->
      </tools>

      <app>
        <!-- The app layer is the composition root.
             It wires all layers together and may import any of them. -->
      </app>
    </layers>
  </architecture>

  <feature_areas_for_atomic_specs>
    <!-- One named child element per feature area that will get its own
         functional/technical/test spec triplet.
         Element name must be the kebab-case slug used in docs/features/<slug>/. -->

    <feature_slug>
      <!-- Describe what this slice defines. -->
    </feature_slug>
  </feature_areas_for_atomic_specs>

  <public_contract_expectations>
    <!-- Numbered list of invariants that must hold on all public APIs or tools. -->
    1.
    2.
  </public_contract_expectations>

  <acceptance_criteria>
    <!-- Numbered list of project-level acceptance criteria.
         Present tense. Machine-verifiable phrasing preferred. -->
    1.
    2.
    3.
  </acceptance_criteria>

  <testing_strategy>
    <!-- Numbered list of test levels and what each covers.
         Plot will propose TDD defaults. Confirm or override. -->
    1. Domain tests cover [...] without external effects.
    2. Integration tests cover [...] against real [storage/process/network].
    3. End-to-end tests cover [...] via [CLI/MCP/API].
  </testing_strategy>

</spec>
