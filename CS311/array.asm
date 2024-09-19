;Cassandra Mendoza
;41726991
;I hereby declare that all work is solely my work, and that I have neither given, nor received help from anyone

    segment .data
a       dw       -278,124,-172      ;array of 3 values
b       db      38,-120,-92         ;array of 3 values
sum     dq      0 
result   dq      0                   ;memory for result

    segment .text
    global main
main:
     movsx    rax, byte [b] ;move b into rax
     sub    rax, 10         ;subtract 10
     movsx  rbx, word [a]   ;move a into rbx
     add    rbx,rax         ;add rax to rbx
     add    [sum], rbx      ;solution 
     movsx  rcx,byte [b] ;move b into rcx
     add    rcx, 32         ;add 32 to rcx
     movsx  rdx, word [a]   ; move a into rdx
     sub    rcx,rdx         ;subtract rdx from rcx
     add    [sum], rcx  
     
     movsx    rax, byte [b+1] ;move b into rax
     sub    rax, 10         ;subtract 10
     movsx  rbx, word [a+2]   ;move a into rbx
     add    rbx,rax         ;add rax to rbx
     add    [sum], rbx      ;solution 
     movsx  rcx,byte [b+1] ;move b into rcx
     add    rcx, 32         ;add 32 to rcx
     movsx  rdx, word [a+2]   ; move a into rdx
     sub    rcx,rdx         ;subtract rdx from rcx
     add    [sum], rcx  
     
     movsx    rax, byte [b+2] ;move b into rax
     sub    rax, 10         ;subtract 10
     movsx  rbx, word [a+4]   ;move a into rbx
     add    rbx,rax         ;add rax to rbx
     add    [sum], rbx      ;solution 
     movsx  rcx,byte [b+2] ;move b into rcx
     add    rcx, 32         ;add 32 to rcx
     movsx  rdx, word [a+4]   ; move a into rdx
     sub    rcx,rdx         ;subtract rdx from rcx
     add    [sum], rcx  
     
     xor    rax,rax
     xor    rbx, rbx
     xor    rcx, rcx
     xor    rdx, rdx  

     ret   
