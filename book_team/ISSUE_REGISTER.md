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
