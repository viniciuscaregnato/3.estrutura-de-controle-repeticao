"""
Programa: parte 3. exercicio 8
Descrição: imprima na tela a soma dos numeros de 1 a 100.
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""
# Alocação de memória
i = None
inicio = None
fim = None
soma = None

# Entrada de dados
inicio = 1
fim = 101
soma = 0

# Processamento e saída de dados

for i in range(inicio, fim):
    soma += i
    print(soma)

# Saida de dados
print(f'o resultado final é, então {soma}')

