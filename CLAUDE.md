# CLAUDE.md — project operating instructions

Book: *CNC & Laser für Einsteiger: Deine erste Geschenkbox aus Holz* (German, du-form, digital-only). Author: Amir Mobasheraghdam. Agents work in English; reader text is German.

## Read first
1. `AGENTS.md`, `PROJECT_STATE.md`, `publishing/PUBLISHING_BLOCKERS.md`
2. `book_team/ENGINEERING_SPEC.md` (single engineering source of truth; geometry is a RECONSTRUCTION, the original CAD is lost)
3. `book_team/EDITOR_IN_CHIEF.md`, `WORKFLOW.md`, `QUALITY_GATES.md`

## Public/private boundary (hard rule)
This repository is PUBLIC. Never commit or stage the manuscript, figures, covers, renders, reconstructed geometry, or review reports that quote manuscript text. These live in the private workspace (`private_work/`, git-ignored paths in `.gitignore`). Public files may contain agent definitions, templates, statuses, issue ids and severities only.

## Team
The main session is Agent 00 (Editor-in-Chief & Technical Director). Specialists are in `.claude/agents/aNN-*.md` (24 roles, listed in `book_team/TEAM_STRUCTURE.md`). Delegate only to the roles the change needs (`WORKFLOW.md` matrix). Specialists never delegate to each other. No agent approves its own output.

## Non-negotiables
- No fabricated screenshots, software interfaces, workshop experience, measurements, physical tests, prices or publisher approvals.
- Simulations and renders are not physical tests; agent beginner reviews are simulated heuristic reviews.
- Nominal 160 x 120 x 70 mm, t = 3.0 mm nominal; do not change validated dimensions for aesthetics.
- Every figure needs a master prompt/spec, source traceability, validation notes and an approval status before use.
- Every chapter must pass Gate 1 (Engineering), Gate 2 (Beginner educational), Gate 3 (Language & visual) before "APPROVED FOR AUTHOR REVIEW". That status is not approval for sale; human technical, legal, and author approval remain required.

## Commands
```sh
python scripts/validate_agent_config.py     # validates .claude/agents and book_team (run after any role edit)
```
Private build/validation commands are in `README.md` and require the private sources.

## Git
Normal non-destructive commits to the designated branch only; inspect every staged path; commit only public-safe infrastructure.
