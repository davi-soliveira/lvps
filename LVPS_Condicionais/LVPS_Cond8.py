def main():
    #declaração de variaveis
    ano = int(0)
    idade = int(0)
    #recebimnto de variaveis
    ano = int(input())
    #processamento de variavel
    idade = 2021 - ano

    if idade >=16:
        print("PODE VOTAR")
    else:
        print("NÃO PODE VOTAR")
if __name__ == "__main__":
    main()