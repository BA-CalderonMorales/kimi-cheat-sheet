<div align="center">

# Kimi Cheat Sheet

<a href="https://www.kimi.com/"><img width="1040" height="476" alt="Kimi cheat sheet" src="assets/image.png" /></a>

> **Your practical guide to using Kimi Code CLI effectively — from first steps to advanced workflows.**

A reference for developers who want to leverage Kimi's agentic capabilities while staying in control. Focuses on patterns that augment your thinking, not replace it.

> **Note:** Kimi CLI is evolving into [Kimi Code](https://github.com/MoonshotAI/kimi-code) — the next-generation terminal AI agent from the same team. Installing Kimi Code automatically migrates your configuration and sessions. This project remains available; see the [official docs](https://moonshotai.github.io/kimi-cli/en/) for the latest.

**Based on official Kimi CLI documentation** — Commands verified against the [official Kimi repository](https://github.com/MoonshotAI/kimi-cli). For the latest updates, refer to the official docs.

</div>

## Quick Start

```bash
# Install with the official script (installs uv first)
curl -LsSf https://code.kimi.com/install.sh | bash

# Or via uv (Python 3.12-3.14 supported, 3.13 recommended)
uv tool install --python 3.13 kimi-cli

# Upgrade
uv tool upgrade kimi-cli --no-cache

# Launch Kimi
kimi

# Check version
kimi --version
```

## Table of Contents

- **[Level 1: Getting Started](#level-1-getting-started)**
- **[Level 2: Basic Commands](#level-2-basic-commands)**
- **[Level 3: Intermediate Usage](#level-3-intermediate-usage)**
- **[Level 4: Advanced Features](#level-4-advanced-features)**
- **[Level 5: Expert Workflows](#level-5-expert-workflows)**
- **[Command Reference](#command-reference)**
- **[Best Practices](#best-practices)**

## Level 1: Getting Started

Essential commands to start using Kimi effectively.

<details>
<summary><strong>Installation & Setup</strong></summary>

```bash
# Install with the official script (installs uv first)
curl -LsSf https://code.kimi.com/install.sh | bash

# Or via uv
uv tool install --python 3.13 kimi-cli

# Verify installation
kimi --version

# Login to your Kimi account
kimi login

# Check your configuration
kimi info
```

</details>

<details>
<summary><strong>First Steps</strong></summary>

```bash
# Start interactive mode
kimi

# Run with a specific prompt
kimi -p "explain this codebase"

# Run in non-interactive mode (print mode)
kimi --print "explain this codebase"

# Continue previous session
kimi --continue

# Resume specific session
kimi --session <SESSION_ID>
```

> **Login:** On first launch, run `/login` inside the session — pick **Kimi Code** for browser OAuth, or another platform and enter an API key. `/login` (and `/model`) require the default config file; they are unavailable when `--config` or `--config-file` is used.

</details>

<details>
<summary><strong>Basic Navigation</strong></summary>

```bash
# Keyboard shortcuts in interactive mode
Ctrl+C                    # Interrupt current operation / clear input
Ctrl+D                    # Exit Kimi
Ctrl-X                    # Toggle agent/shell mode
Shift-Tab                 # Toggle plan mode
Ctrl-O                    # Edit in external editor
Ctrl-J / Alt-Enter        # Insert newline
Ctrl-S                    # Steer: inject input into the running turn
Ctrl-V                    # Paste (text, images, video)
Ctrl-E                    # Expand full approval request content
↑/↓                       # History / question navigation

# Completion menu: type / for slash commands, @ for file paths
# (arrow keys + Enter to select)

# Working directory options
kimi -w /path/to/project                    # Set working directory
kimi --add-dir /path/to/shared              # Add additional directory
```

</details>

## Level 2: Basic Commands

Core patterns for everyday development.

<details>
<summary><strong>Thinking Mode</strong></summary>

```bash
# Enable thinking mode (shows reasoning)
kimi --thinking

# Disable thinking for faster responses
kimi --no-thinking

# Thinking mode helps you understand HOW Kimi approaches problems,
# not just the solution. Use it when learning new patterns.
```

</details>

<details>
<summary><strong>Approval Modes</strong></summary>

```bash
# Interactive mode (default) — approve each action
kimi

# YOLO mode — auto-approve all actions, user still reachable
kimi --yolo

# AFK mode — auto-approve all actions and auto-dismiss questions
kimi --afk

# Print mode — non-interactive, implicitly enables --afk
kimi --print "your prompt"

# Quiet mode — minimal output
kimi --quiet "your prompt"
```

**When to use each:**
- **Interactive**: Default for most work — stay in control
- **YOLO**: Trusted, repetitive tasks in known codebases — user still reachable
- **AFK** (`--afk` or `/afk`): Unattended runs — auto-approves and auto-dismisses questions
- **Print**: CI/CD, automation, scripting (implicitly enables `--afk`)
- **Quiet**: Piping output to other tools

</details>

<details>
<summary><strong>Session Management</strong></summary>

```bash
# Continue previous session
kimi --continue

# Export a session as a ZIP archive
# (context.jsonl, wire.jsonl, state.json, ...)
kimi export -o session-backup.zip

# Sessions persist context — use them for multi-turn problem solving
# (Inside a session, /export writes a Markdown file instead)
```

</details>

<details>
<summary><strong>File and Directory Operations</strong></summary>

```bash
# Read files
kimi -p "Read src/app.py and explain the main function"

# Edit files
kimi -p "Add error handling to src/utils.py"

# Multiple directories
kimi --add-dir ../shared --add-dir ../utils -p "analyze all"

# View project structure
kimi -p "Explain the architecture of this project"
```

</details>

<details>
<summary><strong>Interactive Slash Commands</strong></summary>

Use these inside an active Kimi session (type `/` to see the popup).

**Session control:**
```bash
/new                      # Create a new session
/sessions                 # List and switch sessions (alias: /resume)
/title <text>             # View or set session title (alias: /rename)
/undo                     # Roll back to a previous turn and retry
/fork                     # Fork the current session
/clear                    # Clear context and start fresh (alias: /reset)
/compact                  # Manually compact context to reduce tokens
/export                   # Export session to a Markdown file
/import <path|session>    # Import context from a file or session
```

**Configuration:**
```bash
/model                    # Switch model and thinking mode
/login                    # Log in or configure platform (alias: /setup)
/logout                   # Sign out
/reload                   # Reload config without exiting
/editor                   # Set external editor (Ctrl-O to open)
/theme dark|light         # Switch terminal color theme
```

**Approval modes:**
```bash
/yolo                     # Toggle auto-approve all actions
/afk                      # Toggle AFK mode (auto-approves + auto-dismisses questions)
/plan                     # Toggle plan mode (read-only exploration)
```

**Skills and workspace:**
```bash
/skill:<name>             # Load a specific skill
/flow:<name>              # Execute a flow skill
/add-dir <path>           # Add directory to workspace scope
/init                     # Analyze project and generate AGENTS.md
```

**Debugging and info:**
```bash
/debug                    # Show messages, tokens, checkpoints, history
/usage                    # Show API usage and quota (alias: /status)
/mcp                      # Show connected MCP servers and tools
/hooks                    # Show configured hooks
/task                     # Open background task browser
/web                      # Switch to Web UI
/vis                      # Switch to Agent Tracing Visualizer
```

**Utility:**
```bash
/btw <question>           # Ask a side question without interrupting main chat
/help                     # Show help (aliases: /h, /?)
/version                  # Show version
/changelog                # Show recent changelog (alias: /release-notes)
/feedback                 # Submit feedback
/upgrade                  # Install Kimi Code (automatic migration)
```

</details>

## Level 3: Intermediate Usage

Configuration and customization options.

<details>
<summary><strong>Configuration</strong></summary>

```bash
# Config file location: ~/.kimi/config.toml (TOML or JSON)

# Common settings:
# - default_model
# - default_thinking
# - default_yolo
# - default_plan_mode
# - theme (dark/light)
# - default_editor
# - skip_afk_prompt_injection
# - show_thinking_stream
# - merge_all_available_skills (default true)
# - telemetry (default true)
# - loop_control.max_steps_per_turn (default 1000)

# Use custom config file (TOML or JSON)
kimi --config-file /path/to/config.toml

# Inline config override (TOML or JSON)
kimi --config '{"default_thinking": false}'
```

</details>

<details>
<summary><strong>Model Selection</strong></summary>

```bash
# Use specific model (kimi-for-coding is the default model)
kimi -m kimi-for-coding

# List and switch models interactively
# Run /model inside a session (refreshes the model list)

# Model capabilities vary — check kimi info for details
```

</details>

<details>
<summary><strong>Custom Agents</strong></summary>

```bash
# Use built-in agent
kimi --agent okabe

# Use custom agent file
kimi --agent-file /path/to/agent.yaml

# Agents define behavior patterns — use them to specialize Kimi for specific tasks
```

</details>

<details>
<summary><strong>AGENTS.md for Project Context</strong></summary>

```bash
# Create AGENTS.md in project root
# Kimi will read this for project-specific context

# Example AGENTS.md content:
"""
# Project Guidelines

## Tech Stack
- Python 3.12 with FastAPI
- PostgreSQL database
- pytest for testing

## Patterns
- Use dependency injection
- Write async functions for I/O
- Follow PEP 8 style guide
"""
```

</details>

## Level 4: Advanced Features

Powerful features for complex workflows.

<details>
<summary><strong>MCP Integration</strong></summary>

```bash
# MCP (Model Context Protocol) extends Kimi with external tools

# Add streamable HTTP server
kimi mcp add --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY: your-key"

# Add stdio server
kimi mcp add --transport stdio chrome-devtools -- npx chrome-devtools-mcp@latest

# List configured servers
kimi mcp list

# Remove a server
kimi mcp remove chrome-devtools

# Authorize an MCP server (OAuth)
kimi mcp auth linear

# Test a server connection and list its tools
kimi mcp test context7

# Clear a cached OAuth token (re-auth with kimi mcp auth <name>)
kimi mcp reset-auth linear

# MCP enables:
# - Database connections
# - API integrations
# - Custom tools
```

MCP server config lives in `~/.kimi/mcp.json` (`mcpServers` format, compatible with other MCP clients):

```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "your-key"
      }
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest"]
    }
  }
}
```

Or load from another file / pass JSON directly:

```bash
kimi --mcp-config-file /path/to/mcp.json
kimi --mcp-config '{"mcpServers": {"test": {"url": "https://..."}}}'
```

</details>

<details>
<summary><strong>Skills System</strong></summary>

```bash
# Skills are reusable capabilities
# User-level: ~/.kimi/skills/**/SKILL.md
# (also ~/.claude/skills/, ~/.codex/skills/ — merged by default)
# Project-level: .kimi/skills/, .claude/skills/, .codex/skills/ (repo root)
# Discovery priority: Project > User > Extra > Built-in
# Single-file <name>.md skills are also supported

# Add extra skills directories (additive, via config)
# extra_skill_dirs = ["~/my-skills-collection"]

# Override auto-discovery with your own directories (repeatable)
kimi --skills-dir /path/to/custom/skills

# Skill format (YAML frontmatter + body):
# ---
# name: your-skill-name
# description: When and why to use this skill
# ---
# Detailed instructions here
```

</details>

<details>
<summary><strong>Non-Interactive Automation</strong></summary>

```bash
# Print mode for automation
kimi --print "summarize all TODO comments"

# With input piping
cat error.log | kimi --print "find the root cause"

# With output redirection
kimi --print "generate docs" > output.md

# Machine-readable output (JSONL)
kimi --print --output-format stream-json "analyze this"
```

</details>

<details>
<summary><strong>Background Tasks</strong></summary>

```bash
# Kimi supports background task execution
# Configure in ~/.kimi/config.toml:
# [background]
# max_running_tasks = 4

# Useful for long-running operations
```

</details>

<details>
<summary><strong>Shell Command Mode</strong></summary>

Kimi CLI doubles as a shell. Press Ctrl+X to toggle shell command mode, letting you run shell commands directly without leaving Kimi.

```bash
# In interactive mode, press Ctrl+X to switch to shell mode
# Run any shell command natively
ls -la
git status
npm test

# Press Ctrl+X again to return to agent mode
```

Built-in shell commands like `cd` are handled by the agent, not the shell.
</details>

<details>
<summary><strong>IDE Integration (ACP)</strong></summary>

Kimi CLI supports Agent Client Protocol (ACP) for IDE integration:

```bash
# Start as ACP server
kimi acp

# Configure in Zed (~/.config/zed/settings.json):
# {
#   "agent_servers": {
#     "Kimi CLI": {
#       "type": "custom",
#       "command": "kimi",
#       "args": ["acp"],
#       "env": {}
#     }
#   }
# }

# VS Code extension available via:
# Kimi Code VS Code Extension in marketplace
```

See [IDE Integration Docs](https://moonshotai.github.io/kimi-cli/en/guides/ides.html) for details.
</details>

<details>
<summary><strong>Zsh Integration</strong></summary>

Use Kimi CLI with Zsh for AI-powered shell:

```bash
# Install zsh-kimi-cli plugin
git clone https://github.com/MoonshotAI/zsh-kimi-cli.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/kimi-cli

# Add to ~/.zshrc plugins:
plugins=(... kimi-cli)

# Press Ctrl+X to switch to agent mode
```

See [Zsh Integration Guide](https://github.com/MoonshotAI/zsh-kimi-cli) for details.
</details>

## Level 5: Expert Workflows

Advanced patterns for power users.

<details>
<summary><strong>Web Interface</strong></summary>

```bash
# Run Kimi web interface
kimi web

# Provides browser-based interaction
# Useful for visual workflows and sharing
```

</details>

<details>
<summary><strong>Visualization & Debugging</strong></summary>

```bash
# Run agent tracing visualizer
kimi vis

# Helps debug agent decision-making
# Understand HOW Kimi arrived at a solution
```

</details>

<details>
<summary><strong>Plugin System</strong></summary>

```bash
# Manage plugins
kimi plugin list
kimi plugin install <plugin>
kimi plugin remove <plugin>

# Extend Kimi with custom functionality
```

</details>

<details>
<summary><strong>ACP Server Mode</strong></summary>

```bash
# Run as ACP (Agent Communication Protocol) server
kimi acp

# Enables integration with other tools
# Used by term, web, and external integrations
```

</details>

<details>
<summary><strong>Piping and Scripting</strong></summary>

```bash
# Pipe content to Kimi
git diff | kimi --print "create a commit message"

# Use in scripts
#!/bin/bash
FILES=$(find src -name "*.py")
echo "$FILES" | kimi --print "check for syntax errors"

# Combine with other tools
cat README.md | kimi --print "extract API endpoints" | grep http
```

</details>

## Command Reference

### Global Options

| Option | Description |
|--------|-------------|
| `-w, --work-dir` | Set working directory |
| `--add-dir` | Add directory to workspace (repeatable) |
| `-S, --session` / `-r, --resume` | Resume session (with ID; interactive picker without) |
| `-C, --continue` | Continue previous session |
| `-m, --model` | Select model |
| `--thinking / --no-thinking` | Enable/disable thinking mode |
| `-y, --yolo` (aliases `--yes`, `--auto-approve`) | Auto-approve all tool calls; user still reachable |
| `--afk` | Away-from-keyboard: auto-approve and auto-dismiss questions |
| `-p, --prompt` (alias `-c, --command`) | Provide prompt directly |
| `--print` | Non-interactive mode, implicitly enables `--afk` |
| `--quiet` | Shortcut for `--print --output-format text --final-message-only` |
| `--plan` | Start a new session in plan mode |
| `--config` | Load TOML/JSON configuration string |
| `--config-file` | Use custom config file (TOML or JSON) |
| `--agent` | Select built-in agent (`default`, `okabe`) |
| `--agent-file` | Use custom agent file |
| `--mcp-config-file` | Load MCP config file (repeatable) |
| `--mcp-config` | Load MCP config JSON string (repeatable) |
| `--skills-dir` | Append skills directories, overriding auto-discovery (repeatable) |
| `--max-steps-per-turn` | Max steps per turn (default 1000) |
| `--max-retries-per-step` | Max retries per step |
| `--max-ralph-iterations` | Ralph Loop iterations (0 disables, -1 unlimited) |
| `--input-format` | Print-mode input format: `text` or `stream-json` |
| `--output-format` | Print-mode output format: `text` or `stream-json` |
| `--final-message-only` | Only output the final assistant message |
| `-V, --version` | Show version number and exit |
| `--verbose` | Detailed runtime information |
| `--debug` | Log debug info to `~/.kimi/logs/kimi.log` |
| `--acp` | ACP server mode (deprecated, use `kimi acp`) |

### Subcommands

| Command | Description |
|---------|-------------|
| `kimi login` | Authenticate with Kimi |
| `kimi logout` | Sign out |
| `kimi info` | Show version and protocol info |
| `kimi export` | Export a session as a ZIP file |
| `kimi mcp` | Manage MCP configurations |
| `kimi plugin` | Manage plugins |
| `kimi term` | Run Toad TUI |
| `kimi vis` | Run tracing visualizer |
| `kimi web` | Run web interface |
| `kimi acp` | Run ACP server |

## Best Practices

### Think Critically

Kimi is an assistant, not a replacement for your judgment:

- **Review changes** before accepting — understand what changed and why
- **Use thinking mode** when learning — see the reasoning, not just results
- **Start interactive** — switch to --yolo only for trusted, repetitive tasks
- **Question assumptions** — if something feels off, dig deeper

### Stay Secure

- Never commit API keys or credentials
- Review code before running in production
- Use --yolo sparingly in unknown codebases
- Keep sensitive data out of prompts when possible

### Work Effectively

- Use AGENTS.md for project context
- Create skills for repetitive workflows
- Leverage sessions for multi-turn problems
- Combine Kimi with traditional tools (grep, find, git)

### Continuous Learning

- Check kimi info for available capabilities
- Review thinking output to understand patterns
- Build your own skills for domain-specific tasks
- Share effective patterns with your team

## Additional Resources

**Official Kimi Documentation:**
- [Kimi CLI Repository](https://github.com/MoonshotAI/kimi-cli) — Main repository and documentation
- [Kimi Code Repository](https://github.com/MoonshotAI/kimi-code) — Next-generation terminal AI agent
- [Official Documentation](https://moonshotai.github.io/kimi-cli/en/) — Complete documentation
- [LLM-Friendly Version](https://moonshotai.github.io/kimi-cli/en/llms.txt) — Structured for AI consumption

**Related Tools:**
- [Codex Cheat Sheet](https://github.com/BA-CalderonMorales/codex-cheat-sheet) — Companion guide for OpenAI Codex CLI

**Community:**
- GitHub Issues — Bug reports and feature requests
- Discussions — Community Q&A and workflows

## Contributing

Contributions are welcome:

- Report issues or inconsistencies
- Suggest new examples
- Share your workflows
- Improve documentation

## License

MIT License — Free to use and modify.

---

**Last updated: July 2026**  
**Based on**: Kimi Code CLI (pip: kimi-cli)

---
*Last synced: 2026-07-19 via [workspace manager](https://github.com/BA-CalderonMorales)*
