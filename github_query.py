import requests


GITHUB_TOKEN = "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"


GITHUB_API_URL = "https://api.github.com/graphql"


# 🔹 Cabeçalhos da requisição
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}


# 🔹 Requisição para a API do GitHub
response = requests.post(GITHUB_API_URL, json={"query": ""}, headers=HEADERS)


# 🔹 Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)