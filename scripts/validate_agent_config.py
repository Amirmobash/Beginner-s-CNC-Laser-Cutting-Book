#!/usr/bin/env python3
"""Validate the Claude Code agent configuration and book_team files. Exit 1 on any failure; refuses a run with zero checks."""
import sys, re
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
VALID_TOOLS = {"Read", "Grep", "Glob", "Bash", "Write", "Edit", "WebSearch", "WebFetch", "NotebookEdit"}
SECTIONS = ["Mission", "Domain expertise", "Responsibilities", "Required inputs", "Expected deliverables", "Tools and permitted actions",
            "Technical constraints", "Quality standards", "Review checklist", "Failure conditions", "Escalation rules", "Reporting format"]
HEAD_FIELDS = ["Agent identifier", "Role name"]
REQUIRED_FILES = ["CLAUDE.md"] + [f"book_team/{n}" for n in ["EDITOR_IN_CHIEF.md", "TEAM_STRUCTURE.md", "WORKFLOW.md", "QUALITY_GATES.md", "approval_register.md",
    "ENGINEERING_REVIEW_TEMPLATE.md", "BEGINNER_REVIEW_TEMPLATE.md", "LANGUAGE_VISUAL_REVIEW_TEMPLATE.md", "ISSUE_REGISTER.md", "PRODUCTION_STATE.md", "ENGINEERING_SPEC.md"]]
fails, checks = [], 0
def chk(cond, msg):
    global checks; checks += 1
    if not cond: fails.append(msg)
files = sorted((ROOT / ".claude/agents").glob("*.md"))
chk(len(files) == 24, f"expected 24 agent files, found {len(files)}")
seen_n, seen_names = set(), set()
for f in files:
    t = f.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    chk(bool(m), f"{f.name}: no frontmatter")
    if not m: continue
    fm = yaml.safe_load(m.group(1))
    chk(fm.get("name") == f.stem, f"{f.name}: name != filename")
    chk(re.fullmatch(r"[a-z0-9-]+", str(fm.get("name", ""))) is not None, f"{f.name}: invalid name")
    chk(len(str(fm.get("description", ""))) > 60, f"{f.name}: description too short")
    tools = {x.strip() for x in str(fm.get("tools", "")).split(",") if x.strip()}
    chk(bool(tools) and tools <= VALID_TOOLS, f"{f.name}: invalid tools {tools - VALID_TOOLS}")
    chk(fm.get("name") not in seen_names, f"{f.name}: duplicate name"); seen_names.add(fm.get("name"))
    n = re.search(r"^# Agent (\d\d) ", t, re.M); chk(bool(n), f"{f.name}: missing '# Agent NN' heading")
    if n: seen_n.add(n.group(1)); chk(f.name.startswith("a" + n.group(1) + "-"), f"{f.name}: number mismatch")
    for s in SECTIONS: chk(re.search(rf"^## {re.escape(s)}\s*$", t, re.M) is not None, f"{f.name}: missing section {s}")
    for h in HEAD_FIELDS: chk(f"**{h}:**" in t, f"{f.name}: missing {h}")
    chk("Project invariants" in t and "Verdict:" in t, f"{f.name}: missing invariants or verdict format")
    chk(t.count("- [ ] ") >= 4, f"{f.name}: checklist too short")
    chk(len(t) > 3500, f"{f.name}: definition too short ({len(t)} chars)")
chk(seen_n == {f"{i:02d}" for i in range(1, 25)}, f"agent numbers 01-24 incomplete: {sorted(seen_n)}")
for r in REQUIRED_FILES:
    p = ROOT / r; chk(p.is_file() and p.stat().st_size > 400, f"missing or empty: {r}")
gi = (ROOT / ".gitignore").read_text()
for must in ["/manuscript/", "/figures/", "/cover/", "/engineering/", "/book_team/private/"]:
    chk(must in gi, f".gitignore does not protect {must}")
q = (ROOT / "book_team/QUALITY_GATES.md").read_text()
for g in ["Gate 1", "Gate 2", "Gate 3"]: chk(g in q, f"QUALITY_GATES missing {g}")
print(f"checks run: {checks}, failures: {len(fails)}")
for x in fails: print("FAIL", x)
sys.exit(1 if fails or checks == 0 else 0)
