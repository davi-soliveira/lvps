def main():
    #declaração de variavel
    resp = str("")
    
    #recebimento de variavel
    resp = input().upper()
    
    #validação
    while resp != "S" and resp != "N":#se a resposta for diferente de s e n o while e ativado
        print("RESPOSTA INCORRETA, DIGITE S OU N")
        
        resp = input().upper()
    #vai entrar no if quando a respota for igual a S OU N    
    if resp == "S" or resp == "N":
        print("RESPOSTA CORRETA")
    
    
    
if __name__ == "__main__":
    main()