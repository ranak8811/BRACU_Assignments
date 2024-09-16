.MODEL SMALL

FIND_FACTORIAL MACRO M1
    MOV AL, M1
    MOV BL, AL
    DEC BL

L:
    MUL BL
    DEC BL
    CMP BL, 1
    JG L

ENDM


.STACK 100H

.DATA
ANS DW ?

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV AH, 1
    INT 21H
    SUB AL, '0'

    FIND_FACTORIAL AL

    MOV ANS, AX

    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN

