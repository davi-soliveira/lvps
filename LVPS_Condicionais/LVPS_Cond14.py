def main():
    # declaração de variavel
    #G-GASOLINA A-ALCOOL
    litro = int(0)
    tipo = str("")
    G = float(0.0)
    A = float(0.0)
    valor_desc = float(0.0)
    valor_pagar = float(0.0)
    
    #recebimento de variavel
    litro = int(input())
    tipo = input()
    #processamento
    G = litro*3.30
    A = litro * 2.90
    if tipo == 'G':
        if litro<=20:
            valor_desc  = G * 0.04
            valor_pagar = G - valor_desc
            print(f'{valor_pagar:.2f}')
        else:
            valor_desc = G * 0.06
            valor_pagar = G - valor_desc
            print(f'{valor_pagar:.2f}')
            
            
    else:
        if litro<= 20:
            valor_desc  = A * 0.03
            valor_pagar = A - valor_desc
            print(f'{valor_pagar:.2f}')
        else:
            valor_desc = A * 0.05
            valor_pagar = A - valor_desc
            print(f'{valor_pagar:.2f}')
            
            
    
    
if __name__ == "__main__":
    main()