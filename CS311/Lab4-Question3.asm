; Cassandra Mendoza
; 41726991
; I pledge that this submission is solely my work, and that I have neither given, nor received help from anyone

segment .data

g1       dq  41     ;grade 1
g2       dq  72     ;grade 2
g3       dq  69     ;grade 3
g4       dq  91     ;grade 4
quot     dq  0
rem      dq  0

segment .text
global main 
main: 

mov     rax, [g1]   ;move grade 1 into rax
add     rax, [g2]   ;add grade 2 to rax total
add     rax, [g3]   ;add grade 3 to rax total
add     rax, [g4]   ; add grade 4 to rax total
mov     rbx, 4      ; move sum into rbx
xor     rdx, rdx    ;zero out rdx
idiv    rbx         ; divide sum of rbx by 4 
mov     [quot], rax ; save the quotient 
mov     [rem], rdx  ; save the remainder
xor rax, rax
xor rbx, rbx
xor rdx, rdx 
ret
