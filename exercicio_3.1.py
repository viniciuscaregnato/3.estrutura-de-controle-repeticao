"""
Programa: parte 3. exercicio 1
Descrição:  calcule o valor de um polinomio de grau n supondo que o usuario informou o grau do
polinomio e os coeficientes na ordem da lista ordenada
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""

# Alocação de memória
g_polinomio = None
coef = []
polinomio_str = ""
resultado = 0

# Entrada de dados
g_polinomio = int(input("Digite o grau do polinomio: "))
for i in range(g_polinomio):
    coeficiente = float(input(f"Digite o coeficiente de x^{i+1}: "))
    coef.append(coeficiente)
x_valor = float(input("digite o valor de x: "))

# Processamento de dados
for i, coeficiente in enumerate(coef):
    resultado += coeficiente*(x_valor**(i+1))

#saida de dados
print(f"Resultado do polinômio para x = {x_valor}: {resultado}")
