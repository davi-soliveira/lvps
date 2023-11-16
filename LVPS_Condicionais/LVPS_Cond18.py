def main():
    #declaração de variaveis
    salario_fixo = float(0.0)
    vendas = float(0.0)
    salario_comissao = float(0.0)
    #recebimento de variaveis
    salario_fixo = float(input())
    vendas = float(input())
    
    if vendas <= 1500:
        salario_comissao = salario_fixo + (vendas*0.03)
        print(f'{salario_comissao:.1f}')
    else:
        salario_comissao = salario_fixo + ((vendas/2) * 0.03 + (vendas/2)*0.05)
        print(f'{salario_comissao:.1f}')
    
    
if __name__ == '__main__':
    main()