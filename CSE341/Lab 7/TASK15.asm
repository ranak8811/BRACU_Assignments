.MODEL SMALL
.STACK 100H

.DATA
numbers DW 10, 57, 25, 55, 30, 12
msg_max DB 'The maximum number is: $'
newline DB 0AH, 0DH, '$'

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, msg_max
    MOV AH, 9
    INT 21H

    MOV CX, 5
    MOV BX, OFFSET numbers

    MOV AX, [BX]
    ADD BX, 2

    DEC CX
FIND_MAX_LOOP:
    CALL MAX_TWO_NUMBERS
    ADD BX, 2
    LOOP FIND_MAX_LOOP

    CALL print_number

    LEA DX, newline
    MOV AH, 9
    INT 21H

    MOV AH, 4CH
    INT 21H

MAIN ENDP

MAX_TWO_NUMBERS PROC
    MOV DX, [BX]
    CMP AX, DX
    JGE RETURN_MAX
    MOV AX, DX

RETURN_MAX:
    RET
MAX_TWO_NUMBERS ENDP

print_number PROC
    MOV BX, 10
    MOV CX, 0

convert_loop:
    XOR DX, DX
    DIV BX
    PUSH DX
    INC CX
    CMP AX, 0
    JNE convert_loop

print_digits:
    POP DX
    ADD DL, '0'
    MOV AH, 2
    INT 21H
    LOOP print_digits

    RET
print_number ENDP

END MAIN
