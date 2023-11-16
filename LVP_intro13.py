def main():
    #declaração de variavel
    dias_totais = int(0)
    dias = int(0)
    mes = int(0)
    anos = int(0)
    r_anos = int(0)
    
    #recebimento de variavel
    dias_totais = int(input('')) 
    
    #processamento
    anos = dias_totais // 365
    r_anos = dias_totais % 365
    mes = r_anos // 30
    dias = r_anos % 30
    
    
    #saida de dados
    print(anos,mes,dias)
if __name__ == "__main__":
    main()
    
    
    
    
    #div anos que ele tem mod resto das idades