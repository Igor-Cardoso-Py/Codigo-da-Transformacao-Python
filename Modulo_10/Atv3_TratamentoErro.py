import requests

def clima_com_erros(cidade):
    api_key = "SUA_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # dispara erro em status >= 400

        dados = resposta.json()

        temperatura = dados["main"]["temp"]
        condicao = dados["weather"][0]["description"]

        print(f"Temperatura: {temperatura}°C")
        print(f"Clima: {condicao}")

    except requests.exceptions.Timeout:
        print("❌ Erro: a requisição demorou demais.")
    except requests.exceptions.HTTPError as e:
        print("❌ Erro HTTP:", e)
    except requests.exceptions.RequestException:
        print("❌ Falha na conexão com a API.")
    except KeyError:
        print("❌ Erro ao processar os dados da API.")

cidade = input("Digite uma cidade: ")
clima_com_erros(cidade)