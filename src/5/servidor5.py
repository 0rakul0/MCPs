import requests
import datetime
from geopy.geocoders import Nominatim
from fastmcp import FastMCP
import asyncio


serv_mcp = FastMCP("mcp-busca-temperatura")


@serv_mcp.tool()
async def busca_temperatura_atual(localidade: str):
    '''Retorna o temperatura atual da localidade indicada'''

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(localidade)

    latitude, longitude = getLoc.latitude, getLoc.longitude

    URL = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'hourly': 'temperature_2m',
        'forecast_days': 1
    }

    response = requests.get(URL, params=params)
    if response.status_code == 200:
        resultado = response.json()
        hora = datetime.datetime.now(datetime.UTC).replace(tzinfo=None)
        lista_horas = [datetime.datetime.fromisoformat(temp_str) for temp_str in resultado['hourly']['time']]
        index_proximo = min(range(len(lista_horas)), key=lambda x: abs(lista_horas[x]-hora))
        temp_atual = resultado['hourly']['temperature_2m'][index_proximo]
        return f'{temp_atual:.2f} ºC'

if __name__ == "__main__":
    serv_mcp.run(transport='sse')