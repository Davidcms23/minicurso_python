import numpy as np

# 1. Geração de Dados
temperaturas = np.random.uniform(low=-10, high=35, size=10)
print("Temperaturas em graus Celsius:", temperaturas)

# 2. Conversão de Unidades
temperaturas_fahrenheit = (temperaturas * 9/5) + 32
print("\nTemperaturas em graus Fahrenheit: ", temperaturas_fahrenheit)

# 3. Estatísticas Descritivas
print(f"Média: {np.mean(temperaturas):.2f}°C")
print(f"Mediana: {np.median(temperaturas):.2f}°C")
print(f"Desvio Padrão: {np.std(temperaturas):.2f}°C")
print(f"Temperatura Máxima: {np.max(temperaturas):.2f}°C")
print(f"Temperatura Mínima: {np.min(temperaturas):.2f}°C")

# 4. Estatísticas Descritivas
print("\nTemperaturas acima de 25°C: ", temperaturas[temperaturas > 25])

print("\nTemperaturas abaixo de 0°C: ", temperaturas[temperaturas < 0])
