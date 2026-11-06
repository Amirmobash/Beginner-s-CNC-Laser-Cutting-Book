# Quality gates

Every chapter needs three independent gates. Verdicts: **PASS / REVISION REQUIRED / BLOCKED**. Only the lead reviewer's verdict counts for a gate; the Editor-in-Chief records it.

## Gate 1 — Engineering approval
Lead: A01. Supporting (only if relevant): A03, A04, A05, A06, A07, A08, A12.
| Criterion | Evidence required |
|---|---|
| Technical correctness | Statement traced to spec or source |
| Manufacturing feasibility | Reviewer rationale; physical claims flagged as untested |
| Geometric consistency | Numbers match ENGINEERING_SPEC.md and figures |
| G-code accuracy | Worked examples recomputed |
| Machine compatibility | Dependencies named, no universal claims |
| Material assumptions | Nominal vs measured separated |
| Workholding | Thin lid fully supported, clamps outside tool path |
| Safety | A08 PASS; every hazard has a mitigation or stop rule |
| Source validity | A12: claims VERIFIED or marked unverified |
BLOCKED when: any CRITICAL safety/engineering finding is open.

## Gate 2 — Beginner educational approval
Lead: A09. Supporting: A10, A13, A17.
| Criterion | Evidence required |
|---|---|
| No unexplained prerequisites | A13 walkthrough lists none open |
| Clear objectives | Objective + "Du brauchst" present |
| Natural progression | Builds on earlier chapters |
| Reproducible instructions | Numbered steps, executable literally |
| Expected results | Stated after each procedure |
| Sufficient screenshots | Genuine screenshots where software UI is taught, or BLOCKED-pending item recorded |
| Exercises | Present, answerable |
| Troubleshooting | Common mistake and verification given |
A13 reviews are SIMULATED heuristic reviews, not participant testing. A chapter an absolute beginner cannot follow cannot pass.

## Gate 3 — Language and visual approval
Leads: A11 (language), A19 (visual). Supporting: A14, A15, A16, A18, A20.
| Criterion | Evidence required |
|---|---|
| Natural German, consistent du | A11 findings resolved |
| Terminology consistency | Register updated |
| Image clarity and visual accuracy | A14/A19 review of each figure against the model |
| Correct figure placement and single captions | A20 page check |
| Authentic screenshots only | A17 metadata |
| Master prompt per figure | A16 file exists and matches the delivered figure |
| Accessible captions/alt text | Present and accurate |
| Book-wide visual consistency | A19 |
BLOCKED when: an unfinished, misleading or poor-quality instructional graphic remains.

## Final integration review (Editor-in-Chief)
Cross-check text vs figures vs spec; confirm gates ran with the required reviewers; confirm privacy and rights register; result = APPROVED FOR AUTHOR REVIEW (never "approved for sale").

## Severity scale
CRITICAL: could injure, destroys engineering correctness or misleads about evidence. MAJOR: blocks beginner success or accuracy but not safety. MINOR: polish.
