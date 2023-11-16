def main():
    #DECLARAÇÃO DE VARIAVEL
    nome = str("")
    invertido = str("")
    
    nome = input().upper()
    for i in nome:
        invertido = nome[-1::-1]
    print(invertido)
   

        
    
    
    
if __name__ == "__main__":
    main()