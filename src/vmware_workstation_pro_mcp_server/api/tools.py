"""MCP Tools implementation for VMware Workstation Pro."""

from typing import Dict, Any
import os
from fastmcp import FastMCP
from ..client.vmware_client import VMwareClient

# Helper to get credentials from environment
VMREST_USER = os.environ.get("VMREST_USER", "")
VMREST_PASS = os.environ.get("VMREST_PASS", "")


async def list_vms_impl() -> Dict[str, Any]:
    """List all VMs in VMware Workstation Pro."""
    async with VMwareClient(username=VMREST_USER, password=VMREST_PASS) as client:
        vms = await client.list_vms()
        return {"vms": vms}


async def get_vm_info_impl(vm_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific VM."""
    async with VMwareClient(username=VMREST_USER, password=VMREST_PASS) as client:
        info = await client.get_vm_info(vm_id)
        return info


async def power_vm_impl(vm_id: str, action: str) -> Dict[str, Any]:
    """Perform a power action on a VM."""
    async with VMwareClient(username=VMREST_USER, password=VMREST_PASS) as client:
        result = await client.power_vm(vm_id, action)
        return result


async def get_vm_power_state_impl(vm_id: str) -> Dict[str, Any]:
    """Get the power state of a specific VM."""
    async with VMwareClient(username=VMREST_USER, password=VMREST_PASS) as client:
        state = await client.get_vm_power_state(vm_id)
        return state


def register_tools(mcp: FastMCP) -> None:
    """Register all MCP tools with the FastMCP instance."""
    
    @mcp.tool
    async def list_vms() -> Dict[str, Any]:
        """List all VMs in VMware Workstation Pro."""
        return await list_vms_impl()
    
    @mcp.tool
    async def get_vm_info(vm_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific VM."""
        return await get_vm_info_impl(vm_id)
    
    @mcp.tool
    async def power_vm(vm_id: str, action: str) -> Dict[str, Any]:
        """Perform a power action on a VM. Valid actions are 'on', 'off', 'shutdown', 'suspend', 'pause', 'unpause'."""
        return await power_vm_impl(vm_id, action)
    
    @mcp.tool
    async def get_vm_power_state(vm_id: str) -> Dict[str, Any]:
        """Get the power state of a specific VM."""
        return await get_vm_power_state_impl(vm_id)