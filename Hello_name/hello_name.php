<?php
// Função para ler uma linha do console
function input() {
    return trim(fgets(STDIN));
}

echo "Digite seu nome: ";
$nome = input();

echo "Olá, " . $nome . "\n";
?>
