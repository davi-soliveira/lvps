"""
Faça um programa que, dados os nove primeiros números e os dois dígitos verificadores, informe se o CPF é válido ou inválido.

A regra de negócio (validação)  deve ser feita em formato de função.

Algoritmo do CPF - O que está por trás do gerador de CPF

Para exemplificar o processo vamos gerar um CPF válido, calculando os dígitos verificadores de um número hipotético, 111.444.777-XX.

Calculando o Primeiro Dígito Verificador

O primeiro dígito verificador do CPF é calculado utilizando-se o seguinte algoritmo. 

1) Distribua os 9 primeiros dígitos em um quadro colocando os pesos 10, 9, 8, 7, 6, 5, 4, 3, 2 abaixo da esquerda para a direita, conforme representação abaixo:

1	1	1	4	4	4	7	7	7
10	9	8	7	6	5	4	3	2
2) Multiplique os valores de cada coluna:

1	1	1	4	4	4	7	7	7
10	9	8	7	6	5	4	3	2
10	9	8	28	24	20	28	21	14
3) Calcule o somatório dos resultados (10+9+...+21+14) = 162

4) O resultado obtido (162) será divido por 11. Considere como quociente apenas o valor inteiro, o resto da divisão será responsável pelo cálculo do primeiro dígito verificador.

Vamos acompanhar: 162 dividido por 11 obtemos 14 como quociente e 8 como resto da divisão. Caso o resto da divisão seja menor que 2, o nosso primeiro dígito verificador se torna 0 (zero), caso contrário subtrai-se o valor obtido de 11, que é nosso caso. Sendo assim nosso dígito verificador é 11-8, ou seja, 3 (três). Já temos portanto parte do CPF, confira: 111.444.777-3X.

Calculando o Segundo Dígito Verificador

1) Para o cálculo do segundo dígito será usado o primeiro dígito verificador já calculado. Montaremos uma tabela semelhante a anterior só que desta vez usaremos na segunda linha os valores 11,10,9,8,7,6,5,4,3,2 já que estamos incorporando mais um algarismo para esse cálculo. Veja:

1	1	1	4	4	4	7	7	7	3
11	10	9	8	7	6	5	4	3	2
2) Na próxima etapa faremos como na situação do cálculo do primeiro dígito verificador, multiplicaremos os valores de cada coluna e efetuaremos o somatório dos resultados obtidos: (11+10+...+21+6) = 204.

1	1	1	4	4	4	7	7	7	3
11	10	9	8	7	6	5	4	3	2
11	10	9	32	28	24	35	28	21	6
3) Realizamos novamente o cálculo do módulo 11. Dividimos o total do somatório por 11 e consideramos o resto da divisão.

Vamos acompanhar: 204 dividido por 11 obtemos 18 como quociente e 6 como resto da divisão.

4) Caso o valor do resto da divisão seja menor que 2, esse valor passa automaticamente a ser zero, caso contrário (como no nosso caso) é necessário subtrair o valor obtido de 11 para se obter o dígito verificador. Logo, 11-6= 5, que é o nosso segundo dígito verificador.

Neste caso chegamos ao final dos cálculos e descobrimos que os dígitos verificadores do nosso CPF hipotético são os números 3 e 5, portanto o CPF ficaria assim: 111.444.777-35.
"""
def f_limpaCPF(cpf):
    novo = str('')
    for i in range(len(cpf)):
        if (cpf[i] != '.'):
            novo += cpf[i]
    return novo

def f_dv(cpf,peso):
    total = 0
    for i in range(len(cpf)):
        total += int(cpf[i]) * peso
        peso -= 1
    resto = total % 11
    if (resto < 2):
        return '0'
    else:
        return str(11-resto)

def f_testaCPF(cpf):
    dv = cpf[12:]
    cpf = f_limpaCPF(cpf[:11])
    dv1 = f_dv(cpf,10)
    cpf = cpf + dv1
    dv2 = f_dv(cpf,11)
    testeDV = dv1+dv2
    if (dv == testeDV):
        return True
    else:
        return False

def main():
    #declaração de variáveis
    cpf = str('')
    #entrada de dados
    cpf = input()

    if (f_testaCPF(cpf)):
        print('CPF VÁLIDO')
    else:
        print('CPF INVÁLIDO')

    return 0

if __name__ == "__main__":
    main()