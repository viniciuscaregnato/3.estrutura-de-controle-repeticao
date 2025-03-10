"""
Programa: parte 3. exercicio 2
Descrição: determine a raiz quadrada de um n´umero dado pelo usuario, sabendo que o algoritmo de
para o c´alculo da raiz quadrada do numero a é dado pela sequencia
x1 > 0

xn+1 =1/2 . (xn + a/xn)
Autor: Vinicius Garcia
Versão: 0.0.1
Data: 03/03/2025
"""

# entrada de dados
x = 0

# armazenamento de dados
while True:
    x = float(input("digite um numero maior que zero: "))
    if x > 1:
        break
    else:
        print(f" numero {x} inválido. Digitar novamente.")

# processamento de dados
resultado = x**(1/2)

# saida de dados
print(f' a raiz de {x} é {resultado}.')