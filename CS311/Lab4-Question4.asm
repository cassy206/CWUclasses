; Cassandra Mendoza
; 41726991
; I pledge that this submission is solely my work, and that I have neither given, nor received help from anyone

segment .date
a       dq  -326
b       dq  7
quot    dq  0
rem     dq  0

segment .text
global main
main: 

mov     rax, [a]    ;moves a into rax
neg     rax         ;turns negative into positive number
mov     rbx, [b]    ;moves b into rbx
xor     rdx,rdx     ;zeros out rdx
idiv    rbx         ;divides rax by rbx
neg     rax         ; turns rax back into negative number
neg     rdx         ; times rdx by negative turning result negative as well
mov     [quot], rax ; whole number result 
mov     [rem],  rdx ; remainder of division

xor rax, rax
xor rbx, rbx, 
xor rdx, rdx 
ret
