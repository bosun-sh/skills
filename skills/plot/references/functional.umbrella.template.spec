<spec name="[PROJECT] Functional Specification" status="initial" extends="concept.spec">

  <purpose>
    <!-- One-paragraph summary of what the system does from a functional
         perspective. What it stores, what workflows it enables, through what
         surfaces, and for whom. -->
  </purpose>

  <actors>
    <!-- One <actor> element per system actor. Attribute id is kebab-case.
         Body lists what workflows the actor triggers. -->

    <actor id="actor-name">
      <!-- Description. Triggers: workflow-a, workflow-b. -->
    </actor>
  </actors>

  <surfaces>
    <!-- One <surface> element per access surface (mcp, cli, api, ui, sdk).
         Attribute id is kebab-case. Body describes the surface contract. -->

    <surface id="surface-name">
      <!-- How this surface exposes the system's behavior.
           All tools/endpoints available on one surface must also be on all
           other surfaces unless explicitly documented otherwise. -->
    </surface>
  </surfaces>

  <workflows>
    <!-- One <workflow> element per major workflow.
         Attribute id is kebab-case. -->

    <workflow id="workflow-name">
      <trigger><!-- What actor action or system event starts this workflow. --></trigger>
      <preconditions><!-- What must be true before this workflow runs. --></preconditions>
      <steps>
        1.
        2.
        3.
      </steps>
      <postconditions><!-- What is true after successful completion. --></postconditions>
      <failure_modes>
        <!-- Comma-separated or one-per-line list of failure conditions. -->
      </failure_modes>
    </workflow>
  </workflows>

  <inputs_outputs>
    <!-- One <row> per workflow. Attribute values are compact type sketches. -->

    <row workflow="workflow-name"
         input="InputType { field: type }"
         output="OutputType { field: type }"/>
  </inputs_outputs>

  <error_scenarios>
    <!-- One <scenario> per observable error condition.
         id is ES-PROJ-NN but lives at umbrella scope (or use a project prefix). -->

    <scenario id="error-slug">
      <!-- Describe: what state triggers this error, and what the structured
           response must include (error code, context, suggestions). -->
    </scenario>
  </error_scenarios>

  <acceptance_criteria>
    <!-- One <ac> per acceptance criterion. id is AC-FUN-NN (zero-padded).
         concept_ac references the numbered item in concept.spec's
         <acceptance_criteria> that this criterion satisfies. -->

    <ac id="AC-FUN-01" concept_ac="1">
      <!-- Present tense. Machine-verifiable. -->
    </ac>
  </acceptance_criteria>

  <glossary>
    <!-- One <term> per domain concept that needs a precise definition. -->

    <term name="term-name">
      <!-- Precise definition in one to three sentences. -->
    </term>
  </glossary>

  <cross_references>
    <!-- Updated by Plot each time a feature slice is approved.
         One <ref> per feature area. -->

    <!-- <ref feature="feature-slug" path="features/feature-slug/functional.spec"/> -->
  </cross_references>

</spec>
