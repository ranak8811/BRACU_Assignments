ORG 100H

.DATA
PROMPT1 DB 'Enter first number: $'
PROMPT2 DB 'Enter second number: $'
PROMPT3 DB 'Enter third number: $'
MAX_MSG DB 'Maximum number is: $'
MIN_MSG DB 'Minimum number is: $'
NEWLINE DB 0AH, 0DH, '$'

.CODE
START:
    MOV AX, @DATA
    MOV DS, AX
    MOV ES, AX

    ; Prompt for first number
    MOV AH, 9
    LEA DX, PROMPT1
    INT 21H

    MOV AH, 1
    INT 21H
    SUB AL, '0'
    MOV BL, AL    ; Store first number in BL

    ; New line
    MOV AH, 9
    LEA DX, NEWLINE
    INT 21H

    ; Prompt for second number
    MOV AH, 9
    LEA DX, PROMPT2
    INT 21H

    MOV AH, 1
    INT 21H
    SUB AL, '0'
    MOV CL, AL    ; Store second number in CL

    ; New line
    MOV AH, 9
    LEA DX, NEWLINE
    INT 21H

    ; Prompt for third number
    MOV AH, 9
    LEA DX, PROMPT3
    INT 21H

    MOV AH, 1
    INT 21H
    SUB AL, '0'
    MOV DL, AL    ; Store third number in DL

    ; New line
    MOV AH, 9
    LEA DX, NEWLINE
    INT 21H

    ; Initialize max and min to first number
    MOV AH, BL
    MOV BH, BL

    ; Compare second number with max and min
    CMP CL, AH
    JA SET_MAX_CL
    CMP CL, BH
    JB SET_MIN_CL
    JMP COMP_THIRD

SET_MAX_CL:
    MOV AH, CL
    JMP COMP_THIRD

SET_MIN_CL:
    MOV BH, CL
    JMP COMP_THIRD

COMP_THIRD:
    ; Compare third number with max and min
    CMP DL, AH
    JA SET_MAX_DL
    CMP DL, BH
    JB SET_MIN_DL
    JMP DISPLAY

SET_MAX_DL:
    MOV AH, DL
    JMP DISPLAY

SET_MIN_DL:
    MOV BH, DL
    JMP DISPLAY

DISPLAY:
    ; Display maximum number
    MOV AH, 9
    LEA DX, MAX_MSG
    INT 21H
    MOV DL, AH
    ADD DL, '0'
    MOV AH, 2
    INT 21H

    ; New line
    MOV AH, 9
    LEA DX, NEWLINE
    INT 21H

    ; Display minimum number
    MOV AH, 9
    LEA DX, MIN_MSG
    INT 21H
    MOV DL, BH
    ADD DL, '0'
    MOV AH, 2
    INT 21H

    ; New line
    MOV AH, 9
    LEA DX, NEWLINE
    INT 21H

    ; Exit program
    MOV AX, 4C00H
    INT 21H

RET
