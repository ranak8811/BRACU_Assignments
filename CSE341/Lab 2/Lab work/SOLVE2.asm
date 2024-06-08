
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

; add your code here
         
.DATA

      ;(30+15)*(575-225)+210 have to implement


.CODE

MAIN PROC
    
    
    MOV AX, 30
    MOV BX, 15
    ADD AX, BX
    
    MOV BX, 575
    MOV CX, 225
    MOV DX, 210
    SUB BX, CX
    
    MUL BX
    ADD AX, DX
    
    
    
    

ret