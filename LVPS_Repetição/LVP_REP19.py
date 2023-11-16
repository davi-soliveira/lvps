def main():
    #declaração de variavel
    s = float(0.0)
    resultado = float(0.0)
    denominador = int(0)
    #definindo valores das variaveis
    resultado = 0
    denominador = 0
    # faz a fepetição ate 37 somando mais 1 a cada repetição
    for numerador in range(1,10,1):
        resultado += numerador / denominador #pega o resultado e armazena 
        
    print(resultado)
    
    
    
if __name__ == "__main__":
    main()