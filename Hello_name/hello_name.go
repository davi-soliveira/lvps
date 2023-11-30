package main

import (
	"fmt"
)

func main() {
	var nome string

	// Solicite ao usuário que insira seu nome
	fmt.Print("Digite seu nome: ")

	// processamento
	fmt.Scanln(&nome)

	// saida de dados
	fmt.Printf("Olá, %s!\n", nome)
}
