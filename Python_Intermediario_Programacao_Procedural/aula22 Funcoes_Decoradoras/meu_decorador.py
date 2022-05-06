import requests
import time

# CRIAR UM DECORATOR calcular_tempo
def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time() # PEGAR O TIMESTAMP NESSE PONTO
        funcao()
        tempo_final = time.time() # PEGAR O TIMESTAMP NESSE PONTO
        print(f'Duração foi de {tempo_final - tempo_inicial:.2f} segundos')
    return wrapper

@calcular_tempo
def pegar_contacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_contacao_dolar()