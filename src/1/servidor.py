from fastmcp import FastMCP

serv_mcp = FastMCP("mcp-teste")

@serv_mcp.tool()
async def dar_bom_dia(nome_user: str, id_user: int) -> str:
    return f'oi, {nome_user}! (ID {id_user})'


if __name__ == "__main__":
    ### stdio permite entrada e saida de dados.
    ### sse deixa o server on
    serv_mcp.run(transport='sse')