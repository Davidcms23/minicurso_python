import pandas as pd

# 1° Carregar os Dados
df = pd.read_csv('vendas.csv')

# 2° Visualizar os Dados
df.head()

# 3° Adicionar Coluna de Total
df['Total'] = df['Quantidade'] * df['Preço Unitário']
df.head()

# 4° Analisar Vendas Totais
vendas_totais = df.groupby('Produto')['Total'].sum()
vendas_totais

# 5° Filtrar Vendas por Data
vendas_2024_01_03 = df[df['Data'] == '2024-01-03']
vendas_2024_01_03

# 6° Salvar o Resultado
df.to_csv('vendas_atualizadas.csv', index=False)
