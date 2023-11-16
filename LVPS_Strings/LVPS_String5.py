def main():
    #DECLARAÇÃO DE VARIAVEL
    nome = str("")
    #recebimento de variavel
    nome = input().upper()
    
   #inicia com o numero completo da variavel e vai subtraindo 1
    for i in range(len(nome),-1,-1):
        
        print(nome[0:i])
    
if __name__ == "__main__":
    main()