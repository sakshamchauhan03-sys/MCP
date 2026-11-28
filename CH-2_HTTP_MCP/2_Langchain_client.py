import asyncio
import sys
from pathlib import Path
import os

mcp_server_script=os.path.join(os.path.dirname(os.path.abspath(__file__)), "1_MCP_server_stdio.py")
#path to the virtual environment
venv_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".venv")

from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    #create a MultiServerMCPClient instance
    client = MultiServerMCPClient(
    #mcp server config(json)
    {
        
        "data_fetch_mcp_stdio":{
            "transport":"stdio",
            "command": os.path.join(venv_path, "Scripts", "python.exe") ,
            "args": [str(mcp_server_script)],
        },
        
        "data_fetch_mcp_http":{
            "transport":"streamable-http",
            "url":"http://localhost:8050/mcp"
        }
    }
    )
    #list the tool
    tools=await client.get_tools()
    print("Available tools:",tools)

if __name__=="__main__":
    asyncio.run(main())
