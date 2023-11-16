def main():
  #declaração de variavel
  sexo = str("")

  #recebimento de variavel
  sexo = input().upper()
  while (sexo != "M" and sexo != "F") :
      print("SEXO INVÁLIDO, DIGITE F OU M")

      sexo = input().upper()
  if sexo == "M" or sexo == "F":
      print("SEXO VÁLIDO")


if __name__ == "__main__":
  main()