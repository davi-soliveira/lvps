from f import f_verificaLetra
def main():
    texto = input().upper()
    letra = input().upper()
    while (f_verificaLetra(letra,texto) == True):
        print("LETRA EXISTENTE, DIGITE OUTRA")
        letra = input().upper()
    print("LETRA INEXISTENTE")
    texto = texto + letra
    print(texto)

    return 0

if __name__ == "__main__":
    main()
