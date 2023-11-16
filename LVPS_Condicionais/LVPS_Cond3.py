def main()

    #declaração de variaveis
    n1 = int(0)
    n2 = int(0)
    diferenca = int(0)
    #recebimento de variaveis
    n1 = int(input())
    n2 = int(input())
    
    #processamento
    
    diferenca = n1 - n2
    if diferenca <0:
        
        print(diferenca *-1)
        
    else:
        print(diferenca)
        
if __name__ == "__main__":
    main()