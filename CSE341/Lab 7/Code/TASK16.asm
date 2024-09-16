.MODEL SMALL
.STACK 100H
.DATA
x DW 3
n DW 6
result DW 1

newline DB 0AH, 0DH, '$'
msg_result DB 'Result: $'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AX, x
    MOV BX, n
    CALL POWER

    LEA DX, msg_result
    MOV AH, 9
    INT 21H
    
    MOV AX, result
    CALL PRINT_NUMBER

    LEA DX, newline
    MOV AH, 9
    INT 21H

    MOV AH, 4CH
    INT 21H

MAIN ENDP

POWER PROC
    MOV AX, 1
    MOV CX, BX

POWER_LOOP:
    CMP CX, 0
    JE DONE
    
    MOV BX, x
    MUL BX
    
    DEC CX
    JNZ POWER_LOOP

DONE:
    MOV result, AX
    RET
POWER ENDP

PRINT_NUMBER PROC
    MOV BX, 10
    XOR CX, CX

CONVERT_LOOP:
    XOR DX, DX
    DIV BX
    PUSH DX
    INC CX
    CMP AX, 0
    JNE CONVERT_LOOP

PRINT_DIGITS:
    POP DX
    ADD DL, '0'
    MOV AH, 2
    INT 21H
    LOOP PRINT_DIGITS

    RET
PRINT_NUMBER ENDP

END MAIN
