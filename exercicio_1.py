"""
Programa: parte 2. exercicio 1
Descrição: leia um numero e imprima na tela o seu dobro se ele for menor do que 10. Se o numero
for de 10 ate 20, imprima a sua metade. Em qualquer outro caso, imprima na tela que o
numero nao é valido.

Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""

# Alocação de memória
numero = None

# Entrada de dados
numero = float(input("Digite um numero: "))

# Processamento de dados
if numero < 10:
    resposta = numero*2
elif 10 <= numero < 20:
    resposta = numero/2
else:
    resposta = str("o numero nao é valido.")

# Saída de dados
print(resposta)