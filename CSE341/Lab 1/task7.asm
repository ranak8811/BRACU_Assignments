.MODEL SMALL

.STACK 100H

.DATA

A DW 5
B DW 6
C DW 3
               ;
.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
               
   
    MOV AX, A             ;X * Y / Z
    MOV BX, B
    MOV CX, C
    
    MUL BX      
    DIV CX
    
    MOV AH, 4CH
    INT 21H     
    
    MAIN ENDP 

END MAIN
