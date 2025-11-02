"""VMware Workstation Pro MCP Server main module."""

from fastmcp import FastMCP
from .config import SERVER_CONFIG
from .api.tools import register_tools


def create_app() -> FastMCP:
    """Create and configure the FastMCP application."""
    mcp = FastMCP(SERVER_CONFIG["name"])
    
    # Register all MCP tools
    register_tools(mcp)
    
    return mcp


def main():
    """Run the MCP server."""
    app = create_app()
    app.run(host=SERVER_CONFIG["host"], port=SERVER_CONFIG["port"])


if __name__ == "__main__":
    main()