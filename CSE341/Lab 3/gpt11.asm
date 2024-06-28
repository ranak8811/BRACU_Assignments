ORG 100H

.DATA
prompt1 DB 'Enter side 1 of the triangle: $'
prompt2 DB 'Enter side 2 of the triangle: $'
prompt3 DB 'Enter side 3 of the triangle: $'
valid_msg DB 'TRIANGLE IS VALID$'
invalid_msg DB 'TRIANGLE IS NOT VALID$'
newline DB 0DH, 0AH, '$'

.CODE

    ; Prompt for side 1
    MOV AH, 9
    LEA DX, prompt1
    INT 21H

    MOV AH, 1
    INT 21H
    SUB AL, '0'
    MOV BL, AL    ; Store side 1 in BL

    ; New line
    MOV AH, 9
    LEA DX, newline
    INT 21H

    ; Prompt for side 2
    MOV AH, 9
    LEA DX, prompt2
    INT 21H

    MOV AH, 1
    INT 21H
    SUB AL, '0'
    MOV CL, AL    ; Store side 2 in CL

    ; New line
    MOV AH, 9
    LEA DX, newline
    INT 21H

    ; Prompt for side 3
    MOV AH, 9
    LEA DX, prompt3
    INT 21H

    MOV AH, 1
    INT 21H
    SUB AL, '0'
    MOV DL, AL    ; Store side 3 in DL

    ; Check triangle validity using triangle inequality theorem
    CMP BL, CL
    JGE INVALID_TRIANGLE
    CMP BL, DL
    JGE INVALID_TRIANGLE
    CMP CL, DL
    JGE INVALID_TRIANGLE

    ; If passed all checks, triangle is valid
    MOV AH, 9
    LEA DX, valid_msg
    INT 21H
    JMP END_PROGRAM

INVALID_TRIANGLE:
    ; If any check fails, triangle is not valid
    MOV AH, 9
    LEA DX, invalid_msg
    INT 21H

END_PROGRAM:
    ; Exit program
    MOV AH, 4CH
    INT 21H

RET
