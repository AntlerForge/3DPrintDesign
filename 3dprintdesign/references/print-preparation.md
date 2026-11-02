# FDM print preparation

Use for exports, slicing, fit coupons, print packs and physical-start checks.
Operate the slicer when authorized control tools exist; otherwise teach the
next relevant steps and label unobserved results. No slicer is assumed installed.

## Establish the actual target

Confirm printer model, nozzle, usable build dimensions and exclusions, plate
surface, material and supported slicer. For Bambu targets prefer Bambu Studio
when present and suitable; help set it up only when requested/approved. Other
FDM printers use their supported slicer and correct machine profile. Never
substitute a nearby printer profile merely because nominal bed size matches.

Inspect the active printer/profile after opening a project and before sending.
A saved profile name does not prove the live device selection. Include supports,
brims, purge/prime structures, exclusion zones and toolhead/sequential-print
clearance in the actual usable plate. Do not hardcode a familiar plate size.

## Export the intended revision

Identify exact bodies/components, quantities and accepted interfaces. Preserve
the editable native design separately. Use a supported mesh export and verify
units, bounding dimensions, connected shells, thin detail and modeled threads
in the receiving application. STL has no dependable unit metadata; inspect
imported scale. A CAD 3MF export is not automatically a configured slicer project
or stored G-code. If tools cannot inspect the export, state that limitation.
See [data management](data-management.md#native-archives-and-export-limits).

## Orientation, strength and fit

Choose orientation from load paths and layer adhesion, contact area/stability,
critical mating faces, visible surfaces, overhangs and removable supports.
Avoid placing a highly loaded hook/flexure across weak layer bonds merely to
save supports. Wall count, infill, material, temperatures and layer height are
design variables, not a universal strength recipe. A stronger-looking preview
does not establish load capacity. Safety-critical applications need appropriate
engineering and validation beyond this skill.

Keep wall thickness, designed fit gap, hole compensation and thread allowance
separate. Use [fit coupons](mechanical-assemblies.md#fit-coupons-and-accepted-interfaces)
on the target printer/material/orientation/profile. Label variants and retain
the accepted revision. Do not upscale an entire assembly to fix one bore.

Supports need inspection at actual contacts and removal paths. Choose normal,
tree or other supported methods from geometry/material, not a universal preference.
Keep support away from accepted mating surfaces when possible. Check whether
bridges can be printed, whether narrow islands start unsupported, and whether
cavities trap supports. Use per-object settings where needed; disabling supports
globally because one object needs none can break its neighbour.

## Adhesion and environment

Use the actual printer, plate and filament manufacturer's guidance for surface
cleaning, adhesive/release layer, nozzle/bed temperature, ambient range, draft
avoidance, ventilation and enclosure use. Glue can be a release layer rather
than an adhesion fix; do not apply a generic treatment to an unknown plate.
Confirm material dryness and relevant profile calibration.

An enclosure does not guarantee a cold room is within specification, and raising
bed temperature is not a general ambient-heating solution. Check the actual
model's specified operating range, even for enclosed machines. Do not prescribe
heated chambers, improvised heaters or a hotter bed to cure an unexplained
adhesion problem. Diagnose plate condition, first-layer behavior, nozzle/profile,
material and environment separately. Preserve the printer's safety controls.

## Slice, inspect and save

Slice the final layout. Inspect layer preview around thin walls, overhangs,
threads, bridges, slots and first layers. Check supports/brims against neighbours
and bed limits, skipped/outside objects, warnings and per-object overrides.
Changing geometry, arrangement or profile invalidates the previous slice.
Temperatures/flow limits must match the selected material, not just its name.

Save the editable slicer project and reopen or inspect it for retained settings
and objects when possible. Keep sliced/toolpath exports separate. A filename
does not prove embedded toolpaths; inspect the saved artifact or slicer's own
report before claiming them. Give time/material as estimates, including support
and waste. A completed slice is not a claim of zero warnings or physical success.

## Complete print packs

Maintain a manifest of part ID, revision, quantity, plate assignment and reused
accepted parts. Include hardware quantities, assembly order and test directions.
Check object counts and placements on every requested plate after combining
projects. Slice and inspect all plates, not only the selected one. Verify one
nonempty saved toolpath per plate when delivering sliced outputs; otherwise
label the project as requiring slicing. If file inspection is unavailable,
state exactly which previews or saved results were observed.

Use one authoritative current pack and identify optional individual projects.
Preserve the user's later layout and keep guide estimates tied to the final
profile/revision. Fewer beds is not automatically faster or lower waste.

## Physical start and evidence

Preparation, export, slicing and transfer-only requests are not start approval.
Before an authorized start, read back the exact plate/job, actual device,
material/spool mapping, estimates and relevant calibration choices. Confirm
the bed is clear/seated, suitable material loaded and environment safe with
the user or available reliable evidence. Obtain explicit approval for that job;
do not infer a batch of starts from a requested quantity of parts.

Reuse explicit approval for the unchanged job rather than asking for every
click. If submission is uncertain, inspect the printer's current job/download
state before retrying to avoid duplicate starts. Do not send when readiness or
approval is unresolved. Physical actions during assembly/tests also need scope.

Distinguish saved, transferred, queued, preheating, printing, first-layer checked,
completed and physically accepted. Layer zero or a queue entry does not prove
a successful print. Keep fit, load, release force, fatigue and stability feedback
with the exact part revision, not as universal future defaults.

Official printer/slicer entry points: [sources](sources.md#printing).
