# Lógica de progamação

# Passo 0 - Entender o desafio que você quer resolver

# Passo 1 -  Percorrer todos os arquivos da pasta base de dados(pasta vendas)
import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir('C:/Curso-Basico-Python/oo-Vendas/Vendas')
print(lista_arquivo)

tabela_total = pd.DataFrame()
# Passo 2 - Importar a base de dados de vendas
for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:
        tabela_vendas = pd.read_csv(f'C:/Curso-Basico-Python/oo-Vendas/Vendas/{arquivo}')
        tabela_total = pd.concat([tabela_total, tabela_vendas])

# Passo 3 - Tratar/Complílar as base de dados
print(tabela_total.head())

# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)

print(tabela_produtos)

# Passo 5 - Calcular o produto que mais faturou (em faturamento)
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print(tabela_faturamento)

# Passo 6 - Calcular loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
tabela_loja = tabela_total.groupby('Loja').sum()
tabela_loja = tabela_loja[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print(tabela_loja)

grafico = px.bar(tabela_loja, x=tabela_loja.index, y='Faturamento')
grafico.show()
