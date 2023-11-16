def main():
    #declaração de variaveis
    carros_vendidos = int(0)
    valor_vendas = float(0.0)
    salario_fixo = float(0.0)
    valor_recebe_carro = float(0.0)
    salario_final = float(0.0)
    
    #recebimento de variaveis
    carros_vendidos = int(input("numero carros vendidos: "))
    valor_vendas= int(input("valor total das vendas: "))
    salario_fixo= int(input("salario fixo: "))
    valor_recebe_carro= int(input("Valor recebido por carro: "))
    
    #processamento
    salario_final = (valor_vendas * 0.05) + (valor_recebe_carro * carros_vendidos) + salario_fixo
    
    #saida de dados
    print(f'{salario_final}')
    
if __name__ == "__main__":
    main()