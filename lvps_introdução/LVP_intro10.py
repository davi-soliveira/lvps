def main():
    #declaração de variaveis
    fah = float(0.0)
    cel = float(0.0)
    #recebimento de valores
    fah = float(input("insira o valor em fahrenhei para ser convertido para celsius: "))
    #processamento
    cel = (fah - 32)/1.8
    
    #saida de dados
    print(f'{cel}')
    
if __name__ == "__main__":
    main()