from fastmcp import FastMCP

# create an instance of FastMCP
mcp = FastMCP()

@mcp.tool()
def fetch():
    '''use this tool to fetch data from the server'''
    return {"data": "Hello,MCP!"}

@mcp.tool()
def process():
    '''use this tool to process the fetch data'''
    return {"result": "Data processed successfully!"}

if __name__ == "__main__":
    mcp.run(transport="stdio")
