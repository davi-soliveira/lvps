def main():
    #declaração de variavel
    a = float(0.0)
    b = float(0.0)
    c = float(0.0)
    
    x1 = float(0.0)
    x2 = float(0.0)
    
    #recebimento de variavel
    a = float(input())
    b = float(input())
    c = float(input())
    
    #preocessamento   
    d = (b)**2-(4*a*c)
    if d>=0:
        x1 = (-(b)+(d**(1/2)))/(2*a)
        x2 = (-(b)-(d**(1/2)))/(2*a)
        print(f'{x1} {x2}')
    else:
        print('Não possui raiz')
        
    
    
    
if __name__ == "__main__":
    main()