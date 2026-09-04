---
name: session-management
description: Use sessions effectively for multi-turn problem solving
---

# Session Management

Sessions preserve context across interactions.

## Continue Previous Session

```bash
kimi --continue
```

## Resume Specific Session

```bash
kimi --session <SESSION_ID>
```

## Export Session Data

Export a session as a ZIP archive (`context.jsonl`, `wire.jsonl`, `state.json`, ...):

```bash
kimi export -o session-backup.zip
```

Inside a session, `/export` writes a Markdown file instead.

## Best Practices

- Use sessions for complex, multi-step problems
- Export important sessions before major changes
- Start fresh sessions for unrelated tasks
- Sessions persist until explicitly cleared

## When to Start Fresh

- Context has become cluttered
- Switching to unrelated work
- Previous attempts led to confusion
- Want to try a different approach
