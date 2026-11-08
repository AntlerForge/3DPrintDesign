# Mechanical assemblies, fit and finishing

Use for multiple parts, hardware, moving mechanisms and edits near accepted
interfaces. The [atlas](workflow-atlas.md) describes features, not assembly qualification.

## Requirements and hardware

Separate load carrying, orientation control, positioning, locking, release and
tactile feedback. A bearing or detent does not automatically provide them all.
Turn "always level" or "never tips" into bounded load/handling conditions and
measurable acceptance checks. For stability, consider support footprint, mass,
load position, sliding friction and overturning. A ballast pocket is capacity,
not installed mass or demonstrated stability.

Ask for actual available hardware specifications and quantities when needed.
Read the user's accessible stock and fit records first; ask only for gaps that
change the joint. Keep project requirements separate from available stock.
Do not count the same installed bearing twice, treat package quantities as a
current count, or infer a machine thread from a seller's self-tapper marking.
Keep measured values, manufacturer nominal values and assumptions separate.
Check shaft diameter/usable length, bearing ID/OD/width, fastener head diameter
and height, thread length, nut dimensions, engagement and driver access. A screw
assortment does not prove a particular length or quantity is available. Budget
all shaft stubs, cutting allowance and retention before releasing a cut list.

Design torque transfer, axial retention, shoulders and assembly order as well
as bores. A matching bore does not attach a shaft. Bearing envelopes are not
detailed races or qualified printed fits. Keep radial location, axial retention,
clamping and running clearance as distinct requirements.

## Fit coupons and accepted interfaces

Use representative, labelled coupons before a large print when clearance is
uncertain. Vary one unknown at a time or label a two-variable matrix clearly.
For each variant name both mating parts, insertion direction, hardware and the
test: slide, rotate, retain, clamp or release. Show a section/exploded detail for
hidden nut/screw paths. Do not prescribe physical testing without approval.

Record CAD dimensions separately from measured prints, with variant ID,
printer/nozzle, material, orientation, slicer profile and revision. Transfer of
an accepted fit to changed conditions is an assumption until checked. There
is no universal FDM bearing interference, insert pocket or thread allowance.
Use the user's accepted result for the same interface and setup before trying
a generic recommendation. Preserve different accepted project fits rather than
averaging them into one correction.

For an untested size, start with an additive allowance from a comparable feature
class and bracket it with labelled candidates. Treat that as a test plan, not an
accepted fit. Do not infer a global shrinkage percentage from one measured size.
Keep journal OD, rod-hole ID, bearing housing ID, nut across-flats, nut-thickness
space and blind insertion travel independent. State whether an allowance is
diametral, total across-flats, per side or axial. Check existing slicer hole and
contour compensation before adding a CAD allowance.

Use representative wall thickness, insertion length, orientation and supports.
Check a thin sleeve on its shaft and inside its bearing together: fitting the
outside can tighten the bore. A nut's coupon needs screw alignment and
anti-rotation checks as well as insertion. Measure the actual nut rather than
scaling a smaller pocket by nominal thread size.
If a nut slides freely but stops short of its screw axis, inspect travel/blind
depth before widening its already accepted pocket.
Retain enough material beyond a deeper entry. Binding during insertion is a
different problem and can need debris removal or thickness clearance instead.

When the user reports a result, add it to the designated private shared fit
record, if one exists, and link the project's exact variant. Otherwise keep
the result in the private project note; establish a reusable record only when
useful and within the available write scope. See the [fit-record template](fit-record.md).
Do not mark every unselected candidate failed. Record unknown settings as
unknown, and distinguish as-printed from filed, drilled or otherwise finished.

Apply the accepted variant to every affected production instance and verify
the exported interface. Preserve accepted dimensions during unrelated edits.
Retest changed interfaces and affected assemblies, not every unchanged coupon.
A fit coupon does not qualify loaded motion, fatigue or whole-assembly stability.

## Native motion versus physical mechanisms

1. Define axes, reference frame, allowed degrees of freedom, load cases and
   interfaces. Use components/joints for moving identity, not only body moves.
   Distinguish linked instances from independent parts.
2. Prove one moving chain before repeating it. Confirm grounding, rigid groups,
   joint axes, range and motion links in the actual intended revision. Retract
   a lock for free movement and check its engagement/stroke separately.
3. Drive joints through the required range. Inspect critical phases and repeated
   stations. Include screw heads, nuts, shafts, retainers and release hardware,
   moving each envelope with its owning part. Report checked pairs, phases and
   excluded contacts. Samples do not prove an exhaustive continuous clearance.
4. For gearing use documented real tooth geometry, not decorative teeth. Check
   center distance, phase, face overlap and engagement. Zero tooth overlap also
   occurs when gears are too far apart. Native motion links impose ideal ratios;
   they do not establish force transmission, backlash, deflection, wear or slip.
5. Keep intended fitted interference distinct from unexpected contact. An
   overlap of conservative envelopes is a potential contact, not proof that
   actual rounded profiles rub. Investigate the pair/phase instead of globally
   suppressing collisions or silently thinning the part.

Use conservative world-space bounds if available. For a rotated local box,
transform all eight corners or use an equivalent affine bound; two transformed
opposite corners can under-enclose geometry. Bounds filter candidate pairs;
they do not prove exact shape clearance. Bound expensive kernel work and
save progress before extending a sweep. See [operation](capabilities.md).

When motion demonstration is requested, show the actual model moving or guide
the native drive operation. A generated illustration is not motion evidence.
Save the driveable native result; after restore, inspect joints and drive again
before claiming restored motion. Cloud structure-only reopening is a different test.

## Round edges without changing the fit

Save a baseline. Separate handling/visual edges from bores, bearing seats, tooth
profiles, shoulders, locating faces and snap geometry. Choose radii from local
material and purpose; do not fillet every edge with one value. Concave fillets
can add material and reduce clearance. Check remaining wall and inside/outside
corner relationships.

Select by ownership and geometry, verify count and reacquire after topology
changes. Before/after comparisons must include protected dimensions, axes and
mating geometry. Unchanged body counts or bounding boxes do not prove identical
interfaces. Inspect feature health and rerun affected clearance/motion checks.

## Parts and assembly deliverables

Use the same durable part IDs, revisions and quantities in CAD, exports, plate
labels, hardware lists and assembly instructions. Include exploded/section views
where useful, assembly order, insertion directions, tool access, fastener
engagement and acceptance tests. Mark reused accepted parts explicitly so an
omitted duplicate is not mistaken for a missing part. Record unresolved load,
holding, friction, fatigue, wear and stability tests plainly. Use the
[print-pack procedure](print-preparation.md#complete-print-packs) before delivery.
