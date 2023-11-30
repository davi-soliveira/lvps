def main():
    #declaração de variavel
    numero = int(0)
    soma = int(0)
    media = int(0)
    s_negativo = int(0)
    flag = str('')
    #contador de numero negativo
    cont = int(0)
    #recebimetno de continuarção ou parada
    flag = input('você deseja digitar um numero <S/N>: ').upper()
    while flag == 'S':#estrutura de repetição
        numero = int(input())#recebimento de varivaeis
        if numero < 0:# se o numero for enor que 0 entra na condição
            s_negativo = s_negativo + numero #faz o armazenamento
            cont = cont + 1#faz a contagem das vezes em que entrou nessa condição
            media = s_negativo/cont # faz a media dos numeros negativos
        else:# se o numero for positivo ele entra no else
            soma = soma+numero
        flag = input('você deseja digitar um numero <S/N>: ').upper()#recebimetno de continuarção ou parada
    print(f'{soma} {media}')#saida de variaveis
    
    return 0
    
if __name__ == "__main__":
    main()
