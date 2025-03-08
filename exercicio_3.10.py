"""
Programa: parte 3. exercicio 10
Descrição: leia dois numeros a e b e calcule a potencia a^b sem utilizar uma funcao nativa do Python.
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""
# Alocação de memória
a = None
b = None
resultado = None

# Entrada de dados
resultado = 1
a = int(input(f"Digite o valor para a: "))
b = int(input(f"Digite o valor para b: "))

# Processamento de dados
for _ in range(b):
    resultado *=a

# saida de dados
print(f"{a}^{b} = {resultado}")