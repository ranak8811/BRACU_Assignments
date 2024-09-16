.MODEL SMALL

PARENTHESIS_CHECK MACRO STR
    LEA SI, STR
    MOV CX, 0

LOOP_CHECK:
    MOV AL, [SI]
    CMP AL, '$'
    JE CHECK_DONE

    CMP AL, '('
    JE OPEN_PAREN

    CMP AL, ')'
    JE CLOSE_PAREN

    JMP NEXT_CHAR

OPEN_PAREN:
    INC CX
    JMP NEXT_CHAR

CLOSE_PAREN:
    DEC CX
    CMP CX, 0
    JL NOT_BALANCED
    JMP NEXT_CHAR

NEXT_CHAR:
    INC SI
    JMP LOOP_CHECK

CHECK_DONE:
    CMP CX, 0
    JE BALANCED
    JMP NOT_BALANCED

BALANCED:
    LEA DX, msg_balanced
    MOV AH, 9
    INT 21H
    JMP END_CHECK

NOT_BALANCED:
    LEA DX, msg_not_balanced
    MOV AH, 9
    INT 21H

END_CHECK:
ENDM


.STACK 100H

.DATA
equation DB '(2+3)*(5-(7/2)())$', '$'
msg_balanced DB 'Parentheses are balanced.$', '$'
msg_not_balanced DB 'Parentheses are not balanced.$', '$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, equation
    MOV AH, 9
    INT 21H

    PARENTHESIS_CHECK equation

    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN

