---
name: thinking-mode
description: Decide when to enable or disable thinking mode based on the task
---

# Thinking Mode

Thinking mode shows Kimi's reasoning process, not just the final answer.

## When to Enable

- Learning new concepts or patterns
- Complex problem-solving
- Debugging unfamiliar code
- Understanding architectural decisions

## When to Disable

- Repetitive, well-understood tasks
- Quick lookups or simple edits
- When speed matters more than explanation
- In CI/CD automation

## Command

```bash
kimi --thinking    # Enable
kimi --no-thinking # Disable
```

## Tip

Start with thinking enabled. As you learn Kimi's patterns, disable it for routine tasks.
