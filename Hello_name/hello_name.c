#include<stdio.h>

int main(void)
{
  char nome[61];
  
  printf("Digite seu nome: ");
  scanf("%s",nome);
  
  printf("Olá, %s", nome);
  
  return 0;
}