
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

; add your code here
         
.DATA
A DW 234AH
B DW 123BH                ; D = A + B - C
                          ; A, B, C 16 bit number
C DW 34AAH
D DW 0H

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AX, A
    MOV BX, B
    MOV CX, C
    
    MOV DX, AX
    
    ADD AX, BX
    SUB AX, CX
    
    ADD AX, DX
    SUB DX, AX
    ADD AX,DX
    NEG DX
    
    MOV [D], DX
    
    

ret




