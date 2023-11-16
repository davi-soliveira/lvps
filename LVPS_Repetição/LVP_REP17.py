def main():
    #declaração de variavel
    s = float(0.0)
    resultado = float(0.0)
    denominador = int(0)
    #recebimento de variavel
    resultado = 0
    denominador =1
    for numerador in range(1,100,2):
        resultado += numerador / denominador
        denominador += 1
    print(resultado)
    
    
    
if __name__ == "__main__":
    main()