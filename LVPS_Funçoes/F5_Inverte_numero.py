"""
Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721. Usar, exclusivamente, DIV e MOD.

NÃO USAR STRING
"""
def f_tam(n):
    #declaração de variavel
    tam = int(0)
    #inicialização da variavel acumuladora
    tam = 0
    #processamento
    while (n > 0):
        n = n // 10
        tam += 1
        #retorno do resultado
    return tam

def f_inverte(a):
    #declaração de variavel
    novo = int(0)
    p = int(0)
    resto = int(0)
    #inicializando variavel
    novo = 0
    #descobrindo tamanho do numero  
    p = f_tam(a)-1
    #descobrir o tamanho do númeor
    while (a > 0):
        resto = a % 10
        novo += resto * 10 ** p
        p = p - 1
        a = a // 10
    return novo

    
def main():
    #declaração de variavel
    x = int(0)
    
    #recebimento de variavel
    x = int(input())
    x = f_inverte(x)
    #saida de dados
    print(x)

    return 0
    
if __name__ == "__main__":
    main()