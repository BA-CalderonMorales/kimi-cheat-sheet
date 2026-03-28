<div align="center">

# KIMI CODE CLI CHEAT SHEET (BETA)

<img width="626" height="322" alt="image" src="https://github.com/user-attachments/assets/7bb43810-7bfb-44e1-8a1b-18aea61d4504" />

> **Your practical guide to using Kimi Code CLI effectively — from first steps to advanced workflows.**

A reference for developers who want to leverage Kimi's agentic capabilities while staying in control. Focuses on patterns that augment your thinking, not replace it.

**Based on official Kimi CLI documentation** — Commands verified against the [official Kimi repository](https://github.com/MoonshotAI/kimi-cli). For the latest updates, refer to the official docs.

</div>

## Quick Start

```bash
# Install with pip
pip install kimi-cli

# Or with uv (recommended)
uv pip install kimi-cli

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
# Install with pip
pip install kimi-cli

# Or with uv
uv pip install kimi-cli

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

</details>

<details>
<summary><strong>Basic Navigation</strong></summary>

```bash
# Keyboard shortcuts in interactive mode
Ctrl+C                    # Cancel current operation
Ctrl+D                    # Exit Kimi
Tab                       # Auto-complete
↑/↓                       # Command history

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

# YOLO mode — auto-approve all actions (use with caution)
kimi --yolo

# Print mode — non-interactive, implies --yolo
kimi --print "your prompt"

# Quiet mode — minimal output
kimi --quiet "your prompt"
```

**When to use each:**
- **Interactive**: Default for most work — stay in control
- **YOLO**: Trusted, repetitive tasks in known codebases
- **Print**: CI/CD, automation, scripting
- **Quiet**: Piping output to other tools

</details>

<details>
<summary><strong>Session Management</strong></summary>

```bash
# Continue previous session
kimi --continue

# List sessions (via export)
kimi export --list

# Export session data
kimi export > session_backup.json

# Sessions persist context — use them for multi-turn problem solving
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

## Level 3: Intermediate Usage

Configuration and customization options.

<details>
<summary><strong>Configuration</strong></summary>

```bash
# Config file location: ~/.kimi/config.toml

# Common settings:
# - default_model
# - default_thinking
# - default_yolo
# - max_steps_per_turn
# - mcp client settings

# Use custom config file
kimi --config-file /path/to/custom.toml

# Inline config override
kimi --config 'default_thinking = false'
```

</details>

<details>
<summary><strong>Model Selection</strong></summary>

```bash
# Use specific model
kimi -m kimi-for-coding

# List available models
# (Configured in ~/.kimi/config.toml)

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

# Configure MCP servers in ~/.kimi/config.toml
# Or pass config files:
kimi --mcp-config-file /path/to/mcp.toml

# Manage MCP configurations
kimi mcp list
kimi mcp add <name> -- <command>

# MCP enables:
# - Database connections
# - API integrations
# - Custom tools
```

</details>

<details>
<summary><strong>Skills System</strong></summary>

```bash
# Skills are reusable capabilities
# Location: ~/.kimi/skills/**/SKILL.md

# Add custom skills directories
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

# JSON output
kimi --print --output-format json "analyze this"
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
| `--add-dir` | Add directory to workspace |
| `-S, --session` | Resume specific session |
| `-C, --continue` | Continue previous session |
| `-m, --model` | Select model |
| `--thinking / --no-thinking` | Enable/disable thinking mode |
| `-y, --yolo` | Auto-approve all actions |
| `-p, --prompt` | Provide prompt directly |
| `--print` | Non-interactive mode |
| `--quiet` | Minimal output mode |
| `--config-file` | Use custom config file |
| `--agent` | Select built-in agent |
| `--agent-file` | Use custom agent file |
| `--mcp-config-file` | Load MCP config |
| `--skills-dir` | Add skills directory |

### Subcommands

| Command | Description |
|---------|-------------|
| `kimi login` | Authenticate with Kimi |
| `kimi logout` | Sign out |
| `kimi info` | Show version and protocol info |
| `kimi export` | Export session data |
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
- [Official Documentation](https://moonshotai.github.io/kimi-cli/) — Complete documentation
- [LLM-Friendly Version](https://moonshotai.github.io/kimi-cli/llms.txt) — Structured for AI consumption

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

**Last updated: March 2026**  
**Based on**: Kimi Code CLI (pip: kimi-cli)
