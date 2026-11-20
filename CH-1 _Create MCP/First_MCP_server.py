from fastmcp import FastMCP

# create an instance of FastMCP
mcp = FastMCP()

@mcp.tool()
def fetch():
    return {"data": "Hello,MCP!"}

@mcp.tool()
def process():
    return {"result": "Data processed successfully!"}

if __name__ == "__main__":
    mcp.run(transport="stdio")
