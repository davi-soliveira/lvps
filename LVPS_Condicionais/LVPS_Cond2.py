def main():
    #declaração de variaveis
    a = int(0)
    b = int(0)
    res_ab = int(0)
    res_ba = int(0)
    
    #recebimento de variaves
    a = int(input())
    b = int(input())
    
    #processamento e saida de dados
    
    if(a>b):
        res_ab = a + b
        print(res_ab)
    else:
        res_ba = a * b
        print(res_ba)
    
    
    
if __name__ == "__main__":
    main()