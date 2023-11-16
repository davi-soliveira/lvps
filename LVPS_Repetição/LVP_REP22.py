def main():
    #declaração de variáveis
    nick = str("") 
    soma = int(0)
    ponto = str("")
    soma_pontos = int(0)
    #inicialização de variáveis
    soma_pontos = 0
    cont = 0
    #entrada de dados
    nick = input("")
    while (nick != ""):
        soma = 0
        for i in range(10):
            ponto = input("")
            if (ponto == "A1"):
                soma += 5
            elif (ponto == "A2"):
                soma += 7
            elif (ponto == "A3"):
                soma += 10
            elif (ponto == "E1"):
                soma -= 2
            elif (ponto == "E2"):
                soma -= 5
            elif (ponto == "E3"):
                soma = 0

            if (soma < 0):
                soma = 0

        #imprime cada jogador com sua pontuação final
        print(f'{nick} {soma} pontos')
    
        #acumula pontos para calcular a média
        soma_pontos += soma
        #verifica o jogador com a maior pontuação
        if (cont == 0):
            nick_maior = nick
            soma_maior = soma
        elif (soma > soma_maior):
            nick_maior = nick
            soma_maior = soma
        cont += 1
        nick = input("")
    print(f'Média de pontos = {soma_pontos/cont:.2f} por jogo')
    print(f'Vencedor {nick_maior} com {soma_maior} pontos')

    return 0

if __name__ == "__main__":
    main()
