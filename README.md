### install uv
```{bash}
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### lib FastMCP
- uv init
- uv add fastmcp
- uv add openai python-dotenv wikipedia


### notas de desenvolvimento
- servirdor:
  - para testar usar o transport='stdio'
  - no cliente mudar para `caminho_serv = Path(__file__).parent / 'servidor.py'`
  - para produção usar transport='sse' 
  - no cliente mudar para `caminho_serv = 'http://localhost:8000/sse'`

### para fazer os testes
- instalar `npx @modelcontextprotocol/inspector`


### estudar
```
https://www.youtube.com/watch?v=KRw4vVX9aHU
```
