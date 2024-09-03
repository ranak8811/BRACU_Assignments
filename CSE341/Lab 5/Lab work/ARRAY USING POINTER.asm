.MODEL SMALL
.STACK 100H

.DATA
A DB 1,2,3,4,5
B DB 5 DUP(?)
C DB "HELLO $"

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    ;MY CODE IS HERE
    ;POINTER / INDEX
    ; LEA WORKS AS POINTER
    
    LEA SI, A
    
    MOV CX, 6
    
    PRINT:
    MOV AH, 2    
    MOV DX, [SI]    ;PRINTING ARRAY UISNG POINTER
    ADD DX, 48   
    INT 21H
    
    INC SI
    LOOP PRINT
    
    
    MAIN ENDP
END MAIN