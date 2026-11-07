# Independent technical and project-continuity review

Review date: 2026-11-04. Scope: all nine chapter sources, appendix, `engineering/spec.json`, exported panel SVGs, presence of associated DXF/PDF drawings, and retained nominal-geometry results. This review is AI-assisted desk review. It is **not** an independent professional certification, human authorship approval, or physical manufacturing test.

## Conclusion

The manuscript now follows one gift-box project from product idea through material, digital design, laser cutting, assembly, detached-lid CNC engraving and final inspection. The old two-nameplate project does not survive in the reviewed chapter text. Part identifiers, nominal dimensions and the decision to engrave L0 flat before bonding L1 are consistent. The project is suitable for continued editorial and engineering development. It is **not ready for unsupervised manufacturing or commercial release**.

Exact machine selection, current manufacturer capability/safety documentation, current laser-software version, CNC sender, real CAM export, practical workholding, cutting parameters, adhesive performance, physical prototype, beginner test and substantial human author revision remain unresolved. The book identifies these limits rather than supplying unsupported settings.

## Evidence categories

- **Research-supported:** a specific source supports a limited factual statement. Development-branch source code does not prove identical installed-version UI behaviour.
- **Software-verified:** a named program/version actually performed a recorded operation. Binary availability or readable source is not an end-to-end tutorial test.
- **Digitally validated:** geometry or file assertions passed for the stated model. No real process capability follows from this.
- **Human-tested:** a named person performed a recorded procedure on identified hardware/material. No such test exists in this production run.
- **Draft instruction:** a reasoned workflow requiring the above additional checks. This is the status of physical procedures throughout the manuscript.

## Chapter status

| Chapter | Research-supported information | Software verification | Digital validation / continuity | Human-tested machining or beginner trial |
| --- | --- | --- | --- | --- |
| 1: Product and roadmap | CAD/CAM/controller roles use S06/S08/S19; local safety specifics still require authoritative site review | No machine operation; conceptual diagrams | Same seven-part box; L0 flat before L1 glue; stated160×120×70 mm | NOT PERFORMED |
| 2: Material and equipment | Material and process assumptions explicit; exact product specifications/prices remain unverified | No material or hardware test | Thickness3 mm is explicitly assumed;154×114 mm nominal interior and64 mm walls agree | NOT PERFORMED |
| 3: Software setup | Project source evidence supports separate design/CAM/sender roles | Inkscape1.4/FreeCAD1.0.0 are available locally; complete Windows install/click sequence and LightBurn are unverified | Folder/revision discipline supports one project | NOT PERFORMED |
| 4: G-code | S01/S03/S02/S18 support selected GRBL1.1 concepts | Paper/virtual example; not a live controller parser acceptance test | L-path arithmetic correct; units/origins explicit; examples deliberately not complete programs | NOT PERFORMED |
| 5: Box design | Derived from original project specification; kerf must be measured | Native FreeCAD/OpenCascade model results recorded separately; no laser software test | Seven exported panel polygons match spec; corner complement and dimensions digitally checked | NOT PERFORMED |
| 6: Laser job | Operation concepts and process limits identified; device-specific manual still missing | LightBurn version/import/preview not actually tested; instructions explicitly conditional | Nominal cutting geometry exists; no compensated production job or universal laser code | NOT PERFORMED |
| 7: Assembly | Original engineering sequence; adhesive and local safety guidance still require product-specific sources | Not applicable as a software test | Parts and dimensions match; base glues beneath walls; L0 and L1 remain separate for CNC | NOT PERFORMED |
| 8: CNC engraving | S01/S08/S09/S10/S19/S20 support limited controller/FreeCAD concepts; source/installed UI distinction explicit | Actual installed FreeCAD1.0.0 ShapeString and CAM Engrave study generated131 path commands; native voxel simulation exercised; no machine-ready export tested | Engraving zone and detached lid agree; depth and cut parameters intentionally unset | NOT PERFORMED |
| 9: Inspection and iteration | Diagnostic possibilities distinguished from proven causes | No physical result or measurement claimed | Sketch-to-finished-box continuity retained; generated visualisations identified honestly | NOT PERFORMED |

All practical chapters remain draft procedures awaiting competent supervised verification on a specific installation. “Research-supported” is not a blanket statement that every safety sentence has a fully current jurisdiction-specific citation.

## Independent checks executed during this review

A separate Python read-only assertion run completed with exit0. It checked:

1. All seven actual exported panel SVG polygon coordinates agree with the panel coordinates in `spec.json` within export rounding.
2. Each panel has SVG, DXF and PDF files:21 named per-panel assets present.
3. SVG dimensions explicitly use millimetres.
4. `actual_measured_thickness_mm`, `kerf_mm` and engraving `depth_mm` remain null; geometry is uncompensated.
5. Overall dimensions are160×120×70 mm;3+64+3=70 mm; nominal interior154×114 mm; L1 produces0.3 mm geometric clearance per side.
6. The engraving zone is `[20,25,140,95]`, i.e.120×70 mm, within L0.
7. All nine chapter sources contain over1000 whitespace-delimited words, headings and existing instructional image references. This checks substantive source presence, not literary quality.
8. The33 image references in the nine chapters resolve to files. Existing images were not all visually inspected in this particular desk-review pass; layout/image review is separate.
9. The old120×80/100×60 mm nameplate projects and former “MEINE WERKSTATT” sample do not remain in these chapters.

Retained engineering results inspected, not represented as physical evidence:

- `engineering/validation/geometry_results.json`:71 nominal assertions passed, including exported-polygon cross-sections, complementary corner ownership and layout separation.
- `engineering/validation/freecad_results.json`:7 valid solids;21 pairwise intersections with zero volume;160×120×70 mm assembled bounding box; total volume272602.68 mm³ within numerical precision.
- Nominal BRep wall/base contact areas sum to1644 mm². This is geometric contact, **not** bond strength or a load rating.

## Specific dimensional and process findings

- B0 and L0 are160×120 mm; wall ring extends from z3 to67 mm; L0 occupies z67..70 mm.
- F0/R0 have nine complementary vertical bands and a160×64 mm maximum outline; S0/S1 have120×64 mm maximum outlines. Band height64/9 mm is not rounded in the source geometry.
- L1 is153.4×113.4×3 mm, centred beneath L0 and inside a154×114 mm nominal opening. Available height beneath L1 is61 mm locally, versus64 mm to L0 outside that plate. Contents must respect that intrusion.
- Nominal exact-touch fingers are not a released real fit. Kerf, actual thickness, adhesive allowance and heat damage need coupon evidence. The comb alone does not qualify the entire corner joint.
- Base and locator are glued rather than mechanically retained in slots. Adhesive and plywood edge condition are essential validation subjects.
- A160×120 mm part requires additional usable space for actual workholding. The350×362 mm nesting file is stock planning, not a universally executable full-bed job.
- The120×70 mm text zone reserves design space only. It does not model clamps, tool holder or extraction shoe.
- A3-mm plywood lid has limited material reserve and may flex. No engraving depth, spindle speed, feed or laser setting is released.
- Physical lid removal/grip comfort must be tested: L0 is flush in plan with the walls and this revision has no dedicated handle. A render cannot prove convenient opening.

## Editorial findings and remaining corrections

- A minor folder-naming inconsistency between chapter1.6 and chapter3.4 was corrected to the canonical numbered folder names; it does not affect engineering geometry.
- Chapter7–9 and appendix identifiers, dimensions and existing per-panel file paths were checked. No conflicting machine-ready code or numerical cut-depth recommendation was found, so no technical correction to these dimensions was required.
- Windows-specific authentic screenshots and exact verified UI operations are still missing. Diagrams must not be represented as screenshots.
- Laser operation software and CNC sender remain conditional, not a fully chosen and tested production ecosystem. A final book must close that gap rather than treating an unspecified “manufacturer sender” as a complete beginner instruction.
- The local virtual lettering/CAM study now exists in the former virtual study file (lost with the original production run; superseded on 2026-11-07 by a Python-based verification of the new sample engraving, see book_team/ENGINEERING_SPEC.md), with recorded endpoint checks and native material-removal simulation. Its hypothetical inputs are not manufacturing settings. A machine-specific production export and actual fixture/process verification still require hardware/tooling decisions.
- Current safety, publisher and accessibility law checks remain the responsibility of the dedicated research/legal review; no legal compliance conclusion is made here.

## Release conditions

Use `engineering/validation/physical_test_plan.md` for the missing manufacturing evidence and `publishing/` for authorship, permissions and provider gates. A named human technical reviewer must examine the actual devices, material, fixture, toolpath and observed results. A genuine beginner must test the final versioned lesson sequence. The author must add substantial original work and approve the revisions. No row above authorises machine operation or publication.
