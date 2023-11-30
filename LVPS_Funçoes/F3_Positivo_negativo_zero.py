"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento  negativo ou 'Z' se for zero./
"""
# Função que identifica se o numero e positivo,negativo ou igual a 0
def f_ident(num):
    # Indetifica se o numero e positivo
    if num > 0:
        resultado = "P"
    #indentifica se o numero e negativo
    elif num < 0:
        resultado = "N"
    #indentifica se o numero e igual a 0
    elif num == 0:
        resultado = "Z" 
    #retorna o resultado    
    return resultado
    
#função principal

def main():
    #declaração de variavfel
    num = int(0)
    resultado = str("")
    
    #recebimento de valores
    num = int(input())
    
    #invocação da função   
    resultado = f_ident(num)
        
    #saida de dados    
    print(resultado) 
    
if __name__ == "__main__":
    main()