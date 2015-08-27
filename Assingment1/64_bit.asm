SYS_EXIT  equ 1
SYS_WRITE equ 4
STDIN     equ 0
STDOUT    equ 1


section .data
   msg db "The sum of the two numbers", 0xA,0xD 
   len equ $ - msg   

segment .bss
   answer resb 1

section	.text
   global _start    ;must be declared for using gcc
	
_start:             ;tell linker entry point
   mov	rax, '3'
   sub  rax, '0'
	
   mov 	rbx, '4'
   sub  rbx, '0'
   add 	rax, rbx
   add	rax, '0'
	
   mov 	[answer], rax
   mov	rcx, msg	
   mov	rdx, len
   mov	rbx, STDOUT
   mov	rax, SYS_WRITE
   int	0x80
	
   mov	rcx, answer
   mov	rdx, 1
   mov	rbx, STDOUT
   mov	rax, SYS_WRITE
   int	0x80
	
   mov	rax, SYS_EXIT
   int	0x80

