# Object-to-workflow atlas

Choose the main volume first, then interfaces and detail. These are conditional
plans, not Autodesk command recipes or manufacturing approval. Matching IDs,
dependencies, branches and checks are in [workflow-graph.json](workflow-graph.json).
Official command references are in [sources](sources.md#modelling-and-control).

## Choose a family

| Shape/need | Route ID | First construction |
|---|---|---|
| Plate, solid bracket | `plate-bracket` | Closed profile, Extrude |
| Constant-thickness wall/channel | `wall-channel` | Thin Extrude or closed wall section |
| Open box/tray | `open-enclosure` | Shell or explicit cavity cut |
| Hollow split body | `closed-clamshell` | Closed Shell, Split Body |
| Tapered container | `tapered-container` | Taper/Draft with controlled cavity |
| Cup, knob, turned adapter | `axisymmetric` | Revolve a radial section |
| Bent tube/constant-section handle | `path-sweep` | Profile along path |
| Round-to-rectangle/changing section | `transition-loft` | Located sections, Loft |
| Flat raised/recessed mark | `flat-relief` | Clean profiles, shallow Join/Cut |
| Curved relief | `curved-relief` | Test Emboss or surface construction |
| Holes/vents/repeated details | `feature-pattern` | Prove a seed, then Pattern |
| Threaded bore/shaft | `threads` | Cylinder then specified modeled thread |
| Standoff/insert seat | `boss-insert` | Boss, hardware-specific pocket |
| Reinforcement | `rib-web` | Rib/Web or explicit gusset |
| Bent sheet, not printed imitation | `sheet-metal` | Sheet rule, flanges, Flat Pattern |
| Controlled compound curvature | `surface-body` | Patches then valid closure |
| Sculpted grip/organic shape | `organic-form` | Coarse Form then precise interfaces |
| STL/scan to engineered part | `mesh-rebuild` | Inspect, repair or dimensional rebuild |

## Dependencies and order

A feature requires valid parent geometry at its place in history. A pattern
needs a valid seed; a thread needs its cylindrical support. Create stable
datums before dependent interfaces. Prefer cosmetic fillets late, but functional
root blends or defining curvature may belong in the seed or before hollowing.
Reordering needs dependency checks, not just visually independent features.

Decide what controls the part: outside envelope, usable cavity, normal wall
thickness, seating datum or mating gap. For tapered walls, horizontal inset is
not normal thickness. Keep wall, floor, fit allowance and thread parameters
separate. Use simple constrained sketches without fixing every entity to hide
missing design intent. Project only references whose changes should drive the child.

## Solid and hollow routes

**plate-bracket.** Use a closed section and explicit extent/operation. An L
section extruded across width is compact; separate base/upright features help
when dimensions vary independently. Locate holes from datums, not rounded edges.
Check thickness, hole centres, driver access and load direction. Valid geometry
does not establish load capacity.

**wall-channel.** Thin Extrude follows a planar open/closed curve with a chosen
wall side. A closed inner/outer section gives explicit unequal widths and ends.
Use Sweep for a nonplanar route, Rib/Web for reinforcement. Check joined corners,
end closure and thickness in section; construction-only lines are not profiles.

**open-enclosure.** Shell when offset walls express intent. Select opening faces
to remove. Use an explicit cavity cut when inside dimensions or floor thickness
control the design. Add cavity-dependent fixtures after hollowing. Inspect usable
space at actual component height and unintended cuts through other bodies.

**closed-clamshell.** For a closed Shell select the body in the Browser, not an
opening face or an ambiguous "nothing." Split with a defined plane/surface and
organize halves before mating features. Split/hollow separately if halves need
different walls. Check partitions, tongue/groove clearance and support access.
Do not trap unremovable FDM supports inside a sealed cavity.

**tapered-container.** Fix the controlling end/datum. Extrusion taper suits simple
draft; Draft tilts selected faces about a fixed reference; Loft suits changing
section shapes. For outside-controlled uniform walls, test draft then Shell.
For inside-controlled space, construct that cavity explicitly. Draft after Shell
only when its effects on both wall faces are intended. Inspect sections at
relevant heights. A failed Shell is not permission to thin a specified wall.

**axisymmetric.** Revolve a section around an explicit axis. Including inside and
outside in the section can avoid fragile shelling at a neck. Check radius versus
diameter dimensions, axis overlap, bore and axial lengths. Add asymmetric details
later; pattern grips about the actual axis.

**path-sweep.** Define path and starting section plane/orientation. Inspect bend
curvature versus section size before adding spline points to fix self-overlap.
Guides may change scale as well as orientation. Check wall continuity, twist,
exit direction and end fittings. Use Loft when distinct sections control shape.

**transition-loft.** Locate and order simple sections, inspect connectors/seams
and choose rails versus a centerline deliberately. Rails must intersect every
section; a centerline follows different rules. Inspect twist, continuity, body
type and internal clearance, not only silhouette. Use controlled surface regions
if the solid loft cannot express the shape robustly.

## Detail routes

**flat-relief.** Use user-authorized clean profiles. Imported SVG scale, duplicate
loops, islands and self-intersections need checking before extrusion. A decal
is appearance, not printable relief. Check raised regions join and recessed
regions leave enough wall. A stencil needs separate island/bridge planning.

**curved-relief.** Test a small representative Emboss before dense detail. Inspect
target faces, seams, wrap, local depth and attachment. A projected curve is not
relief; straight extrusion through a curved face does not guarantee constant
normal depth. If needed use limited patches/surfaces with that distinction stated.

**feature-pattern.** Prove a full functional seed. Choose features, bodies or
components according to intended identity. Distinguish spacing from overall
extent: for `n > 1`, span is `(n - 1) * spacing`. Check first/middle/last instances
and boundaries. Per-instance termination may require an adaptive compute mode;
identical copied cuts are not always correct.

**threads.** Confirm standard, designation, pitch, hand and engagement. Use
Modeled when the printed export must contain the physical helix; cosmetic
threads are not mesh geometry. Check the selected face, lead-in, wall thickness
and exported helix. Use a representative fit coupon rather than promising a
nominal thread will mate. Insert seats use the next route instead.

**boss-insert.** Start from mounting coordinates and the actual hardware drawing.
Separate height, outside diameter, bore and insert depth. No universal insert
pocket or press fit exists. Use ordinary sketch/extrude/cut when an extension
tool is unavailable. Inspect floor/lid stack, remaining membrane, reinforcement,
insertion heat/tool access and screw engagement. Prove one before patterning.

**rib-web.** Define supports and sketch plane. Rib and Web extend differently
relative to that plane; an explicit triangular gusset extrusion is an alternative
when termination is unclear. Check real attachment, root shape and access.
Printed layer direction remains a separate strength decision.

## Complex geometry and other manufacturing routes

**sheet-metal.** Choose actual material, thickness and bend rule, then base/edge
flanges. For cuts across bends use Unfold/Cut/Refold where appropriate. Use the
current Flat Pattern for developed output, not temporary Unfold. Check reliefs,
bend direction, overlaps and allowances against the process. A solid L-shaped
print is not a qualified bent sheet. Check current export entitlement.

**surface-body.** Build controlled curves/patches, trim/extend/match, then close
a volume by Stitch/Boundary Fill or Thicken an appropriate skin. Repair real
gaps instead of inflating stitch tolerance. Inspect open edges, offset folding,
body type, volume and required thickness before adding solid details.

**organic-form.** First rule out Extrude/Revolve/Sweep/Loft. For genuine sculpted
curvature start with a coarse symmetric T-Spline, inspect the control frame for
folds and add control geometry only as needed. Finish Form/convert successfully
before adding precise bores and mating features. An open result may need the
surface route. Recheck dimensions after relaxation; auto-repair is not proof.

**mesh-rebuild.** Preserve the source. Verify units and a known dimension; a mesh
does not recover original parametric history merely by conversion. Repair or
selectively convert if useful and available; rebuild simple engineered regions
from reliable dimensions when better. A perspective picture with one scale
length does not reveal hidden wall thickness or remove perspective distortion.
Compare the result's functional dimensions, body type and exported geometry.
