#Faça um programa que apresente a frase "Olá, Mundo!", na linguagem do título.
section .data
    hello db 'Olá, Mundo!',0   

section .text
    global _start             

_start:
    
    mov eax, 4                
    mov ebx, 1                
    mov ecx, hello            
    mov edx, 13               
    int 0x80                  

   
    mov eax, 1       
    int 0x80         
