<spec name="[Feature Name] Functional Specification" feature="[feature-slug]" extends="../../functional.spec">

  <summary>
    <!-- One-paragraph description of this feature slice. What does it do, who
         uses it, and what value does it deliver? -->
  </summary>

  <use_cases>
    <!-- One <use_case> per use case. id is UC-<FEAT>-NN (zero-padded).
         actor references an id from the umbrella functional spec's <actors>.
         surface is "both", "mcp", "cli", "api", etc. -->

    <use_case id="UC-FEAT-01" actor="actor-id" surface="both">
      <goal><!-- What the actor is trying to accomplish. --></goal>
      <preconditions><!-- What must be true before this use case runs. --></preconditions>
      <inputs>
        <!-- Input shape. JSON example or TypeScript type sketch. -->
      </inputs>
      <steps>
        1.
        2.
        3.
      </steps>
      <outputs>
        <!-- Output shape. JSON example or TypeScript type sketch. -->
      </outputs>
      <postconditions><!-- What is true after successful completion. --></postconditions>
    </use_case>
  </use_cases>

  <error_scenarios>
    <!-- One <scenario> per observable error condition specific to this slice.
         id is ES-<FEAT>-NN. ref references the ERR-PROJ-NN from the umbrella
         error taxonomy. -->

    <scenario id="ES-FEAT-01" ref="ERR-PROJ-NN">
      <trigger><!-- What state or input triggers this error. --></trigger>
      <observable>
        <!-- What the structured error response must include:
             error code, message content, context fields. -->
      </observable>
    </scenario>
  </error_scenarios>

  <acceptance_criteria>
    <!-- One <ac> per acceptance criterion.
         id is AC-<FEAT>-NN.
         rolls_up_to references an AC-FUN-NN from the umbrella functional spec. -->

    <ac id="AC-FEAT-01" rolls_up_to="AC-FUN-NN">
      <!-- Present tense. Machine-verifiable statement. -->
    </ac>
  </acceptance_criteria>

  <out_of_scope>
    <!-- Free-form prose. List what this slice explicitly excludes. -->
  </out_of_scope>

</spec>
