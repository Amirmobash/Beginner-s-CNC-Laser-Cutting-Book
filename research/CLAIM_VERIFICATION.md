# Claim-to-source verification

Only the following bounded findings have documentary support; a source-code read is not a validated end-user workflow.

| Source | Claim | Chapters | Scope |
|---|---|---|---|
| S01 | GRBL 1.1 lists G0/G1, G20/G21, G90/G91, G54–G59 and M3/M4/M5; laser mode gives M4 dynamic power behavior. | 4, 6, 8 | high for documented GRBL1.1; not all derivatives |
| S02 | Homing order and safety-door support are firmware configuration dependent. | 4, 8 | high for reference source; not target-machine wiring |
| S03 | Parser distinguishes units, G94 feed, spindle commands and laser mode; G90.1 is unsupported. | 4, 8 | high for reference parser only |
| S04 | Feed hold, door suspension and operating states have distinct handling. No safety-rated hardware guarantee follows. | 1, 6, 8 | high for software; hardware safety unverified |
| S06 | FreeCAD advertises Windows/macOS/Linux and Python API; desktop CAD role. | 3, 5, 8 | high for general project description |
| S07 | Repository root license text is LGPL2.1; reuse and redistribution obligations differ from original design outputs. | 3, appendix | high for this notice; package components need separate review |
| S08 | FreeCAD development branch contains a GRBL postprocessor; metric initialization and pre/postamble are configurable. | 8 | high for retrieved branch; NOT menu proof for installed1.0.0 |
| S09 | ShapeString uses a font file, size and tracking properties. | 8 | high for code; font-specific engraving quality unverified |
| S10 | FreeCAD development source contains CAM Engrave operation; it is distinct from plain text creation. | 8 | high for source; no hardware/toolpath execution asserted |
| S11 | LaserGRBL is a Windows GRBL laser GUI; SVG vector import is explicitly experimental. Minimal Z control is listed as missing. | 3, 6 | high for README; current release not launched |
| S12 | EPUBCheck is the official EPUB conformance checker; source README identifies v5.4.0 as production-ready. | appendix, publishing | high for retrieved README; installed execution separately reported |
| S13 | Ace automates only a limited portion of EPUB accessibility evaluation and requires human review. | appendix, publishing | high; not a legal compliance certificate |
| S14 | Pandoc supports DOCX and EPUB3 outputs and resource-path handling. | appendix | high; project pins installed3.1.11.1, main manual may differ |
| S15 | EPUB Accessibility defines discovery metadata and whole-publication conformance; text alternatives and human evaluation matter. | appendix, publishing | high for W3C working source; no BFSG determination |
| S18 | Reference GRBL homing and hard-limit functions depend on switches and configuration. | 4, 8 | high for reference source; no machine equivalence |
| S19 | FreeCAD CAM Job manages model, stock and postprocessor separately. | 8 | high for retrieved development source |
| S20 | FreeCAD simulator models tool/material movement; voxel simulation has representational limitations including tilted cuts. | 8 | high for code; does not certify fixtures/real material |
| S21 | OpenBuilds CAM describes DXF/SVG/bitmap/Gerber-to-G-code conversion. | 3 | high for role; not tested controller/enclosure compatibility |
| S22 | OpenBuilds CONTROL is a GRBL host/interface; its build matrix names Windows/Linux/Mac. | 3, 8 | high for role; release and machine not tested |
| S23 | UGS describes cross-platform Java G-code sender and GRBL/TinyG/g2core/Smoothieware compatibility; stable Windows download is offered. | 3, 8 | high for role; target controller untested |
| S24 | Official archived LightBurn documentation explicitly redirects to a newer documentation site. | 3, 6 | high; signals archival/currency limitation |
| S26 | Inkscape describes native SVG, open-source vector design and Windows/macOS/Linux. | 3, 5 | high for general capabilities |
| S27 | Archived LightBurn docs support SVG/DXF import and warn to convert text objects into paths; import limitations exist. | 5, 6 | medium for current product: archived documentation |
| S28 | Archived LightBurn docs distinguish Line and Fill operations, output enable, speed units and closed-shape kerf offset. | 6 | medium for current product: do not reproduce old default values |
| S29 | Archived LightBurn docs distinguish absolute coordinates, current position and user origin. | 4, 6 | medium for current product; device-specific origin still required |
| S30 | Archived LightBurn license page discusses trial, perpetual-version use and paid updates; its old USD prices are obsolete evidence, not current quotes. | 3 | low for current terms; historical only |
| S31 | Current Inkscape source notice distinguishes mostly GPL2+ source from binaries covered by GPL3+ due to components. | 3, publishing | high for retrieved notice; use does not force original artwork GPL |

## Unverified release-blocking claims

- Exact machine compatibility, approved enclosure, laser classification, cutting3mm plywood, EU prices and accessory totals.
- Current LightBurn version, German UI menus, license package and Windows installation.
- Current Fusion terms, German tutorial counts and all exact vendor offers.
- Current BoD/KDP/tolino rules and BFSG applicability.
- Real finger-joint fit, kerf, adhesive compatibility and safe CNC engraving parameters.

Do not turn any of these into categorical purchase or manufacturing recommendations.
