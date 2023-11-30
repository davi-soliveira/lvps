"""
Faça um programa, em Python 3.x, que receba strings e informe, a partir de uma função, escreva uma nova STRING SEM as VOGAIS. 
Apresente a nova string. A condição de parada é quando for informada uma string vazia ("").

Dica: passe a entrada para maiúsculo
"""
def remove_vogais(texto):
    vogals = "AEIOU"
    resultado = ""
    for char in texto:
        if char.upper() not in vogals:
            resultado += char
    return resultado

def main():
    palavra = input("")
    while palavra != "":
    
        nova_palavra = remove_vogais(palavra.upper())
        print(nova_palavra)
        palavra = input("")
if __name__ == "__main__":
    main()