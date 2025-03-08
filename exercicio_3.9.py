"""
Programa: parte 3. exercicio 9
Descrição:  leia 6 numeros e imprima o cubo e a raiz c´ubica de cada um deles.
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""
# Alocação de memória
numeros = []

# Entrada de dados
numeros = [float(input(f"Escreva o {i+1}° numero: ")) for i in range(6)]

# Processamento e saída de dados

for num in numeros:
    cubo = num**3
    raiz_cubica = num**(1/3)
    print(f"Número: {num}, Cubo: {cubo:.2f}, Raiz cúbica: {raiz_cubica:.2f}")
