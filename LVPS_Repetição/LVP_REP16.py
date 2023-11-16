def main():
    #declaração de variavel
    idade = int(0)
    media = float(0.0)
    soma = int(0)
    #flag
    i = int(0)
    
    idade = int(input('Digite sua idade ou 0 para sair: '))
    while idade > 0:
        i += 1
        soma += idade
        idade = int(input('Digite sua idade ou 0 para sair: '))
    media = soma/i
    print(media)
    
    return 0
    
    
    
    
    
if __name__ == "__main__":
    main()