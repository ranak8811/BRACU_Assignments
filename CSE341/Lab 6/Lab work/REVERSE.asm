.MODEL SMALL
.STACK 100H

.DATA
NAME1 DB "NOWSHIN"

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV SI, OFFSET NAME1
    MOV CX, 7          ; Length of the string

    ; Push characters onto the stack
    PUSH_LOOP:
    MOV AL, [SI]
    PUSH AX
    INC SI
    LOOP PUSH_LOOP

    ; Pop characters and display them in reverse order
    POP_LOOP:
    POP AX
    MOV DL, AL         ; Move the character to DL for printing
    MOV AH, 2          ; Function to display character
    INT 21H
    LOOP POP_LOOP

    MOV AH, 4CH        ; Exit to DOS
    INT 21H

MAIN ENDP
END MAIN
