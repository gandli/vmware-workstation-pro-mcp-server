"""Entry point for VMware Workstation Pro MCP Server."""

try:
    # For development environment
    from src.vmware_workstation_pro_mcp_server.server import main
except ImportError:
    # For installed package environment
    from vmware_workstation_pro_mcp_server.server import main

if __name__ == "__main__":
    main()
