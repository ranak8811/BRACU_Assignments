
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

ORG 100h

; add your code herE

.DATA

X DW 5
Y DW 6
Z DW 5

.CODE

MAIN PROC
    MOV AX, [X]
    MOV BX, [Y]
    
    MUL BX
    XOR DX, DX
    DIV CX




