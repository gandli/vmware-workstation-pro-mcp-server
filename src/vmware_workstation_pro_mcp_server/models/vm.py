"""VM data models for VMware Workstation Pro MCP Server."""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class VMPowerInfo(BaseModel):
    """VM power state information."""
    
    power_state: str = Field(..., description="Current power state of the VM")
    
    @classmethod
    def from_api_response(cls, data: Dict[str, Any]) -> "VMPowerInfo":
        """Create a VMPowerInfo instance from API response data."""
        return cls(power_state=data.get("power_state", "unknown"))


class VMInfo(BaseModel):
    """Detailed VM information."""
    
    id: str = Field(..., description="VM identifier")
    path: str = Field(..., description="Path to the VM")
    name: Optional[str] = Field(None, description="VM name")
    cpu_count: Optional[int] = Field(None, description="Number of CPUs")
    memory_mb: Optional[int] = Field(None, description="Memory in MB")
    power_state: Optional[str] = Field(None, description="Current power state")
    
    @classmethod
    def from_api_response(cls, data: Dict[str, Any]) -> "VMInfo":
        """Create a VMInfo instance from API response data."""
        return cls(
            id=data.get("id", ""),
            path=data.get("path", ""),
            name=data.get("display_name", None),
            cpu_count=data.get("cpu", {}).get("processors", None),
            memory_mb=data.get("memory", None),
            power_state=data.get("power_state", None)
        )


class VMList(BaseModel):
    """List of VMs."""
    
    vms: List[VMInfo] = Field(default_factory=list, description="List of VMs")
    
    @classmethod
    def from_api_response(cls, data: List[Dict[str, Any]]) -> "VMList":
        """Create a VMList instance from API response data."""
        vm_list = [VMInfo.from_api_response(vm) for vm in data]
        return cls(vms=vm_list)