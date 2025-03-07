#include <unistd.h> // Para a função write

int main() {

    char msg[] = "Hello\n";             // msg db `Hello\n`
    int len_msg = sizeof(msg) - 1;      // len_msg equ $ - msg

    char msg2[] = "Outro Print\n";      // msg2 db `Outro Print\n`
    int len_msg2 = sizeof(msg2) - 1;    // len_msg2 equ $ - msg2

    // mov rax, 1 -> syscall number: 1 (sys_write)
    // mov rdi, 1 -> file descriptor 1 (stdout)
    // mov rsi, msg -> string para print 
    // mov rdx, len_msg -> tamanho da string
    // syscall 
    write(1, msg, len_msg);

    int rax = 10;      // mov rax, 10
    int rcx = 0;       // xor rcx, rcx

    // label1:
    // cmp rax, rcx
    // je sair_label1
    while (rax != rcx) {
        rcx++;          // inc rcx
        // jmp label1
    }
    // sair_label1:

    int rbx = 2;     // mov rbx, 2
    // cmp rbx, 1
    // jg label2 
    if (rbx > 1) {
        // label2:
        // mov rax, 1 -> syscall number: 1 (sys_write)
        // mov rdi, 1 -> file descriptor 1 (stdout)
        // mov rsi, msg2 -> string para print
        // mov rdx, len_msg2 -> tamanho da string
        // syscall
        write(1, msg2, len_msg2);
    }

    // exit:
    // mov rax, 60 -> syscall number: 60 (sys_exit)
    // xor rdi, rdi 
    // syscall
    _exit(0);

    return 0;
}