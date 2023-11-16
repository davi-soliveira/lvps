def main():
    #declaraçao de variavel
    n1 = str()
    n2 = str()
    
    #recebimento de variavel
    n1 = input()
    n2 = input()
    
    if len(n1) == len(n2):
        print("MESMO TAMANHO")
        if n1 == n2:
            print("CONTEÚDO IGUAL")
        else:
            print("CONTEÚDO DIFERENTE")
    else:
        print("TAMANHO DIFERENTE")
        if n1 == n2:
            print("CONTEÚDO IGUAL")
        else:
            print("CONTEÚDO DIFERENTE")
    
    
if __name__ == "__main__":
    main()