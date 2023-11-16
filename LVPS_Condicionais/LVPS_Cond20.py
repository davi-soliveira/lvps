def main():
    h1 = int(0)
    h2 = int(0)
    m1 = int(0)
    m2 = int(0)
    soma = int(0)
    produto = int(0)
    
    #recebimento de variaveis
    h1 = int(input())
    h2 = int(input())
    m1 = int(input())
    m2 = int(input())
    
    #processamento
    if h1 > h2:
        if m1>m2:
            soma = h1 + m2
            produto = h2 * m1
            print(f'{soma} {produto}')
        soma = h1 + m1
        produto = h2 * m2
        print(f'{soma} {produto}')
    else:
        if h2>h1:
            if m2 > m1:
                soma = h2 + m1
                produto = h1 * m2
                print(f'{soma} {produto}')
            soma = h2 + m2
            produto = h1 * m1
            print(f'{soma} {produto}')
   
    
    
    
    
if __name__ == '__main__':
    main()