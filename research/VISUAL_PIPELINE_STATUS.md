# Visual and editorial reconstruction — status (2026-11-05)

Honest status of the directive's phases 4 and 8–14. Nothing below was produced unless it says so.

## What exists after this session
- `research/GITHUB_BENCHMARK_REPORT.md` — README/licence-level benchmark of 26 repositories (maintenance, tests and releases NOT verified: GitHub web/API returned 403).
- `research/IMAGE_PROMPT_TEMPLATE.md` — the 13-section per-figure master prompt template (blank; not filled).
- `quality/IMAGE_VALIDATION_REGISTER.md` — register structure; **zero figures approved**.

## Not done, and why
| Item | Status | Blocker |
|---|---|---|
| Blender render scenes (9 scenes) | NOT DONE | Blender not installed here; the authoritative STEP/FreeCAD geometry is private (`/engineering/` git-ignored) and absent from this checkout. |
| Per-figure `FXX_MASTER_PROMPT.md` files | NOT DONE | Each needs verified geometry from the private model; writing them without it would invent dimensions. Output location `assets/` is git-ignored, so they stay local. |
| Image generation / critique loop | NOT DONE | Depends on the two rows above; also no image-generation tool is available in this session. |
| Three cover concepts | NOT DONE | Same geometry dependency; cover sources are private. |
| Manuscript rewrite (German) | NOT DONE | `/manuscript/` absent from this checkout. |
| Rebuild DOCX/PDF/HTML/EPUB | NOT DONE | Sources absent; build scripts need them. |
| Real software screenshots (Inkscape, FreeCAD, LightBurn, CONTROL…) | NOT DONE | No GUI apps/German Windows UI in this session; LightBurn/OpenBuilds sites 403. Figures stay PENDING; no substitute screenshots invented. |
| CAMotics independent simulation | NOT DONE | Needs private engraving G-code. |
| Private production ZIP | NOT DONE | Nothing was changed privately. |

## How to continue (in the environment holding the private sources)
1. Restore `manuscript/ engineering/ figures/ cover/` and run the README build/validate commands to confirm a clean baseline.
2. Install Blender (human-verified licence/asset terms). Export the existing STEP assembly to meshes per part; script the 9 scenes headlessly from those meshes; keep scripts under `engineering/` (private).
3. Per figure: fill `research/IMAGE_PROMPT_TEMPLATE.md` into `assets/image_prompts/FXX_MASTER_PROMPT.md` with dimensions read from the generator, render, then record a decision in `quality/IMAGE_VALIDATION_REGISTER.md` (engineer, illustrator, beginner reviews).
4. Add the CAMotics run and a rendered-page non-blank/clipping check to the validators.
5. Text on covers must stay editable typography; test as a thumbnail.
6. Human approvals remain release gates (see `publishing/PUBLISHING_BLOCKERS.md`).
