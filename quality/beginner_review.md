# Beginner review — chapters 1–6

Review date: 2026-11-04. Scope: source-manuscript reading, source-path checks, comparison with `engineering/spec.json`, and installed Inkscape keymap inspection. This is an agent editorial review, not a pilot with a first-time human reader and not a verified Windows or machine tutorial.

## Checks actually performed

- Read all six current chapters and compared their product dimensions, panel identifiers, manufacturing order, material assumptions and origin definitions with the engineering specification.
- Executed Python assertions for W160/D120/H70, thickness3, wall height64, locator153.4×113.4, seven IDs, nine finger bands and engraving zone `[20,25,140,95]`.
- Parsed each chapter's figure Markdown and confirmed all 23 referenced chapter1–6 PNG paths existed at review time; this does not inspect image content or rendered placement.
- Checked literal repository source-path references in chapters1–6. `research/hardware_comparison.md`, `scripts/engineer_box.py`, the named engineering directories, individual SVGs, layout, coupon and associated drawing PDFs exist. Generated reader working-file names are exercises, not claimed included assets.
- Read `engineering/validation/FIT_COUPON.md`: the coupon contains full-height complementary corner strips plus a thickness-slot comb, not only a generic thickness test.
- Inspected `/usr/share/inkscape/keys/inkscape.xml`: standard bindings map `r`/F4 to Rect and `s`/F1 to Select. This supports the shortcut statements, but does not prove complete GUI usability.

## Chapter-level findings

| Chapter | Findings and changes | Remaining beginner test |
|---|---|---|
| 1 | Product names, separate flat L0 engraving and delayed L1 glue-up match the spec. A folder scheme different from chapter3 was found and reported to the root editor; no chapter1 edit made by this reviewer. | First-time reader must identify all seven panels and distinguish optional L1 from the baseline seven-panel drawing set. |
| 2 | Thickness measurement, total equipment cost and lack of current machine/price verification are explicit. The 600×400 material planning example can accommodate the actual350×362 layout, but the actual layout size should be named; reported to root. | Obtain genuine current hardware offers, inspect approved protection setup and test whether each beginner understands that no machine purchase is currently endorsed. |
| 3 | Main roles are separated. Inkscape/FreeCAD versions are fixed locally; unknown LightBurn version and Windows steps are disclosed. Added source S26 for SVG-native role and specified default shortcut mapping. | Actual Windows installation, GUI controls and repeatable laser import need version-specific screenshots and observed user trials. |
| 4 | G-code examples use explicit GRBL1.1 assumptions and intentionally non-executable teaching headers. Exercise endpoints and30mm/18s idealized arithmetic were checked. No manufacturing feed is recommended. | Have a beginner explain modal state and origins without prompting; verify an actual selected-controller postprocessor/simulator separately. |
| 5 | All panel sizes, locator gap0.3/side,9 bands,7.111mm pitch and engraving area match the spec. Added exact350×362 layout size, explicit optional-L1 baseline and description of corner coupons plus thickness comb. | Real thickness measurements, corner assembly, glue-up, lid fit and dimensions after kerf correction remain untested. Parametric command use needs supervised beginner instructions when thickness differs. |
| 6 | Operation assignment does not treat color as universal machine instructions. Personal name remains a separate CNC operation. Added bounded archived-document references S24/S27–29. All physical gates remain open. | Complete current-version LightBurn walkthrough and selected enclosed-laser tutorial are absent; a genuine supervised material test must be recorded. |

## Release implications

The source chapters form a coherent digital learning draft. They do not yet meet the user's requirement for a complete, practically verified click-by-click tutorial on a selected machine. Do not present conceptual laser preparation as a tested live-interface lesson. Required outside work: choose a supported exact machine/software combination, verify current terms and hardware safety documentation, capture permitted authentic screenshots, conduct a novice pilot and record supervised physical trials. Review chapter7–9 in their separate review reports.
