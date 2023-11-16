def main():
    #declaração de variavel
    op = int(0)
    
    #recebimento de variavel
    op = int(input())
    
    #validação
    
    while op < 1 or op > 6:
        print("OPÇÃO INVÁLIDA. DIGITE UM VALOR DE 1 A 6")
        
        op = int(input())
        
    if op >=1 and op <=6:
        print("OPÇÃO VÁLIDA")
    return 0
if __name__ == "__main__":
    main()