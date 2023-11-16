def main():
    #declaração de variavel
    velocidade = float(0.0)
    v_i = float(0.0)
    aceleracao = float(0.0)
    espaco = float(0.0)
    e_i = float(0.0)
    tempo = float(0.0)
    
    #recebimento de variavel
    aceleracao = float(input())
    tempo = float(input())
    
    #processamento
    velocidade = v_i + (aceleracao * tempo)
    espaco = e_i + v_i * tempo + (1/2)*aceleracao*(tempo**2)
    
    #saida de dados
    
    print(f'{velocidade} m/s e {espaco} m')
    
    
    
if __name__ == "__main__":
    main()