<spec name="[PROJECT] Technical Specification" status="initial" extends="concept.spec">

  <architecture_overview>
    <!-- Numbered list of strict import rules per architectural layer.
         Use screaming architecture: layer names and directory names use business
         language. Each rule states what a layer owns and what it must not import.

         1. Domain layer (src/domain/) must not import [infrastructure, adapters,
            external SDKs]. It may only import types and pure logic.
         2. [Storage/Infrastructure] layer (src/[layer]/) may import [fs, yaml].
            It must not import [adapters, LLM SDKs].
         3. Tools layer (src/tools/) imports domain types and service interfaces.
            It must not contain domain logic.
         4. App layer (src/app/) is the composition root. It may import any layer. -->
  </architecture_overview>

  <source_layout>
    <!-- One <file> per source file. Each names the path and its single
         responsibility. -->

    <file path="src/domain/types.ts"><!-- Domain type definitions. --></file>
    <file path="src/domain/ports.ts"><!-- Port interfaces for all external dependencies. --></file>
    <file path="src/app/compose.ts"><!-- Composition root. Wires all layers together. --></file>
  </source_layout>

  <runtime>
    <engine><!-- Runtime (e.g., Bun, Node). --></engine>
    <language><!-- Language and strict mode settings. --></language>
    <effect>
      <!-- Whether Effect-style error propagation and cancellation is used,
           and at what layer boundaries. -->
    </effect>
    <cancellation>
      <!-- AbortSignal or cancellation policy for slow operations. -->
    </cancellation>
    <dependencies>
      <!-- Key runtime dependencies. Dev dependencies listed separately. -->
    </dependencies>
  </runtime>

  <storage_conventions>
    <root>
      <!-- Default root path. Override mechanism (env var or config). -->
    </root>
    <files>
      <!-- One <file> per owned data file or store. -->
      <file name="filename.yaml"><!-- Schema version and contents. --></file>
    </files>
    <write_policy>
      <!-- Atomic write strategy (e.g., temp file + rename). Conflict detection. -->
    </write_policy>
    <diagnostics>
      <!-- What parse and schema errors must include (file path, line number,
           field path, constraint description). -->
    </diagnostics>
  </storage_conventions>

  <domain_types>
    <!-- One <interface> per core domain type. List typed fields. -->

    <interface name="TypeName">
      id: string
      <!-- field: type -->
    </interface>
  </domain_types>

  <ports>
    <!-- One <port> per external-facing interface (storage, execution,
         judge/LLM, clock, logger). List method signatures. -->

    <port name="PortName">
      <!-- methodName(param: Type): ReturnType -->
    </port>
  </ports>

  <tool_registry>
    <!-- Authoritative list of tool IDs, groups, and actions.
         Per-feature specs reference these IDs; they do not define new ones.

         plugin-name.tool-id
           Group: group-name
           Action: description

         Composition root in src/app/compose.ts:

           const group = defineGroup({ id: "group", ... }, (g) => g.tool(tool))
           export const appPlugin = plugin("app-name").group(group) -->
  </tool_registry>

  <json_schema_conventions>
    <!-- Numbered list of JSON Schema rules for tool input/output. -->
    1. Every public tool input schema is object-rooted with additionalProperties: false.
    2. All schemas are declared via jsonSchema&lt;T&gt;() from the tool framework.
    3. Outputs are structured objects, not raw strings, when agents may consume them.
    4.
  </json_schema_conventions>

  <error_taxonomy>
    <!-- One <error> per error code. code is ERR-PROJ-NN. -->

    <error code="ERR-PROJ-01" domain="[layer]">
      <!-- Description. What context must the error include. -->
    </error>
  </error_taxonomy>

  <configuration>
    <!-- One <env_var> per environment variable or config option. -->

    <env_var name="VAR_NAME" default="" required="false">
      <!-- Purpose and effect. -->
    </env_var>
  </configuration>

  <cross_references>
    <!-- Updated by Plot each time a feature slice is approved. -->

    <!-- <ref feature="feature-slug" path="features/feature-slug/technical.spec"/> -->
  </cross_references>

</spec>
