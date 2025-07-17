import asyncio
from fastmcp import Client

caminho_serv = 'http://0.0.0.0:8080/mcp'

cliente = Client(caminho_serv)

async def consulta_o_genero(cliente, nome_user):
    async with cliente:
        argumentos = {"nome": nome_user}
        result = await cliente.call_tool("estimar_genero", argumentos)
        print(result)

if __name__ == '__main__':
    asyncio.run(consulta_o_genero(cliente=cliente, nome_user='Minerva'))
