def main():
    #declaração de variaveis
    custo_fabrica = float(0.0)
    custo_final = float(0.0)
    imposto = float(0.0)
    perct_distribuidor = float(0.0)
    
    #recebimento de valores
    custo_fabrica = float(input())
    #processamento
    perct_distribuidor = custo_fabrica * 0.28
    imposto = custo_fabrica * 0.45
    custo_final = custo_fabrica + imposto + perct_distribuidor
    
    #saida de dados
    print(f'{custo_final}')
    return 0
if __name__ == "__main__":
    main()