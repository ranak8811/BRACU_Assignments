.MODEL SMALL
.STACK 100H

.DATA
    pkey DB "Press any key...$"
    newline DB 0AH, 0DH, '$'

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    MOV ES, AX

    MOV AX, 123
    MOV BL, 100
    DIV BL
    
    MOV CH, AH
    MOV AH, 0
    PUSH AX
    
    MOV AL, CH
    MOV BL, 10
    DIV BL
    
    MOV DH, AH
    MOV AH, 0
    PUSH AX
    
    MOV AL, DH
    MOV AH, 0
    PUSH AX

    MOV CX, 3
    MOV AH, 2

BEGIN:
    POP DX
    ADD DL, 48
    INT 21H
    LOOP BEGIN

    LEA DX, newline
    MOV AH, 9
    INT 21H

EXIT:
    MOV AH, 4CH
    INT 21H


    MAIN ENDP
END MAIN
