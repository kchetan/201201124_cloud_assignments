SYS_EXIT  equ 1
SYS_WRITE equ 4
STDIN     equ 0
STDOUT    equ 1


section .data
   msg db "The sum of numbers 3 + 4 =", 0xA,0xD 
   len equ $ - msg   
   
segment .bss
   answer resb 1

section	.text
   global _start
	
_start:
   mov	eax, '3'
   sub  eax, '0'
	
   mov 	ebx, '4'
   sub  ebx, '0'
   add 	eax, ebx
   add	eax, '0'
	
   mov 	[answer], eax
   mov	ecx, msg	
   mov	edx, len
   mov	ebx, STDOUT
   mov	eax, SYS_WRITE
   int	0x80
	
   mov	ecx, answer
   mov	edx, 1
   mov	ebx, STDOUT
   mov	eax, SYS_WRITE
   int	0x80

exit:

   mov	eax, SYS_EXIT
   int	0x80

