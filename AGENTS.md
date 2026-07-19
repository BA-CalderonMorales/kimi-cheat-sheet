# AGENTS.md - Kimi Cheat Sheet

## Quick Reference

- **Purpose**: Reference guide for Kimi Code CLI
- **Official Docs**: https://moonshotai.github.io/kimi-cli/
- **Verify**: `kimi --help` before documenting

## Key Principles

1. **Accuracy First** - Verify all commands against official Kimi CLI
2. **Think Critically** - Help users understand WHEN, not just HOW
3. **Stay Current** - Kimi CLI updates frequently
4. **No Hype** - Focus on practical utility

## Structure

- **Level 1-5**: Progressive learning path
- **Command Reference**: Quick lookup table
- **Best Practices**: Guidelines for effective use

## When Making Changes

- Verify commands with `kimi --help`
- Check official docs: https://moonshotai.github.io/kimi-cli/
- Maintain consistent formatting with collapsible sections
- Update "Last updated" date in README

## Target Audience

Developers who:
- Want to leverage AI assistance effectively
- Value understanding over memorization
- Need practical patterns for real work

## Working Rules

- Stop and explain before major architectural changes
- One change per commit, commit before starting next
- Do not bundle unrelated work into the same commit
- **Branch flow (canonical):** All changes go through `develop`. Branch a topic branch off `develop`, make the change, merge the topic branch into `develop`, then merge `develop` into `main`. Never open a PR directly from a topic branch to `main`. This keeps `develop` as the integration branch and makes contribution easy to demonstrate and follow.

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **kimi-cheat-sheet** (150 symbols, 147 relationships, 0 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> Index stale? Run `node .gitnexus/run.cjs analyze` from the project root — it auto-selects an available runner. No `.gitnexus/run.cjs` yet? `npx gitnexus analyze` (npm 11 crash → `npm i -g gitnexus`; #1939).

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows. For regression review, compare against the default branch: `detect_changes({scope: "compare", base_ref: "main"})`.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `query({search_query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `context({name: "symbolName"})`.
- For security review, `explain({target: "fileOrSymbol"})` lists taint findings (source→sink flows; needs `analyze --pdg`).

## Never Do

- NEVER edit a function, class, or method without first running `impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `rename` which understands the call graph.
- NEVER commit changes without running `detect_changes()` to check affected scope.

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/kimi-cheat-sheet/context` | Codebase overview, check index freshness |
| `gitnexus://repo/kimi-cheat-sheet/clusters` | All functional areas |
| `gitnexus://repo/kimi-cheat-sheet/processes` | All execution flows |
| `gitnexus://repo/kimi-cheat-sheet/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Understand architecture / "How does X work?" | `.claude/skills/gitnexus/gitnexus-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/gitnexus/gitnexus-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/gitnexus/gitnexus-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/gitnexus/gitnexus-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/gitnexus/gitnexus-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/gitnexus/gitnexus-cli/SKILL.md` |

<!-- gitnexus:end -->
