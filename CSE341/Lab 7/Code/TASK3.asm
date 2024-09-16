.MODEL SMALL

STRING_REVERSE MACRO STR
    LEA SI, STR
    LEA DI, STR

    MOV CX, 0
FIND_LENGTH:
    MOV AL, [DI]
    CMP AL, '$'
    JE LENGTH_FOUND
    INC CX
    INC DI
    JMP FIND_LENGTH

LENGTH_FOUND:
    DEC DI

    MOV BX, CX
    MOV AX, 2
    DIV AX
    MOV CX, BX

SWAP_LOOP:
    CMP SI, DI
    JGE END_SWAP

    MOV AL, [SI]
    MOV BL, [DI]
    MOV [SI], BL
    MOV [DI], AL

    INC SI
    DEC DI
    LOOP SWAP_LOOP

END_SWAP:
ENDM


.STACK 100H

.DATA
str DB 'AMR AKTA CASIO GHORI KINTE HOBE$', '$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, str
    MOV AH, 9
    INT 21H

    STRING_REVERSE str

    MOV AH, 2
    MOV DL, 0AH
    INT 21H
    MOV DL, 0DH
    INT 21H

    LEA DX, str
    MOV AH, 9
    INT 21H

    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN

