def main():
    #DECLARAÇÃO DE VARIAVEL
    nome = str("")
    inverso = str("")
    
    #RECEBIMENTO DA VARIAVEL
    nome = input()
    #atribui o nome inverso a variavel inverso
    inverso = nome[::-1]
    
    #faz a checagem para saber se os nomes são iguais
    if nome == inverso:
        print("É PALÍNDROMO")
    else:
        print("NÃO É PALÍNDROMO")
    
if __name__ == "__main__":
    main()