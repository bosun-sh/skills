<spec name="[Feature Name] Technical Specification" feature="[feature-slug]" extends="../../technical.spec">

  <slice_layout>
    <!-- One <file> per source file owned by this slice.
         Each names the path and its single responsibility. -->

    <file path="src/[layer]/[feature-slug].ts"><!-- Responsibility. --></file>
    <file path="src/tools/[feature-slug].ts"><!-- Tool definition for this slice. --></file>
  </slice_layout>

  <domain_types>
    <!-- New or extended domain types introduced by this slice.
         Use "No new domain types." if this slice reuses umbrella types only.
         Tool-layer value objects (InputType, ResultType) that have no domain
         semantics are not listed here. -->
  </domain_types>

  <ports_used>
    <!-- Prose listing which port methods from the umbrella technical spec this
         slice invokes. Example:
         GovernanceStore.readOKRs, writeOKRs (via [layer].ts internal path). -->
  </ports_used>

  <touchpoints>
    <!-- Files or external resources read and written by this slice.
         Schema version used for each. -->

    Creates or reads:
      <!-- path/to/file.yaml  (schema: schema-name.v1, content: description) -->
  </touchpoints>

  <tools>
    <!-- One <tool> per tool definition this slice contributes.
         id must match the authoritative ID in the umbrella tool_registry.
         api is the constructor used (e.g., defineTool, defineGroup). -->

    <tool id="app.tool-id" api="defineTool" group="app (group-name)">
      <description>
        <!-- Agent-readable, action-oriented description. State side effects
             explicitly. -->
      </description>
      <input_schema>
        {
          "type": "object",
          "properties": {
            "field": {
              "type": "string",
              "description": "..."
            }
          },
          "additionalProperties": false
        }
      </input_schema>
      <output_schema>
        {
          "type": "object",
          "properties": {
            "result": {
              "type": "string",
              "description": "..."
            }
          },
          "required": ["result"],
          "additionalProperties": false
        }
      </output_schema>
      <errors>
        <error ref="ERR-PROJ-NN"/>
      </errors>
      <handler_contract>
        <!-- Numbered steps describing what the handler does:
             1. Validate input (framework handles this).
             2. ...
             3. Return structured output. -->
        1. Validate input against input_schema (framework handles this).
        2.
        3.
      </handler_contract>
    </tool>
  </tools>

  <plugin_composition>
    <!-- How this slice's tools are wired into the composition root.
         Reference the umbrella tool_registry composition expression. -->
  </plugin_composition>

  <effects>
    <!-- Prose listing every external effect this slice causes.
         Be specific: fs/promises.mkdir, fs/promises.writeFile, Bun.spawn, fetch.
         State what is NOT used (no LLM, no network) to narrow scope. -->
  </effects>

  <observability>
    <!-- Logger calls for each path. Format: Logger.level("message", { context }). -->
    On success: Logger.info("...", { ... }).
    On [warning condition]: Logger.warn("...", { ... }).
    On [error condition]: Logger.error("...", { ... }).
  </observability>

</spec>
