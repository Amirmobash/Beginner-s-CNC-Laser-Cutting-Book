# Issue register (public-safe)

Schema: ID | chapter | severity | gate | owner | status | summary (paraphrased, no manuscript quotes) | source reviewers. Quoted evidence stays in `private_work/book/book_team/reviews/`.
Status values: OPEN, PARTLY-OPEN, FIXED-PENDING-REVIEW (correction applied, not yet re-reviewed), CLOSED (reviewer confirmed), DECIDED, WONTFIX.

Pilot origin: Chapter 1, review round 1 (13 reviewers, 2026-11-06), corrections 1, review round 2 (7 reviewers), corrections 2. About 150 raw findings were consolidated into the entries below (duplicates across reviewers merged).

| ID | Chapter | Severity | Gate | Owner | Status | Summary | Source |
|---|---|---|---|---|---|---|---|
| CH1-001 | 1 | MAJOR | G1 | A01 | FIXED-PENDING-REVIEW | Model provenance/untested status was not disclosed in text and caption | A01,A12,A14,A15,A19 |
| CH1-002 | 1 | MAJOR | G1 | A08 | CLOSED | No explicit stop rules; 'supervision' undefined | A08 round 2: PASS |
| CH1-003 | 1 | MAJOR | G1 | A08 | CLOSED | Laser eye/skin hazard not named in prose | A08 round 2 |
| CH1-004 | 1 | MAJOR | G1 | A08 | CLOSED | No exclusion of open/unenclosed lasers | A08 round 2 |
| CH1-005 | 1 | MAJOR | G1 | A14 | CLOSED | Figure F02 showed an unsupported workpiece, ambiguous German term, uncovered beam | A04,A08,A14 round 2 |
| CH1-006 | 1 | MAJOR | G1 | A04 | FIXED-PENDING-REVIEW | Clamps-outside-zone/tool-path rule missing | A04 |
| CH1-007 | 1 | MAJOR | G1 | A01 | FIXED-PENDING-REVIEW | L1 described inconsistently with the spec in several places | A01 (corrections 2) |
| CH1-008 | 1 | MAJOR | G1 | A01 | FIXED-PENDING-REVIEW | Engraving coordinates used without origin/axes | A01,A12 |
| CH1-009 | 1 | MAJOR | G1 | A01 | FIXED-PENDING-REVIEW | Sequence risk: lid not trial-fitted before engraving | A01 |
| CH1-010 | 1 | MAJOR | G1 | A12 | FIXED-PENDING-REVIEW | Citation markers not registered for the chapter or not supporting the sentence | A12 (markers removed from reader text) |
| CH1-011 | 1 | MINOR | G1 | A12 | OPEN | General safety statements unsourced (need source or author decision) | A12,A08 |
| CH1-012 | 1 | MAJOR | G2 | A10 | FIXED-PENDING-REVIEW | No parts identification table | A09,A13 |
| CH1-013 | 1 | MAJOR | G2 | A10 | FIXED-PENDING-REVIEW | Prerequisite 'machine access and trained supervisor' missing | A09 |
| CH1-014 | 1 | MAJOR | G2 | A10 | PARTLY-OPEN | Undefined jargon (glossary added; some terms still to defer or define) | A09,A13 |
| CH1-015 | 1 | MAJOR | G2 | A10 | FIXED-PENDING-REVIEW | Test-fit station inconsistent between list and process figure | A05,A09 |
| CH1-016 | 1 | MAJOR | G2 | A10 | PARTLY-OPEN | Procedures lacked numbering/expected results (mostly fixed; 1.6 gaps remain) | A09 |
| CH1-017 | 1 | MAJOR | G2 | A18 | OPEN | Beginner needs a simple chain diagram (drawing -> CAM -> toolpath -> postprocessor -> controller) and a whole-machine schematic | A13 |
| CH1-018 | 1 | MAJOR | G3 | A11 | PARTLY-OPEN | Terminology drift and mixed wir/du voice (wir/du decision reserved for the author) | A11 |
| CH1-019 | 1 | MAJOR | G3 | A14 | FIXED-PENDING-REVIEW | Figure F04: mixed projection, e-stop placement, overload, text overflow | A14,A18,A19 |
| CH1-020 | 1 | CRITICAL | G3 | A16 | FIXED-PENDING-REVIEW | Master prompts missing for three figures (process rule) | A16 |
| CH1-021 | 1 | MAJOR | G3 | A16 | FIXED-PENDING-REVIEW | F01 prompt contradicted spec numbering/output and claimed approval | A16 |
| CH1-022 | 1 | MAJOR | G3 | A19 | DECIDED | Dark hero render vs cream book identity (decision DEC-001: keep as documented hero exception) | A19,A15 |
| CH1-023 | 1 | MAJOR | G3 | A20 | OPEN | Alt text identical to caption; figure-id prefix in captions; needs layout/accessibility decision | A11 |
| CH1-024 | 1 | MINOR | G3 | A11 | PARTLY-OPEN | Sentence-level German polish items | A11 |
| CH8-001 | 8 | MAJOR | G1 | A03 | CLOSED | F30 section depicted a V-notch while the verified model is a flat pocket; redrawn to scale | A03,A14,A13 R4 |
| CH8-002 | 8 | MAJOR | G1 | A01 | CLOSED | Letter-gap value was computed across lines; recomputed per line (2.0 mm) and text corrected | A01 R4 |
| CH8-003 | 8 | MAJOR | G2 | A10 | FIXED-PENDING-REVIEW | Tool story (flat end mill vs V-bit) unified in chapters 8, 9 and F30 | A09 |
| CH8-004 | 8 | MAJOR | G2 | A10 | PARTLY-OPEN | ShapeString exercise made stepwise with numeric targets; beginners may still need screenshots of FreeCAD (none captured: FreeCAD not available) | A13 |
| CH8-005 | 8 | MINOR | G1 | A03 | OPEN | No 3D material-removal simulation, no depth passes, no entry/exit modelled (stated in text) | A03 |
| CH8-006 | 8 | MINOR | G3 | A11 | PARTLY-OPEN | Terminology Gravurzone/Schriftzug/Schriftart unified in changed passages; sentence-level polish remains | A11 |
| COV-001 | cover | MAJOR | G3 | A19 | CLOSED | Cover C: decagonal mat, duplicated label, AMIR removed; thumbnails re-tested | A19 R4 |
| COV-002 | cover | MINOR | G3 | A19 | OPEN | Polish items (lighting, subtitle hierarchy); cover text 'Dein erstes Holzprojekt' differs from the book title 'CNC & Laser für Einsteiger: Deine erste Geschenkbox aus Holz' - author to decide whether title page and cover text should align | A19,A11 |
| FIG-001 | 8 | MINOR | G3 | A14 | OPEN | F27 label/leader collisions and F13 crowded text (minor) | A14 R4 |
| RIGHT-001 | 8 | MAJOR | - | A23 | OPEN | Font Inter SemiBold: licence per package SIL OFL 1.1/Apache-2.0; human licence review required before commercial use | A23 |
| FIN-001 | 8 | MAJOR | G1 | A03/A04 | OPEN | Engraving only digitally checked: no 3D removal simulation, no forces/deflection, vertical plunges at 1 mm cutter; physical validation required | A03,A04 |
| FIN-002 | 8 | MAJOR | G2 | A17 | OPEN | FreeCAD menu steps (ShapeString, job, depth coupling) not shown step by step; genuine screenshots pending beyond F34 | A13,A17 |
| FIN-003 | 3,5,6 | MAJOR | G2 | A17 | BLOCKED | No laser-software, sender, Windows or German-UI screenshots (software/hardware unavailable) | A17 |
| FIN-004 | all | MAJOR | G3 | A11 | OPEN | Terminology and list formatting partly harmonised; further editorial pass and author voice decision needed | A11 |
| FIN-005 | all | MAJOR | G1 | A12 | OPEN | Citation markers missing for safety/licence claims; 11 sources uncited | A12 |
| FIN-006 | rights | MAJOR | - | A23 | OPEN | Asset register, render provenance, F11/F34 screenshot use, font embedding, marks: human/legal review | A23 |
| FIN-007 | pub | MAJOR | - | A23 | OPEN | Channel, ISBN, imprint, BFSG, current policies, authorship disclosure | A23 |
| FIN-008 | titles | MINOR | G3 | A19 | CLOSED | Title/subtitle unified across cover, title page, metadata, HTML, EPUB | build check |
| FIN-009 | pub | MINOR | G3 | A21 | CLOSED | EPUBCheck 0 messages; Ace 0 violations (2026-11-14 build); DOCX opened in LibreOffice only | validators |

| FIN-010 | 8 | CRITICAL | G1 | A03 | OPEN | Engraving toolpath: four FreeCAD variants checked digitally; all contain vertical plunges or rapids in material; not suitable for direct machine execution; operator must define entry/exit in the machine CAM and test on scrap | A03/A04 |
| FIN-011 | front | MAJOR | G3 | A11 | OPEN | Author profile, foreword and AI-assistance wording drafted as placeholders; author decision and channel check required | A23 |
| FIN-012 | all | MAJOR | G2 | A09 | OPEN | Late editorial changes (du voice, ch.3/5/8 beginner blocks, Appendix H) corrected but not re-reviewed (beyond two-round limit) | A09/A11/A13 |
| AUD-001 | 8 | CRITICAL | G1 | A07 | CLOSED | Z0 convention contradiction between study and book text; conversion rule added and re-checked | R-A01/A07/A08 |
| AUD-002 | 8 | MAJOR | G1 | A03 | OPEN | No toolpath variant has a verified safe entry; chapter made optional with acceptance checklist; physical validation required | A03/A04 |
| AUD-003 | all | MAJOR | G1 | A12 | OPEN | Safety statements without source in S01–S31 labelled; expert review required; 13 citations only partly supported | A12/A08 |
| AUD-004 | 3,6,8 | MAJOR | G2 | A17 | BLOCKED | Genuine LightBurn, sender, FreeCAD CAM dialog, Windows and German-UI screenshots missing | A17 |
| AUD-005 | figs | MAJOR | G3 | A14 | OPEN | Seven figures not revised after audit; cover mat colour and lid seam need new render | A14/A19 |
| AUD-006 | spec | MINOR | G1 | A01 | CLOSED | Public ENGINEERING_SPEC.md said 47 checks; the actual suite runs 48 (48 unique, all pass; verified by running validate_model.py 2026-11-25); spec corrected. Independent Codex check not performed | A01 |
| AUD-007 | all | MINOR | G3 | A11 | OPEN | Post-review small corrections not re-reviewed; language status REVISION for ch.1, 4–9 | A11 |
