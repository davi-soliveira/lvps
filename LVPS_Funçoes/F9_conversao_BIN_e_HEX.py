"""
Faça um programa que recebe n números inteiros maiores ou iguais a zero. Considere que a entrada de encerra quando um número menor que zero for informado pelo usuário.

- Faça uma função externa que receba um número inteiro maior ou igual a zero na base 10 e retorne um número inteiro maior ou igual a zero que representa, na base 2 (binário), o número na base 10 fornecido como entrada para esta função.

- Faça uma função externa que receba um número inteiro maior ou igual a zero na base 10 e retorne um número inteiro maior ou igual a zero que representa, na base 16 (hexadecimal), o número na base 10 fornecido como  entrada para esta função.

- Para cada número LIDO imprima seu respectivo valor na base 2 e na base 16, conforme modelo abaixo. 

PODE USAR STRING
"""
import f

def main():
    n = int(input())
    while (n >= 0):
        bin = f.f_dec2bin(n)
        hex = f.f_dec2hex(n)
        print(f'DEC={n} BIN={bin} HEX={hex}')
        n = int(input())
    return 0

if __name__ == "__main__":
    main()




