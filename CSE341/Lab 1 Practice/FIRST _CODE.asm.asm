
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

; add your code here   

.DATA 

A DW 10
B DW 20
C DW 0

.CODE 

MAIN PROC
    
    MOV AX, [A]
    MOV BX, [B]
    
    SUB BX, AX
    MOV [A], BX





