def main():
    #declaração de variavel
    flag = ('')
    n1 = int(0)
    media = float(0)
    i = int(0)
    soma = int(0)
    
    #recebimento de variavel
    
    flag = input('<s/n>')
    
    while flag == 's':
        
        n1 = int(input())
        soma = soma + n1
        i = i +1
        media = soma / i
        flag = input('<s/n>')
    print(media)
    
    
    return 0
if __name__ == '__main__':
    main()
