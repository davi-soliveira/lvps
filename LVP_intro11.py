def main():
    #declaração de variaveis
    raio = float(0.0)
    area = float(0.0)
    
    #recebimento de variaveis
    raio = float(input("digite o raio da circunferencia: "))
    
    #processamento
    area = 3.14159 * (raio**2)
    
    #saida de dados
    print(f'{area}')
    
if __name__ == "__main__":
    main()