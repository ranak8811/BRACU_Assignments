.MODEL SMALL

FIND_FACTORIAL MACRO M1
    MOV AX, M1
    MOV CX, AX
    DEC CX

L:
    MUL CX
    DEC CX
    CMP CX, 1
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
    XOR AH, AH

    FIND_FACTORIAL AX

    MOV ANS, AX

    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN

