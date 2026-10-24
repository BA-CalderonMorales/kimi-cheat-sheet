<div align="center">

# Kimi Cheat Sheet

<a href="https://www.kimi.com/"><img width="1040" height="476" alt="Kimi cheat sheet" src="assets/image.png" /></a>

> A working reference for **Kimi Code CLI** ([github.com/MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code)). Every command below was checked against Kimi Code 2.3.1 and the [official docs](https://moonshotai.github.io/kimi-code/).

</div>

> **Kimi Code is the current CLI.** The old Python `kimi-cli` was archived in September 2026 and its final release (1.52.0) is a deprecation stub. Bare `kimi` now prints a notice and installs Kimi Code for you.
>
> - New here? Start with the [install guide](https://github.com/MoonshotAI/kimi-code#readme) and the [official docs](https://moonshotai.github.io/kimi-code/).
> - Coming from the old CLI? See [Migrating](#migrating-from-the-old-kimi-cli) below.

## Quick Start

```bash
# Install (macOS/Linux, single binary, no Node required)
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash

# Or with npm (needs Node 22.19+)
npm install -g @moonshot-ai/kimi-code

# Or with Homebrew
brew install kimi-code

# Windows
irm https://code.kimi.com/kimi-code/install.ps1 | iex

# Launch and check the version
kimi
kimi --version
```

The binary is called `kimi` whichever way you install it.

## Table of Contents

- **[Level 1: Getting Started](#level-1-getting-started)**
- **[Level 2: Basic Commands](#level-2-basic-commands)**
- **[Level 3: Intermediate Usage](#level-3-intermediate-usage)**
- **[Level 4: Advanced Features](#level-4-advanced-features)**
- **[Level 5: Expert Workflows](#level-5-expert-workflows)**
- **[Command Reference](#command-reference)**
- **[Migrating from the old Kimi CLI](#migrating-from-the-old-kimi-cli)**
- **[Best Practices](#best-practices)**

## Level 1: Getting Started

<details>
<summary><strong>Installation and Login</strong></summary>

```bash
# Install
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash

# Verify
kimi --version

# Log in from the terminal (device-code flow, no TUI)
kimi login

# Or log in from inside a session with /login
```

`kimi login` prints a verification URL and a code. Open the URL, enter the code, and the token lands in the same place the TUI stores it.

</details>

<details>
<summary><strong>First Steps</strong></summary>

```bash
kimi                              # interactive session in this directory
kimi -p "explain this codebase"   # one prompt, non-interactive, prints the reply
kimi --continue                   # pick up the most recent session here
kimi --session                    # pick a session from a list
kimi --session 01HZ...XYZ         # resume a specific session
```

</details>

<details>
<summary><strong>Basic Navigation</strong></summary>

```bash
# Keyboard shortcuts
Enter                     # submit
Shift-Enter / Ctrl-J      # newline
↑/↓                       # browse input history
Esc                       # close a popup, cancel a completion, or stop streaming
Ctrl-C                    # interrupt streaming output, or clear the input box
Ctrl-D                    # exit (with an empty input box)
Shift-Tab                 # toggle Plan mode
!                         # shell mode from an empty prompt
Ctrl-G                    # edit the current input in $VISUAL or $EDITOR
Ctrl-V                    # paste an image or video (Alt-V on Windows)
Ctrl-S                    # steer the running turn with your input
Ctrl-O                    # expand or collapse tool output
Ctrl-E                    # expand the full diff in an approval prompt
Ctrl-T                    # expand or collapse the todo list
Esc Esc                   # open the undo selector

# Additional directories
kimi --add-dir /path/to/shared
```

</details>

## Level 2: Basic Commands

<details>
<summary><strong>Permission Modes</strong></summary>

```bash
kimi                             # manual: ask before each risky action
kimi --yolo                      # "Ask When Needed": routine edits and commands run, risky ones still ask
kimi --auto                      # "Never Ask": everything runs and is decided automatically
kimi --plan                      # start in Plan mode
```

Three modes, and the middle one is not what the old `--yolo` did. In Kimi Code, `--yolo` skips approval for regular tool calls but still asks about risky actions, questions, and plan exits. `--auto` skips all of it.

| Mode | Use it for |
|---|---|
| Manual (default) | Day-to-day work where you want to see each step |
| Ask When Needed (`--yolo`) | Trusted repos, repetitive edits, batch refactors |
| Never Ask (`--auto`) | CI, scripted runs, sandboxed environments |

Plan mode is never bypassed by `--yolo`. Exiting plan mode still needs your review.

</details>

<details>
<summary><strong>Session Management</strong></summary>

```bash
kimi --continue                   # most recent session in this directory
kimi --session                    # interactive picker
kimi -S 01HZ...XYZ                # resume by ID

kimi export                       # export the most recent session as a ZIP
kimi export 01HZ...XYZ -o out.zip
kimi export -y                    # skip the confirmation prompt

kimi session list                 # list sessions non-interactively
```

Inside a session, `/export` writes a Markdown file. `/export-debug-zip` writes the debug archive.

</details>

<details>
<summary><strong>Slash Commands</strong></summary>

Type `/` in the TUI to see the list. These are the ones in 2.3.1:

```bash
# Account and configuration
/login                    # log in (OAuth device code for Kimi Code, API key for Kimi Platform)
/logout                   # clear credentials
/provider                 # manage providers and refresh model lists
/model                    # switch model
/secondary-model          # pick the model subagents use (alias: /subagent-model)
/settings                 # open the settings panel (alias: /config)
/permission               # choose a permission mode
/experiments              # experimental features (alias: /experimental)
/editor                   # set the external editor
/theme                    # switch the theme

# Session management
/new                      # fresh session (alias: /clear)
/sessions                 # browse and restore sessions (alias: /resume)
/tasks                    # background task list (alias: /task)
/fork                     # fork the session, keep this one open
/title [text]             # show or set the session title (alias: /rename)
/compact [instruction]     # compact the context
/undo [count]             # undo recent prompts
/reload                   # reload config.toml and tui.toml
/reload-tui               # reload tui.toml only
/init                     # generate AGENTS.md
/export-md [path]         # export the session as Markdown (alias: /export)
/export-debug-zip         # export the session as a debug ZIP
/copy                     # copy the last assistant message
/add-dir [path]           # add a workspace directory
/web                      # open this session in the web UI
/desktop                  # open the desktop app page (alias: /install-desktop)

# Modes and run control
/yolo                     # Ask When Needed (alias: /yes)
/auto                     # Never Ask
/plan [on|off]            # toggle Plan mode
/swarm                    # swarm mode on or off
/tower                    # Tower multi-agent mode
/goal                     # autonomous goal mode

# Information
/help                     # shortcuts and command list (aliases: /h, /?)
/btw [question]           # side question, does not touch the main conversation
/usage                    # token usage and quota
/status                   # session runtime state
/mcp                      # MCP servers and their status
/plugins                  # plugin manager
/version                  # version number
/feedback                 # send feedback (alias: /bug)

# Exit
/exit                     # quit (aliases: /quit, /q)
```

Built-in skills ship as their own slash commands: `/mcp-config`, `/custom-theme`, `/update-config`, `/check-kimi-code-docs`, `/import-from-cc-codex`, and `/sub-skill`.

Your own skills show up as `/skill:<name>`. Sub-skills appear as `/<parent>.<sub>`, for example `/code-style.review`.

</details>

## Level 3: Intermediate Usage

<details>
<summary><strong>Configuration</strong></summary>

```bash
# ~/.kimi-code/config.toml   runtime settings
# ~/.kimi-code/tui.toml      terminal UI preferences
# ~/.kimi-code/mcp.json      MCP servers
# Override the whole directory with KIMI_CODE_HOME

# Most useful settings
default_model = "kimi-code/k3"
default_permission_mode = "manual"     # manual | yolo | auto
default_plan_mode = false
merge_all_available_skills = true
telemetry = true

[thinking]
enabled = true
effort = "high"                       # low | medium | high | xhigh | max

[loop_control]
max_attempts_per_step = 10
reserved_context_size = 50000

[task]
max_running_tasks = 4
```

Validate a config before you switch to it:

```bash
kimi doctor                    # check config.toml and tui.toml
kimi doctor config ./config.toml
kimi doctor tui ./tui.toml
```

</details>

<details>
<summary><strong>Model Selection</strong></summary>

```bash
# Managed aliases are prefixed with kimi-code/
kimi -m kimi-code/kimi-for-coding
kimi -m kimi-code/k3

# Switch from inside a session
/model

# Refresh the model list from providers
/provider refresh
```

| Model ID | Context | Notes |
|---|---|---|
| `kimi-code/k3.1-pro` | 1M | Flagship, released Oct 23 2026 |
| `kimi-code/k3.1-pro-highspeed` | 1M | Roughly 2-3x faster than the flagship |
| `kimi-code/k3` | 1M | K3, 2.8T params |
| `kimi-code/k3-256k` | 256K | K3 on a smaller context budget |
| `kimi-code/kimi-for-coding` | 1M | K2.8 Preview, the default for coding |
| `kimi-code/kimi-for-coding-highspeed` | 256K | K2.7 Code, 5-6x faster, higher price |

Effort levels are `low`, `high`, and `max` on the K3 family. K2.8 Preview defaults to `max`. K3.1 Pro rejects thinking-disabled requests.

The `kimi-k2*` series is retired. Do not put it in a config.

Subagents can run on a different, cheaper model:

```toml
[secondary_model]
default_model = "kimi-code/kimi-for-coding-highspeed"
```

</details>

<details>
<summary><strong>Custom Agents</strong></summary>

```bash
# Start a session with a specific agent
kimi --agent reviewer
kimi --agent-file /path/to/agent.md
```

The agent is bound when the session is created and cannot be switched later in that session. `--agent` and `--agent-file` cannot be combined, and neither works with `--session` or `--continue`.

</details>

<details>
<summary><strong>AGENTS.md for Project Context</strong></summary>

```markdown
# AGENTS.md in the project root

## Tech Stack
- Python 3.12 with FastAPI
- PostgreSQL
- pytest

## Patterns
- Use dependency injection
- Write async functions for I/O
- Follow PEP 8
```

`/init` writes one for you by analyzing the project.

</details>

## Level 4: Advanced Features

<details>
<summary><strong>MCP Integration</strong></summary>

```bash
# Configure in the TUI
/mcp-config

# Or edit ~/.kimi-code/mcp.json
```

```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": { "CONTEXT7_API_KEY": "{env:CONTEXT7_API_KEY}" }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest"]
    }
  }
}
```

Project-local servers go in `<project>/.kimi-code/mcp.json`.

Timeouts live in `config.toml` under `[mcp]`:

```toml
[mcp]
startup_timeout_ms = 30000
tool_timeout_ms = 60000
default_deferred = false     # load tools on demand
```

</details>

<details>
<summary><strong>Agent Skills</strong></summary>

```bash
# Load skills from a custom directory, replacing auto-discovery for this run
kimi --skills-dir /path/to/team-skills

# Or add directories permanently
# extra_skill_dirs = ["~/my-skills-collection"] in config.toml
```

Skills are `SKILL.md` files with YAML frontmatter:

```markdown
---
name: your-skill-name
description: When and why to use this skill
---

Detailed instructions here.
```

Invoke one with `/skill:<name>`.

</details>

<details>
<summary><strong>Non-Interactive Automation</strong></summary>

```bash
# One prompt, print the reply
kimi -p "summarize all TODO comments"

# Machine-readable output, one JSON object per line
kimi -p "list changed files" --output-format stream-json

# Pipe input
cat error.log | kimi -p "find the root cause"

# Redirect output
kimi -p "generate docs" > output.md
```

In `-p` mode no approval is requested: regular tool calls run under the `auto` policy, while static deny rules still apply. `--output-format` only works with `--prompt`, and `--prompt` cannot be combined with `--yolo`, `--auto`, or `--plan`.

Exit codes are meaningful: `0` when the goal completes, `3` when it blocks, `6` when it pauses.

</details>

<details>
<summary><strong>Background Tasks</strong></summary>

```toml
[task]
max_running_tasks = 4
keep_alive_on_exit = false
bash_task_timeout_s = 600
print_background_mode = "steer"
```

Background tasks come from the Bash tool or a subagent's `run_in_background`. In print mode Kimi Code stays alive while they run, so a slow build does not end the run.

</details>

<details>
<summary><strong>Shell Mode</strong></summary>

Press `!` in an empty prompt to drop into a shell. Commands run in the session's working directory and their output stays in the session. Press `Ctrl-B` while a command runs to move it to a background task.

</details>

<details>
<summary><strong>Hooks</strong></summary>

```toml
[[hooks]]
event = "PreToolUse"
matcher = "Bash"
command = "node ~/.kimi-code/hooks/check-bash.mjs"
timeout = 5
```

Hooks run scripts at lifecycle checkpoints. The useful ones are formatting after an edit, extra approval on a dangerous command, and notifications when a long task finishes.

</details>

<details>
<summary><strong>IDE Integration (ACP)</strong></summary>

```bash
# Run as an ACP server
kimi acp
```

```json
{
  "agent_servers": {
    "Kimi Code": {
      "type": "custom",
      "command": "kimi",
      "args": ["acp"]
    }
  }
}
```

The editor starts the process itself, so you rarely run `kimi acp` by hand. See [IDE Integration](https://moonshotai.github.io/kimi-code/en/guides/ides.html).

</details>

## Level 5: Expert Workflows

<details>
<summary><strong>Web Interface</strong></summary>

```bash
kimi web                      # run the server and open the browser
kimi web --no-open            # start it without opening a browser
kimi web --port 58628         # pick a port
kimi web rotate-token         # issue a new bearer token
```

The server binds to loopback by default and prints a bearer token that the web UI picks up from the URL fragment. `--dangerous-bypass-auth` turns authentication off entirely. Only use that on a trusted network.

`kimi server` is deprecated and prints a notice instead of running. Use `kimi web`.

</details>

<details>
<summary><strong>Remote Control</strong></summary>

```bash
kimi rc          # alias: kimi remote
```

Runs the local server and opens the web UI through Remote Control, so you can reach it from another device.

</details>

<details>
<summary><strong>Session Visualizer</strong></summary>

```bash
kimi vis                          # home view listing sessions
kimi vis 01HZ...XYZ               # open one session
kimi vis --host 0.0.0.0 --port 8123 --no-open
```

Useful for watching how the agent reached a decision.

</details>

<details>
<summary><strong>Providers</strong></summary>

```bash
kimi provider list
kimi provider list --json
kimi provider catalog list anthropic
kimi provider catalog add anthropic --api-key sk-ant-...
kimi provider remove <providerId>
```

Provider types are `kimi`, `anthropic`, `openai`, `openai_responses`, `google-genai`, and `vertexai`. Credentials come from the config file, not the shell environment, unless you point `api_key_env` at a variable.

</details>

<details>
<summary><strong>Piping and Scripting</strong></summary>

```bash
git diff | kimi -p "create a commit message"

#!/bin/bash
FILES=$(find src -name "*.py")
echo "$FILES" | kimi -p "check for syntax errors"

cat README.md | kimi -p "extract API endpoints" | grep http
```

</details>

<details>
<summary><strong>Goal Mode</strong></summary>

```bash
/goal Update the checkout docs, run docs build, and stop if still blocked after 20 turns
```

`/goal` keeps an objective alive across automatically continuing turns. Subcommands: `status`, `pause`, `resume`, `cancel`, `replace <objective>`, and `next <objective>`.

If your objective starts with one of those words, put `--` first:

```bash
/goal -- cancel the old rollout note after the new docs are published
```

</details>

## Command Reference

### Global Options

| Option | Description |
|---|---|
| `-V, --version` | Print the version and exit |
| `-h, --help` | Show help |
| `-S, --session [id]` | Resume a session; with an ID opens it, without one opens a picker |
| `-c, --continue` | Continue the most recent session in this directory |
| `-m, --model <model>` | Model alias for this run; defaults to `default_model` |
| `-p, --prompt <prompt>` | Run one prompt non-interactively and print the reply |
| `--output-format <format>` | `text` or `stream-json`; only valid with `--prompt` |
| `-y, --yolo` | Start in Ask When Needed mode |
| `--auto` | Start in Never Ask mode |
| `--plan` | Start in Plan mode |
| `--skills-dir <dir>` | Load skills from this directory instead of the discovered ones; repeatable |
| `--agent <name>` | Start the session with this agent |
| `--agent-file <path>` | Load an agent definition from a Markdown file and select it |
| `--add-dir <dir>` | Add a workspace directory; repeatable |

`-r` and `--resume` are hidden aliases for `--session`. `--yes` and `--auto-approve` are hidden aliases for `--yolo`.

Mutually exclusive combinations, rejected at startup: `--continue` with `--session`, `--yolo` with `--auto`, and `--prompt` with `--yolo`, `--auto`, or `--plan`.

### Subcommands

| Command | Description |
|---|---|
| `kimi login` | Log in with the device-code flow |
| `kimi doctor` | Validate `config.toml` and `tui.toml` |
| `kimi export` | Export a session as a ZIP |
| `kimi fork` | Fork a session into a new session |
| `kimi migrate` | Migrate data from a legacy kimi-cli install |
| `kimi upgrade` | Check for and install updates (alias: `kimi update`) |
| `kimi provider` | Manage providers (`add`, `remove`, `list`, `catalog`) |
| `kimi session` | Manage sessions (`list`) |
| `kimi acp` | Run as an ACP server over stdio |
| `kimi web` | Run the local server and open the web UI |
| `kimi rc` | Run the local server through Remote Control (alias: `kimi remote`) |
| `kimi vis` | Open the session visualizer |
| `kimi app` | Open the desktop app with a new chat for this directory |
| `kimi install-desktop` | Open the desktop app download page |
| `kimi server` | Deprecated; prints a notice and exits |

### Data Locations

| Path | Contents |
|---|---|
| `~/.kimi-code/config.toml` | Runtime settings |
| `~/.kimi-code/tui.toml` | Terminal UI preferences |
| `~/.kimi-code/mcp.json` | MCP servers |
| `~/.kimi-code/credentials/` | OAuth tokens |
| `~/.kimi-code/sessions/` | Session history |
| `~/.kimi-code/skills/` | User-level skills |
| `~/.kimi-code/plugins/` | Plugins |
| `~/.kimi-code/logs/kimi-code.log` | Diagnostic log |
| `<project>/.kimi-code/local.toml` | Project-local workspace settings |

## Migrating from the old Kimi CLI

The old Python `kimi-cli` was archived on September 23, 2026. Release 1.52.0 is a stub: running `kimi` with no arguments prints a deprecation notice and runs the Kimi Code installer instead.

```bash
# Migrate config, MCP servers, history, and chosen sessions
kimi migrate

# Non-interactive
kimi migrate --run
kimi migrate --run --config-only
```

Migrated: `config.toml`, MCP server definitions, input history, and selected sessions (tagged `[imported]`).

Not migrated: OAuth login credentials, MCP OAuth authorizations, and kimi-cli plugins. Run `/login` again and re-authorize each MCP server.

Migration never modifies or deletes `~/.kimi/`. Once you are happy with Kimi Code, remove the old package so its `kimi` executable stops shadowing the new one:

```bash
uv tool uninstall kimi-cli     # if you installed it with uv
brew uninstall kimi-cli        # if you used Homebrew
```

## Best Practices

### Think Critically

- Read the diff before you accept it
- Use Plan mode when you are still deciding what to build
- Start in manual mode; switch to Ask When Needed only for trusted repos
- Push back when the plan feels wrong

### Stay Secure

- Keep API keys in `api_key_env`, not in `config.toml`
- Deny dangerous commands with `[[permission.rules]]`
- Review what each MCP server can reach before you connect it
- Keep `Never Ask` mode for isolated environments, not your laptop

### Work Effectively

- Commit an `AGENTS.md` so every session starts with the same context
- Package repeated workflows as skills
- Use sessions for multi-turn problems, and fork when you want to explore a different approach
- Give subagents a cheaper model through `[secondary_model]`

## Additional Resources

**Official documentation:**
- [Kimi Code docs](https://moonshotai.github.io/kimi-code/) - Documentation hub
- [Getting started](https://moonshotai.github.io/kimi-code/en/guides/getting-started.html) - Install and first run
- [kimi command](https://moonshotai.github.io/kimi-code/en/reference/kimi-command.html) - Flags and subcommands
- [Slash commands](https://moonshotai.github.io/kimi-code/en/reference/slash-commands.html) - TUI command reference
- [Keyboard shortcuts](https://moonshotai.github.io/kimi-code/en/reference/keyboard.html) - Key bindings
- [Config files](https://moonshotai.github.io/kimi-code/en/configuration/config-files.html) - Every setting
- [Providers and models](https://moonshotai.github.io/kimi-code/en/configuration/providers.html) - Model IDs and credentials
- [MCP](https://moonshotai.github.io/kimi-code/en/customization/mcp.html) - MCP setup
- [Skills](https://moonshotai.github.io/kimi-code/en/customization/skills.html) - Agent skills
- [Migration guide](https://moonshotai.github.io/kimi-code/en/guides/migration.html) - From kimi-cli

**Repositories:**
- [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) - The current CLI. MIT licensed, active development
- [Kimi Code docs](https://moonshotai.github.io/kimi-code/) - Documentation hub
- [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) - Archived Python CLI, kept for reference

**Install and getting started:**
- [kimi.com/code](https://www.kimi.com/code) - Product page and desktop app
- [Getting started](https://moonshotai.github.io/kimi-code/en/guides/getting-started.html) - Install and first run

**Related tools:**
- [Codex Cheat Sheet](https://github.com/BA-CalderonMorales/codex-cheat-sheet) - Companion guide for OpenAI Codex CLI
- [OpenCode Cheat Sheet](https://github.com/BA-CalderonMorales/opencode-cheat-sheet) - Companion guide for OpenCode

## Contributing

Corrections are welcome. Report anything that no longer matches `kimi --help`.

- Report bugs or inconsistencies
- Suggest new examples
- Improve documentation
- Share your workflows

## License

MIT License. Free to use and modify.

---

**Last updated: October 2026**
**Based on**: Kimi Code CLI 2.3.1 (npm: `@moonshot-ai/kimi-code`, Homebrew: `kimi-code`)
