# GitHub benchmark report

Date: 2026-11-05. Author of project: Amir Mobasheraghdam. Report language: English (book language: German).

## 1. Method and evidence limits (read first)

What was actually done in this session:

- Fetched, via `raw.githubusercontent.com`, the **root README** and the **root license file** of all 26 repositories in the brief.
- Read in full or in substantial part: CutCase `docs/architecture.md` and `docs/geometry-and-fabrication.md`; CardBoxGen `cardboxgen/fabrication.py` and README architecture section.
- Nothing was cloned or executed. No third-party code, figures, screenshots or assets were copied into this repository.

What could **not** be done (blocked, not skipped silently):

- `github.com` and `api.github.com` returned HTTP 403 from the session proxy (policy denial, not retried). Therefore **maintenance status, last release, open issues, test-suite contents, CI state and stars were NOT verified** for any repository. Every row below that says "not verified" means exactly that. Do not read absence as "unmaintained" or presence as "healthy".
- Wikis, GitHub Releases pages and sample images were not reachable. "Features verified" therefore means *stated in the README/docs I read*, i.e. an **advertised** capability, unless marked **READ-CODE** (I read implementing source).
- Nothing was run, so **no capability is "demonstrated"** in this report.
- Blender is not installed here and the private product geometry (`engineering/`, `figures/`, `cover/`) is intentionally absent from this public checkout (see `.gitignore`). Renders, cover concepts, per-figure prompts, rebuilt editions and walkthrough screenshots therefore were **not produced**. See `research/VISUAL_PIPELINE_STATUS.md`.

Licence column: taken from the licence file/README text I fetched. GPL/LGPL version numbers are given only where the text showed them. Licence ≠ legal advice; a human rights review is still required before any redistribution.

## 2. Summary table

| # | Repository | Licence (as read) | Action |
|---|---|---|---|
| A1 | florianfesti/boxes | GPL-3.0 (README: "GPL v3+") | ADAPT PRINCIPLE |
| A2 | wcchun1234/CutCase | MIT | ADAPT PRINCIPLE |
| A3 | wcchun1234/CardBoxGen | MIT | ADAPT PRINCIPLE |
| A4 | paulh-rnd/TabbedBoxMaker | GPL-2.0 (LICENSE text is v2) | STUDY |
| A5 | xxv/openscad-boxmaker | LGPL-2.1+ (README only; no LICENSE file at root) | STUDY |
| A6 | MIDILLI-Tech/visual-box-designer | Apache-2.0 | STUDY |
| B1 | Jack000/SVGnest | MIT | STUDY |
| B2 | Jack000/Deepnest | **No licence file at root; none in package.json** | REJECT (for redistribution/integration) |
| B3 | OpenBuilds/OpenBuilds-CAM | GPL (version not read) | STUDY |
| B4 | arkypita/LaserGRBL | GPL (version not read) | STUDY |
| C1 | FreeCAD/FreeCAD | LGPL (version not read) | USE AS EXTERNAL TOOL |
| C2 | FreeCAD/FreeCAD-documentation | CC0-1.0 (repo root) | STUDY |
| C3 | gnea/grbl | GPL-3.0 | STUDY |
| C4 | CauldronDevelopmentLLC/CAMotics | GPL-2.0+ | USE AS EXTERNAL TOOL (proposed, not yet run) |
| C5 | OpenBuilds/OpenBuilds-CONTROL | GPL (version not read) | STUDY |
| C6 | cncjs/cncjs | MIT | STUDY |
| C7 | vlachoudis/bCNC | GPL | STUDY |
| D1 | blender/blender | GPL (software); output/asset terms not verified | USE AS EXTERNAL TOOL (not installed here) |
| D2 | microsoft/playwright | Apache-2.0 | USE AS EXTERNAL TOOL |
| P1 | quarto-dev/quarto-cli | MIT | STUDY |
| P2 | jgm/pandoc | GPL (COPYING.md) | USE AS EXTERNAL TOOL (already used) |
| P3 | pagedjs/pagedjs | MIT | STUDY |
| P4 | w3c/epubcheck | BSD-style text (exact variant not confirmed) | USE AS EXTERNAL TOOL (already used) |
| P5 | daisy/ace | MIT | USE AS EXTERNAL TOOL (already attempted; blocked) |
| R1 | mhatalski/awesome-cnc | not checked (link list) | STUDY |
| R2 | ad-si/awesome-laser-cutting | not checked (link list) | STUDY |

Common to every row, fields 6 and 12 unless stated: **maintenance/release: not verified (API blocked)**.

## 3. Per-repository records

Field order: Purpose · Language/deps · Licence · Maintenance · Features (advertised unless READ-CODE) · Docs quality · Relevance · Visual value · Validation value · Limitations · Commercial/attribution · Action.

### A1 florianfesti/boxes — https://github.com/florianfesti/boxes
- Purpose: online box generator, Inkscape plug-in and Python library of parametrized generators.
- Language: Python 3; Sphinx docs.
- Licence: GPL-3.0 (README: "GPL v3+").
- Maintenance: not verified.
- Features (README): thickness-scaled finger joints incl. T-connections; `burn` parameter compensating laser kerf "up to the point where plywood can be press fitted"; dovetails; flex cuts; SVG/PS output (DXF/PLT/G-code only via external pstoedit).
- Docs: README plus Sphinx generator list (not read in full).
- Relevance: high for finger-joint scaling and burn/kerf terminology; hinge/flex boxes exist but our box is a lift-off lid design.
- Visual value: low (2D output; README images are the project's own).
- Validation value: medium — a second implementation to cross-check our finger counts and kerf convention by *independent reimplementation*, not code reuse.
- Limitations: no assembled 3D preview stated; G-code route is via an external converter (not endorsed for our use).
- Commercial/attribution: GPL-3. Copying code into our generator, or shipping derived code, imposes GPL obligations; do not reuse its sample images. Principles/ideas are not copyrightable but copying expression is.
- Action: **ADAPT PRINCIPLE.**

### A2 wcchun1234/CutCase — https://github.com/wcchun1234/CutCase
- Purpose: browser laser-cut box designer; "generates a rotatable Three.js assembly preview and a production SVG layout from the same geometry model" (README).
- Language: plain JavaScript/HTML/CSS; Three.js; npm; Node tests.
- Licence: MIT.
- Maintenance: not verified.
- Features: READ-CODE-level docs (architecture.md, geometry doc read in full): canonical *inside* dimensions with outside derived; named panels; complementary A/B finger patterns with **odd segment count** and centred remainder; kerf model with loose/standard/tight multipliers (0.65/1.0/1.35); separate lift-off lid (top plate + four inner lips, overhang and clearance parameters); explode slider; panel features cut/engrave/mark; validation embedded in SVG metadata; fit-test coupon export; `test.js` geometry/SVG invariants; `verify-ui.mjs` headless-browser visual checks incl. non-blank canvas and mobile viewport. (Test contents beyond what the docs describe: not read.)
- Docs: good — user guide, architecture, geometry notes, roadmap.
- Relevance: **highest**. Its key architecture — one geometry model → panel polygons in local 2D → each panel receives both a sheet-layout origin and a 3D placement basis — is exactly the single-source-of-truth principle the brief requires.
- Visual value: high as a concept (consistent exploded view); its rendered output is not photoreal.
- Validation value: high — invariant tests + UI smoke tests are a transferable pattern.
- Limitations: its kerf model is explicitly a "fast iteration control, not a full replacement for material calibration" (its own words); finger fit is physical-test dependent; lid is a simple lip-plus-plate design, ours has a locator.
- Commercial/attribution: MIT permits reuse with copyright notice retained; still prefer independent implementation. Do not copy its UI or wiki images.
- Action: **ADAPT PRINCIPLE.**

### A3 wcchun1234/CardBoxGen — https://github.com/wcchun1234/CardBoxGen
- Purpose: deterministic SVG generator for laser-cut trays/boxes; CLI plus Pyodide web app.
- Language: Python 3.9+; pytest-style tests (stated), Pyodide for web.
- Licence: MIT. README states version 0.8.1 (not independently checked against releases).
- Features: READ-CODE for `fabrication.py`: kerf defined unambiguously as **full width removed**, burn radius = kerf/2; explicit functions for final-vs-drawn tab width/slot width/depth (tab = drawn − kerf, slot = drawn + kerf); frozen dataclasses. README: parameter validation with *blocking* errors, `FingerPlan` mating edge pairs, deterministic non-overlapping sheet layout, `CUT/SCORE/ENGRAVE` layers, calibration coupon via `--calibration`, checked example SVGs, CI check that the web bundle matches package source, tests for "assembly edge pairing".
- Docs: good; wiki-ready sources.
- Relevance: high for the *validation vocabulary*: a stated kerf convention, mating-pair checks and calibration-first workflow.
- Visual value: low (SVG only). Validation value: **high**.
- Limitations: card-box focus; no 3D assembly view stated.
- Commercial/attribution: MIT; same independent-implementation preference.
- Action: **ADAPT PRINCIPLE.**

### A4 paulh-rnd/TabbedBoxMaker — https://github.com/paulh-rnd/TabbedBoxMaker
- Purpose: Inkscape extension for tab-jointed boxes, now also CLI.
- Language: Python; Inkscape. README v2.0 (21 Jun 2025) credits Elliot White (original), Paul Hutchison, Bert Huijben (CLI/testability refactor).
- Licence: GPL-2.0 (LICENSE text is version 2).
- Features (README): kerf-corrected tabs, press-fit dimples, dividers, dogbone corners for end mills, CLI without Inkscape, 11 stated test scenarios, CI on Ubuntu/Windows/macOS.
- Relevance: medium; dogbone corners are relevant to the CNC (not laser) side only.
- Limitations: README links CI to a different owner's fork — which repo is canonical is unverified.
- Commercial: GPL-2.0 — no code reuse in a product; ideas only.
- Action: **STUDY.**

### A5 xxv/openscad-boxmaker — https://github.com/xxv/openscad-boxmaker
- Purpose: OpenSCAD library; same box → 2D cut layout and 3D preview; easy-to-remove lid.
- Language: OpenSCAD.
- Licence: LGPL-2.1+ per README text; **no LICENSE file at repo root** was found.
- Relevance: confirms the 2D/3D-from-one-source idea; our project already has a native FreeCAD/STEP assembly from the same geometry (PROJECT_STATE), so no pipeline change is justified.
- Action: **STUDY.** Do not introduce OpenSCAD.

### A6 MIDILLI-Tech/visual-box-designer — https://github.com/MIDILLI-Tech/visual-box-designer
- Purpose: browser 2D/3D box designer with holes, cutouts, text labels; JSON export to the vendor's own tools.
- Licence: Apache-2.0. README version badge 1.0.8.
- Relevance: medium for text-placement UX; it is not a finger-joint/kerf-first tool in its README (export feeds vendor tools).
- Limitations: ecosystem tied to the vendor's other tools.
- Action: **STUDY.** Not adopted.

### B1 Jack000/SVGnest — https://github.com/Jack000/SVGnest
- Purpose: browser SVG nesting. Licence MIT. Relevance: low — our seven panels fit one sheet and layout is governed by grain direction, spacing and hold-down, not density. Validation value: its collision/spacing concept could inform an overlap check, but our independent solids check already exists.
- Action: **STUDY.**

### B2 Jack000/Deepnest — https://github.com/Jack000/Deepnest
- Purpose: desktop nesting app built on SVGnest; C engine, DXF via conversion, common-line merging (README).
- Licence: **no licence file at root and none in `package.json`** (read: name, version 1.0.5, author only). Without a licence, default copyright applies.
- Action: **REJECT** for integration/redistribution. Nesting is not needed for this single-box project.

### B3 OpenBuilds/OpenBuilds-CAM — https://github.com/OpenBuilds/OpenBuilds-CAM
- Purpose: cloud/web CAM converting DXF/SVG/bitmap/Gerber to G-code. Licence GPL.
- Verified: README lists those input types only; capabilities (e.g. multi-panel SVG, laser vs spindle output) not tested.
- Relevance: already assessed in `research/software_decision.md` as plausible for a verified GRBL setup but not asserted.
- Action: **STUDY** until tested against a real machine configuration.

### B4 arkypita/LaserGRBL — https://github.com/arkypita/LaserGRBL
- Purpose: Windows GUI for GRBL lasers. Licence GPL.
- README states plainly: "Vector file import (svg only) **[Experimental]**"; requires S-word laser power modulation; compatible with Grbl v0.9/v1.1; Windows only.
- Action: **STUDY.** Not recommended as primary — consistent with the existing project decision.

### C1/C2 FreeCAD & FreeCAD-documentation
- FreeCAD: LGPL (root file). Local version recorded in README: 1.0.0. Already used in this project for the native assembly and virtual CAM operation.
- Documentation repo: root licence CC0; the official wiki's own licence was not checked here.
- Gap: menu/command names were **not** re-verified in this session; keep verifying against the installed 1.0.0 at screenshot time.
- Actions: C1 **USE AS EXTERNAL TOOL**; C2 **STUDY**.

### C3 gnea/grbl — https://github.com/gnea/grbl
- Purpose: Arduino 328p CNC firmware. Licence GPL-3.0. README: macros/variables/most canned cycles unsupported. Laser mode is a firmware setting documented on the wiki (not reachable here) — I do **not** state a `$32` value from memory in the book.
- Action: **STUDY.** Machine-specific; no universal program.

### C4 CauldronDevelopmentLLC/CAMotics
- Purpose: open-source **3-axis machining simulation** (README). Licence GPL-2.0+. Relevance: an independent check that the lid-engraving G-code removes material where intended, complementing the existing FreeCAD native simulation. It does not simulate a laser.
- Not yet done: nothing was run; the engraving G-code is private/absent here.
- Action: **USE AS EXTERNAL TOOL (proposed validation step).**

### C5/C6/C7 Controllers
- OpenBuilds-CONTROL (GPL; Grbl host), cncjs (MIT; web UI for Grbl/Marlin/Smoothieware/TinyG/g2core), bCNC (GPL; Python sender for grblHAL/GRBL; README warns macOS release may be broken).
- Rule from the brief: one sender in the book, chosen by the real machine. Current decision stays provisional (`research/software_decision.md`). No change.
- Action: all **STUDY**.

### D1 blender/blender
- GPL software. Not installed in this environment; not tested. Whether a CAD→Blender route (STEP→mesh, then materials) preserves exact joint geometry has not been shown. Licensing of any bundled assets/add-ons and of renders must be confirmed from blender.org by a human.
- Action: **USE AS EXTERNAL TOOL** — plan only; see `research/VISUAL_PIPELINE_STATUS.md`.

### D2 microsoft/playwright
- Apache-2.0. Valid for browser-hosted software only (e.g. a web CAM). It cannot capture native FreeCAD/Inkscape windows; use OS screenshot tools there. Used already by `scripts/check_browser.cjs` per repo contents.
- Action: **USE AS EXTERNAL TOOL.**

### P1–P5 Publishing
- Quarto (MIT), Pandoc (GPL; already used), Paged.js (MIT), EPUBCheck (BSD-style; already used, 0 errors recorded), Ace (MIT; blocked by managed-browser `file://` policy per PROJECT_STATE).
- No concrete weakness of the working WeasyPrint/Pandoc pipeline has been demonstrated by this research, so **nothing is replaced**. Paged.js is the only candidate worth a trial if WeasyPrint cannot achieve full-page cover and chapter-opening layouts; that is a hypothesis, not a finding.
- Actions: Quarto **STUDY**; Pandoc, EPUBCheck, Ace **USE AS EXTERNAL TOOL**; Paged.js **STUDY**.

### R1/R2 Awesome lists
- Link directories; not authoritative. Not followed to original sources in this session (needs the blocked hosts). Teaching-pattern analysis is therefore **pending**.
- Action: **STUDY.**

## 4. Engineering patterns adopted into the project plan

| Pattern | Source | Status in this project |
|---|---|---|
| One canonical parametric model; derive 2D layout, 3D assembly and dimensions from it | CutCase architecture | Already the project's design (native FreeCAD/STEP + SVG/DXF from one generator, per PROJECT_STATE). Re-confirmed; not re-verified here (files absent). |
| State the kerf convention explicitly (full width vs half) and give drawn→final formulas | CardBoxGen | **Recommend** documenting in `research/TECHNICAL_NOTES.md`; not yet applied to private generator. |
| Odd segment count / complementary A-B edges so mating edges match | CutCase | Check against private generator when available. |
| Blocking validation vs warnings; embed validation in exported metadata | CardBoxGen, CutCase | Proposed. |
| Calibration/fit coupon before any full cut | CardBoxGen, CutCase, Boxes.py | Already present (coupons); physical fit still untested. |
| Digital check ≠ physical fit | CutCase docs | Already stated in README. |
| UI smoke/visual checks with non-blank and mobile assertions | CutCase `verify-ui.mjs` | Existing `check_browser.cjs`; could add rendered-page non-blank/clipping assertions. |

"Adopted" above means *recommended and recorded*; I did not change the private generator.

## 5. Rights summary for a commercial book

- Copyleft (GPL/LGPL: Boxes.py, TabbedBoxMaker, openscad-boxmaker, OpenBuilds-CAM/-CONTROL, LaserGRBL, grbl, CAMotics, bCNC, FreeCAD, Blender, Pandoc): no source or bundled-asset reuse in the book's generator or distributed files without legal review. Using them as tools does not by itself put the book under their licence, but verify per tool.
- Permissive (MIT/Apache: CutCase, CardBoxGen, SVGnest, cncjs, visual-box-designer, Playwright, Quarto, Paged.js, Ace): reuse permitted with notice retention; still prefer original implementation and original images.
- Unlicensed: Deepnest (as fetched) — do not reuse.
- No third-party screenshots, sample photos or UI artwork may be included. All book figures must be self-produced.
- Third-party sample images in READMEs were not downloaded.
