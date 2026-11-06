# Workflow and task dependencies

## Chapter lifecycle
DRAFT -> ENGINEERING REVIEW (Gate 1) -> ENGINEERING CORRECTIONS -> BEGINNER EDUCATIONAL REVIEW (Gate 2) -> EDUCATIONAL CORRECTIONS -> LANGUAGE AND VISUAL REVIEW (Gate 3) -> EDITORIAL CORRECTIONS -> FINAL INTEGRATION REVIEW -> APPROVED FOR AUTHOR REVIEW

Statuses used in the register: DRAFT, IN GATE 1/2/3, REVISION REQUIRED, BLOCKED, APPROVED FOR AUTHOR REVIEW, NOT REVIEWED.

## Re-review triggers
- Technical content changed after Gate 1 -> repeat the affected Gate 1 reviewers (and Gate 2 if the instruction changes).
- A figure changed so that an instruction step changes -> repeat Gate 2 for that section.
- Any figure/typography change -> Gate 3 visual re-check of that figure.
- Unresolved safety, technical or rights issue -> status BLOCKED regardless of gate state.

## Task dependencies
```
spec (A01) -> geometry (A02) -> figures (A14/A15/A18) -> prompts (A16, written BEFORE generation)
                          \-> screenshots (A17, needs installed software)
spec + sources (A12) -> chapter text (A10) -> Gate 1 -> corrections (A10) -> Gate 2 -> corrections -> Gate 3 -> corrections
all gates -> build (A21/A22) -> layout check (A20) -> rights check (A23) -> Editor-in-Chief integration review
cover (A19) -> metadata (A24)
```

## Targeted delegation matrix (do not invoke all roles for every change)
| Change type | Required reviewers |
|---|---|
| Dimension, joint, fit, assembly | A01, A02 (revalidate) |
| Laser, kerf, layout text | A05, A01, A08 |
| CAM, G-code, coordinates | A07, A03, A08 |
| CNC machining, workholding | A04, A08, A03 |
| Material, glue, finish | A06, A12 |
| Safety wording or safety-relevant figure | A08 (blocking) |
| Prose/typo/style only | A11 |
| New or changed figure | A14 or A15 or A18 (maker), A16 (prompt), A19 (aesthetics), plus the engineering owner of the content |
| Software screenshot | A17 + A13 |
| Build/format | A21, A22, A20 |
| Licence/asset | A23 |

## Loop prevention
Each gate allows at most two revision rounds. After round two without PASS the Editor-in-Chief escalates to the author with the open issue list. Specialists never re-delegate.

## Task file format (`book_team/tasks/TASK-NNN.md`)
`id | title | owner agent | reviewers | inputs | output path | depends on | status | due gate`

## Privacy handling
Task files and public reports contain issue ids, severities and statuses; manuscript quotes and figure content stay in the private workspace (`private_work/book/book_team/`). Public files never quote the manuscript.
