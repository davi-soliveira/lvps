"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado, UTILIZANDO DIV E MOD. SEM USAR RECURSO DE STRING
"""
def f_tam(n):
    #declaração de variavel
    tam = int(0)
    #inicialização da variavel acumuladora
    tam = 0
    #processamento
    while (n > 0):
        n = n // 10
        tam +=1
        #retorno do resultado
    return tam
def main():
    #declaração de variavel
    x = int(0)
    
    #entrada de dados
    x = int(input())
    
    #saida de dados e evocação da fução
    print(f_tam(x))
    return 0
    
    
    
if __name__ == "__main__":
    main()