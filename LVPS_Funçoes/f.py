#f.py
def f_dec2bin(n):
    #declaração de variáveis
    b = str("")
    #inicialização da variavel acumuladora
    b = ""
    while(n > 0):
        resto = n % 2
        b = str(resto) + b
        n = n // 2
    return b

def f_dec2hex(n):
    #declaração de variáveis
    h = str("")
    #inicialização da variavel acumuladora
    h = ""
    while(n > 0):
        resto = n % 16
        if (resto < 10):
            h = str(resto) + h
        else:
            h = f_letrahex2(resto) + h
        n = n // 16
    return h
#solução elegante
def f_letrahex2(x):
    hex = 'ABCDEF'
    return hex[x-10]