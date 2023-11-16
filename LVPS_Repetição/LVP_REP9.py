def main():
    #declaração de variavel
    numero = int(0)
    soma = 0
    media = int(0)
    #contador e 
    i = 1
    while i <= 5:
        numero = int(input())
        
        soma = soma + numero
        i = i + 1
        media = soma/5
    print(media)
    
    
    
    
    
if __name__ == "__main__":
    main()