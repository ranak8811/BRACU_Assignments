.MODEL SMALL
.STACK 100H

.DATA
A DB 'ABIR$', 0

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV CX, 4
    MOV SI, 0

    PUSH_LOOP:
        MOV DL, A[SI]
        PUSH DX
        INC SI
        LOOP PUSH_LOOP

    MOV CX, 4

    POP_LOOP:
        POP DX
        MOV AH, 2
        MOV DL, DL
        INT 21H
        LOOP POP_LOOP

    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN
