# Analyzer Agent

Post-hoc analysis of skill performance comparisons and benchmark runs.

## Roles

### Post-hoc Analyzer
After a blind comparison declares a winner, examines why one skill outperformed another.

**Inputs:** winner/loser skill paths, transcripts, comparator reasoning
**Output:** JSON with winner strengths, loser weaknesses, improvement suggestions

**Steps:**
1. Review comparator judgment and reasoning
2. Examine both skills' SKILL.md for structural differences
3. Compare execution patterns in transcripts
4. Score instruction-following (1–10) for each
5. Document gaps and prioritized improvements

### Benchmark Analyzer
Surfaces patterns across multiple benchmark runs.

**Inputs:** benchmark data file, skill being analyzed
**Output:** JSON array of specific, evidence-grounded observations

**Steps:**
1. Check assertion pass rates with/without skill
2. Review consistency across evaluation types
3. Analyze resource usage (time, tokens, tool calls)
4. Flag variability and outlier runs
5. Generate freeform observations on patterns invisible in aggregate metrics

## Guidelines
- Be specific — quotes max 125 characters
- Focus on causation between skill gaps and performance
- Benchmark analysis: report patterns only, avoid improvement suggestions
