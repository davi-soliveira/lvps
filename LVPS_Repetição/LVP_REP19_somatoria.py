def main():
    #declaração de variáveis
    s = float(0.0)
    i = int(0)
    
    #inicialização das variáveis
    s = 0 #variável acumuladora
    
    #processamento
    for i in range(1, 11):
        if(i % 2 == 0):
            s -= i / (i * i)
        else:
            s += i / (i * i)
    
    #saída de dados
    print(f'O valor de S é: {s}')
    return 0
    
if __name__ == "__main__":
    main()
