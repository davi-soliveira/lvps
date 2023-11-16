def main():
    
    #declaração de variaveis
    a = int(0)
    b = int(0)
    c = int(0)
    soma = int(0)
    
    #recebimento de variaveis
    a = int(input())
    b = int(input())
    c = int(input())
    
    #processamento
# faz a checagem para saber se todos os lados são iguais
    if a==b==c:
        print('EQUILÁTERO')
#faz a checagem para saber se um lado e diferente
    elif a==b!=c or a==c!=b or a!=b==c:
        print('ISÓSCELES')
#faz a checagem para saber se todos os lados são diferentes
#sendo diferentes ele faz o calculo para saber se os 2 menores numeros são maiores que o primeiro, sendo maior e um triangulo escaleno sendo menor não e um triangulo.
    if a!=b!=c:
        if a>b and a>c:
            soma = b+c
            if soma>a:
                print('ESCALENO')
            else:
                print('NÃO É TRIÂNGULO')
        elif b>c:
            soma = c+a
            if soma>b:
                print('ESCALENO')
            else:
                print('NÃO É TRIÂNGULO')
        else:
            soma = b+a
            if soma>c:
                print('ESCALENO')
            else:
                print('NÃO É TRIÂNGULO')

    
if __name__ == "__main__":
    main()
