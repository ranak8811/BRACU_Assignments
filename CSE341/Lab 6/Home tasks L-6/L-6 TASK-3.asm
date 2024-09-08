.MODEL SMALL
.STACK 100H

.DATA
newline DB 0AH, 0DH, '$'
msg_unique DB "All digits are unique.$"
msg_not_unique DB "Digits are not unique.$"
digits DB 5 DUP(?)

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    MOV ES, AX

    XOR AX, AX
    MOV CX, 5
    MOV SI, 0

INPUT_LOOP:
    MOV AH, 1
    INT 21H
    CMP AL, 0DH
    JE DONE_INPUT
    SUB AL, '0'
    MOV digits[SI], AL
    INC SI
    LOOP INPUT_LOOP

DONE_INPUT:

    MOV SI, 0
CHECK_UNIQUE:
    MOV DI, SI
    INC DI
COMPARE_LOOP:
    CMP DI, CX
    JGE NEXT_DIGIT
    MOV AL, digits[SI]
    CMP AL, digits[DI]
    JE NOT_UNIQUE
    INC DI
    JMP COMPARE_LOOP

NEXT_DIGIT:
    INC SI
    CMP SI, CX
    JL CHECK_UNIQUE
    JMP UNIQUE

NOT_UNIQUE:
    LEA DX, msg_not_unique
    MOV AH, 9
    INT 21H
    JMP END_PROGRAM

UNIQUE:
    LEA DX, msg_unique
    MOV AH, 9
    INT 21H

END_PROGRAM:

    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN