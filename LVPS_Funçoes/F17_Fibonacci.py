"""
Faça um programa em linguagem Python que lê um número n digitado pelo usuário(esse número vai ser a quantidade de termos) e imprime os n primeiros números da sequência de Fibonacci
"""
def fibonacci(n):
    fib_sequence = [1, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]

def main():

    n = int(input(""))

    result = fibonacci(n)
    for termo in result:
        print(termo)
if __name__ == "__main__":
    main()