import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
vendas_norte = np.random.randint(5000, 15000, size=12)
vendas_sul = np.random.randint(3000, 12000, size=12)
vendas_leste = np.random.randint(4000, 14000, size=12)
vendas_oeste = np.random.randint(6000, 16000, size=12)

# Gráfico de linha

plt.figure(figsize=(10, 6))
plt.plot(meses, vendas_norte, marker='o', linestyle='-', color='r', label='Norte')
plt.plot(meses, vendas_sul, marker='o', linestyle='--', color='g', label='Sul')
plt.plot(meses, vendas_leste, marker='o', linestyle='-.', color='b', label='Leste')
plt.plot(meses, vendas_oeste, marker='o', linestyle=':', color='m', label='Oeste')
plt.title('Vendas Mensais por Região')
plt.xlabel('Meses')
plt.ylabel('Vendas (R$)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Gráfico de Barras

vendas_totais = [np.sum(vendas_norte), np.sum(vendas_sul), np.sum(vendas_leste), np.sum(vendas_oeste)]
regioes = ['Norte', 'Sul', 'Leste', 'Oeste']

plt.figure(figsize=(8, 6))
plt.bar(regioes, vendas_totais, color=['r', 'g', 'b', 'm'])
plt.title('Vendas Totais por Região')
plt.xlabel('Regiões')
plt.ylabel('Total de Vendas (R$)')
plt.show()

# Histograma

plt.figure(figsize=(10, 6))
plt.hist(vendas_norte, bins=5, color='c', edgecolor='black')
plt.title('Distribuição das Vendas Mensais - Região Norte')
plt.xlabel('Vendas (R$)')
plt.ylabel('Frequência')
plt.show()

# Personalização e Salvamento

plt.figure(figsize=(10, 6))
plt.plot(meses, vendas_norte, marker='o', linestyle='-', color='r', label='Norte')
plt.title('Vendas Mensais - Região Norte')
plt.xlabel('Meses')
plt.ylabel('Vendas (R$)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('grafico_vendas_norte.png', format='png')
plt.savefig('grafico_vendas_norte.pdf', format='pdf')
plt.savefig('grafico_vendas_norte.svg', format='svg')
plt.show()
