import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession,StdioServerParameters,Client
import asyncio


# path to the mcp server script
mcp_server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "1_MCP_server_stdio.py")
print(mcp_server_path)

#create an server parameters
server_params=StdioServerParameters(
     command="python",
     args=[str(mcp_server_path)],
     env={}
)

# create a client session
async def main():
    #create context manager
    async with stdio_client(server_params)as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            #fetch the tools
            tools=await session.list_tools()
            print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())


