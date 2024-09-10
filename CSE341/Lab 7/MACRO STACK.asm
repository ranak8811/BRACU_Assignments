.MODEL SMALL

PUSHTOSTACK MACRO M1, M2, M3
    PUSH M1
    PUSH M2
    PUSH M3
    
ENDM 

POPFROMSTACK MACRO M1, M2, M3
    POP M1
    POP M2
    POP M3
    
ENDM

.STACK 100H
.DATA

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AX, 3
    MOV BX, 4
    MOV CX, 5
    PUSHTOSTACK AX, BX, CX
    
    MOV AX, 0
    MOV BX, 0
    MOV CX, 0
    POPFROMSTACK CX, BX, AX
    
    
    MAIN ENDP
END MAIN