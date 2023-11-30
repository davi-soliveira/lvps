"""
Faça um programa, em Python 3.x, que receba uma letra minúscula. 
Para esse programa, crie uma função, baseado na Tabela ASCII, converta letras minúsculas em maiúsculas 
(NÃO É PERMITIDO O USO DO MÉTODO .upper())

Dica: pesquisem sobre as funções ord() e chr(
"""
def f_maiusculo(t):
    nova = ""
    for i in range(len(t)):
        if (ord(t[i]) > 96):
            letra = chr(ord(t[i])-32)
            nova += letra
        else:
            nova += t[i]
    return nova

def main():
    t = input()
    
    print(f_maiusculo(t))

    return 0

if __name__ == "__main__":
    main()