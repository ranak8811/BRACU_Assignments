ORG 100H

.DATA

A DW 10 
B DW 20


.CODE

MAIN PROC
    MOV AX, [A] 
    MOV BX, [B]
    
    
    INC AX
    SUB BX, AX
    MOV [A], BX