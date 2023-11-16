def main():
    #declaração de variaveis
    total = int(0)
    brancos = int(0)
    nulos = int(0)
    validos = int(0)
    
    #recebimentos de dados
    total = int(input("quantidade de eleitores: "))
    branco = int(input("quantidade de votos em branco: "))
    nulo = int(input("quantidade de votos nulos: "))
    validos = int(input("quantidade de votos validos: "))
    
    #processamento de dados
    
    resultado1 = (branco * 100) / total
    resultado2 = (nulo * 100) / total
    valido     = (validos * 100) / total
    
    print(f"brancos = {resultado1}% \n nulos = {resultado2}% \n validos = {valido}% ")
    
    
if __name__ == "__main__":
    main()