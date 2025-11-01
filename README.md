# VMware Workstation Pro MCP Server

<div align="center" id="top">
  <img src="assets/VMware_Workstation_Pro.webp" width=150 height=150 alt="agentman"></img>
</div>
</p>

<p align="center">
<a href="https://pypi.org/project/vmware-workstation-pro-mcp-server/"><img src="https://img.shields.io/pypi/v/vmware-workstation-pro-mcp-server?color=%2334D058&label=pypi" alt="PyPI version" /></a>
<a href="https://pypi.org/project/vmware-workstation-pro-mcp-server/"><img src="https://img.shields.io/pypi/pyversions/vmware-workstation-pro-mcp-server.svg?color=brightgreen" alt="Python versions" /></a>
<a href="https://github.com/gandli/vmware-workstation-pro-mcp-server/issues"><img src="https://img.shields.io/github/issues-raw/gandli/vmware-workstation-pro-mcp-server" alt="GitHub Issues" /></a>
<a href="https://pepy.tech/projects/vmware-workstation-pro-mcp-server"><img alt="Pepy Total Downloads" src="https://img.shields.io/pepy/dt/vmware-workstation-pro-mcp-server?label=pypi%20%7C%20downloads&color=brightgreen"/></a>
<a href="https://github.com/gandli/vmware-workstation-pro-mcp-server/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/vmware-workstation-pro-mcp-server?color=brightgreen" alt="License" /></a>
</p>

An **MCP (Model Context Protocol)** server for managing **VMware Workstation Pro** virtual machines via the **REST API**.

---

## Features

- Host network management
- Virtual machine management
- Network adapter configuration
- VM power control
- Shared folder management

---

## Prerequisites

- **VMware Workstation Pro** (with REST API enabled)
- **Python 3.10+**
- **[uv](https://github.com/astral-sh/uv)** (recommended) or **pip**

---

## Usage

### 1. Configure the VMware Workstation Pro REST API

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

The API will be available at `http://localhost:8697` by default.

![Windows_Powershell_Start_REST_API](assets/Windows_Powershell_Start_REST_API.png)

![VM_Network_Adapters_Management](assets/VM_Network_Adapters_Management.png)

---

### 3. Configure the MCP Server

```json
"vmware-workstation-pro": {
  "isActive": true,
  "name": "vmware-workstation-pro",
  "type": "stdio",
  "command": "uvx",
  "args": [
    "vmware-workstation-pro-mcp-server"
  ],
  "env": {
    "VMREST_USER": "user",
    "VMREST_PASS": "Password123!"
  }
}
```

---

## MCP Tools

### `list_vms`

- **Description:** List all available virtual machines.
- **Parameters:** None

### `get_vm_info`

- **Description:** Retrieve detailed information about a specific VM.
- **Parameters:**

  - `vm_id` _(string)_ — The ID of the virtual machine

### `power_vm`

- **Description:** Perform a power operation on a VM.
- **Parameters:**

  - `vm_id` _(string)_ — The ID of the virtual machine
  - `action` _(string)_ — One of: `"on"`, `"off"`, `"suspend"`, `"pause"`, `"unpause"`, `"reset"`

### `get_vm_power_state`

- **Description:** Get the current power state of a VM.
- **Parameters:**

  - `vm_id` _(string)_ — The ID of the virtual machine

---

## References

- [FastMCP Documentation](https://gofastmcp.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [uvx](https://github.com/modelcontextprotocol/uvx)
- [Fetch Server Example](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)
- [VMware Workstation REST API](https://developer.broadcom.com/xapis/vmware-workstation-pro-api/latest/)


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=gandli/vmware-workstation-pro-mcp-server&type=date&legend=bottom-right)](https://www.star-history.com/#gandli/vmware-workstation-pro-mcp-server&type=date&legend=bottom-right)