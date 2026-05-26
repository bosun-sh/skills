<spec name="[Feature Name] Test Specification" feature="[feature-slug]" extends="../../test.spec">

  <fixtures_used>
    <!-- Which fixture directories this slice's tests rely on.
         Reference paths defined in the umbrella test.spec's <fixtures>.
         Note any new fixtures needed for this slice. -->

    tests/fixtures/valid/ (as baseline for [scenario] tests).
    <!-- No new fixtures needed / New fixture needed at tests/fixtures/[name]/. -->
  </fixtures_used>

  <test_cases>
    <!-- One <test_case> per test case.
         id is TC-<FEAT>-NN (zero-padded).
         level is one of: unit, integration, contract, e2e.
         covers is a space-separated list of UC-<FEAT>-NN and AC-<FEAT>-NN IDs
         (or ES-<FEAT>-NN for error scenario tests). -->

    <test_case id="TC-FEAT-01" level="integration" covers="UC-FEAT-01 AC-FEAT-01">
      <given><!-- The initial state or setup. --></given>
      <input><!-- The input passed to the handler or command. JSON. --></input>
      <when><!-- The action taken (e.g., "handler is called with the above input"). --></when>
      <expected_output>
        <!-- The exact structured output. JSON. -->
      </expected_output>
      <expected_errors>None.</expected_errors>
    </test_case>

    <test_case id="TC-FEAT-02" level="integration" covers="ES-FEAT-01 AC-FEAT-NN">
      <given><!-- The error-triggering state. --></given>
      <input><!-- The input. --></input>
      <when><!-- The action. --></when>
      <expected_output>None (error is returned instead).</expected_output>
      <expected_errors>
        <!-- The exact structured error. JSON. -->
        {
          "code": "ERR-PROJ-NN",
          "message": "..."
        }
      </expected_errors>
    </test_case>
  </test_cases>

  <coverage_matrix>
    <!-- Maps each use case in this slice to the test cases that cover it. -->

    <row uc="UC-FEAT-01" tests="TC-FEAT-01"/>
  </coverage_matrix>

</spec>
