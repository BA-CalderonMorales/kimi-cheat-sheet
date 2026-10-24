---
name: thinking-mode
description: Decide when to turn Kimi Code thinking on or off based on the task
---

# Thinking Mode

Thinking mode shows Kimi's reasoning, not just the final answer.

## How it works in Kimi Code

Thinking is on by default and controlled from the config or the TUI, not from a startup flag. The old `kimi --thinking` and `kimi --no-thinking` flags are gone.

```bash
# In a session
/effort            # alias: /thinking

# In config.toml
[thinking]
enabled = true
effort = "high"    # low | medium | high | xhigh | max
```

Or set `default_effort` per model entry in `[models."<alias>"]`.

## When to turn it on

- Learning a new concept or pattern
- Complex problem-solving
- Debugging unfamiliar code
- Understanding why a design decision was made

## When to turn it off

- Repetitive, well-understood tasks
- Quick lookups or small edits
- When speed matters more than the explanation
- CI and scripted runs

## Watch for the models that do not let you

`kimi-for-coding-highspeed` always thinks, and K3.1 Pro rejects thinking-disabled requests with a 400. Setting `enabled = false` does not turn reasoning off for those.

## Tip

Start with thinking on. Turn it down once you know the task shapes Kimi Code handles well.
