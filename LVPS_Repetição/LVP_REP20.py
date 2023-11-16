def main():
    #declaração de variáveis
    n = int(0)
    turmas = int(0)
    turma = str("")
    qte = int(0)
    alunos = int(0)
    matricula = str("")
    freq = str("")
    conta_ausencia = int(0)
    perc_ausencia = float(0.0)
    maior_20 = int(0)
    turma_menor = str("")
    turma_maior = str("")


    n = int(input())
    for turmas in range(0,n,1):
        #obtendo nome da turma e quantidade de alunos da turma
        turma = input()
        qte = int(input())
        conta_ausencia = 0
    #obtendo dados de aus/pres dos alunos da turma
        for alunos in range(0,qte,1):
            matricula = input()
            freq = input()
    #contando a quantidade de ausentes da turma
            if (freq.upper() == "A"):
                conta_ausencia += 1
    #calculando o percentual de ausencia da turma
        perc_ausencia = conta_ausencia*100/qte
    #apresentando o nome da turma e seu percentual de ausência
        print(f'TURMA={turma} AUSENCIA= {perc_ausencia:.2f} %')
    #verificando qual turma teve o maior e o menor percentual de ausência
        if (turmas == 0):
            maior_perc = perc_ausencia
            menor_perc = perc_ausencia
        elif (perc_ausencia > maior_perc):
            maior_perc = perc_ausencia
            turma_maior = turma
        elif (perc_ausencia < menor_perc):
            menor_perc = perc_ausencia
            turma_menor = turma
    #verificando quantas turmas tiveram percentual de ausência maior que 20%
        if (perc_ausencia > 20):
            maior_20 += 1
    #saida de dados final
    print(f'TURMA COM MAIOR % DE AUSENCIA= {turma_maior} AUSENCIA= {maior_perc:.2f}%')
    print(f'TURMA COM MENOR % DE AUSENCIA= {turma_menor} AUSENCIA= {menor_perc:.2f}%')
    print(f'{maior_20} TURMAS COM % DE AUSENCIA SUPERIOR A 20%')

    return 0

if __name__ == "__main__":
    main()
    
    