"""
Faça um programa que verifique os números de 1 a 5000 (ambos incluídos), identificando os que são quadrados perfeitos e capicuas (capicuas é aquilo que lido de trás para frente é a mesma coisa: 121, 1001, 4334 etc)

Utilize as seguintes funções externas criadas por você:

a) uma função que retorne o tamanho de um número 

b) um função que inverta um número

c) uma função que verifique se o número é um quadrado perfeito

d) um função que verifique se um número é uma capicua

os outputs devem seguir o seguinte modelo

X É CAPICUA E QUADRADO PERFEITO

OU

X É CAPICUA

OU

X É QUADRADO PERFEITO

onde X é o número que está sendo testado

NÃO UTILIZE STRINGS
"""
#LVP FUNÇÃO 10
def f_tam(n):
    #declaração de variáveis
    tam = int(0)
    #inicialização da variável acumuladora
    tam = 0
    #processamento
    while (n > 0):
        n = n // 10
        tam += 1
    #retorno do resultado
    return tam

def f_inverte(a):
    #declaração de variáveis
    novo = int(0)
    p = int(0)
    resto = int(0)
    
    #inicialização da variável acumuladora
    novo = 0
    #descobrir o tamanho do número
    p = f_tam(a)-1
    while (a > 0):
        #apropriação do último algarismo do número
        resto = a % 10
        #acumulando o novo número
        novo += resto*10**p
        #redução de a por 10
        a = a // 10
        #redução da potencia por 1
        p = p - 1
        #retorno do resultado
    return novo

def f_capicua(x):
    if (x == f_inverte(x) and x >= 10):
        return True
    return False

def f_qperfeito(x):
    #declaração de variáveis
    y = int(0)
    #inicialização de variável acumuladora 
    y = 1
    while (y**2 <= x):
        if (y**2 == x):
            return True
        y += 1
    return False

def main():
    #declaração de variáveis
    n = int(0)

    #entrada de dados
    for n in range(1,5001):
        if (f_capicua(n) and f_qperfeito(n)):
            print(f'{n} É CAPICUA E QUADRADO PERFEITO')
        elif (f_capicua(n)):
            print(f'{n} É CAPICUA')
        elif (f_qperfeito(n)):
            print(f'{n} É QUADRADO PERFEITO')
    return 0

if __name__ == "__main__":
    main()
