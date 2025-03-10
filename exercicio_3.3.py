"""
Programa: parte 3. exercicio 3
Descrição: leia cinco n´umeros e imprima na tela o quadrado de cada um deles.
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""


# entrada de dados
numeros = []

# armazenamento de dados
for i in range(5):
    num = float(input(f"digite o {i+1}° numero: "))
    numeros.append(num)

# processamento e saida de dados
for num in numeros:
    quadrado = num**2
    print(f'o quadrado de {num} é {quadrado}')