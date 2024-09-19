; Cassandra Mendoza
; 41726991
; I pledge that this submission is solely my work, and that I have neither given, nor received help from anyone

segment .data
x1      dq  14
y1      dq  27
x2      dq  96
y2      dq  19
diffx   dq  0
diffy   dq  0

segment .text
global main
main:

mov rbx, 1          ;store value of 1 in rbx
mov rcx, 0          ;store value of 0 in rcx
mov rdx, [x2]       ;move x2 into rdx 
sub rdx, [x1]       ;subtract x1 from rdx
mov [diffx],rdx     ;move differnce of x2-x1 into diffx
cmovle rax, rbx    ;move value of rax to what value of rbx if rdx is zero or negative
cmovg rax,rcx      ;move value of rax to value of rcx if rdx is positive
xor rax,rax         ;zero out rax
mov rdx, [y2]       ;move x2 into rdx 
sub rdx, [y1]       ;subtract x1 from rdx
mov [diffy],rdx     ;move difference of y2-y1 into diffy
cmovle rax, rbx    ;move value of rax to what value of rbx if rdx id zero or negative
cmovg rax,rcx      ;move value of rax to value of rcx if rdx is positive
xor rax, rax
xor rbx, rbx
xor rcx, rcx
xor rdx, rdx
ret
