import requests

TOKEN = "token_token_token"
URL = "https://api.github.com/graphql"

# Função para consultar repositórios em lotes de 10
def fetch_repositories(after_cursor=None):
    query = f"""
    {{
      search(query: "stars:>10000", type: REPOSITORY, first: 10, after: "{after_cursor if after_cursor else ''}") {{
        edges {{
          node {{
            ... on Repository {{
              name
              createdAt
              updatedAt
              pullRequests {{
                totalCount
              }}
              releases {{
                totalCount
              }}
              issues {{
                totalCount
              }}
              closedIssues: issues(states: CLOSED) {{
                totalCount
              }}
              primaryLanguage {{
                name
              }}
              stargazerCount
            }}
          }}
        }}
        pageInfo {{
          hasNextPage
          endCursor
        }}
      }}
    }}
    """
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(URL, json={"query": query}, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro {response.status_code}: {response.text}")
        return None

# Função principal para pegar 100 repositórios
def get_all_repositories():
    all_repositories = []
    after_cursor = None
    while len(all_repositories) < 100:  # Limita para 100 repositórios
        data = fetch_repositories(after_cursor)
        if data and "data" in data and data["data"]["search"]["edges"]:
            all_repositories.extend(data["data"]["search"]["edges"])

            # Verifica se há mais páginas
            page_info = data["data"]["search"]["pageInfo"]
            if not page_info["hasNextPage"]:
                break
            after_cursor = page_info["endCursor"]
        else:
            break

        # Se já tiver 100 ou mais, sai do loop
        if len(all_repositories) >= 100:
            all_repositories = all_repositories[:100]
            break

    return all_repositories

# Obter os 100 repositórios
repositories = get_all_repositories()

# Exibir os dados coletados
if repositories:
    print(f"{'Repository Name':<50} {'Created At':<20} {'Stars':<10} {'Pull Requests':<15} {'Releases':<10} {'Issues':<10} {'Closed Issues':<15} {'Language'}")
    print("-" * 125)  # Linha de separação
    for repo in repositories:
        name = repo["node"]["name"]
        created_at = repo["node"]["createdAt"]
        stars = repo["node"]["stargazerCount"]
        pull_requests = repo["node"]["pullRequests"]["totalCount"]
        releases = repo["node"]["releases"]["totalCount"]
        issues = repo["node"]["issues"]["totalCount"]
        closed_issues = repo["node"]["closedIssues"]["totalCount"]
        language = repo["node"]["primaryLanguage"]["name"] if repo["node"]["primaryLanguage"] else "N/A"

        # Exibindo as informações formatadas
        print(f"{name:<50} {created_at:<20} {stars:<10} {pull_requests:<15} {releases:<10} {issues:<10} {closed_issues:<15} {language}")
