import asyncio
from fastmcp import Client

caminho_serv = 'http://localhost:8000/sse'

cliente = Client(caminho_serv)

async def teste_server(cliente, nome_user, id_user):
    async with cliente:
        argumentos = {"nome_user": nome_user, "id_user":id_user}
        result = await cliente.call_tool("dar_bom_dia", argumentos)
        print(f'Resultado obtido do servidor: {result}')

if __name__ == '__main__':
    asyncio.run(teste_server(cliente=cliente, nome_user='Jefferson', id_user=1))
