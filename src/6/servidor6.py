from fastmcp import FastMCP
import json

# Inicializa o serviço MCP
serv_mcp = FastMCP("genero-por-nome", host="0.0.0.0", port=3000)

# Carrega os dados do JSON
with open("nomes_data.json", "r", encoding="utf-8") as f:
    nomes_data = json.load(f)


@serv_mcp.tool(description="Estima o gênero de uma pessoa com base no primeiro nome")
async def estimar_genero(nome: str) -> dict:
    """
    Retorna o gênero estimado, probabilidade e total de amostras para um nome.
    Args:
        nome (str): nome

    Returns:
        {
        "nome": "Jefferson",
        "genero_estimado": "Masculino",
        "probabilidade": 0.977,
        "total_amostras": 25112
        }
        Ou, se o nome não for encontrado:
        {
        "nome": "Xablau",
        "mensagem": "Não há registro do nome no banco de dados."
        }
    """
    nome = nome.strip().upper()

    if nome not in nomes_data:
        return {
            "nome": nome.title(),
            "mensagem": "Não há registro do nome no banco de dados."
        }

    dados_nome = nomes_data[nome]
    genero = "Masculino" if dados_nome["id_genero"] == 1.0 else "Feminino"

    return {
        "nome": nome.title(),
        "genero_estimado": genero,
        "probabilidade": round(dados_nome["taxa"], 3),
        "total_amostras": dados_nome["total_nome"]
    }


if __name__ == "__main__":
    serv_mcp.run(transport="streamable-http")
