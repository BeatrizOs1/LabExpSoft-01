import requests

GITHUB_TOKEN = "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"

GITHUB_API_URL = "https://api.github.com/graphql"

# 🔹 Query GraphQL para buscar os 10 repositórios mais populares
QUERY = """
{
  search(query: "stars:>10000", type: REPOSITORY, first: 10) {
    edges {
      node {
        ... on Repository {
          name
          createdAt
          updatedAt
          primaryLanguage {
            name
          }
          releases {
            totalCount
          }
          pullRequests(states: MERGED) {
            totalCount
          }
          issues {
            totalCount
          }
          closedIssues: issues(states: CLOSED) {
            totalCount
          }
        }
      }
    }
  }
}
"""

# 🔹 Cabeçalhos da requisição
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

# 🔹 Requisição para a API do GitHub
response = requests.post(GITHUB_API_URL, json={"query": QUERY}, headers=HEADERS)

# 🔹 Verifica se a resposta deu certo
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)
