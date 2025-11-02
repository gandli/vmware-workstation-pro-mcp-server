# VMware Workstation Pro MCP Server

<div align="center" id="top">
  <img src="assets/VMware_Workstation_Pro.webp" width=150 height=150 alt="VMware Workstation Pro 图标"></img>
</div>

<p align="center">
<a href="https://pypi.org/project/vmware-workstation-pro-mcp-server/"><img src="https://img.shields.io/pypi/v/vmware-workstation-pro-mcp-server?color=%2334D058&label=pypi" alt="PyPI 版本" /></a>
<a href="https://pypi.org/project/vmware-workstation-pro-mcp-server/"><img src="https://img.shields.io/pypi/pyversions/vmware-workstation-pro-mcp-server.svg?color=brightgreen" alt="Python 版本" /></a>
<a href="https://github.com/gandli/vmware-workstation-pro-mcp-server/issues"><img src="https://img.shields.io/github/issues-raw/gandli/vmware-workstation-pro-mcp-server" alt="GitHub Issues" /></a>
<a href="https://pypi.org/project/vmware-workstation-pro-mcp-server/"><img alt="PyPI - 下载量" src="https://img.shields.io/pypi/dm/vmware-workstation-pro-mcp-server" /></a>
<a href="https://github.com/gandli/vmware-workstation-pro-mcp-server/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/vmware-workstation-pro-mcp-server?color=brightgreen" alt="许可证" /></a>
</p>

## 概述

一个通过 **REST API** 管理 **VMware Workstation Pro** 虚拟机的 **模型上下文协议(MCP)** 服务器。该服务器可以与支持MCP标准的AI助手和其他工具无缝集成。

## 功能特性

- **主机网络管理**：配置和管理虚拟网络
- **虚拟机管理**：创建、修改和删除虚拟机
- **网络适配器配置**：自定义虚拟机网络设置
- **虚拟机电源控制**：启动、停止、暂停和重置虚拟机
- **共享文件夹管理**：配置主机和虚拟机之间的共享文件夹

## 系统要求

- **VMware Workstation Pro 14+**（已启用REST API）
- **Python 3.10+**
- **[uv](https://github.com/astral-sh/uv)**（推荐）或 **pip**

## 安装方法

```bash
# 使用uv安装（推荐）
uv pip install vmware-workstation-pro-mcp-server

# 或使用pip安装
pip install vmware-workstation-pro-mcp-server
```

## 设置指南

### 1. 配置 VMware Workstation Pro REST API

首先，为VMware Workstation REST API设置凭据：

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

### 2. 启动 VMware Workstation Pro REST API

启动REST API服务：

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

API服务默认将在 `http://localhost:8697` 上可用。

![Windows PowerShell 启动 REST API](assets/Windows_Powershell_Start_REST_API.png)

![虚拟机网络适配器管理](assets/VM_Network_Adapters_Management.png)

### 3. 配置 MCP 服务器

将以下配置添加到您的MCP客户端设置中：

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

## 可用的 MCP 工具

### `list_vms`

- **说明：** 列出所有可用的虚拟机。
- **参数：** 无
- **返回：** 包含虚拟机ID和基本信息的虚拟机对象数组

### `get_vm_info`

- **说明：** 获取特定虚拟机的详细信息。
- **参数：**
  - `vm_id` _(string)_ — 虚拟机的ID
- **返回：** 详细的虚拟机配置和状态信息

### `power_vm`

- **说明：** 对虚拟机执行电源操作。
- **参数：**
  - `vm_id` _(string)_ — 虚拟机的ID
  - `action` _(string)_ — 可选值：`"on"`、`"off"`、`"suspend"`、`"pause"`、`"unpause"`、`"reset"`
- **返回：** 操作状态

### `get_vm_power_state`

- **说明：** 获取虚拟机的当前电源状态。
- **参数：**
  - `vm_id` _(string)_ — 虚拟机的ID
- **返回：** 虚拟机的当前电源状态

## 参考资料

* [VMware Fusion MCP Server](https://github.com/yeahdongcn/vmware-fusion-mcp-server)
* [FastMCP 文档](https://gofastmcp.com/)
* [Model Context Protocol](https://modelcontextprotocol.io/)
* [uvx](https://github.com/modelcontextprotocol/uvx)
* [Fetch Server 示例](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)
* [VMware Workstation REST API 文档](https://developer.broadcom.com/xapis/vmware-workstation-pro-api/latest/)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=gandli/vmware-workstation-pro-mcp-server&type=date&legend=bottom-right)](https://www.star-history.com/#gandli/vmware-workstation-pro-mcp-server&type=date&legend=bottom-right)
