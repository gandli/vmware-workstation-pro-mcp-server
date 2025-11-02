# VMware Workstation Pro MCP Server

<div align="center" id="top">
  <img src="assets/VMware_Workstation_Pro.webp" width=150 height=150 alt="VMware Workstation Pro Logo"></img>
</div>

<p align="center">
<a href="https://pypi.org/project/vmware-workstation-pro-mcp-server/"><img src="https://img.shields.io/pypi/v/vmware-workstation-pro-mcp-server?color=%2334D058&label=pypi" alt="PyPI version" /></a>
<a href="https://pypi.org/project/vmware-workstation-pro-mcp-server/"><img src="https://img.shields.io/pypi/pyversions/vmware-workstation-pro-mcp-server.svg?color=brightgreen" alt="Python versions" /></a>
<a href="https://github.com/gandli/vmware-workstation-pro-mcp-server/issues"><img src="https://img.shields.io/github/issues-raw/gandli/vmware-workstation-pro-mcp-server" alt="GitHub Issues" /></a>
<a href="https://pypi.org/project/vmware-workstation-pro-mcp-server/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/vmware-workstation-pro-mcp-server" /></a>
<a href="https://github.com/gandli/vmware-workstation-pro-mcp-server/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/vmware-workstation-pro-mcp-server?color=brightgreen" alt="License" /></a>
</p>

## Overview

A **Model Context Protocol (MCP)** server for managing **VMware Workstation Pro** virtual machines through its **REST API**. This server enables seamless integration with AI assistants and other tools that support the MCP standard.

## Features

- **Host Network Management**: Configure and manage virtual networks
- **Virtual Machine Management**: Create, modify, and delete VMs
- **Network Adapter Configuration**: Customize VM network settings
- **VM Power Control**: Start, stop, pause, and reset virtual machines
- **Shared Folder Management**: Configure shared folders between host and VMs

## System Requirements

- **VMware Workstation Pro 14+** with REST API enabled
- **Python 3.10+**
- **[uv](https://github.com/astral-sh/uv)** (recommended) or **pip**

## Installation

```bash
# Install with uv (recommended)
uv pip install vmware-workstation-pro-mcp-server

# Or install with pip
pip install vmware-workstation-pro-mcp-server
```

## Setup Guide

### 1. Configure the VMware Workstation Pro REST API

First, set up credentials for the VMware Workstation REST API:

```pwsh
.\vmrest.exe -C
VMware Workstation REST API
Copyright (C) 2018-2025 Broadcom.
All Rights Reserved

vmrest 1.3.1 build-24832109
Username: user
New password:
Retype new password:
Processing...
Credential updated successfully
```

### 2. Start the VMware Workstation Pro REST API

Launch the REST API service:

```pwsh
cd "C:\Program Files (x86)\VMware\VMware Workstation"
.\vmrest.exe
VMware Workstation REST API
Copyright (C) 2018-2025 Broadcom.
All Rights Reserved
vmrest 1.3.1 build-24832109
-
Using the VMware Workstation UI while API calls are in progress is not recommended and may yield unexpected results
-
Serving HTTP on 127.0.0.1:8697
-
Press Ctrl+C to stop.
```

The API service will be available at `http://localhost:8697` by default.

![Windows PowerShell Start REST API](assets/Windows_Powershell_Start_REST_API.png)

![VM Network Adapters Management](assets/VM_Network_Adapters_Management.png)

### 3. Configure the MCP Server

Add the following configuration to your MCP client setup:

```json
{
  "mcpServers": {
    "vmware-workstation-pro": {
      "command": "uvx",
      "args": ["vmware-workstation-pro-mcp-server"],
      "env": {
        "VMREST_USER": "your-username",
        "VMREST_PASS": "your-password"
      }
    }
  }
}
```

## Available MCP Tools

### `list_vms`

- **Description:** List all available virtual machines.
- **Parameters:** None
- **Returns:** Array of VM objects with their IDs and basic information

### `get_vm_info`

- **Description:** Retrieve detailed information about a specific VM.
- **Parameters:**
  - `vm_id` _(string)_ — The ID of the virtual machine
- **Returns:** Detailed VM configuration and status information

### `power_vm`

- **Description:** Perform a power operation on a VM.
- **Parameters:**
  - `vm_id` _(string)_ — The ID of the virtual machine
  - `action` _(string)_ — One of: `"on"`, `"off"`, `"suspend"`, `"pause"`, `"unpause"`, `"reset"`
- **Returns:** Operation status

### `get_vm_power_state`

- **Description:** Get the current power state of a VM.
- **Parameters:**
  - `vm_id` _(string)_ — The ID of the virtual machine
- **Returns:** Current power state of the VM

## References

* [VMware Fusion MCP Server](https://github.com/yeahdongcn/vmware-fusion-mcp-server)
* [FastMCP Documentation](https://gofastmcp.com/)
* [Model Context Protocol](https://modelcontextprotocol.io/)
* [uvx](https://github.com/modelcontextprotocol/uvx)
* [Fetch Server Example](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)
* [VMware Workstation REST API](https://developer.broadcom.com/xapis/vmware-workstation-pro-api/latest/)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=gandli/vmware-workstation-pro-mcp-server&type=date&legend=bottom-right)](https://www.star-history.com/#gandli/vmware-workstation-pro-mcp-server&type=date&legend=bottom-right)
