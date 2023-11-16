def main():
    #declaração de variaveis
    n1 = int(0)
    n2 = int(0)
    n3 = int(0)
    maior_1 = int(0)
    maior_2 = int(0)
    
    #recebimento de variaveis
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    #processamento
    resultado = maior_1 + maior_2
    if n1>n2 and n1>n3:
        maior_1 = n1
        if n2>n3:
            maior_2 = n2
        else:
            maior_2 = n3
    resultado = maior_1 + maior_2
    if n2 >n1 and n2 >n3:
        maior_1 = n2
        if n1>n3:
            maior_2 = n1
        else:
            maior_2 = n3
    resultado = maior_1 + maior_2
    if n3>n1 and n3>n2:
        maior_1=n3
        if n1>n2:
            maior_2 = n1
        else:
            maior_2 = n2
    resultado = maior_1 + maior_2
    
    print(resultado)
    
    
if __name__ == "__main__":
    main()