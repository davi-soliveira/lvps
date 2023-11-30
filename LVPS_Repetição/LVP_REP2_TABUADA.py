def main():
    #declaração de variavel
    mult = int(0)
    i = int(1)
    #recebimento de variavel
    mult = int(input())
    while i<10+1:
        resp = i * mult
        print(f'{i} X {mult} = {resp}')
        i = i+1
    return 0
if __name__ == "__main__":
    main()
