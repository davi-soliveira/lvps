def main():
    #declaração de variaveis
    t1 = str("")
    t2 = str("")
    g1 = int(0)
    g2 = int(0)
    resultado = str("")
    soma = int(0)
    soma_gols = int(0)
    cont_jogos = int(0)
    media_gols = float(0.0)
    mais_gols = int(0)
    time_mais_gols = str("")
    menor_num_gols = int(0)
    
    #inicialização de variaveis acumuladoras
    soma = 0
    soma_gols = 0
    cont_jogos = 0
    
    #entrada de dados
    t1 = input()#inicialização da v. de controle
    while (t1 != ""): #condição de parada
        t2 = input()
        g1 = int(input())
        g2 = int(input())
        if (g1 > g2):
            resultado = t1
        elif (g2 > g1):
            resultado = t2
        else:
            resultado = "Empate"
        print(f'{t1} x {t2}')
        if (g1 != g2):
            print(f'Vencedor: {resultado}')
        else:
            print(f'{resultado}')
        soma = g1+g2
        soma_gols += soma
        #verifica time que fez mais gols
        if (cont_jogos == 0):
            if (g1 > g2):
                mais_gols = g1
                time_mais_gols = t1
            else:
                mais_gols = g2
                time_mais_gols = t2
        else:
            if (g1 > g2) and (g1 > mais_gols):
                mais_gols = g1
                time_mais_gols = t1
            elif (g2 > mais_gols):
                mais_gols = g2
                time_mais_gols = t2
        #verifica menor numero de gols em uma partida
        if (cont_jogos == 0):
            menor_num_gols = soma
        elif (soma < menor_num_gols):
            menor_num_gols = soma
            
        cont_jogos += 1
        t1 = input() #atualização da v. de controle
    media_gols = soma_gols/cont_jogos
    print(f'Média de Gols: {media_gols:.2f} por jogo')
    print(f'Time que fez mais gols em um jogo: {time_mais_gols}')
    print(f'Menor número de gols em uma partida {menor_num_gols}')
    
    return 0
    
if __name__ == "__main__":
    main()
