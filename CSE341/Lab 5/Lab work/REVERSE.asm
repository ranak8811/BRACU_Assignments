.MODEL SMALL

.STACK 100H

.DATA

NAME1 DB "NOWSHIN"

.CODE

MAIN PROC
    
    MOV AX, @DATA
    MOV DS, AX
    
    MOV SI, 0
    MOV CX, 7
    
    PUSH_LOOP:
    
    
    
    
    
    MAIN ENDP
END MAIN