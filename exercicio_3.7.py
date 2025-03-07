"""
Programa: parte 3. exercicio 6
Descrição: imprima na tela todos os numeros pares de 1 a 100.
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""
# Alocação de memória
i=""
fim=0

# Entrada de dados
chave = input("Digite 'pares': ")
i=0
fim = 100

# Processamento e saida de dados
if chave == "pares":
    while i <= fim:
        print(i)
        i += 2
