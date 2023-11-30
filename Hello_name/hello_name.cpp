#include <iostream>
#include <string>

int main() {
    std::string nome;

    // Solicite ao usuário que insira seu nome
    std::cout << "Digite seu nome: ";
    std::cin >> nome;

    // Imprima a saudação com o nome
    std::cout << "Olá, " << nome << "!" << std::endl;

    return 0;
}
