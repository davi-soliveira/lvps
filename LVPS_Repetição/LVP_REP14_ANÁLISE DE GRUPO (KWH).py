def main():
#declaração
    pkwh = float(0.0)
    cons = int(0) #variável de controle
    qkwh = float(0.0)
    tipo = str('')
    total = float(0.0)
    maior = float(0.0)
    menor = float(0.0)
    totalR = float(0.0)
    totalC = float(0.0)
    totalI = float(0.0)
    somakwh = float(0.0)
    cont_cons = int(0)
    media = float(0.0)
    
    #inicialização variaveis acumuladoras
    totalR = 0
    totalC = 0
    totalI = 0
    somakwh = 0
    cont_cons = 0 #conta quantidade de consumidores
    pkwh = float(input("Valor do kwh: "))
    cons = int(input("Digite o cod consum.:")) #inicialização da v. controle
    while (cons != 0): #condição de parada
        qkwh = float(input("Consumo: "))
        tipo = input("tipo: ")
        #letra a
        total = pkwh*qkwh
        print(f'{cons} {total}')
        #letras b e c
        if (cont_cons == 0): #verifica se é o primeiro consumidor
            maior = qkwh
            menor = qkwh
        elif (qkwh > maior):
            maior = qkwh
        elif (qkwh < menor):
            menor = qkwh
        #letra d
        if (tipo.upper() == "R"):
            totalR += qkwh
        elif (tipo.upper() == "C"):
            totalC += qkwh
        elif (tipo.upper() == "I"):
            totalI += qkwh
        #letra e
        somakwh += qkwh
        cont_cons += 1
        cons = int(input("Digite o cod consum.:")) #atualização da v. controle
    #finaliza a letra e)
    media = somakwh / cont_cons
    #saidas
    print(f'{maior}')
    print(f'{menor}')
    print(f'{totalR}')
    print(f'{totalC}')
    print(f'{totalI}')
    print(f'{media}')
    return 0
if __name__ == "__main__":
    main()
