---
name: skill-creator
description: Creates new Claude Code skills through iterative testing and refinement. Use when asked to create, build, or develop a new skill.
---

# Skill Creator

This skill guides you through creating high-quality Claude Code skills via a structured workflow of intent capture, drafting, testing, and iteration.

## Core Process

### 1. Capture Intent
Understand what the skill should do:
- What is the skill's purpose and name?
- When should it trigger?
- What are the expected outputs?
- Are test cases (evals) needed?

### 2. Interview & Research
Before writing anything, ask about:
- Edge cases and failure modes
- Output format requirements
- Success criteria
- Example inputs and outputs

### 3. Draft SKILL.md
Create the skill file with:
- YAML frontmatter: `name`, `description` (used for trigger matching)
- Clear, concise instructions
- Keep under 500 lines; add hierarchy if approaching the limit

### 4. Create Evals
Write test cases in `evals/evals.json`:
- Cover happy path and edge cases
- Include expected outputs or assertions
- Aim for 5–10 representative cases

### 5. Run & Compare
Spawn parallel subagent runs:
- **with-skill**: Claude using the new SKILL.md
- **baseline**: Claude without the skill
- Use the comparator agent to blind-evaluate results

### 6. Review & Iterate
After feedback:
- Generalize from patterns, don't overfit to single cases
- Keep prompts lean — remove what doesn't help
- Explain the *why* behind instructions
- Repeat until satisfied or progress plateaus

## Key Principles

- **SKILL.md is the source of truth** — write it as if Claude has never seen your task before
- **Descriptions drive triggers** — the `description` field determines when the skill activates
- **Less is more** — a focused 100-line skill beats a bloated 500-line one
- **Test before shipping** — evals prevent regressions as you iterate

## Agents

This skill uses three specialized sub-agents:

- **agents/analyzer.md** — Post-hoc analysis of why one skill outperformed another
- **agents/comparator.md** — Blind side-by-side comparison of two outputs
- **agents/grader.md** — Evaluates whether task execution meets stated expectations

## Output

When done, the skill folder should contain:
```
skills/<skill-name>/
  SKILL.md          # Main skill instructions
  agents/           # Optional sub-agents
  evals/
    evals.json      # Test cases
  assets/           # Optional supporting files
```
