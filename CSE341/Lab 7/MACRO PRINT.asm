.MODEL SMALL

PRINT MACRO M1
    MOV DX, M1
    MOV AH, 2
    INT 21H
    
    ENDM

.STACK 100H
.DATA

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AX, 3 
    ADD AX, 48
    PRINT AX
    
    
    MAIN ENDP
END MAIN