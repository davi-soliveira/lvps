import math
def main():
    #declaração de variaveis
    area = float(0.0)
    
    
    #recebimento de informaçoes
    area = float(input())
    
    #processamento
    litros = area/6
    latas = math.ceil(litros/18)
    galoes = math.ceil(litros/3.6)
    v_latas = latas*80
    v_galos = galoes*25
    #saida de dados
    print(f'Você utilizará {latas} de 18L. valor = {v_latas:.2f}')
    print(f'Você utilizará {galoes} de 3.6L. valor = {v_galos:.2f}')
    
    
    
    
if __name__ == "__main__":
    main()
    
    
