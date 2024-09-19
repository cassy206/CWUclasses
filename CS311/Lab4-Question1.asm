;Cassandra Mendoza
;41726991
;I pledge that the submission is solely my work, that I have neither given, nor received help from anyone

segment .data

x1   dq  4    ;x1 cordinate
y1   dq  1    ;y1 cordinate
x2   dq  7    ;x2 cordinate
y2   dq  2    ;y2 cordinate

segment .text
global main

main:
    mov rax,[x2]    ;move x2 into rax
    mov rbx,[y2]    ;move y2 into rbx
    sub rax,[x1]    ;subtract x1 from x2 
    sub rbx,[y1]    ;subtract y1 from y2
    imul rax,rax    ; square sum of rax
    imul rbx,rbx    ;square sum of rbx
    add rax,rbx     ; add both sums together
    
    xor rax, rax
    xor rbx, rbx 
    ret 
   
     
