# Engineering specification (single source of truth)

Owner: Agent 01 (Senior Mechanical Design Engineer). Maintained with Agent 02 (CAD). Changes need A01 approval and A02 re-validation.

## Provenance (read first)
- The ORIGINAL CAD/STEP/FreeCAD sources of the first production run are **lost**. Only the DOCX/PDF manuscript and its documented nominal values survive.
- The 3D/2D geometry used for figures since 2026-11-06 is a **RECONSTRUCTION** built from those documented values (private workspace: `engineering/box_model.py`, validation JSON). It must never be called the original verified design.
- Nothing in this specification is a measured value. No physical prototype has been built or tested.

## Nominal product (documented in the manuscript)
| Item | Value |
|---|---|
| Outside size W x D x H | 160 x 120 x 70 mm |
| Plywood thickness | 3.0 mm NOMINAL (actual must be measured) |
| Parts | B0 base, F0/R0 front/rear wall, S0/S1 side walls, L0 lid, L1 lid guide |
| B0, L0 | 160 x 120 mm |
| F0, R0 | up to 160 x 64 mm outer bounding box |
| S0, S1 | up to 120 x 64 mm outer bounding box |
| L1 | 153.4 x 113.4 mm |
| Wall height | 64 mm (3 + 64 + 3 = 70) |
| Joint segments per corner | 9 alternating, 64/9 mm each; in each level only one wall occupies the corner |
| Inside footprint | 154 x 114 mm |
| Engraving zone on L0 | X20..X140, Y25..Y95 (120 x 70 mm) |
| Workpiece origin | left-front corner of the lid top surface; X right, Y depth, Z up |

## Documented functions and sequence (from the manuscript; unverified physically)
- L1 is a thin plate, slightly smaller than the inside footprint (153.4 x 113.4 mm vs 154 x 114 mm), glued to the underside of L0 after the flat engraving; its function is to locate the lid on the walls.
- Sequence: dry fit, glue the body (walls + B0), engrave L0 flat and separate, attach L1, final check. Recommendation from the pilot review (A01): trial-seat L0 on the body before engraving.

## Reference engraving (decision of the author, 2026-11-07)
- The product engraving is the German greeting "Frohes Fest" (two lines), with optional examples "Frohe Weihnachten" and "Frohes neues Jahr". No year, no English greetings. The old sample "AMIR" is retired from all product depictions; the author's name remains in cover and metadata only.
- Font Inter SemiBold (licence per package: SIL OFL 1.1 / Apache-2.0; human licence review still required). Lettering must stay inside the engraving zone with at least 10 mm margin.
- Digital verification (2D, own calculation; no physical engraving performed; no 3D material-removal simulation): fit in zone, letter gaps within each line, reachability for a 1.0 mm end mill, clearing path inside the zone, clearance to the example clamps. Tool diameter, depth (0.6 mm example) and stepover are verification assumptions, not machining recommendations. Details and geometry files are private.

## Reconstruction assumptions (NOT stated in the manuscript)
1. L1 thickness = 3.0 mm; L1 sits inside the wall ring directly under L0 (0.3 mm clearance per side).
2. Segment parity (counted from the bottom): F0/R0 own segments 1,3,5,7,9; S0/S1 fingers fill 2,4,6,8.
3. No kerf compensation in the nominal drawings.
4. Cutting layout (private reconstruction): two columns, 10 mm gaps, about 350 x 411 mm. The original layout size (350 x 362 mm in the old text) could not be reproduced from the documented data and must be treated as unverified.

## Digital validation status of the reconstruction (2026-11-06)
47 automated checks passed (panel count, closed contours, bounding boxes, volume = area x thickness, pairwise zero overlap, corner columns fully and exactly filled, complementary segments, L1 clearance, engraving zone inside lid, layout gaps and areas). Digital validation is **not** physical fit verification.

## Not verified / open
Actual plywood thickness, kerf, joint fit, glue joint, lid fit, laser and CNC process parameters, machine compatibility, any physical result.
