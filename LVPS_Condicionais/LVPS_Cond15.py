def main():
    #declaração de variavel
    h_inicio = int(0)
    h_fim = int(0)
    duracao = int(0)
    
    #recebimento de variaveis
    h_inicio = int(input())
    h_fim = int(input())
    
    #processamento
    if h_inicio >= h_fim:
        duracao = (24 - h_inicio) + h_fim
        print(duracao)
    else:
        duracao = h_fim - h_inicio
        print(duracao)
    
    
if __name__ == "__main__":
    main()