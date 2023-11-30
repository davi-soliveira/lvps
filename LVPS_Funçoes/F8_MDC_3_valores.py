"""
Baseado no exercício 1.12.60 Livro Farrer - página 85 com algumas modificações no enunciado.

Faça um programa em Python3, DE FORMA MODULAR (DEFININDO E USANDO SUAS PRÓPRIAS FUNÇÕES) EM ARQUIVO EXTERNO para resolver o seguinte problema:

a) Definir uma função em Python 3 que calcule o valor do máximo divisor comum (mdc) entre três números inteiros positivos. Esta função recebe como parâmetro três números inteiros positivos e retorna o valor do mdc calculado. 

b) Faça um programa principal que leia 4 conjuntos com 3 números inteiros positivos. Para cada conjunto de três números lidos, imprima os números lidos na ordem em que foram lidos e o valor do mdc calculado. A saída deste programa deverá ser EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo.

c) Invocar o programa principal.

Seu formato de saída deve ser IDÊNTICO A ESTE EXEMPLO, onde os valores de  N1, N2 e N3 são os três números de entrada lidos, e RESULTADO é o valor resultante do cálculo do mdc entre N1, N2 e N3.

MDC(N1, N2, N3)=RESULTADO 
input=6
12
15
30
36
75
8
12
28
180
240
270
output=MDC(6, 12, 15)=3
MDC(30, 36, 72)=6
MDC(8, 12, 28)=4
MDC(180, 240, 270)=30
"""
def f_menor(a,b,c):
    if (a < b and a < c):
        return a
    elif (b < c):
        return b
    else:
        return c
def f_mdc(a,b,c):
    divisor = f_menor(a,b,c)
    while (divisor > 0):
        if (a % divisor == 0 and b % divisor == 0 and c % divisor == 0):
            return divisor
        divisor -= 1

def main():
    #declaração de variáveis
    a = int(0) 
    b = int(0)
    c = int(0)
    #entrada de dados
    for i in range(4):
        a = int(input())
        b = int(input())
        c = int(input())
        print(f'MDC({a}, {b}, {c})={f_mdc(a,b,c)}')
    return 0

if __name__ == "__main__":
    main()