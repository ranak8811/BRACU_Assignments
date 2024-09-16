.MODEL SMALL
.STACK 100H

.DATA
array DB 5, 10, 15, 20, 25
msg_found DB 'Value found!$'
msg_not_found DB 'Value not found.$'
newline DB 0AH, 0DH, '$'
search_value DB 15

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV AL, search_value
    CALL SEARCH_ARRAY

    CMP AX, 1
    JE FOUND_VALUE
    JMP NOT_FOUND_VALUE

FOUND_VALUE:
    LEA DX, msg_found
    MOV AH, 9
    INT 21H
    JMP FINISH

NOT_FOUND_VALUE:
    LEA DX, msg_not_found
    MOV AH, 9
    INT 21H

FINISH:
    LEA DX, newline
    MOV AH, 9
    INT 21H

    MOV AH, 4CH
    INT 21H

MAIN ENDP

SEARCH_ARRAY PROC
    MOV SI, OFFSET array
    MOV CX, 5

SEARCH_LOOP:
    CMP AL, [SI]
    JE VALUE_FOUND

    INC SI
    DEC CX
    JNZ SEARCH_LOOP

    MOV AX, 0
    RET

VALUE_FOUND:
    MOV AX, 1
    RET
SEARCH_ARRAY ENDP

END MAIN
