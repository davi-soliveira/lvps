def main():
    
    #declaração de variavel
    n1 = float(0.0)
    n2 = float(0.0)
    n3 = float(0.0)
    n4 = float(0.0)
    media = float(0.0)
    #recebimento de variavel
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    
    #processamento e saida de dados
    
    media = (n1+n2+n3+n4)/4
    
    if media >= 60:
        print("Aprovado")
    else:
        print("Reprovado")
    
if __name__ == "__main__":
    main()