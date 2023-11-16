def main():
    #declaração de variaveis
    horas_totais = float(0.0)
    horas_semanais = float(0.0)
    salario_hora = float(0.0)
    salario_total = float(0.0)
    correcao = float(0.0)
    total = float(0.0)
    
    #recebimento de variaveis
    horas_totais = float(input())
    salario_hora = float(input())
    
    #processamento
    horas_semanais = horas_totais / 4
    if horas_semanais >40:
        salario_total = horas_totais * salario_hora
        correcao = salario_total * 0.1
        total = salario_total + correcao
        print(f'{total:.1f}')
    else:
        salario_total = horas_totais * salario_hora
        print(f'{salario_total:.1f}')
    
if __name__ == '__main__':
    main()