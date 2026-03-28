---
name: mcp-setup
description: Configure Model Context Protocol servers to extend Kimi capabilities
---

# MCP Setup

MCP (Model Context Protocol) extends Kimi with external tools.

## Configure in ~/.kimi/config.toml

```toml
[mcp.client]
tool_call_timeout_ms = 60000

[mcp.servers.your-server]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-name"]
```

## Manage MCP Servers

```bash
kimi mcp list                    # List configured servers
kimi mcp add <name> -- <command> # Add a server
kimi mcp remove <name>           # Remove a server
```

## Common MCP Servers

- **Filesystem**: File operations with access control
- **Database**: Query databases safely
- **GitHub**: Repository management
- **Web**: Fetch and process web content

## Security

- Review what each MCP server can access
- Use environment variables for secrets
- Test in isolated environment first
