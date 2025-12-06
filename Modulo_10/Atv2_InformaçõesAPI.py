import requests

def exibir_info_clima(cidade):
    api_key = "SUA_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    resposta = requests.get(url)
    dados = resposta.json()

    temperatura = dados["main"]["temp"]
    condicao = dados["weather"][0]["description"]
    umidade = dados["main"]["humidity"]

    print("\n=== CLIMA ===")
    print(f"Temperatura: {temperatura}°C")
    print(f"Clima: {condicao}")
    print(f"Umidade: {umidade}%")

cidade = input("Digite uma cidade: ")
exibir_info_clima(cidade)