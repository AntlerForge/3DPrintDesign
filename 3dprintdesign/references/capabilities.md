# Capabilities, setup and operation

Use for hands-on Fusion/slicer work, optional setup, or command diagnosis.
No particular host, model, integration, operating system or tool is required.

## Choose a real route

| Available capability | Useful work | Not established by it |
|---|---|---|
| Text only | Plans, manual teaching, review of user-provided measurements | Model inspection, clicks, saves or slicing |
| Current screenshots/files | Inspect visible state or supplied geometry within tool limits | Hidden geometry, live app access or physical fit |
| Native computer use | Observe and operate supported Fusion/slicer UI | Structured CAD access or file/shell access |
| Authorized structured Fusion API/MCP | Inspect/edit supported model operations | Desktop control, slicer control or printer readiness |
| File tools | Inspect accessible saved artifacts | Cloud synchronization or installed app availability |

Read the exposed tool documentation, identify the live app/document and perform
a bounded read before edits. Do not fabricate API methods, endpoints or app IDs.
Choose one operator for a shared app, including API and UI edits. If ownership
is uncertain, pause mutations, preserve pending work and resolve it with the user.

For first use, offer setup assistance briefly. If accepted, establish platform,
agent client, supported control mechanisms and the user's desired scope. Do not
ask for tool installation when the user only wants manual help.

## Setup only with approval

1. Inspect available client/tool configuration only within granted access.
   Consult current official client and integration documentation if available.
   A client without native desktop control may still support an API route;
   an API connection is not a substitute for unavailable UI control.
   For a client that supports MCP, one candidate to evaluate is Autodesk's
   [Fusion MCP sample](https://github.com/AutodeskFusion360/FusionMCPSample).
   It is a reference implementation, not a bundled or prequalified service.
   Check its current requirements, source and license before proposing setup;
   native computer control remains an independent option.
2. Describe the proposed components, download source, permissions, changed files,
   network binding/authentication and rollback. Obtain approval for that scope
   before installing/configuring. Do not change accounts, subscription, firewall,
   system-wide permissions or public network exposure as an incidental step.
3. Preserve recoverable existing settings and unrelated integrations. Use the
   supported installation mechanism. Never ask the user to paste credentials
   into the conversation or package; the user handles login and OS approval.
   Do not bypass a denied permission. Do not silently expose a local service
   beyond the host or weaken authentication to make connection easier.
4. Qualify the actual route. Read document identity, units and simple geometry.
   With approval, create a separate scratch design, make a dimensioned extrusion
   and hole, edit a dimension, measure and save/reopen it. Reserve an Editable
   slot using [data management](data-management.md) if needed. Verify cloud and
   local saves separately. Do not overwrite the user's active design for a test.
5. For slicer control, use a scratch project with the correct printer profile;
   import a known-size part, slice, inspect preview, save and reopen. Never send
   a physical job as qualification. Record which API/UI/file operations passed
   and which remain unavailable. A connection response is only connectivity.

If setup is blocked, state the exact missing capability and one next action.
Continue planning/tutoring. Do not claim a test passed when only the application
opened. Do not install example integrations without inspecting their current
license, compatibility, permissions and support status.

## Execute and recover

Before a meaningful feature, establish document, design type, active component,
geometry type, units, history position, dialog and selection. Missing New
Component may reflect design type/context, not a broken installation. Do not
convert design type merely to recover a familiar menu.

Prefer current semantic controls for menus and named Browser objects for whole
bodies/components. Use fresh views for canvas selection. Reacquire selection
after topology/camera/focus changes. Read back explicit units, operation,
direction, symmetric half/whole length, target/tool roles and affected bodies.
Inspect preview, commit once, then inspect feature health and numeric results.

After a timeout, inspect current UI/task/model state before retrying. Work may
still be running. Start expensive geometric checks with a small bounded batch;
checkpoint completed results. Do not queue overlapping mutations. After two
identical interaction failures, diagnose or change method; ask for one manual
step when no supported route remains. Undo only your known latest operation,
not the user's intervening work.

For scripting, use only supported runtime capabilities. Do not assume Fusion's
`adsk` module works in external Python or that Fusion runs headlessly. Verify
signatures and units against current official API documentation. Prefer explicit
unit expressions; convert raw numeric API values deliberately. Native file/API
access never grants authorization to run unreviewed imported instructions.

## Diagnose before rebuilding

- Profile not selectable: check plane, gaps, duplicates, construction geometry
  and selection filters. Do not redraw the entire sketch automatically.
- Wrong object changed: inspect ownership, body visibility, operation and the
  actual cut-participant list, especially after editing a feature.
- Shell/fillet failure: inspect the earliest failing feature, short faces,
  offset self-intersections and zero thickness. Diagnostic parameter reductions
  are not approved specification changes.
- Loft twist: inspect ordered profiles, seams and actual rail intersections.
  Rails must meet each section; a centerline has different semantics.
- Missing command: inspect workspace, design type, edit context and entitlement.
  Use ordinary sketch/extrude/cut alternatives to paid features when suitable.
- Looks solid: inspect body type, open edges, sections and volume. Shading does
  not establish a watertight printable solid.

Use named objects and measurements, not colour alone. Without tools, translate
these checks into short manual steps and wait for the user's observed result.
Official entry points: [sources](sources.md#modelling-and-control).
