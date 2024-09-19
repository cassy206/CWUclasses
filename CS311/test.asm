    segment .data
A   dw  -132, 34
B   db  26, -18    
R   dq  0
    
    segment .text
    global main
    
 main:
 ; add first array sequence
    xor    RAX, RAX
    xor    RBX, RBX
    movsx  RAX, word[A] 
    movsx  RBX, byte[B] 
    sub    RBX, RAX
    lea    RAX, [R]
    add    [RAX], RBX
 ; add second array sequence
    movsx  RAX, word[A+2] 
    movsx  RBX, byte[B+1] 
    sub    RBX, RAX
    lea    RAX, [R]
    add    [RAX], RBX
 ; zero out registers
    xor    RAX, RAX
    xor    RBX, RBX
 ret
