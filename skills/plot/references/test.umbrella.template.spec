<spec name="[PROJECT] Test Specification" status="initial" extends="concept.spec">

  <test_pyramid>
    <!-- One <level> per test level.
         Each states what is in scope, what is excluded, and speed expectations. -->

    <level name="domain-unit">
      Tests pure domain logic in src/domain/. No file system, network, process,
      or adapter imports. Use in-memory objects. Fast; no setup required.
    </level>

    <level name="integration">
      Tests [storage/infrastructure layer] against real [tmp file system / real
      process / real network]. Each test creates an isolated environment.
      Covers [valid input, invalid input, error classes].
    </level>

    <level name="contract">
      Tests [tool registry / public API] shape and handler delegation. Verifies
      every registered tool has an id, description, and object-rooted input
      schema. Uses [real or stubbed] service dependencies.
    </level>

    <level name="end-to-end">
      Tests full workflows via [CLI / MCP stdio / HTTP]. Uses real
      [file system / dependencies] and fake [external services] (gated by env
      var for real calls). Covers the primary happy path and key failure paths.
    </level>
  </test_pyramid>

  <runners_and_layout>
    <runner><!-- Test runner command (e.g., bun test, jest, vitest). --></runner>
    <unit_tests>
      Co-located with source. File name pattern: *.test.ts next to the file
      under test.
    </unit_tests>
    <integration_tests>
      tests/integration/. One file per feature slice.
    </integration_tests>
    <e2e_tests>
      tests/e2e/. One file per cross-cutting scenario.
    </e2e_tests>
    <coverage_targets>
      <!-- Coverage expectations per test level. -->
      Domain unit: [coverage expectation].
      Integration: covers all [N] error classes per slice.
      Contract: all registered tool IDs pass registry snapshot.
    </coverage_targets>
  </runners_and_layout>

  <fixtures>
    <!-- One <fixture> per fixture directory. Describe its purpose and contents. -->

    <fixture path="tests/fixtures/valid/">
      <!-- Files representing valid, parseable, schema-correct input for happy
           path tests. -->
    </fixture>

    <fixture path="tests/fixtures/invalid-[error-type]/">
      <!-- Files representing a specific error class for negative tests. -->
    </fixture>
  </fixtures>

  <naming_conventions>
    <test_ids>
      Format: TC-&lt;FEAT&gt;-NN where FEAT is the feature code and NN is a
      zero-padded two-digit sequence number within the feature.
    </test_ids>
    <feat_codes>
      <!-- One line per feature area: FEAT_CODE: feature-slug -->
    </feat_codes>
    <describe_blocks>
      Top-level: describe("feature/&lt;kebab-feature-name&gt;")
      Nested groupings: describe("&lt;scenario-name&gt;") as needed.
    </describe_blocks>
    <it_blocks>
      it("&lt;TC-id&gt;: &lt;behavior description in plain English&gt;")
      Example: it("TC-INIT-01: creates store with required files in a fresh directory")
    </it_blocks>
  </naming_conventions>

  <test_doubles>
    <!-- Describes fake or stub implementations of port interfaces.
         One block per double. -->

    <name>Fake[PortName]</name>
    <location>tests/doubles/fake-[port-name].ts</location>
    <behavior>
      <!-- Implements [PortName] port. Stores scripted responses. Returns the
           scripted response for a matching request hash. If no script matches,
           returns a default [success/empty] response. -->
    </behavior>
    <scripted_responses>
      <!-- How callers set up scripted responses before a test:
           fake.script(hash, response) for normal responses.
           fake.script(hash, { throws: true }) for error simulation.
           fake.script(hash, { malformed: true }) for shape-validation testing. -->
    </scripted_responses>
  </test_doubles>

  <acceptance_matrix>
    <!-- Updated by Plot each time a feature slice is approved.
         Maps each umbrella AC to the test cases that satisfy it. -->

    <!-- <row ac="AC-FUN-01" tests="TC-FEAT-01,TC-FEAT-02"/> -->
  </acceptance_matrix>

  <commands>
    <command purpose="run all tests"><!-- e.g., bun test --></command>
    <command purpose="run unit tests only"><!-- e.g., bun test src/ --></command>
    <command purpose="run integration tests only"><!-- e.g., bun test tests/integration/ --></command>
    <command purpose="run e2e tests only"><!-- e.g., bun test tests/e2e/ --></command>
    <command purpose="registry snapshot"><!-- e.g., bunx ohtools --app src/ohtools.ts list --></command>
  </commands>

  <cross_references>
    <!-- Updated by Plot each time a feature slice is approved. -->

    <!-- <ref feature="feature-slug" path="features/feature-slug/test.spec"/> -->
  </cross_references>

</spec>
