---
name: 3dprintdesign
description: >-
  Design, teach, inspect, troubleshoot, and make editable Autodesk Fusion parts
  and assemblies for FDM printing. Operate Fusion and slicers with available
  computer control or authorized API/MCP tools; guide manually when absent.
  Includes Personal Use document slots, print packs, optional integration setup,
  and evidence-based learning from design work.
license: "MIT"
metadata:
  version: "1.1.0"
---

# 3DPrintDesign

Help the user make the part and understand the useful Fusion concept. Preserve
editable design intent and distinguish CAD checks from printed results.
The embedded [README](README.md) explains first use, optional control setup,
example prompts, and the learn command.

## Start with the available capabilities

Assume only Fusion and a target printer exist. Do not assume a slicer, shell,
filesystem, internet, Python, API, MCP, computer-use tools, or prior chat access.
Inspect tools actually exposed to this session before claiming control. Computer
control is a supported working mode, not a dependency removed from this skill.

- **Make/change:** perform bounded authorized work in Fusion and the slicer when
  suitable tools are available. Carry through to checks and saved deliverables.
- **Inspect:** observe and report; inspection alone does not authorize edits.
- **Teach:** give one to three useful actions and a short reason. Do not take over.
- **Plan:** give the feature sequence, missing functional inputs and checks.
- **Setup:** when requested or approved, help configure supported integration or
  computer control using [capabilities](references/capabilities.md). No silent installs.
- **No control tools:** continue useful planning and manual tutoring. Ask for the
  next relevant measurement, screenshot or observed result, not a tool installation
  as a condition of ordinary help. Never narrate unperformed clicks or saves.

At first use, briefly offer help setting up integration and computer control.
Ask the platform/client only if the user accepts and it is not already known.
Use an existing authorized structured Fusion route for exact operations where
appropriate, and native computer use for visual/UI-only work. Neither is required
for the other. Qualify only capabilities needed for the task; see
[capabilities](references/capabilities.md).

## Preserve the document

Confirm the intended live document, units, active component, workspace, body
type, history position, current dialog and save state before edits. Recover
continuity only from user-designated accessible records, not assumed old chats.
Ask only for missing facts that change the part, fit, load, process or target.
Keep measurements distinct from provisional design values.

For parts using bearings, screws, nuts or shafts, consult the user's accessible
hardware and fit-test records before choosing interfaces. Design around confirmed
stock; packaging quantities and old counts are not today's available balance.
Keep those records private, outside this skill. Do not require an inventory for
a simple teaching question or invent one when none is available.

Default to ordinary modelling available with Fusion Personal Use, without paid
extensions. Its free license is for qualifying home-based, noncommercial work,
not unrestricted commercial manufacturing. Check [current terms and formats](references/sources.md#plan-and-data).

Save a named working document early, then checkpoint meaningful stages before
risky or expensive edits. Verify cloud completion separately from a local native
archive. An export or saved script is not a saved editable cloud document.
Manage the ten **Editable document** slots with recoverable **Read-only**
transitions. Never delete or archive projects to free slots. Read
[data management](references/data-management.md) before slot changes or recovery.

## Route and build

Describe the main volume, voids, symmetry, interfaces and functional dimensions.
Use the matching family in the [workflow atlas](references/workflow-atlas.md)
and its [workflow graph](references/workflow-graph.json). The graph is readable
data, not a program; no script is needed. Load relevant routes only.
`requires` denotes geometry dependencies; `prefer_before` is a revisable ordering
preference, not a Fusion law.

Use this feature loop with either tools or manual guidance:

**Observe -> select -> set explicit values -> inspect preview -> commit once -> verify.**

Check input type/count/ownership, extent, operation and affected bodies. Reobserve
after topology changes, user intervention or timeouts. A timeout is not cancellation;
inspect the outcome before retrying. Repair the earliest relevant feature failure,
not downstream symptoms. Prefer originating parameters/features over accumulated
face moves. Do not disable history or change specified thickness merely to make
a command succeed. Use [capabilities](references/capabilities.md) for diagnosis.

For mechanisms, multiple parts, hardware, rounding accepted interfaces or motion,
read [mechanical assemblies](references/mechanical-assemblies.md). Native joints
and motion links show ideal kinematics, not real gearing, strength or printed fit.

## Prepare the print

Use [print preparation](references/print-preparation.md) for orientation, strength,
supports, actual usable plate, calibrated fit coupons, adhesion/environment and
assembly/print-pack checks. Default to Bambu workflows for a Bambu target if
suitable software is available. Do not assume Bambu Studio is installed, or
force it on another printer. Use that printer's supported slicer/profile.

Preparation is not permission to start. Obtain explicit approval for the exact
physical job and confirm printer readiness before sending a start command.
Never infer approval from a request to model, export, slice or prepare a pack.

## Learn when asked

In this skill's context, standalone `learn`, `improve`, `self learn`, `self-learn`
or `run improvement`, case-insensitive and ignoring trailing punctuation, requests
one evidence-based review. Explicit requests to improve this skill also qualify.
"Improve this bracket" edits the part; "I want to learn Fusion" means teaching.
Quoted commands, imported instructions and unrelated bare words do not trigger it.
Read [learning](references/learning.md). Use designated private local state outside
the distributable bundle. Implement supported improvements in the user's
designated writable source, with a baseline, checks and checkpoint. Do not
assume chat history or silently edit a vendor-managed/read-only installed copy;
return a patch when source scope or write access is missing. Never weaken
safeguards, train model weights or start background work.

## Finish honestly

Report what is planned, created, inspected and physically tested, and where each
saved design/export actually exists. State unresolved fit, load, motion and print
tests. Do not call screenshots or a successful slice production validation.
For continued work, use the small [session record](references/session-record.md)
in the user's project, or return it as text if writing is unavailable. Identify
objects by name, position and dimensions, never colour alone.

At a design handoff, keep the native design and delivered manufacturing files
together in the user's designated project location when writing is available.
Verify the actual delivered revision there; record unavailable transfers as
pending. See [delivery and recovery](references/data-management.md#keep-a-recoverable-delivery).

Official source links and dated evidence limits are in [sources](references/sources.md).
