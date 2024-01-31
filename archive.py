# Adaptado para arquivos normais .py (sem Notebook Jupyter)
import pandas as pd
import plotly.express as px

# Carregar o arquivo CSV
tabela = pd.read_csv("cancelamentos.csv")

# Remover a coluna "CustomerID"
tabela = tabela.drop(columns="CustomerID")

# Exibir informações sobre o DataFrame
print(tabela.info())

# Remover linhas com valores ausentes
tabela = tabela.dropna()

# Exibir contagem de valores na coluna "cancelou"
print(tabela["cancelou"].value_counts())

# Exibir proporção de valores na coluna "cancelou"
print(tabela["cancelou"].value_counts(normalize=True))

# Gerar histogramas para cada coluna
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

# Filtrar dados
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"] <= 4]
tabela = tabela[tabela["dias_atraso"] <= 20]

# Exibir contagem de valores após filtragem
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True))

# Salvar DataFrame filtrado em um novo arquivo Excel
tabela.to_excel("cancelamentos_filtrados.xlsx")
