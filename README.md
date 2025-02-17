# DataVader <img src="https://github.com/user-attachments/assets/ec337bc1-f1af-475b-b0d8-de1de35193cd" alt="Darth Vader" width="60">

### Que os dados estejam com você!

**LABORATÓRIO 01 - Características de repositórios populares**

Estudo das principais características de sistemas populares open-source. Dessa forma, vamos analisar como eles são desenvolvidos, com que frequência recebem contribuição externa, com qual frequência lançam releases, entre outras características. Para tanto, iremos coletar os dados para os 1.000 repositórios com maior número de estrelas no GitHub e discutir os valores obtidos. 


## 🔍 Questões de Pesquisa  

✅ **RQ 01** - Sistemas populares são maduros/antigos?  
🔹 **Métrica:** Idade do repositório (calculado a partir da data de sua criação).  

✅ **RQ 02** - Sistemas populares recebem muita contribuição externa?  
🔹 **Métrica:** Total de Pull Requests aceitas.  

✅ **RQ 03** - Sistemas populares lançam releases com frequência?  
🔹 **Métrica:** Total de releases.  

✅ **RQ 04** - Sistemas populares são atualizados com frequência?  
🔹 **Métrica:** Tempo até a última atualização (calculado a partir da data de última atualização).  

✅ **RQ 05** - Sistemas populares são escritos nas linguagens mais populares?  
🔹 **Métrica:** Linguagem primária de cada um desses repositórios.  

✅ **RQ 06** - Sistemas populares possuem um alto percentual de issues fechadas?  
🔹 **Métrica:** Razão entre número de issues fechadas pelo total de issues.  

---

## 📦 Dependências  

Para que o projeto funcione corretamente, você precisa instalar as seguintes bibliotecas:  

- `requests` - Para fazer requisições HTTP para a API do GitHub.  
- `requests-toolbelt` - Ferramentas auxiliares para manipulação de requisições.  
- `gql` - Para interagir com a API GraphQL do GitHub.  
- `pandas` - Para manipulação e análise dos dados coletados.  

---

## ⚙️ Como configurar o ambiente  

É recomendável usar um ambiente virtual para gerenciar as dependências do projeto.  
Siga os passos abaixo para configurar corretamente o ambiente:

### **1️⃣ Criando um ambiente virtual**  
Abra o terminal e execute o seguinte comando:

```bash
python -m venv .venv
