import wikipedia
from fastmcp import FastMCP

serv_mcp = FastMCP("mcp-busca-wikipedia")

@serv_mcp.tool()
async def buscar_wikipedia(busca: str) -> str:
    return wikipedia.search(busca)


if __name__ == "__main__":
    ### stdio permite entrada e saida de dados.
    ### sse deixa o server on
    serv_mcp.run(transport='sse')