def main():
    #declaração de variaveis
    operacao = int(0)
    n1 = int(0)
    n2 = int(0)
    soma = int(0)
    sub = int(0)
    div = int(0)
    expo = int(0)
    mult = int(0)
    raiz = int(0)
    #recebimento de variaveis
    operacao = int(input())


    #processamento
    if operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4 or operacao == 5 or operacao == 6:
        n1 = int(input())
        n2 = int(input())
        if operacao == 1:
            soma = n1 + n2
            print(soma)
        elif operacao == 2:
            sub = n1- n2
            print(sub)
        elif operacao == 3:
            mult = n1*n2
            print(mult)
        elif operacao == 4:
            div = n1/n2
            print(div)
        elif operacao == 5:
            expo = n1 ** n2
            print(expo)
        elif operacao == 6:
            raiz = n1 ** (1/n2)
            print(raiz)
    else:
        print("OPERACAO INVALIDA")
    
if __name__ == '__main__':
    main()