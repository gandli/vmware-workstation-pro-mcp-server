"""VMware Workstation Pro REST API client implementation."""

import aiohttp
from typing import Dict, Any, List, Optional
import json
import base64


class VMwareClient:
    """Client for VMware Workstation Pro REST API."""

    def __init__(self, host: str = "localhost", port: int = 8697, 
                 username: str = "", password: str = ""):
        """Initialize the VMware client.
        
        Args:
            host: VMware REST API host
            port: VMware REST API port
            username: VMware REST API username
            password: VMware REST API password
        """
        self.base_url = f"http://{host}:{port}/api"
        self.auth_header = None
        if username and password:
            auth_str = f"{username}:{password}"
            auth_bytes = auth_str.encode("ascii")
            base64_bytes = base64.b64encode(auth_bytes)
            base64_auth = base64_bytes.decode("ascii")
            self.auth_header = {"Authorization": f"Basic {base64_auth}"}
        self.session = None

    async def __aenter__(self):
        """Enter the async context manager."""
        self.session = aiohttp.ClientSession(headers=self.auth_header)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the async context manager."""
        if self.session:
            await self.session.close()

    async def list_vms(self) -> List[Dict[str, Any]]:
        """List all VMs in VMware Workstation Pro.
        
        Returns:
            List of VM information dictionaries
        """
        if not self.session:
            raise RuntimeError("Client not initialized. Use async with.")
        
        try:
            async with self.session.get(f"{self.base_url}/vms") as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("vms", [])
                else:
                    error_text = await response.text()
                    return {"error": f"Failed to list VMs: {response.status}", "details": error_text}
        except aiohttp.ClientError as e:
            return {"error": f"Connection error: {str(e)}"}

    async def get_vm_info(self, vm_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific VM.
        
        Args:
            vm_id: VM identifier
            
        Returns:
            VM information dictionary
        """
        if not self.session:
            raise RuntimeError("Client not initialized. Use async with.")
        
        try:
            async with self.session.get(f"{self.base_url}/vms/{vm_id}") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    return {"error": f"Failed to get VM info: {response.status}", "details": error_text}
        except aiohttp.ClientError as e:
            return {"error": f"Connection error: {str(e)}"}

    async def power_vm(self, vm_id: str, action: str) -> Dict[str, Any]:
        """Perform a power action on a VM.
        
        Args:
            vm_id: VM identifier
            action: Power action ('on', 'off', 'shutdown', 'suspend', 'pause', 'unpause')
            
        Returns:
            Result of the power operation
        """
        if not self.session:
            raise RuntimeError("Client not initialized. Use async with.")
        
        valid_actions = {'on', 'off', 'shutdown', 'suspend', 'pause', 'unpause'}
        if action not in valid_actions:
            return {"error": f"Invalid power action: {action}. Valid actions: {valid_actions}"}
        
        try:
            async with self.session.put(
                f"{self.base_url}/vms/{vm_id}/power",
                json={"operation": action}
            ) as response:
                if response.status == 200:
                    return {"success": True, "action": action}
                else:
                    error_text = await response.text()
                    return {"error": f"Failed to {action} VM: {response.status}", "details": error_text}
        except aiohttp.ClientError as e:
            return {"error": f"Connection error: {str(e)}"}

    async def get_vm_power_state(self, vm_id: str) -> Dict[str, Any]:
        """Get the power state of a specific VM.
        
        Args:
            vm_id: VM identifier
            
        Returns:
            Power state information
        """
        if not self.session:
            raise RuntimeError("Client not initialized. Use async with.")
        
        try:
            async with self.session.get(f"{self.base_url}/vms/{vm_id}/power") as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    return {"error": f"Failed to get power state: {response.status}", "details": error_text}
        except aiohttp.ClientError as e:
            return {"error": f"Connection error: {str(e)}"}