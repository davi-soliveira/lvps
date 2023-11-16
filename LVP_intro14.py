def main():
    #declaração de variaveis
    x1 = float(0.0)
    x2 = float(0.0)
    y1 = float(0.0)
    y2 = float(0.0)
    distancia = float(0)
    #recebimento de dados
    x1 = float(input())
    x2 = float(input())
    y1 = float(input())
    y2 = float(input())
    
    #processamento
    
    distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    #saida de dados
    print(distancia)
    
    return 0
    
    
    
    
    
if __name__ == "__main__":
    main()