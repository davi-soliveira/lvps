def main():
    #declaração de variaveis
    a = int(0)
    b = int(0)
    c = int(0)
    
    #recebimento de variaveis
    a = int(input())
    b = int(input())
    c = int(input())
    
    #processamento
    if a>b and a>c:
        print(a)
    else:
        if b>a and b>c:
            print(b)
        else:
            print(c)
    
    
if __name__ == "__main__":
    main()