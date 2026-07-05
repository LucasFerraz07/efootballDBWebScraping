import requests
from bs4 import BeautifulSoup
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

jogadores = []
nomes_vistos = set()

# quantidade de páginas para testar primeiro
TOTAL_PAGINAS = 1259

for pagina in range(1, TOTAL_PAGINAS + 1):

    url = f"https://pesdb.net/efootball/?mode=max_level&all=1&page={pagina}"

    print(f"Coletando página {pagina}...")

    for tentativa in range(1, 4):
        try:
            resposta = requests.get(url, headers=headers, timeout=15)
            break
        except requests.exceptions.RequestException as erro:
            print(f"Falha na página {pagina} (tentativa {tentativa}/3): {erro}")
            if tentativa == 3:
                resposta = None
            else:
                time.sleep(2 * tentativa)

    if resposta is None:
        print(f"Pulando página {pagina} após falhas consecutivas.")
        continue

    soup = BeautifulSoup(resposta.text, "html.parser")

    linhas = soup.find_all("tr")

    for linha in linhas:
        colunas = linha.find_all("td")

        if len(colunas) >= 5:

            posicao = colunas[0].get_text(strip=True)
            nome = colunas[1].get_text(strip=True)
            time_jogador = colunas[2].get_text(strip=True)
            nacionalidade = colunas[3].get_text(strip=True)
            overall = colunas[7].get_text(strip=True)

            if overall.isdigit():

                # evita duplicar nomes
                if nome not in nomes_vistos:
                    nomes_vistos.add(nome)

                    jogadores.append([
                        posicao,
                        nome,
                        time_jogador,
                        nacionalidade,
                        overall
                    ])

    time.sleep(0.3)  # evita bloqueio do site

with open("jogadoresV1.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)

    writer.writerow(["Posição", "Nome", "Time", "Nacionalidade", "Overall"])
    writer.writerows(jogadores)

print("CSV gerado com sucesso!")
print(f"{len(jogadores)} jogadores únicos salvos.")