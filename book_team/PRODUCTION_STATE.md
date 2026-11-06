# Production state

Updated by the Editor-in-Chief. Date: 2026-11-06.

## Team infrastructure (implemented and validated)
- 24 specialist agent definitions in `.claude/agents/` plus `book_team/EDITOR_IN_CHIEF.md`; `python scripts/validate_agent_config.py` -> 622 checks, 0 failures (first run found 6 weak checklists, fixed).
- Verified that Claude Code loads a definition: headless `claude --agent a08-machine-safety-engineer -p ...` answered from its own definition.
- `claude agents` manages background sessions only and does not validate subagent definitions (not usable as a validator).
- The Agent tool in the session that created the files could NOT address the new roles as native subagent types (types are registered at session start: "not found"). Native use works from a fresh session.

## Agents actually invoked (auditable)
Each invocation was a separate Claude Code process loading its own project agent definition (`--agent <id>`), read-only tools (Read, Grep, Glob), output captured in private files.
- Chapter 1 round 1 (13): A01, A04, A05, A08, A09, A11, A12, A13, A14, A15, A16, A18, A19. All exited 0.
- Chapter 1 round 2 re-review (7): A01, A08, A09, A11, A12, A13, A14. All exited 0.
- Not invoked: A02, A03, A06, A07, A10, A17, A20, A21, A22, A23, A24 (their work was done by the main session as procedures: geometry, scripts, builds, screenshot capture, text edits). They are configured but untested as live agents.
- Reviews are artifact-based/simulated; no real participants, no physical tests.

## Gates tested
All three gates were exercised on Chapter 1 with the roles above. Outcome: Gate 1 safety (A08) PASS; every other gate lead REVISION REQUIRED. Loop rule applied: after two review rounds the chapter is escalated to the author (see approval_register).

## Editor-in-Chief decisions
- DEC-001: keep the dark F01 hero render as a documented exception to the cream identity (reversible).
- DEC-002: keep nine stations in the project route; mention the fit sample inside station 4 (instead of a tenth station).
- DEC-003: wir/du voice mix is reserved for the author (minor).
- DEC-004: stop after two review rounds per gate; corrections 2 were NOT re-reviewed.

## Open blockers
Physical tests, human technical review, author contributions, rights/imprint, publisher requirements, original CAD (lost), German/Windows UI screenshots, remaining chapters not gated, issues CH1-011/014/016/017/018/023/024.
