;Cassandra Mendoza
;41726991
;I swear all work turned in has been done with no aid from anyone except TAs


segment .data
t       dw  0x65A9
day     dw  0
month   db  0   
year    dw  1980

segment .text
global main 
main:

xor EDX,EDX     ;zero out EDX
mov DX,[t]      ;move my data into DX
shr DX, 11       ;shift to the right 11
add [day], DX  ;add the value to year
xor DX,DX

xor EBX, EBX
mov BX, [t]     ;change DX to original value of t
shl BX, 5      ;shift to the right
shr BX, 12 
add [month],BX  ;move new month value into DX
xor BX,BX

mov DX, [t]     ;change DX to original value of t
shl DX, 9      ;shift to the left 
shr DX, 9      ;shift to the right 
add [year],DX    ;move new day value into DX
xor DX,DX

xor EDX,EDX     ;zero out EDX
xor EBX, EBX 
ret 


