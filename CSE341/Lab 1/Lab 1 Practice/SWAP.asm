ORG 100H

.DATA

A DW 50 
B DW 60


.CODE

MAIN PROC
    MOV AX, [A] 
    MOV BX, [B]
    
    
    ADD AX, BX
    SUB BX, AX
    ADD AX, BX
    NEG BX