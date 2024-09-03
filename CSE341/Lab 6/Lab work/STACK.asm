.MODEL SMALL

.STACK 100H

.DATA

NAME1 DB "NOWSHIN"

.CODE

MAIN PROC
    
    MOV AX, @DATA
    MOV DS, AX
    
    PUSH 1234H
    
    MOV AX, 6789H
    PUSH AX
    
    POP BX
    
    