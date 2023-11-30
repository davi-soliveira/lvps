def main():
    #declaração de variavel
    s = float(0.0)
    resultado = float(0.0)
    denominador = int(0)
    n1 = int(0)
    n2 = int(0)
    #definindo valores das variaveis
    resultado = 0
    n1 = 38
    n2 = 37
    # faz a fepetição ate 37 somando mais 1 a cada repetição
    for denominador in range(1,37,1):
        resultado += (n1 * n2) / denominador #pega o resultado e armazena 
        n1 -=1 #subtrai 1 a cada repetição
        n2 -=1 #subtrai 1 a cada repetição
    print(resultado)
    
    
    
if __name__ == "__main__":
    main()
