# Personal Use slots, checkpoints and recovery

Use before managing Editable documents, backups or restores. Plan/format facts
are dated in [sources](sources.md#plan-and-data); confirm current UI/entitlements
when relevant. A slot is an Editable **document**, not a project or folder.

## Manage ten Editable documents recoverably

Personal Use permits ten documents Editable at once. Stored documents/projects
are not limited to ten. Read-only keeps the document in place and can be reversed
when a slot is available. Never archive or delete a project or document just to
free a slot, and never create a fresh duplicate merely to resume existing work.

1. Inspect the actual Editable count and candidate documents in Fusion's Data
   Panel/Home. Optional supported API status may help, but is not required and
   does not prove a status setter exists.
2. Identify a saved, inactive candidate within the user's authorized scope.
   Check unsaved edits, external references, assembly dependencies and whether
   another operator is using it. Show the exact candidate/consequence if the
   request did not already authorize this transition.
3. Save and verify its cloud version before closing modified work. Preserve an
   independent native archive if useful and available. If cloud completion is
   blocked, protect local progress and report it; do not discard edits to free a slot.
4. Use the current **Editable / Read-only** status dropdown in the Data Panel
   or the corresponding supported Home control. Set that document Read-only.
   Verify its state and that the Editable count decreased before activating
   the intended document. A click or a folder move is not verification.
5. Record which document changed state. To resume, make that same document
   Editable after confirming a free slot. Reopen and inspect it; do not restore
   an archive into a new cloud item for ordinary resumption.

Without control tools, guide these steps manually and label the user's reported
state as such. Do not invent an exact count from historical records. If no safe
candidate is authorized, keep planning and ask which saved document may change.

## Save early and say what was saved

Create a named working design in the intended destination near the start. After
major stages, save before costly patterns, assembly changes or risky repair.
For a separate study use a uniquely named copy, preserving the production model.

| Checkpoint | Evidence to obtain | Claim it does not support |
|---|---|---|
| Cloud design | Correct destination/name, completed save/sync, visible version; reopen when practical | An independent local backup or verified restored joints |
| Native local archive | Actual supported export, destination and nonempty file; reopen/test restore where feasible | Cloud upload or synchronization |
| Neutral STEP | Reimported geometry, units and key dimensions | Fusion history, parameters or complete joint semantics |
| Manufacturing mesh | Receiving-app scale, bodies and geometry | Editable design intent or printable strength |

If no filesystem inspection is possible, report only the observed save/UI result
or user confirmation. With file tools, record sizes and checksums for important
archives when practical. A checksum detects a changed file, not a usable restore.
A saved macro, script, screenshot or export-dialog close is not a saved design.

## Native archives and export limits

Use F3D for a self-contained native design when available. Distributed designs
may require an F3Z archive including references. Verify the actual UI, design
structure and export result; documentation labels and format availability can
differ. Do not declare all Personal Use assemblies exportable or all F3Z exports
unavailable from a table alone. If native export is blocked, preserve the cloud
design and disclose the backup gap. STEP is useful geometry recovery, not an
equivalent editable assembly archive.

The checked Personal Use format table includes F3D, STEP, STL and 3MF. DXF from
File > Export is commercial-only, while sketch **Export DXF** is available to
all licenses. Use the actual applicable export command rather than assuming a
format is globally prohibited. Verify supported output in the current session.

## Restore only when needed

Restore a local archive only when recovery or a separate cloud copy is intended.
Confirm source revision, destination project/folder, name collision handling,
required slots and references before upload. Preserve the local archive and
original cloud design. Ask before overwriting unrelated work or importing to an
external/shared destination. Do not delete originals after an apparently successful upload.

Open the recovered design and check units, parameters/history, bodies/components,
external references and key dimensions. For mechanisms also check joints and
drive motion. Geometry-only reopening is not a restored-motion test. Mark an
archive "restore untested" until relevant checks pass. Whole-project archiving
is separate account organization outside routine slot management.
