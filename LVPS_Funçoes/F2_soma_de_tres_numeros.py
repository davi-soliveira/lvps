"""
Faça um programa que leia três número e, a partir de uma função, informe o resultado da soma, dos mesmos.
"""
#função que vai fazer a soma
def f_soma(n1,n2,n3):
    
    return n1+n2+n3 # A soma vai ser feita no return
#função principal
def main():
    #declaração de variavel
    n1 = int(0)
    n2 = int(0)
    n3 = int(0)
    resultado = int(0)
    
    #recebimento de vaiaveis
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    #resultado = f_soma(n1,n2,n3) # invocação da função
    
    #saida de resultados
    #print(resultado)
    
    print(f_soma(n1,n2,n3))#modo mais simplificado tirando as linhas 18,21
    
    
if __name__ == "__main__":
    main()