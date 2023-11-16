def main():
    #declaração de variavel
    tamanho_arquivo = float(0)
    velocidade = float(0)
    tempo_download = float(0)
    
    #recebimento de variaveis
    tamanho_arquivo = float(input())
    velocidade = float(input())
    
    #processamento
    tempo_download = tamanho_arquivo/(velocidade/8)
    
    #saida de dados
    print(f'{tempo_download:.2f} segundos')
    
    
    
    
if __name__ == "__main__":
    main()