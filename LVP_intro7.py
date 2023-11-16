def main():
    #Declaração de variaveis
    salario = int(0)
    percentual = int(0)
    
    #recebimento de variaveis
    salario = int(input("digite o valor do se salario: "))
    percentual = int(input("digite o percentual: "))
    
    #processamento de dados
    reajuste = (salario*percentual) / 100
    total = (salario + reajuste)
    
    #saida de dados
    print(f'salario reajustado e = {total}')

if __name__ == "__main__":
    main()