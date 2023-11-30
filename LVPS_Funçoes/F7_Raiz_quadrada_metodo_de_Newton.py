"""
Calculando um quadrado, por aproximação, usando o método de Newton.
Para começar o método, você deve procurar o quadrado perfeito mais próximo do número em questão.

Por exemplo, se você quer calcular uma aproximação para √124, então o quadrado perfeito mais próximo será 121.

Vamos chamar este quadrado perfeito mais próximo de x2. A sua raiz quadrada será x.

Pois bem, √a pode ser aproximada por (a+x2)/2x, em que x2 é o quadrado perfeito mais próximo de a.

Exemplo:

Queremos calcular a raiz quadrada de 124. Veja o passo a passo.

i) Qual é o quadrado perfeito mais próximo? 121.

ii) No numerador, colocamos 124 + 121 = 245.

iii) No denominador, colocamos 2 vezes 11 = 22. Perceba que 11 é a raiz de 121.

iv) Pronto! √124 ≈ 245/22 ≈ 11,136.

Dado o exemplo, faça um programa que calcule a aproximação do quadrado de diversos números INTEIROS pelo método de Newton, utilizando funções em um arquivo externo. Utilize uma função para encontrar o quadrado perfeito mais próximo e outra função para calcular a raiz. A condição de parada será quando um número negativo for informado.

Formate a saída do valor de entrada para 4 casas decimais e o de saída para 6 casas decimais. (pesquisar por format em prints)
"""
def f_maisPróximo(x,a):
    if (a - x**2 < (x+1)**2 - a):
        return x
    else:
        return x + 1

def f_procuraRaizProx(a):
    n = 1
    while(n**2 < a):
        n = n + 1
    n = f_maisPróximo(n-1,a)
    return n**2

def f_calculaRaizNewton(a):
    x2 = f_procuraRaizProx(a)
    x = x2**(1/2)
    raiz = (a+x2)/(2*x)
    return raiz

def main():
    a = int(input())
    while(a >= 0):
        raiz = f_calculaRaizNewton(a)
        print(f'N={a:.4f} RAIZ={raiz:.6f}')
        a = int(input())
    return 0

if __name__ == "__main__":
    main()