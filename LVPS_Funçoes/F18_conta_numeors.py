"""
Faça um programa que conte a incidência de um determinado número [0-9] dentro de um intervalo de valores, começando em 0 e o fim do intervalo determinado pelo usuário.
"""
def f_contaNumero(n,fim):
    contan = 0
    for i in range(fim+1):
        n = str(n)
        i = str(i)
        for j in range(len(i)):
            if (i[j] == n):
                contan += 1
    return contan

def main():
    n = int(input())
    fim = int(input())
    print(f_contaNumero(n,fim))
    return 0

if __name__ == "__main__":
    main()
