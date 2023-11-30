"""
Faça um programa que leia dois número e, a partir de uma função, informe o resultado da soma, dos mesmos.
"""
def f_soma(n1,n2):
    resultado = n1 + n2
    return resultado
    
def main():
    #declaração de variavel
    n1 = int(0)
    n2 = int(0)
    resultado = int(0)
    #recebimento de variaveis
    n1 = int(input())
    n2 = int(input())
    
    resultado = f_soma(n1,n2)
    #saida de dados
    print(resultado)    
    
    
    
if __name__ == "__main__":
    main()