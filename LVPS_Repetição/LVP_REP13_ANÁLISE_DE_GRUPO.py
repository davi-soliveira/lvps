
def main():
#declaração de variáveis
    sexo = str("")
    altura = float(0.0)
    maior = float(0.0)
    menor = float(0.0)
    med_alt_f = float(0.0)
    soma_alt_f = float(0.0)
    cont_m = int(0)
    i = int(0) #variável de controle
    
    #inicilizar variáveis acumuladoras/contadoras
    i = 0
    cont_f = 0
    cont_m = 0
    soma_alt_f = 0
    
    #entrada de dados
    while(i < 5):
        sexo = input()#faz o recebimento do sexo
        altura = float(input())#faz o recebimento da altura
        #coletar a menor e a maior altura do grupo
        if (i == 0): #quando a variavel contadora for igual a 0 os primeiros vaores de altura e sexo serão os maiores e os menores valores
            maior = altura
            menor = altura
        elif (altura > maior):#faz a checagem para saber se a nova altura e maior que a altura anterior
            maior = altura    # altura sendo a maior ela substitui a outra na variavel maior
        elif (altura < menor):#faz a checagem da altura sendo a menor do que a variavel anterior ela substitui no menor
            menor = altura
        if (sexo.upper() == "F"):#sexo sendo igual a F ele entra no if
            soma_alt_f += altura # faz a soma da altura
            cont_f += 1 # faz a contagem de mulheres 
        else:
            cont_m += 1 #faz a contagem do sexo masculino
        i += 1 #varivael contadora
        med_alt_f = soma_alt_f/cont_f #media da altura feminina
    print(maior)
    print(menor)
    print(med_alt_f)
    print(cont_m)
    return 0
if __name__ == "__main__":
    main()
