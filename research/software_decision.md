# Software decision record

Status: **provisional engineering decision; exact machine execution blocked pending hardware and current documentation.** Date2026-11-04.

The gift box uses one source geometry and one stable learning path: Inkscape1.4 for SVG inspection/edits and panel dimensions; a compatible supported LightBurn release for laser operations; FreeCAD1.0.0 for the flat-lid geometry and CNC engraving CAM. A machine-approved sender executes the CNC export. We do not describe the sender as CAD or add alternative toolchains inside individual chapters.

Why these applications: Inkscape is locally available and SVG-native (S26). FreeCAD is locally available, scriptable and has explicit CAM concepts (S06/S08–10/S19). Laser and spindle machines are technically separate even if one controller family can support both. Archived LightBurn primary documentation supports operation concepts but cannot verify current licensing, controllers, menu labels or OS support. That limitation is visible in chapters and release blockers.

The requested candidate Inkscape→OpenBuilds CAM→CONTROL is plausible for a verified GRBL setup (S21/S22). It is not chosen as the asserted complete route because we cannot validate the hosted CAM, the selected enclosed laser or manufacturer-approved mode switching. LaserGRBL's documented experimental SVG import (S11) is an avoidable uncertainty for multiple interlocking panels. Fusion adds unverified cost/eligibility assumptions. UGS remains an appropriate sender candidate only after actual-controller confirmation.

This is not a recommendation to buy LightBurn or a machine. No software was purchased and no account or trial was activated. The final release must record one supported LightBurn version, one machine and one controller firmware, verify Windows installation, collect authentic screenshots, perform export/import/preview tests and record any paid-license terms. Hardware choice may require revisiting this decision; existing geometry stays portable through SVG/DXF.

Official download references: https://inkscape.org/release/ ; https://www.freecad.org/downloads.php ; https://lightburnsoftware.com/ ; https://github.com/OpenBuilds/OpenBuilds-CONTROL/releases ; https://github.com/winder/Universal-G-Code-Sender/releases . The first three current web pages were not successfully inspected in this run; these are retrieval targets, not endorsements of an unverified latest version.
