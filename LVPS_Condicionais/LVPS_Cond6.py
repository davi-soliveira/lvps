def main():
    #declaração de variaveis
    n1 = int(0)
    div = int(0)
    #recebimento de variaveis
    n1 = int(input())
    #processamento
    div = n1%3
    if div == 0:
        print(div)
    else:
        print(n1)

if __name__ == "__main__":
    main()