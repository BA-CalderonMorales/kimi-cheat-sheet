# AGENTS.md - Kimi Cheat Sheet

## Current Shape

- The product is the README single page: progressive levels (Level 1 ->
  Level 5), quick-reference tables, and `<details>` sections for scannable
  command lookups.
- `skills/<name>/` holds on-disk reusable capabilities as `SKILL.md` files
  (mcp-setup, session-management, thinking-mode).
- `assets/` holds the sheet imagery; `.github/workflows/security-scan.yml`
  is the CI gate (shared org-level scan, Trivy by default).
- Community surface: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`.
- Kimi CLI is evolving into Kimi Code; sheet content tracks the official
  docs and calls out the migration path where relevant.
- Pre-rewrite leftovers are pruned; use Git history for legacy reference.

## Key Sections

| To understand... | Read |
|---|---|
| The sheet: levels, commands, examples | `README.md` |
| On-disk skills and how to invoke them | `skills/` |
| Contribution flow and standards | `CONTRIBUTING.md` |
| Official Kimi truth | [moonshotai.github.io/kimi-cli](https://moonshotai.github.io/kimi-cli/) |
| Security gate behavior | `.github/workflows/security-scan.yml` |

Lost in the woods? Start with `README.md` for *what the sheet covers*, then
`CONTRIBUTING.md` for *how changes land*.

## Branch Strategy

- `develop` is the default base for PRs and the integration branch.
- Every change traces: topic branch off `develop`, merge into `develop`,
  then merge `develop` into `main`.
- Never open a PR directly from a topic branch to `main`. This keeps
  `develop` as the integration branch and makes contribution easy to follow.

## CI

- Security scan runs on pushes and PRs against `main` and `develop`
  (org-level reusable workflow); gate failures block merges.

## Rules

- Accuracy first: verify commands with `kimi --help` and the official Kimi
  docs (moonshotai.github.io/kimi-cli) before documenting; update the
  "Last updated" date in the README.
- Think critically - cover WHEN, not just HOW; no hype, only practical
  utility.
- Maintain consistent formatting with collapsible sections; minimal emojis,
  used for structure, not decoration.
- One change per commit; stop and explain before major restructuring; do not
  bundle unrelated work into the same commit.

## Design Principles

- **POLA** - behavior must not astonish: verified flags, current commands,
  no invented workflows.
- **DRY** - the README is the single source of truth; for depth, link to
  official docs instead of restating them.
- **KISS** - a scannable reference beats exhaustive prose; when in doubt,
  delete a section before adding one.
- **DIP** - depend on the official documentation contract, never on
  hearsay; this sheet is a guide to sources, not a replacement for them.

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
