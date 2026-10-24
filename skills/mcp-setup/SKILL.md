---
name: mcp-setup
description: Configure Model Context Protocol servers in Kimi Code, including OAuth login and timeouts
---

# MCP Setup

MCP (Model Context Protocol) extends Kimi with external tools.

## Where the config lives

```bash
~/.kimi-code/mcp.json              # user-level servers
<project>/.kimi-code/mcp.json       # project-level servers
```

The `mcpServers` format is shared with other MCP clients:

```json
{
  "mcpServers": {
    "your-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-name"]
    },
    "remote-server": {
      "url": "https://mcp.example.com/mcp",
      "headers": { "API_KEY": "{env:MCP_API_KEY}" }
    }
  }
}
```

## Manage MCP servers

Use the `/mcp-config` command inside a session for the interactive flow, including OAuth login. From the shell:

```bash
kimi provider list                 # confirm the provider is configured
kimi -p "/mcp"                     # list servers and connection status in a session
```

## Timeouts

Timeouts live in `config.toml`, not in `mcp.json`:

```toml
[mcp]
startup_timeout_ms = 30000        # connection plus tool discovery
tool_timeout_ms = 60000            # single tool call
default_deferred = false           # load tools on demand
```

A per-server `startupTimeoutMs` or `toolTimeoutMs` in `mcp.json` overrides the global value.

## Common servers

- **Filesystem**: file operations with access control
- **Database**: query databases safely
- **GitHub**: repository management
- **Web**: fetch and process web content

## Security

- Review what each MCP server can reach before you connect it
- Keep secrets in environment variables, referenced as `{env:VAR}`
- OAuth tokens are stored outside the config file; re-authorize after a migration from kimi-cli
