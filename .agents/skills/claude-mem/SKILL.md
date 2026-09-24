---
name: claude-mem
description: Persistent memory management, session reflection, and progressive context distillation. Use when capturing key decisions, recording bug workarounds, indexing project-specific knowledge across sessions, or formulating candidate rules.
---

# Claude-Mem: Persistent Memory & Context Distillation

This skill provides a structured workflow for capturing, compressing, and recalling project-specific memory across agent coding sessions, inspired by the `thedotmack/claude-mem` persistent memory paradigm.

## Core Philosophy

1. **Separation of Concerns**:
   - **Static Rules (`GEMINI.md` / `rules/*.md`)**: Project conventions, architecture constraints, style standards ("Always do X").
   - **Dynamic Memory (Claude-Mem)**: Session-derived insights, specific bug resolutions, tool quirks, and architectural decisions ("What actually happened and why").

2. **Evidence-Based Promotion**:
   - Never promote an observation into long-term memory or rules without attached evidence (a passing/failing test, error log, diff, or verified benchmark).

3. **Narrow Rule Phrasing**:
   - Structure synthesized memories into actionable conditionals:
     `When [Trigger / Situation X], do [Action Y] / avoid [Anti-pattern Z] because [Evidence/Reason W].`

---

## Memory Workflows

### 1. Capturing Session Observations

During complex coding, debugging, or environment setup, record significant milestones into a structured memory log:

- **Decisions**: Why a library, architecture, or pattern was chosen over alternatives.
- **Gotchas & Quirks**: System-specific issues (e.g. Windows PowerShell syntax differences, LaTeX compilation order, dependency clashes).
- **Workarounds**: Working fixes for un-intuitive bugs.

Format for a Memory Card:
```markdown
### [MEM-<ID>] <Short Title>
- **Date**: YYYY-MM-DD
- **Context/Trigger**: When configuring or running <Component/Task>
- **Finding**: <What was discovered or what failed>
- **Resolution**: <The precise fix or recommended pattern>
- **Evidence**: <Log line, command, or file reference>
```

### 2. Session End Reflection & Distillation

Before ending a major milestone or multi-step session:
1. Review the conversation transcript and files modified.
2. Identify knowledge that will be valuable for future sessions.
3. Consolidate scratch notes into permanent project memory or Knowledge Items (KI).
4. If a pattern repeated $\ge 2$ times, draft a candidate rule for `GEMINI.md` or `.agents/rules/`.

### 3. Recall & Context Injection

When starting a new feature or troubleshooting an issue:
1. Search previous memory entries for relevant keywords (e.g., error codes, library names).
2. Apply recorded workarounds before attempting trial-and-error fixes.
3. Verify that earlier assumptions still hold against current code.

---

## Mode Creator Workflow

Tailor memory recording templates to specific domains:
- **Bug Hunter Mode**: Tracks reproduction steps, root causes, failing assertions, and verification commands.
- **Architecture Mode**: Records ADRs (Architectural Decision Records), trade-offs, and dependency rationales.
- **Tooling/DevOps Mode**: Documents shell commands, build pipelines, and environment variables.
