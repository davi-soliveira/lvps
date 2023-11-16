def main():
    #declaração de variavel
    resp = str("")
    op = int(0)
    n1 = int(0)
    n2 = int(0)
    soma = int(0)
    sub = int(0)
    mult = int(0)
    div = int(0)
    pot = int(0)
    raiz = int(0)
    
    resp = input("Deseja fazer alguma conta <S/N>: ")
    
    while resp.upper() == "S":
        op = int(input("Digite \n 1-Soma 2-Subtração 3-Multiplicação 4-Divisão 5-Exponeciação 6-Raiz: "))
        n1 = int(input("digite um numero: "))
        n2 = int(input("digite outro numero: "))
        if op == 1:
            soma = n1 + n2
        elif op == 2:
            sub = n1 - n2
        elif op == 3:
            mult = n1 * n2
        elif op == 4:
            div = n1 / n2
        elif op == 5:
            pot = n1 ** n2
        elif op == 6:
            raiz = n1 **(1/n2)

           
            
        resp = input("Deseja fazer alguma conta <S/N>: ")
    print(soma)
    print(sub)
    print(mult)
    print(div)
    print(pot)
    print(raiz)
    print('OPERACAO INVALIDA')
    
    
    
if __name__ == "__main__":
    main()