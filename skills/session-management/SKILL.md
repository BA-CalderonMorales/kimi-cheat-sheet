---
name: session-management
description: Use Kimi Code sessions effectively for multi-turn problem solving
---

# Session Management

Sessions preserve context across turns.

## Continue the previous session

```bash
kimi --continue
```

## Resume a specific session

```bash
kimi --session 01HZ...XYZ
kimi --session          # interactive picker
```

Inside a session, `/sessions` opens the same picker.

## Export a session

```bash
kimi export                      # most recent session, as a ZIP
kimi export 01HZ...XYZ -o out.zip
kimi export -y                   # skip the confirmation prompt
```

Inside a session, `/export` writes Markdown and `/export-debug-zip` writes the debug archive.

## Fork instead of starting over

```bash
kimi fork 01HZ...XYZ
```

Or use `/fork` in the TUI. The original stays untouched, so you can try a different approach without losing the original.

## When to start fresh

- The context has picked up clutter from an unrelated task
- You are switching to different work
- Earlier attempts led nowhere and a clean read will help
- You want to try a different approach

## Good habits

- Use sessions for multi-step problems, new sessions for unrelated work
- Export anything you want to keep before a major change
- Give the session a title with `/title` so you can find it later
