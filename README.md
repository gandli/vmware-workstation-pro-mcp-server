# VMware Workstation Pro MCP Server

一个用于通过 REST API 管理 VMware Workstation Pro 虚拟机的 MCP (Model Context Protocol) 服务器。

## 功能特性

- 🖥️ **虚拟机管理**: 列出、查看和控制 VMware Workstation Pro 虚拟机
- ⚡ **电源控制**: 启动、关闭、暂停、恢复虚拟机
- 📊 **状态监控**: 获取虚拟机详细信息和电源状态
- 🔐 **安全认证**: 支持基本身份验证
- 🚀 **异步操作**: 基于 FastMCP 的高性能异步实现

## 前置要求

- Python 3.10 或更高版本
- VMware Workstation Pro 17.0 或更高版本
- 启用 VMware Workstation Pro REST API

## 安装

### 使用 uvx (推荐)

```bash
uvx vmware-workstation-pro-mcp-server
```

### 使用 pip

```bash
pip install vmware-workstation-pro-mcp-server
```

### 从源码安装

```bash
git clone https://github.com/gandli/vmware-workstation-pro-mcp-server.git
cd vmware-workstation-pro-mcp-server
pip install -e .
```

## VMware Workstation Pro 配置

### 启用 REST API

1. 打开 VMware Workstation Pro
2. 转到 **编辑** > **首选项**
3. 选择 **共享虚拟机** 选项卡
4. 勾选 **启用 REST API**
5. 设置端口 (默认: 8697)
6. 配置用户名和密码 (可选但推荐)

### 验证 API 可用性

```bash
curl -X GET http://localhost:8697/api/vms
```

## 环境变量配置

设置以下环境变量来配置认证 (如果 VMware 启用了认证):

```bash
export VMREST_USER="your_username"
export VMREST_PASS="your_password"
```

Windows PowerShell:

```powershell
$env:VMREST_USER="your_username"
$env:VMREST_PASS="your_password"
```

## 使用方法

The server connects to VMware workstation pro's REST API at `http://localhost:8697` by default. You must configure authentication for the vmrest API using environment variables:

- `VMREST_USER`: Username for the vmrest API (required if authentication is enabled)
- `VMREST_PASS`: Password for the vmrest API (required if authentication is enabled)

These must be set in your shell, in your VS Code MCP config, or in your deployment environment.

### Example: MCP server config for VS Code with credentials

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

- Set `VMREST_USER` and `VMREST_PASS` to your vmrest credentials.
  
### 可用工具

MCP 服务器提供以下工具:

#### 1. `list_vms`

列出所有虚拟机

**返回**: 包含所有虚拟机基本信息的列表

#### 2. `get_vm_info`

获取特定虚拟机的详细信息

**参数**:

- `vm_id` (string): 虚拟机 ID

**返回**: 虚拟机的详细配置信息

#### 3. `power_vm`

对虚拟机执行电源操作

**参数**:

- `vm_id` (string): 虚拟机 ID
- `action` (string): 电源操作，可选值:
  - `on`: 启动虚拟机
  - `off`: 强制关闭虚拟机
  - `shutdown`: 优雅关闭虚拟机
  - `suspend`: 暂停虚拟机
  - `pause`: 暂停虚拟机执行
  - `unpause`: 恢复虚拟机执行

**返回**: 操作结果状态

#### 4. `get_vm_power_state`

获取虚拟机的当前电源状态

**参数**:

- `vm_id` (string): 虚拟机 ID

**返回**: 虚拟机的当前电源状态

## 配置选项

### 自定义 API 端点

默认情况下，服务器连接到 `http://localhost:8697`。如果您的 VMware Workstation Pro 运行在不同的主机或端口上，可以通过修改代码中的 `base_url` 参数来更改。

### 认证配置

如果您的 VMware Workstation Pro 启用了认证，请确保设置了正确的环境变量:

- `VMREST_USER`: VMware REST API 用户名
- `VMREST_PASS`: VMware REST API 密码

## 故障排除

### 常见问题

1. **连接失败**
   - 确保 VMware Workstation Pro 正在运行
   - 验证 REST API 已启用
   - 检查防火墙设置

2. **认证错误**
   - 验证环境变量设置正确
   - 确认用户名和密码有效

3. **虚拟机未找到**
   - 使用 `list_vms` 获取有效的虚拟机 ID
   - 确保虚拟机已在 VMware Workstation Pro 中注册

### 调试模式

要启用详细日志记录，可以设置环境变量:

```bash
export PYTHONPATH=.
export DEBUG=1
```

## 开发

### 项目结构

```
vmware-workstation-pro-mcp-server/
├── vmware_workstation_pro_mcp_server/
│   ├── __init__.py          # 包初始化和导出
│   ├── server.py            # MCP 服务器实现
│   └── vmware_client.py     # VMware REST API 客户端
├── pyproject.toml           # 项目配置
└── README.md               # 项目文档
```

### 本地开发

1. 克隆仓库
2. 安装依赖: `pip install -e .`
3. 运行服务器: `python -m vmware_workstation_pro_mcp_server.server`

## 许可证

MIT License - 详见 LICENSE 文件

## 贡献

欢迎提交 Issue 和 Pull Request！

## 支持

如果您遇到问题或有功能请求，请在 GitHub 上创建 Issue。
