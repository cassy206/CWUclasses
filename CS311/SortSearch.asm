;Cassandra Mendoza
;41726991
;I swear that all code submitted is my own work and I have not gotten or given help to anyone except from TAs


 segment .data
array     dd  12, 14,7, 45, 21, 15, 57, 36, 3, 79    ;numbers in array
size      dd  10                                       ;size of array
value     dd  21                                       ;number to look
location  dd  0                                       ;give location in array for value

segment .text
global main
main:

mov rax, 0                                             ;counter for sorting
mov rcx, 0                                             ;0=false 1=true

compare:

movsx   rbx, word[array + rax*4]                       ;grab the number in rax
movsx   rdx, word[array + rax*4 + 4]                   ;grab the next number to previous number 
cmp     rbx, rdx                                       ;compare the two numbers
jbe     dontswap                                       ;if number in rbx is smaller than rdx, dont need to swap 
                                                       ;if bigger than rdx continue thru code
mov     [array + rax*4], dx                            ;swap the two numbers
mov     [array + rax*4 + 4], bx
mov     rcx, 1                                         ;make rcx true


dontswap:

add     rax, 1                                         ;increase rax by 1
mov     bx, word[size]
dec     rbx
cmp     rax,rbx                                        ;compare rax to size 

jne     compare                                         ;if not the same return to compare

cmp     rcx,0                                           ; check if rcx is true or false
je      endLoop                                         ;if false, end the loop
jmp     main                                            ;if true return to main code


endLoop:
xor     rax, rax                                        ;clear out the registers
xor     rbx, rbx
xor     rcx, rcx
xor     rdx, rdx
 
mov     rcx, 0                                          ;lower and upper for binary search
mov     rbx, 9
push    rax                                             ;stores register on top of stack
 
search:

mov     rax, rbx                                        ;mov rbx into rax
sub     rax, rcx                                        ;subtract rcx from rax
shr     rax, 1                                          ;shift rax right by 1
add     rax, rcx                                        ;add rcx back to rax
movsx   rdx, word[array + rax*4]                        ;move the number 

cmp     [value], rdx                                    ;compare number to middle index number

jb      below                                           ;if below, jump to below section
ja      above                                           ;if above, jump to above section


mov     [location], rax                                 ;if not above or below, we found index, set return
jmp     endsearch                                       ;jump to end

below: 

mov     rbx, rax                                        ;move the middle to the upper
dec     rbx                                             ;decrease upper index by 1
jmp     search                                          ;jump back to search

above:

mov     rcx, rax                                        ;move the middle to lower
inc     rcx                                             ;increase upper index by 1
jmp     search                                          ;jump back to search


endsearch:

pop     rax                                             ;returns item at top and removes it from stack
add      word [location], 1                             ; add 1 to location as array technically starts from 0 but we are starting from 1

xor     rax, rax                                        ;zero out registers 
xor     rbx, rbx
xor     rcx, rcx
xor     rdx, rdx
ret



