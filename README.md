# 3DPrintDesign

A portable AI-agent skill for designing editable Autodesk Fusion parts and
assemblies for 3D printing. It can operate Fusion and slicers through available
computer-control or authorised API/MCP tools, or teach the steps manually.

It defaults to **Fusion Personal Use** and **Bambu printers**, but supports other
FDM printers and their actual slicers. It assumes no particular integration,
computer, account, operating system or previous chat history.

## Get started

1. Download the skill ZIP from [Releases](https://github.com/AntlerForge/3DPrintDesign/releases/latest).
2. Extract it and place the complete `3dprintdesign` folder in your agent
   client's supported skills location. Keep its references together.
3. Invoke it and describe what you want to make:

```text
Use $3dprintdesign. Help me design a printable bracket in Fusion.
```

Installation locations and skill support depend on your client. If it does not
support skills, provide the entrypoint and relevant references as instructions.
The skill itself does not install Fusion, a slicer or computer-control software.

## What it covers

- An 18-route object-to-workflow atlas and readable dependency graph, covering
  brackets, walls, hollow/tapered bodies, relief, patterns, threads and complex forms.
- Fusion Personal Use's ten Editable-document slots, with recoverable Read-only
  transitions rather than deletion or project archiving.
- Editable saves, backups, assemblies, hardware fits, motion and clearance checks.
- Print orientation, strength, supports, calibrated fit coupons and multi-plate packs.
- Private hardware/fit records for reusing proven interfaces and planning tests
  for new sizes, without turning one printer's measurements into global defaults.
- Recoverable handoffs that keep native designs with their delivered print files
  in the user's chosen project location.
- Optional integration/computer-control setup, with permission and real output checks.
- Explicit `learn` cycles that review evidence and implement scoped improvements
  in a designated editable source while keeping private project history separate.

The [embedded README](3dprintdesign/README.md) has setup guidance, example prompts
and the full explanation of `learn`. [SKILL.md](3dprintdesign/SKILL.md) is the agent
entrypoint. Neither a slice nor an animation proves physical fit or strength;
starting a physical print requires explicit approval.

## Checks and limits

The package includes six optional Python standard-library maintainer tests for
links, graph consistency and invalid-case rejection. From the repository root,
with Python 3.9 or newer available:

```sh
python3 -B -m unittest discover -s 3dprintdesign/tests -v
```

Python is not required to use the skill instructions. Package checks do not
prove that a particular Fusion integration, slicer or printer works. See the
[source and validation notes](3dprintdesign/references/sources.md).

## Licence

[MIT](LICENSE). Linked third-party applications and documentation retain their
own terms. This is an independent community skill, not an Autodesk or Bambu Lab
product or endorsement.
