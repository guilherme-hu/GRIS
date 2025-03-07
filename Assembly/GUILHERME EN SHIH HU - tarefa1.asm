bits 64

section .data
    msg db `Hello\n`
    len_msg equ $ - msg       
    msg2 db `Outro Print\n`
    len_msg2 equ $ - msg2    

section .text
    global _start

_start:

    mov rax, 1              
    mov rdi, 1              
    mov rsi, msg            
    mov rdx, len_msg        
    syscall

    mov rax, 10
    xor rcx, rcx
    label1:
        cmp rax, rcx
        je sair_label1

        inc rcx
        jmp label1
sair_label1:        
    
    mov rbx, 2
    cmp rbx, 1
    jg label2

exit:
    mov rax, 60             
    xor rdi, rdi            
    syscall


label2:
    mov rax, 1              
    mov rdi, 1              
    mov rsi, msg2            
    mov rdx, len_msg2        
    syscall
    jmp exit 
