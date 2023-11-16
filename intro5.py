def main():
    #declaração de variavel
    anos = int(0)
    mes = int(0)
    dias = int(0)
    
    #entrada de infomação
    anos = int(input())
    mes = int(input())
    dias = int(input())
    
    #processamento de dados
    dias_totais = ((anos * 365)+(mes * 30) + dias)
    
    #saida de informações
    print(dias_totais)
    
if __name__ == "__main__":
    main()