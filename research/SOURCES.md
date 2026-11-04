# Source register

Access date: 2026-11-04. This is a review of retrievable primary documents, not proof of physical machining or current commercial offers. 27 sources were retrieved and relevant passages reviewed. Each independent file is counted once; archived documents and development code have explicit scope limits. Failed URLs are not counted. Full local evidence is excluded from publication and Git.

## S01 — GRBL: unterstützte Befehle

Publisher: gnea/grbl. URL: https://raw.githubusercontent.com/gnea/grbl/master/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: GRBL 1.1 lists G0/G1, G20/G21, G90/G91, G54–G59 and M3/M4/M5; laser mode gives M4 dynamic power behavior.

Used in chapters: 4, 6, 8. Locator: README lines 37–39, 64–78. Confidence/scope: high for documented GRBL1.1; not all derivatives. SHA-256: `fa761cbcc98c908f19a6e762b4f3dc64b7b4c0caed9624b258f954d6e786a9d8`.

## S02 — GRBL: Konfiguration

Publisher: gnea/grbl. URL: https://raw.githubusercontent.com/gnea/grbl/master/grbl/config.h

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Homing order and safety-door support are firmware configuration dependent.

Used in chapters: 4, 8. Locator: config.h CMD_SAFETY_DOOR and HOMING_CYCLE definitions. Confidence/scope: high for reference source; not target-machine wiring. SHA-256: `ff904e8607c27cf7908fa398fa185f764e82f6b5056fae770617aebb2875b6de`.

## S03 — GRBL: G-Code-Parser

Publisher: gnea/grbl. URL: https://raw.githubusercontent.com/gnea/grbl/master/grbl/gcode.c

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Parser distinguishes units, G94 feed, spindle commands and laser mode; G90.1 is unsupported.

Used in chapters: 4, 8. Locator: gcode.c lines 190, 201, 258–260, 389–419. Confidence/scope: high for reference parser only. SHA-256: `4e63c9f837cc2a79746e45eb2ec6f69beed083cdcbceb5a06bc72d3dfe6f36b8`.

## S04 — GRBL: Zustände und Sicherheitstür

Publisher: gnea/grbl. URL: https://raw.githubusercontent.com/gnea/grbl/master/grbl/protocol.c

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Feed hold, door suspension and operating states have distinct handling. No safety-rated hardware guarantee follows.

Used in chapters: 1, 6, 8. Locator: protocol.c safety-door and suspend state branches. Confidence/scope: high for software; hardware safety unverified. SHA-256: `7ccc5c1afe51c36272ad759e883cfa38d25975d182670fcedbf765a01291208d`.

## S05 — Inkscape: Lizenz

Publisher: inkscape/inkscape. URL: https://raw.githubusercontent.com/inkscape/inkscape/master/COPYING

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **nicht abgerufen**.

Failure: HTTP Error 404: Not Found. No manuscript claim may rely on this failed retrieval.

## S06 — FreeCAD: Projekt und Funktionen

Publisher: FreeCAD/FreeCAD. URL: https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: FreeCAD advertises Windows/macOS/Linux and Python API; desktop CAD role.

Used in chapters: 3, 5, 8. Locator: README Cross platform / Python sections. Confidence/scope: high for general project description. SHA-256: `2de839c26b7343be697550809a5834ea1177edbd1490dd0dec302ec9b8b42372`.

## S07 — FreeCAD: Lizenz

Publisher: FreeCAD/FreeCAD. URL: https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/LICENSE

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Repository root license text is LGPL2.1; reuse and redistribution obligations differ from original design outputs.

Used in chapters: 3, appendix. Locator: LICENSE preamble and terms. Confidence/scope: high for this notice; package components need separate review. SHA-256: `7ffe1954587c77dfba1cf8eb9b2ea743671fa6e63f9e7a2f258119d42e14eefe`.

## S08 — FreeCAD: GRBL-Postprozessor

Publisher: FreeCAD/FreeCAD. URL: https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/src/Mod/CAM/Path/Post/scripts/grbl_post.py

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: FreeCAD development branch contains a GRBL postprocessor; metric initialization and pre/postamble are configurable.

Used in chapters: 8. Locator: Grbl PostProcessor class / init_values. Confidence/scope: high for retrieved branch; NOT menu proof for installed1.0.0. SHA-256: `2f440a1051de3be9d73af72de28156a5a21e6295ff06b5feeb36d32b3ae99253`.

## S09 — FreeCAD: ShapeString

Publisher: FreeCAD/FreeCAD. URL: https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/src/Mod/Draft/draftobjects/shapestring.py

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: ShapeString uses a font file, size and tracking properties.

Used in chapters: 8. Locator: FontFile, Size and Tracking properties. Confidence/scope: high for code; font-specific engraving quality unverified. SHA-256: `01b7fecb7f007f3e8f54baf54b91215303ba8056f61a3e1a60ac1f86f95c182c`.

## S10 — FreeCAD: Gravur

Publisher: FreeCAD/FreeCAD. URL: https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/src/Mod/CAM/Path/Op/Engrave.py

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: FreeCAD development source contains CAM Engrave operation; it is distinct from plain text creation.

Used in chapters: 8. Locator: ObjectEngrave / Create. Confidence/scope: high for source; no hardware/toolpath execution asserted. SHA-256: `6487930c5af5f2eb3589536f04a5948be272d309b14bca4ec173d346da5dd7a7`.

## S11 — LaserGRBL: Windows und GRBL

Publisher: arkypita/LaserGRBL. URL: https://raw.githubusercontent.com/arkypita/LaserGRBL/master/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: LaserGRBL is a Windows GRBL laser GUI; SVG vector import is explicitly experimental. Minimal Z control is listed as missing.

Used in chapters: 3, 6. Locator: README introduction / Existing Features / Missing Features. Confidence/scope: high for README; current release not launched. SHA-256: `250a824105c97400a2fdb735ef43431357dcf74b147316077b4951a43ea1230e`.

## S12 — EPUBCheck: Validierung

Publisher: w3c/epubcheck. URL: https://raw.githubusercontent.com/w3c/epubcheck/main/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: EPUBCheck is the official EPUB conformance checker; source README identifies v5.4.0 as production-ready.

Used in chapters: appendix, publishing. Locator: README introduction / latest release section. Confidence/scope: high for retrieved README; installed execution separately reported. SHA-256: `a9c67e0c86d5bb96a3e51ef298647d29f4200790fa656dda183e3f03300a7a66`.

## S13 — Ace: Accessibility Checker

Publisher: daisy/ace. URL: https://raw.githubusercontent.com/daisy/ace/master/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Ace automates only a limited portion of EPUB accessibility evaluation and requires human review.

Used in chapters: appendix, publishing. Locator: README lines 11–19. Confidence/scope: high; not a legal compliance certificate. SHA-256: `b0f50d0b64f8bef271837cb2197919ea87aa30371db037053eb99db5f03b8291`.

## S14 — Pandoc: Benutzerhandbuch

Publisher: jgm/pandoc. URL: https://raw.githubusercontent.com/jgm/pandoc/main/MANUAL.txt

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Pandoc supports DOCX and EPUB3 outputs and resource-path handling.

Used in chapters: appendix. Locator: MANUAL output formats / resource-path / epub options. Confidence/scope: high; project pins installed3.1.11.1, main manual may differ. SHA-256: `f70736d1c3bf691ab3e3e7f104eb6b941cf7a9eaea32e49c138c0f9c54962218`.

## S15 — EPUB Accessibility

Publisher: w3c/epub-specs. URL: https://raw.githubusercontent.com/w3c/epub-specs/main/epub33/a11y/index.html

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: EPUB Accessibility defines discovery metadata and whole-publication conformance; text alternatives and human evaluation matter.

Used in chapters: appendix, publishing. Locator: accessibilityFeature, accessibilitySummary, accessModeSufficient, conformance sections. Confidence/scope: high for W3C working source; no BFSG determination. SHA-256: `727b76ce6592da75f6bd4d7d4a41d58357dec6fd1323ae5fc6d7a37caef48710`.

## S16 — EPUB 3.3: Inhaltsdokumente

Publisher: w3c/epub-specs. URL: https://raw.githubusercontent.com/w3c/epub-specs/main/epub33/core/epub-contentdocs.html

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **nicht abgerufen**.

Failure: HTTP Error 404: Not Found. No manuscript claim may rely on this failed retrieval.

## S17 — EPUB 3.3: Pakete

Publisher: w3c/epub-specs. URL: https://raw.githubusercontent.com/w3c/epub-specs/main/epub33/core/epub-packages.html

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **nicht abgerufen**.

Failure: HTTP Error 404: Not Found. No manuscript claim may rely on this failed retrieval.

## S18 — GRBL: Begrenzungen und Homing

Publisher: gnea/grbl. URL: https://raw.githubusercontent.com/gnea/grbl/master/grbl/limits.c

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Reference GRBL homing and hard-limit functions depend on switches and configuration.

Used in chapters: 4, 8. Locator: limits.c homing and hard-limit sections. Confidence/scope: high for reference source; no machine equivalence. SHA-256: `d7ac3620641a61ebb5d72a1f608389407c448f4eca1521b4535f6dcacf97f24e`.

## S19 — FreeCAD: Auftrag

Publisher: FreeCAD/FreeCAD. URL: https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/src/Mod/CAM/Path/Main/Job.py

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: FreeCAD CAM Job manages model, stock and postprocessor separately.

Used in chapters: 8. Locator: Stock / Model / PostProcessor properties. Confidence/scope: high for retrieved development source. SHA-256: `7f0acfe379ab9013fe9afafde0ba9e0adf2c48e8a542bd072e60c05ba670ed2e`.

## S20 — FreeCAD: Simulation

Publisher: FreeCAD/FreeCAD. URL: https://raw.githubusercontent.com/FreeCAD/FreeCAD/main/src/Mod/CAM/Path/Main/Gui/Simulator.py

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: FreeCAD simulator models tool/material movement; voxel simulation has representational limitations including tilted cuts.

Used in chapters: 8. Locator: Simulator.py lines 191–198. Confidence/scope: high for code; does not certify fixtures/real material. SHA-256: `1ffa15983659ba34f45c9ae650fc6d24828858f15e377ac2b62941e5f9a54515`.

## S21 — OpenBuilds CAM

Publisher: OpenBuilds/OpenBuilds-CAM. URL: https://raw.githubusercontent.com/OpenBuilds/OpenBuilds-CAM/master/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: OpenBuilds CAM describes DXF/SVG/bitmap/Gerber-to-G-code conversion.

Used in chapters: 3. Locator: complete short README. Confidence/scope: high for role; not tested controller/enclosure compatibility. SHA-256: `2d2d71542f20de0370c72270249415663b3b2c729702120db5b2efba8ddff239`.

## S22 — OpenBuilds CONTROL

Publisher: OpenBuilds/OpenBuilds-CONTROL. URL: https://raw.githubusercontent.com/OpenBuilds/OpenBuilds-CONTROL/master/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: OpenBuilds CONTROL is a GRBL host/interface; its build matrix names Windows/Linux/Mac.

Used in chapters: 3, 8. Locator: README title / build section. Confidence/scope: high for role; release and machine not tested. SHA-256: `aaaa8e8223958a681286d232279a0adfaf6d9530af6aa8814e59fe9207a2fb48`.

## S23 — Universal Gcode Sender

Publisher: winder/Universal-G-Code-Sender. URL: https://raw.githubusercontent.com/winder/Universal-G-Code-Sender/master/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: UGS describes cross-platform Java G-code sender and GRBL/TinyG/g2core/Smoothieware compatibility; stable Windows download is offered.

Used in chapters: 3, 8. Locator: README opening / download table. Confidence/scope: high for role; target controller untested. SHA-256: `027dd3b9cd54f56e9219f7cb1c2c7dee6a05bff00559cb946081d8892a4a43c5`.

## S24 — LightBurn documentation repository

Publisher: LightBurnSoftware/Documentation. URL: https://raw.githubusercontent.com/LightBurnSoftware/Documentation/master/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Official archived LightBurn documentation explicitly redirects to a newer documentation site.

Used in chapters: 3, 6. Locator: README first lines. Confidence/scope: high; signals archival/currency limitation. SHA-256: `fde26c71b092d2fec5902f1959f637ecbc2e5e2195b9987ff1c1e77689f4c310`.

## S25 — LightBurn documentation repository

Publisher: LightBurnSoftware/Documentation. URL: https://raw.githubusercontent.com/LightBurnSoftware/Documentation/main/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **unavailable**.

Failure: HTTP Error 404: Not Found. No manuscript claim may rely on this failed retrieval.

## S26 — Inkscape documentation

Publisher: inkscape/inkscape. URL: https://raw.githubusercontent.com/inkscape/inkscape/master/README.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Inkscape describes native SVG, open-source vector design and Windows/macOS/Linux.

Used in chapters: 3, 5. Locator: README introduction. Confidence/scope: high for general capabilities. SHA-256: `47cfdf57931603431f1f94f54a0c03fac140dafb4c5aeb5ee618e4422fe417fc`.

## S27 — LightBurn archived vector import

Publisher: LightBurnSoftware. URL: https://raw.githubusercontent.com/LightBurnSoftware/Documentation/master/ImportingExternalVectors.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Archived LightBurn docs support SVG/DXF import and warn to convert text objects into paths; import limitations exist.

Used in chapters: 5, 6. Locator: Importing External Vectors. Confidence/scope: medium for current product: archived documentation. SHA-256: `a80c1aecf399659a24994db323a33dec1513de8b81c04a9fd6464dd47f858667`.

## S28 — LightBurn archived operations

Publisher: LightBurnSoftware. URL: https://raw.githubusercontent.com/LightBurnSoftware/Documentation/master/Operations.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Archived LightBurn docs distinguish Line and Fill operations, output enable, speed units and closed-shape kerf offset.

Used in chapters: 6. Locator: Operations headings Output / Speed / Line / Fill / kerf offset. Confidence/scope: medium for current product: do not reproduce old default values. SHA-256: `a76b39077182287af97d8e0f7a3d66285aee4947ccef73c577a88b250ad20f6e`.

## S29 — LightBurn archived origins

Publisher: LightBurnSoftware. URL: https://raw.githubusercontent.com/LightBurnSoftware/Documentation/master/CoordinatesOrigin.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Archived LightBurn docs distinguish absolute coordinates, current position and user origin.

Used in chapters: 4, 6. Locator: Coordinates and Job Origin headings. Confidence/scope: medium for current product; device-specific origin still required. SHA-256: `019a1f103c884958588234f46b1ff9553d79c5476f593eb1c3ebac836252b1ef`.

## S30 — LightBurn archived licensing

Publisher: LightBurnSoftware. URL: https://raw.githubusercontent.com/LightBurnSoftware/Documentation/master/Licensing.md

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Archived LightBurn license page discusses trial, perpetual-version use and paid updates; its old USD prices are obsolete evidence, not current quotes.

Used in chapters: 3. Locator: Licensing / Pricing. Confidence/scope: low for current terms; historical only. SHA-256: `fa132756fd487f72cf505de1221333aa903d7970294e67544b1f7ed183c0b709`.

## S31 — Inkscape GPL notice (GitLab)

Publisher: gitlab.com. URL: https://gitlab.com/inkscape/inkscape/-/raw/master/COPYING

Accessed: 2026-11-04. Revision: not stated in retrieved file; branch snapshot identified by SHA-256, not immutable Git commit. Status: **retrieved and relevant passages reviewed**.

Finding: Current Inkscape source notice distinguishes mostly GPL2+ source from binaries covered by GPL3+ due to components.

Used in chapters: 3, publishing. Locator: COPYING license introduction. Confidence/scope: high for retrieved notice; use does not force original artwork GPL. SHA-256: `6dade9d083ebec650d74dcfcdd93e9646214113eb1ecd1e8a9c3bf2dad91481e`.
