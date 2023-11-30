section .data
    prompt db 'Digite seu nome: ', 0
    mensagem db 'Olá, ', 0

section .bss
    nome resb 255

section .text
    global _start

_start:
    ; Escreva a mensagem de solicitação
    mov eax, 4
    mov ebx, 1
    mov ecx, prompt
    mov edx, 17
    int 0x80

    ; Leia o nome do usuário
    mov eax, 3
    mov ebx, 0
    mov ecx, nome
    mov edx, 255
    int 0x80

    ; Escreva a mensagem de saída com o nome do usuário
    mov eax, 4
    mov ebx, 1
    mov ecx, mensagem
    int 0x80


    ; Saia do programa
    mov eax, 1
    int 0x80
