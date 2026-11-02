# 3DPrintDesign

Version 1.0.1. Design and make editable Fusion parts, inspect assemblies, prepare
FDM print packs, or learn the steps yourself. Hands-on Fusion and slicer control
is supported when your agent has native computer-use tools or an authorized
structured API/MCP connection. Without those tools it guides you manually.

## Install and start

Place the complete `3dprintdesign` folder in your agent client's supported skills
location, following that client's instructions. Keep the lowercase folder name
and bundled references together. The displayed name is **3DPrintDesign**.
If your client does not support skills, provide [SKILL.md](SKILL.md) and the
relevant references as instructions; invocation syntax may differ.

This package does not install Fusion, a slicer or a control integration. Start
with your part and say whether to teach, inspect or make it. The agent should
offer to help set up integration and computer control, but ordinary help does
not require accepting that offer.

## Optional integration and computer control setup

Ask for setup help and name your platform and agent client. The agent first
discovers what the client actually supports. Native computer use can operate
Fusion and slicer UIs; a compatible authorized Fusion API/MCP route can perform
structured model operations. You may use either or both.

Before an approved installation/configuration, it should explain components,
permissions, destinations, privacy/network exposure and a rollback. It must
preserve existing configuration, avoid silent network exposure or global
permission changes, and let you enter credentials and approve OS prompts.
It must not invent a server address or assume an MCP integration is installed.
If current documentation or setup tools are unavailable, it explains the exact
gap and guides the supported manual step instead of claiming installation.

Qualification means a real read and, when you approve a scratch test, a small
edit, measurement and verified save/reopen. A health response alone proves
neither modelling nor desktop control. See [capabilities](references/capabilities.md).

## Example prompts

```text
Use $3dprintdesign. Teach me to make a bracket in Fusion. Ask for the
mounting dimensions and load direction before choosing its dimensions.
```

```text
Use $3dprintdesign. Make the bracket from this dimensioned sketch in Fusion
using available control tools. Save an editable model and check the holes.
Do not print it.
```

```text
Use $3dprintdesign. Help set up Fusion integration and computer control.
My platform is [platform] and my agent client is [client]. Explain changes
before installing or configuring anything.
```

```text
Use $3dprintdesign. All ten Editable slots are used. Inspect the documents
and recommend a saved one to make Read-only. Do not change anything yet.
```

```text
Use $3dprintdesign. Export this revision and prepare a sliced print pack
for my [Bambu or other FDM printer]. Check its real plate, nozzle, material,
orientation and supports. Do not send a print-start command.
```

```text
Use $3dprintdesign. Learn from this session and these fit-test notes.
Implement supported improvements in my designated writable skill source,
check them and update my private project checkpoint. Preserve a rollback.
```

## What learn does

During this skill's work, `learn`, `improve`, `self learn`, `self-learn` and
`run improvement` request one bounded review. It examines available evidence
since the last recorded checkpoint, including corrections, saved results and
physical feedback. It separates observation from interpretation and may find
that no change is justified. It does not train the model or run in the background.

Choose a private local project record for checkpoints and evidence outside the
public skill bundle. The agent cannot assume access to older chats or files.
It reports missing evidence and retains unreviewed ranges. With no file access,
it returns a record and proposed patch as text. At first use, designate the
writable maintained source and permitted scope. Thereafter an explicit learn
command includes implementing supported improvements there, checking them and
saving the checkpoint, without repeated approval for ordinary scoped edits.
Keep a recoverable baseline. Never silently replace a vendor-managed/read-only
installed copy; return a patch when scope or write access is missing. Installation
and publication remain separate. See [learning](references/learning.md).

## Scope and distribution

Fusion Personal Use is the default modelling target. Confirm eligibility under
[Autodesk's current terms](https://www.autodesk.com/products/fusion-360/personal).
Printer settings and fitted dimensions must match your own machine, material
and calibration. Printing requires explicit physical-start approval.

No third-party manuals or integration code are bundled; links to official docs
are in [sources](references/sources.md). No third-party dependencies or executable
helpers are required. This skill is released under the [MIT licence](LICENSE).
Linked third-party software and documentation retain their own terms.
Downloading/loading this package does not itself install Fusion or control tools.

Source and releases: [AntlerForge/3DPrintDesign](https://github.com/AntlerForge/3DPrintDesign).

Validation status and evidence limits are recorded in
[sources](references/sources.md#package-validation). Tests of instructions do not
prove that a live Fusion integration, slicer or printer works.
