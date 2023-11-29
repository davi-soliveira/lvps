def main():
    #declaração
    flag = str('')
    soma = int(0)
    n1 = int(0)
    flag = input('<s/n>')
    while flag == 's':
        n1 = int(input())
        soma = soma + n1
        flag = input('<s/n>')
    print(soma)
    
    
    return 0
if __name__ == "__main__":
    main()
