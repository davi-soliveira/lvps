def main():
    #declaração de variaveis
    numero = int(0)
    centena = int(0)
    parte = int(0)
    unidade = int(0)
    dezena = int(0)
    numero_inveretido = int(0)
    
    #recebimento de variaveis
    numero = int(input(""))
    
    #processameno
    centena = numero // 100
    unidade = numero % 10
    parte = numero //10
    dezena = parte % 10
    numero_invertido = unidade *100 + dezena * 10 + centena
    
    #saida de dados
    print(f'{numero_invertido}')
    
    return 0
if __name__ == "__main__":
    main()