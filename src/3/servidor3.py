import wikipedia
from fastmcp import FastMCP

serv_mcp = FastMCP("mcp-busca-wikipedia")

@serv_mcp.tool()
async def buscar_wikipedia(busca: str) -> str:
    return wikipedia.summary(busca)


if __name__ == "__main__":
    serv_mcp.run(transport='sse')