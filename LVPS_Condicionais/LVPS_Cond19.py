def main():
    #declaração de variaveis
    qtd_atual = int(0)
    qtd_max = int(0)
    qtd_min = int(0)
    qtd_media = int(0)
    
    #rcebimento de variaveis
    qtd_atual = int(input())
    qtd_max = int(input())
    qtd_min = int(input())
    
    #procesamento
    qtd_media = (qtd_max + qtd_min)/2
    
    if qtd_atual >= qtd_media:
        print('NÃO EFETUAR COMPRA')
    else:
        print('EFETUAR COMPRA')
    
    
    
if __name__ == '__main__':
    main()