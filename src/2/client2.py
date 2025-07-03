import asyncio
from pathlib import Path
from fastmcp import Client

caminho_serv = 'http://localhost:8000/sse'

cliente = Client(caminho_serv)

async def teste_server(cliente, busca):
    async with cliente:
        argumentos = {"busca": busca}
        result = await cliente.call_tool("buscar_wikipedia", arguments=argumentos)
        print(f'Resultado obtido do servidor: {result}')
        mensagem_systema = f"""
        você é um bot que faz buscas na wikipedia o usuario buscou pelo seguinte tema {busca}.
        para esta busca, você recebeu a seguinte resposta: {result}.
        com base nesse conteúdo, formate uma resposta amigável
        """

if __name__ == '__main__':
    asyncio.run(teste_server(cliente=cliente, nome_user='Jefferson', id_user=1))
