def main():
    #declaração de variaveis
    peso_ideal = float(0.0)
    altura = float(0.0)
    peso = float(0.0)
    sexo = ('')
    IMC = float(0.0)
    
    #recebimento de variaveis
    sexo = input()
    peso = float(input())
    altura = float(input())
    #processamento e saida de dados
    if sexo == 'M':
        peso_ideal = (72.7 * altura)-58
        IMC = peso/(altura**2)
        if IMC <17:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('MUITO ABAIXO DO PESO')
        elif IMC >=17 and IMC <=18.49:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('ABAIXO DO PESO')
        elif IMC >=18.50 and IMC <= 24.99:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('PESO NORMAL')
        elif IMC >=25 and IMC <= 29.99:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('ACIMA DO PESO')
        elif IMC >=30 and IMC <= 34.99:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('OBESIDADE I')
        else:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('OBESIDADE II (SEVERA)')
    else:# sexo == 'F':       
        peso_ideal = (62.1 * altura)-44.7
        IMC = peso/(altura**2)
        if IMC <17:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('MUITO ABAIXO DO PESO')
        elif IMC >=17 and IMC <=18.49:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('ABAIXO DO PESO')
        elif IMC >=18.50 and IMC <= 24.99:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('PESO NORMAL')
        elif IMC >=25 and IMC <= 29.99:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('ACIMA DO PESO')
        elif IMC >=30 and IMC <= 34.99:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('OBESIDADE I')
        else:
            print(f'PESO IDEAL: {peso_ideal:.2f}')
            print(f'IMC: {IMC:.2f}')
            print('OBESIDADE II (SEVERA)')
if __name__ == '__main__':
    main()