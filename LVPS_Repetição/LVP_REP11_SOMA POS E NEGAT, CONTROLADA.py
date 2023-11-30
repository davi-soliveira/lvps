def main():
    #declaração de variavel
    numero = int(0)
    soma = int(0)
    media = int(0)
    s_negativo = int(0)
    flag = str('')#
    #variavel para continuar a repetição ou parar
    flag = input('deseja digitar um numero <s/n>').upper()
    while flag == 'S':#estrutura de repetição
        numero = int(input())#recebimento de varivaeis
        if numero < 0:# se o numero for enor que 0 entra na condição
            s_negativo = s_negativo + numero #faz o armazenamento
        else:# se o numero for positivo ele entra no else
            soma = soma+numero
        flag = input('deseja digitar um numero <s/n>').upper()#variavel para continuar a repetição ou parar
         
    print(f'{soma} {s_negativo}')#saida de variaveis
    
    return 0
    
if __name__ == "__main__":
    main()
