# Team structure

Agent 00 (Editor-in-Chief, main session) coordinates 24 specialists. Specialists never delegate to each other; all routing goes through Agent 00 (prevents circular review).

| Division | Agents |
|---|---|
| Leadership | 00 Editor-in-Chief & Technical Director (main session; see EDITOR_IN_CHIEF.md) |
| Engineering & Manufacturing | 01 Mechanical Design (spec owner), 02 CAD, 03 CAM & Toolpath, 04 Desktop CNC Machining, 05 Laser Cutting, 06 Wood Materials, 07 CNC Control & G-code, 08 Machine Safety |
| Education & Writing | 09 Instructional Design (Gate 2 lead), 10 Technical Author, 11 German Technical Editor (Gate 3 language lead), 12 Researcher & Fact-Checker, 13 Beginner Usability Tester |
| Visual Production | 14 Technical Illustrator, 15 3D Artist, 16 Image Prompt Engineer, 17 Software Screenshot Specialist, 18 Information Designer, 19 Art Director & Cover Designer (Gate 3 visual lead) |
| Digital Production & Publishing | 20 Layout Designer, 21 Publishing Engineer, 22 Automation & QA Engineer, 23 Rights & Licensing, 24 Marketing & Metadata |

## Implementation reality (auditable)
- Each specialist has a repository-local Claude Code subagent definition in `.claude/agents/aNN-*.md` (frontmatter `name`, `description`, `tools`; body with the 14 required fields). Claude Code loads these when a session starts; in the session that created them, specialists were invoked through general-purpose subagents that were told to follow the role file (see PRODUCTION_STATE.md for what actually ran).
- Subagents run on demand and report back; nothing runs continuously. Parallelism is limited to what the Agent tool provides in a session.
- Roles that are not persistent agents (A16 prompt writing, A17 screenshot capture, A21/A22 builds) are executed as procedures by whoever holds the task; their deliverables are the same.

## Reporting lines
All specialists report to Agent 00. Gate leads: Gate 1 = A01, Gate 2 = A09, Gate 3 = A11 + A19.
Critical safety/engineering findings: A08/A01 -> Agent 00 immediately -> chapter BLOCKED.
