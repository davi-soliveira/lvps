def main():
    #declaração de variavel
    salario_bruto = float(0)
    salario_liquido = float(0)
    ir = float(0)
    inss = float(0)
    sindicato = float(0)
    ganha_hora = float(0)
    horas_trabalhadas = float(0)
    descontos = float(0)

    #recebimento de variavel
    ganha_hora = float(input(""))
    horas_trabalhadas = float(input(""))
    #processamento
    salario_bruto = ganha_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08 
    sindicato = salario_bruto * 0.05
    descontos = ir + inss + sindicato
    salario_liquido = salario_bruto - descontos

    #saida de dados
    #print(f'\n+ Salário Bruto: R$ {salario_bruto:.2f} \n - IR(11%) : R$ {ir:.2f} \n - INSS(8%): R$ {inss:.2f} \n - Sindicato(5%): R$ {sindicato:.2f}\n = Salário Liquido: R$ {salario_liquido:.2f}')
    print(f'+ Salário Bruto : R$ {salario_bruto:.2f}')
    print(f'- IR (11%) : R$ {ir:.2f}')
    print(f'- INSS (8%) : R$ {inss:.2f}')
    print(f'- Sindicato ( 5%) : R$ {sindicato:.2f}')
    print(f'= Salário Líquido : R$ {salario_liquido:.2f}')

if __name__ == "__main__":
    main()