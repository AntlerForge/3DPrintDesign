# Sources and evidence limits

These links support authored workflow summaries, not copied manuals. Access to
the internet is optional; use bundled guidance when offline and say when a
current claim cannot be checked. Command names/menu paths are navigation hints,
not a guarantee about the user's installed version, context or entitlement.

## Plan and data

Release review date: **2026-11-02**. The Personal Use license and format table
were opened during preparation. The activation procedure was supplied by the
release review from Autodesk's article dated 2026-08-20; the preparation browser
could open its URL but extracted no readable text. This is not a live UI test.

- [Personal Use eligibility and terms](https://www.autodesk.com/products/fusion-360/personal):
  qualifying home-based noncommercial use, not unrestricted commercial use.
- [Personal Use Editable/Read-only activation](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-activate-and-deactivate-files-in-Fusion-360-for-personal-use.html):
  ten Editable documents and the document status dropdown, not ten projects.
- [Supported file formats](https://help.autodesk.com/view/fusion360/ENU/?guid=TPD-SUPPORTED-FILE-FORMATS):
  Personal Use F3D/STEP/STL/3MF; sketch Export DXF differs from File > Export.
  F3Z labeling/export details must be checked against the actual assembly/UI.
- [Local archive procedure](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-make-a-local-archive-back-up-file-in-Fusion-360.html):
  official navigation for native recovery. Not freshly runtime-tested here.

Recheck changing terms or format details when they determine the user's outcome.
Do not turn the release review date into a claim that every linked page was
freshly inspected or every supported workflow was executed.

## Modelling and control

The atlas and graph are authored conditional plans. Extrude was reopened on
2026-11-02; remaining links below are official documentation entry points carried
forward for task-specific checking, not newly executed command tests.

| Topic | Official reference |
|---|---|
| Extrude/Thin Extrude | [Extrude](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/SLD-REF-EXTRUDE.htm) |
| Shell and split | [Shell/Split/Components tutorial](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/SLD-TUT-3-SHELL-SPLIT-COMPONENTS.htm) |
| Draft | [Draft](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/GUID-83C650C2-E602-4BBC-AC9A-AB9A96F07B72.htm) |
| Revolve | [Revolve](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/GUID-D74BB28A-9570-43AD-97A4-E094021C036B.htm) |
| Sweep | [Sweep](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/SLD-REF-SWEEP.htm) |
| Loft | [Loft](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/GUID-EC6CECCD-55C1-4B08-95E4-5B1EEDE78D07.htm) |
| Relief | [Emboss](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/SLD-REF-EMBOSS.htm) |
| Patterns | [Rectangular Pattern](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/GUID-9622573F-06FA-462F-AFA7-97CD0C7AA0C9.htm) |
| Threads | [Thread](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/GUID-C37E8172-DE94-4EB0-AFE3-9D3172328441.htm) |
| Boss/Rib/Web availability | [Solids from sketches](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/SLD-CREATE-SOLID-FROM-SKETCH.htm) |
| Sheet metal | [Flat Pattern](https://help.autodesk.com/cloudhelp/ENU/Fusion-Sheet-Metal/files/GUID-121F6E58-0459-4552-85EF-319F44324AE6.htm) |
| Surface closure | [Stitch](https://help.autodesk.com/cloudhelp/ENU/Fusion-Patch/files/SFC-STITCH.htm), [Thicken/Boundary Fill](https://help.autodesk.com/cloudhelp/ENU/Fusion-Model/files/GUID-70C61E8C-C0B5-4381-89EF-B100DEC4149A.htm) |
| Form | [T-Spline utilities](https://help.autodesk.com/cloudhelp/ENU/Fusion-Sculpt/files/FRM-UTILITIES.htm) |
| Mesh export | [Save As Mesh](https://help.autodesk.com/cloudhelp/ENU/Fusion-Mesh/files/MESH-SAVE-AS-MESH.htm) |
| Design context | [Design intent API guide](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/DesignIntent_UM.htm) |
| Structured operation | [Fusion API documentation](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/), [API units](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/Units_UM.htm) |

Control depends on the agent client's exposed capabilities and current supported
integrations. Consult its official setup documentation for that client/version.
No integration server, installer or remote service is supplied by this package.
The official [Fusion MCP sample](https://github.com/AutodeskFusion360/FusionMCPSample)
was opened on 2026-11-02. It describes a reference implementation for running
Fusion API scripts and exposes model/documentation/screenshot tools. It is one
optional setup candidate, not proof of a configured, safe or functioning local
connection. Its MIT license applies to that sample, not automatically to this
skill. No sample code is included here.

## Printing

These are official starting points, not checked printer-specific settings.
Retrieve the actual model/plate/material guidance when available. Do not infer
build size, ambient range or a calibration profile from another printer.

- [Bambu Studio](https://bambulab.com/en/download/studio): optional supported slicer route.
- [Bambu official wiki](https://wiki.bambulab.com/en/): printer, plate, filament and environment guidance.
- [Prusa Knowledge Base](https://help.prusa3d.com/): another FDM manufacturer's printer/slicer guidance.
- [Modelling for printing, tolerances](https://help.prusa3d.com/article/modeling-with-3d-printing-in-mind_164135):
  opened on 2026-11-08. Fit varies with size, orientation, geometry, calibration,
  settings and material. This supports testing comparable interfaces, not a
  universal numerical clearance or transferring one printer's calibration.

Use the target manufacturer's documentation for other machines. No universal
bed temperature, enclosure requirement, fit clearance or strength setting is
established by these links.

## Package validation

Version **1.1.0** is a reference-only portable edition. Naming/frontmatter,
local-link, graph and instruction-routing checks are separate from operational
validation. The saved package may include release-owner test results; only
checks actually run may be reported as passed. Preparation does not establish
successful live CAD, setup, slicer, cloud-restore, printer or physical-fit tests.

Preparation checks run on 2026-11-02:

- Skill Creator `quick_validate.py`: passed using an available validation host.
  The first local attempt lacked its YAML dependency; no dependency was installed.
- Release-owner package suite: six tests passed, including JSON parsing,
  contained/resolvable local links, graph dependencies and invalid-case rejection.
- Parsed metadata checks: lowercase folder/name, package version, display name
  3DPrintDesign and UI description length passed.
- Targeted privacy/dependency text scan found none of the checked private names,
  paths, endpoints or host assumptions. This is not an exhaustive secret audit.

Author instruction walkthroughs, with no control tools assumed, were reviewed
against the saved entrypoint and relevant references. These are manual routing
checks, not independent agent evaluations or successful CAD operations.

| Request | Route and boundary checked |
|---|---|
| Make a bracket from incomplete dimensions | Ask for mounting/load inputs; give manual steps; do not invent edits or saves |
| Ten slots used, need a new design | Inspect/reported status; save then authorized Read-only transition; never archive/delete |
| Setup control, unknown client | Establish platform/client and approved changes; no invented endpoint or health-only success |
| Slice for an unfamiliar FDM machine | Identify actual printer/slicer/plate/environment; no Bambu dependency or print start |
| Learn with a designated writable source | Review available evidence, implement supported scoped changes, check and checkpoint |
| Learn with only a managed installed copy | Return an unapplied patch; no silent install or fictional saved checkpoint |
| Animated gears look clear | Separate ideal linked motion, actual tooth engagement and physical/load tests |

No third-party manuals, integration code or dependencies are bundled. This skill
and its optional maintainer tests are released under the MIT licence in the
bundled `LICENSE` file. Official linked documents and software retain their own
terms; their licences are not changed by this package.

Version 1.0.1 adds the approved public licence and repository links to the initial
portable edition. It does not claim new live CAD, integration or physical tests.

### Version 1.1.0, 8 November 2026

Adds private fit-evidence lookup and recording, independent interface allowances,
provisional extrapolation through labelled coupons, and recoverable delivery
folders. The blank fit template contains no owner's stock, measured tolerances,
machine addresses or project images. Designated private records are optional;
there is no new server, filesystem or integration dependency.

The retained six package tests, Skill Creator validation and privacy/release
checks cover the distributed files. Release notes identify the checks actually
run. Author instruction walkthroughs address the new decisions:

| Request or evidence | Expected next action |
|---|---|
| Two projects have different accepted journals for the same nominal bore | Preserve each fit with its geometry/setup; do not average or overwrite |
| A new bearing size with only earlier fit records | Use comparable allowances to bracket coupons; do not claim a tested result |
| Sleeve fits separately but binds when installed | Check shaft and bearing together; vary OD and bore independently |
| Nut slides freely but stops before screw alignment | Inspect travel and remaining wall; retain accepted width/thickness |
| Record a fit without file access | Return the private record as text and say it is unsaved |
| Delivery folder unavailable after a successful cloud save | Retain accessible native copy, record pending transfer; do not claim full archive |
| Teach one Extrude action | Give the useful step; no inventory or archive setup ceremony |
| Asked to publish improvements from private fitting work | Publish only generic methods; keep filled records and project images private |

These are author walkthroughs, not independent blind evaluations or new
Fusion, slicer, printer, restored-archive or physical-fit tests.
