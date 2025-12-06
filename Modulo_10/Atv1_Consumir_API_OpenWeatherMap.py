import requests

def obter_dados_clima(cidade):
    api_key = "SUA_API_KEY"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    resposta = requests.get(url)
    dados = resposta.json()

    print(dados)  # mostra todos os dados crus da API

cidade = input("Digite uma cidade: ")
obter_dados_clima(cidade)