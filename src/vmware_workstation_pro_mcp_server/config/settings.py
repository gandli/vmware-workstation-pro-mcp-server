"""Configuration settings for VMware Workstation Pro MCP Server."""

import os
from typing import Dict, Any

# VMware REST API settings
VMWARE_CONFIG = {
    "host": os.environ.get("VMREST_HOST", "localhost"),
    "port": int(os.environ.get("VMREST_PORT", "8697")),
    "username": os.environ.get("VMREST_USER", ""),
    "password": os.environ.get("VMREST_PASS", ""),
}

# FastMCP server settings
SERVER_CONFIG = {
    "name": "VMware Workstation Pro MCP Server",
    "host": os.environ.get("MCP_HOST", "0.0.0.0"),
    "port": int(os.environ.get("MCP_PORT", "8000")),
}

def get_config() -> Dict[str, Any]:
    """Get the complete configuration."""
    return {
        "vmware": VMWARE_CONFIG,
        "server": SERVER_CONFIG,
    }