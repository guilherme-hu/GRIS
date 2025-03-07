section .data
    num dq 397401               ; Número a ser verificado 
    par db "par", 0xA           ; String "par" com newline
    len_par equ $ - par         ; Tamanho da string "par"
    impar db "impar", 0xA       ; String "impar" com newline
    len_impar equ $ - impar     ; Tamanho da string "impar"
    
section .text
    global _start
    
_start:
    mov rax, [num]          ; Carrega o número em RAX
    and rax, 1              ; Faz AND bit a bit com 1 para verificar o bit menos significativo
    jz eh_par               ; Se for zero, o número é par
    
    ; Caso seja ímpar
    mov rsi, impar          ; Carrega o endereço da string "impar" em RSI
    mov rdx, 6              ; Comprimento da string "impar" + newline
    jmp print
    
    ; Caso seja par
eh_par:
    mov rsi, par            ; Carrega o endereço da string "par" em RSI
    mov rdx, 4              ; Comprimento da string "par" + newline

    ; Imprime a string
print:
    mov rax, 1              ; syscall write
    mov rdi, 1              ; stdout
    syscall
    
    ; Finaliza o programa
    mov rax, 60             ; syscall exit
    xor rdi, rdi            ; Código de saída 0
    syscall