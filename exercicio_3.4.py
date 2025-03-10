"""
Programa: parte 3. exercicio 4
Descrição: imprima na tela todos os n´umeros pares entre 0 e 20
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""



# entrada de dados
numeros=[]

# armazenamento de dados
numeros = list(range(0,21))

# processamento e saida de dados
for n in numeros:
    if n %2  == 0:
        print(n+2)
    
