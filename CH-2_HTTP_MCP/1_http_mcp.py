from fastmcp import FastMCP

# create an instance of FastMCP
mcp = FastMCP()

@mcp.tool()
def fetch_http():
    '''use this tool to fetch data from the server'''
    return {"data": "Hello,MCP!"}

@mcp.tool()
def process_http():
    '''use this tool to process the fetch data'''
    return {"result": "Data processed successfully!"}

if __name__ == "__main__":
    #run the MCP server with HTTP transport
    mcp.run(transport="streamable-http",host="0.0.0.0",port=8050)
