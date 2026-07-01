# efootballDBWebScraping

Web scraping da base de dados de jogadores do eFootball (pesdb.net), gerando um CSV com posição, nome, time, nacionalidade e overall de cada jogador.

## Pré-requisitos

- Python 3.9+
- pip

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone <url-do-repositorio>
cd efootballDBWebScraping
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Como rodar

```bash
python3 scrapping.py
```

O script percorre as páginas de `https://pesdb.net/efootball/` e salva os dados coletados em `jogadoresV1.csv` na raiz do projeto.

> O scraping percorre 1259 páginas por padrão, então a execução pode levar alguns minutos. Ajuste a constante `TOTAL_PAGINAS` em [scrapping.py](scrapping.py) para testar com menos páginas.

## Saída

Um arquivo `jogadoresV1.csv` com as colunas:

| Coluna | Descrição |
| --- | --- |
| Posição | Posição do jogador |
| Nome | Nome do jogador |
| Time | Time atual |
| Nacionalidade | Nacionalidade do jogador |
| Overall | Overall (rating) do jogador |
