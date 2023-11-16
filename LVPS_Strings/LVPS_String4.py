def main():
    #DECLARAÇÃO DE VARIAVEL
    nome = str("")
    #recebimento de variavel
    nome = input().upper()
    
    #faz a repetição somando a cada linha uma palavra
    for i in range(1,len(nome)+1):#soma mais 1 para colocar o nome completo
        
        print(nome[:i])
    
if __name__ == "__main__":
    main()