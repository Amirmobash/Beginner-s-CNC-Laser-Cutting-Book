# Editorial review — chapters 1–6

Date: 2026-11-04. Reviewed the current Markdown text, engineering specification and relevant documentary evidence. Status: **working manuscript, human editorial approval outstanding**.

## Language and continuity

The reviewed chapters use informal German `du`, one gift-box project and stable panel IDs B0/F0/R0/S0/S1/L0/L1. Uppercase `Sie` instances refer to preceding feminine nouns at sentence starts (for example a geometry or a preview); they are not switches to formal reader address. No unrelated CNC nameplate or plywood-sign project remains in chapters1–6. No author's personal workshop experience or physical success is claimed.

The principal progression is product → material/equipment → digital tools → command literacy → panel geometry → supervised laser planning. Each chapter states goals and prerequisites and includes expected results, practice and self-check answers. Repeated stop points are substantive, but a human editor should check whether final apparatus can consolidate them while preserving their immediate relevance.

## Specific findings

1. **Chapter1/3 folder continuity:** chapter1 originally listed Entwurf/Export/Maschinenauftrag/Pruefprotokoll, while chapter3 establishes numbered01_Entwurf/02_Pruefung/03_Laser/04_CNC/05_Protokoll. Reported to root for chapter1 correction; do not describe the original mismatch as fixed without checking the current file.
2. **Chapter2 stock size:**600×400mm is an illustrative supply format; actual layout is350×362mm. These do not conflict geometrically. Chapter5 now states the actual layout dimensions so readers do not mistake stock format for machine-bed requirements.
3. **Chapter3 software evidence:** added S26 to the SVG/native-role statement. Default Inkscape shortcuts were checked in the installed package keymap. No current price, complete Windows support matrix or commercial-license certification is asserted. FreeCAD development-branch references establish concepts, not identical installed-version menus.
4. **Chapter4 code:** the non-G-code teaching header is intentional. The virtual30mm path with F100mm/min gives18s only when acceleration is ignored; the manuscript labels that assumption. G54, G20/G21, G90/G91, G0/G1, G94 and M3/M4/M5 are supported by retrieved GRBL reference documentation, not all derivatives.
5. **Chapter5 engineering precision:** seven baseline pieces include optional L1. Added explicit baseline qualification, actual nesting dimensions and the real fit-coupon components. Nominal dimensions and unmeasured actual material are distinguished. The0.3mm locator gap is a design quantity, not a measured manufacturing result.
6. **Chapter6 documentation scope:** added archived LightBurn references S24/S27–29 while retaining the warning that current release/menu/licensing evidence is unavailable. The text does not invent a complete screen-by-screen workflow to hide that gap.

## Evidence boundaries

Relevant retrieved sources read for this review: S01 GRBL command list and laser-mode statement; S03 parser excerpts for G94/spindle handling; S06 FreeCAD installation/platform description; S26 Inkscape native SVG description; S27 archived LightBurn external-vector import; the current `research/CLAIM_VERIFICATION.md` and `research/software_decision.md`. Installed keymap file inspected separately. Source access or code inspection is not hardware, GUI or legal verification.

Rights, current retailer policies, author participation and trademark/screenshot permissions still require the publishing review. This review does not approve German/EU legal compliance, production safety, accuracy of inaccessible manufacturer pages or commercial release. Required human work includes natural-language revision by Amir Mobasheraghdam, actual workshop observations, original test photographs, source/rights verification and documented technical approval. Proofreading alone does not establish the substantial human authorship required by a publisher's policy.
