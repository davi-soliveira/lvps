def main():
    #declaração de variaveis
    frase = str("")
    cont_espaco = int(0)
    cont_a = int(0)
    cont_e = int(0)
    cont_i = int(0)
    cont_o = int(0)
    cont_u = int(0)
    
    #inicialização de variaveis acumuladoras
    cont_espaco = 0
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0
    
    #entrada de dados
    frase = input().upper()
    
    for i in range(len(frase)):
        if (frase[i] == " "):
            cont_espaco += 1
        elif (frase[i] == "A"):
            cont_a += 1
        elif (frase[i] == "E"):
            cont_e += 1
        elif (frase[i] == "I"):
            cont_i += 1
        elif (frase[i] == "O"):
            cont_o += 1
        elif (frase[i] == "U"):
            cont_u += 1
    print(f'ESPAÇOS EM BRANCO = {cont_espaco}')
    print(f'A = {cont_a}')
    print(f'E = {cont_e}')
    print(f'I = {cont_i}')
    print(f'O = {cont_o}')
    print(f'U = {cont_u}')
    
    
    
    
    
    
    return 0
    
if __name__ == "__main__":
    main()