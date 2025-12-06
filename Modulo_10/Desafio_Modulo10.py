import requests

def buscar_filme_tmdb(nome_filme):
    api_key = "SUA_API_KEY"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={nome_filme}&language=pt-BR"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        if dados["total_results"] == 0:
            print("Nenhum filme encontrado.")
            return

        filme = dados["results"][0]

        titulo = filme["title"]
        sinopse = filme["overview"]
        data = filme["release_date"]
        nota = filme["vote_average"]

        print("\n=== INFORMAÇÕES DO FILME ===")
        print(f"Título: {titulo}")
        print(f"Lançamento: {data}")
        print(f"Nota: {nota}")
        print(f"Sinopse: {sinopse}")

    except Exception as e:
        print("Erro ao buscar filme:", e)

filme = input("Digite o nome de um filme: ")
buscar_filme_tmdb(filme)