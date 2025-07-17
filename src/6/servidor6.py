from fastmcp import FastMCP
import json

# Inicializa o serviço MCP
serv_mcp = FastMCP("genero-por-nome")

# Carrega os dados do JSON
with open("nomes_data.json", "r", encoding="utf-8") as f:
    nomes_data = json.load(f)

@serv_mcp.tool(description="Estima o gênero de uma pessoa com base no primeiro nome")
async def estimar_genero(nome: str) -> dict:
    """
    Retorna o gênero estimado, probabilidade e total de amostras para um nome.
    """
    nome = nome.strip().upper()

    if nome not in nomes_data:
        return {
            "erro": "Nome não encontrado no banco de dados."
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
    serv_mcp.run(transport="sse")
