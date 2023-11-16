def main():
    #declaração de variaveis
    n1 = int(0)
    n2 = int(0)
    n3 = int(0)
    n4 = int(0)
    soma = int(0)
    
    #recebimento de variaveis
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    
    #processameno
    if n1 > n2 and n1 > n3 and n1 > n4: #checage se n1 e maior
        if n2<n3 and n2<n4:     # checagem para saber se n2 e menor
            soma = n1+n2
            print(soma)
        elif n3<n4:     #checagem para saber se n3 e menor
            soma = n3+n1
            print(soma)
        else:   # n4 e o menor
            soma = n1+n4
            print(soma)
    elif n2>n1 and n2>n3 and n2>n4: #checagem se n2 e maior
        if n1<n3 and n1<n4: # checagem para saber se n1 e o menor
            soma = n1 + n2
            print(soma)
        elif n3<n4: #checagem para saber se n3 e menor
            soma = n3+n2
            print(soma)
        else:   #n4 e o menor
            soma = n4 + n2
            print(soma)
    elif n3>n1 and n3>n2 and n3>n4: # checagem se n3 e maior
        if n1<n2 and n1<n4: # checagem para saber se n1 e o menor
            soma = n1 + n3
            print(soma)
        elif n2<n4: # checagem para saber se n2 e o menor
            soma = n2+n3
            print(soma)
        else:   #n3 e o menor
            soma = n4 + n3
            print(soma)
    else:   # n4 e o maior
        if n1<n2 and n1<n3: # checagem para saber se n1 e o menor
            soma = n1 + n4
            print(soma)
        elif n2<n3: # checagem para saber se n2 e o menor
            soma = n2+n4
            print(soma)
        else:   #n3 e o menor
            soma = n3 + n4
            print(soma)
    
    
    
if __name__ == '__main__':
    main()