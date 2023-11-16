def main():
    #declaração
    sexo = ("")
    peso_ideal = float(0.0)
    altura = float(0.0)
    #recebimento de variaveis
    sexo = input()
    altura = float(input())
    
    #processamento
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f'{peso_ideal:.3f}')
    else:
        peso_ideal = (62.1 * altura) - 44.7
        print(f'{peso_ideal:.3f}')
    
    
    
    
if __name__ == '__main__':
    main()