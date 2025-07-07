import asyncio
import os
from fastmcp import Client
import dotenv
from openai import OpenAI

caminho_serv = 'http://localhost:8000/sse'
cliente = Client(caminho_serv)

async def teste_server(cliente, local):
    dotenv.load_dotenv()

    api_key = os.environ['API_OPENAI_KEY']

    async with cliente:
        argumentos = {"localidade": local}
        result = await cliente.call_tool("busca_temperatura_atual", arguments=argumentos)

        mensagem_systema = f"""
        você é um bot que informa a tempera ao usuario da cidade {local}.
        para esta busca, você recebeu a seguinte resposta: {result}.
        com base nesse conteúdo, formate uma resposta amigável ao usuario.
        """

        client_openai = OpenAI(api_key=api_key)
        response = client_openai.responses.create(
            model='gpt-4o-mini',
            instructions=mensagem_systema,
            input="pode me falar mais sobre esse assunto?"
        )

        print(response.output_text)


if __name__ == '__main__':
    asyncio.run(teste_server(cliente=cliente, busca='Rio de janeiro'))
