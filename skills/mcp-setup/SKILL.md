---
name: mcp-setup
description: Configure Model Context Protocol servers to extend Kimi capabilities
---

# MCP Setup

MCP (Model Context Protocol) extends Kimi with external tools.

## Configure in ~/.kimi/mcp.json

MCP server configuration lives in `~/.kimi/mcp.json` in the `mcpServers` format shared with other MCP clients:

```json
{
  "mcpServers": {
    "your-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-name"]
    }
  }
}
```

## Manage MCP Servers

```bash
kimi mcp list                    # List configured servers
kimi mcp add <name> -- <command> # Add a stdio server
kimi mcp add --transport http <name> <url> # Add an HTTP server
kimi mcp remove <name>           # Remove a server
kimi mcp test <name>             # Test connection and list available tools
kimi mcp auth <name>             # Complete OAuth authorization
kimi mcp reset-auth <name>       # Clear a cached OAuth token
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
