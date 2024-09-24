.MODEL SMALL
.STACK 100H

.DATA
    courses DB 'CSE110$', 0, 'CSE111$', 0, 'CSE220$', 0, 'CSE221$', 0, 'CSE341$', 0
    courses2 DB 'CSE340$', 0, 'CSE471$', 0, 'CSE422$', 0, 'CSE423$', 0, 'CSE460$', 0
    input DB 4 DUP(0)       
    promptMessage DB 'Enter 4-digit course indices (0-9): $'
    addedMessage DB 'Added courses:$'  
    newline DB 0Dh, 0Ah, '$' 

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, promptMessage
    MOV AH, 09H
    INT 21H

    MOV CX, 4
    LEA SI, input
read_input:
    MOV AH, 01H
    INT 21H
    SUB AL, '0'
    MOV [SI], AL
    INC SI
    LOOP read_input

    LEA DX, newline
    MOV AH, 09H
    INT 21H

    LEA DX, addedMessage
    MOV AH, 09H
    INT 21H

    LEA DX, newline
    MOV AH, 09H
    INT 21H

    MOV CX, 4
    LEA SI, input
    LEA DI, courses
display_courses:
    MOV AL, [SI]
    MOV BL, AL
    MOV AX, BX
    SHL AX, 3
    ADD AX, OFFSET courses
    MOV DX, AX

    MOV AH, 09H
    INT 21H

    LEA DX, newline
    MOV AH, 09H
    INT 21H

    INC SI
    LOOP display_courses

    MOV AX, 4C00H
    INT 21H

MAIN ENDP
END MAIN
