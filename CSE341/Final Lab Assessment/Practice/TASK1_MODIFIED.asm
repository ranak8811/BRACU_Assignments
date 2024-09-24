.MODEL SMALL
.STACK 100H

.DATA
    COURSES DB 'CSE110$', 0, 'CSE111$', 0, 'CSE220$', 0, 'CSE221$', 0, 'CSE341$', 0
    COURSES2 DB 'CSE340$', 0, 'CSE471$', 0, 'CSE422$', 0, 'CSE423$', 0, 'CSE460$', 0
    USER_INP DB 4 DUP(0)       
    MSG DB 'Enter 4-digit course indices (0-9): $'
    MSGADD DB 'Added courses:$'  
    NEW_LINE DB 0Dh, 0Ah, '$' 

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, MSG
    MOV AH, 09H
    INT 21H

    MOV CX, 4
    LEA SI, USER_INP
READ:
    MOV AH, 01H
    INT 21H
    SUB AL, '0'
    MOV [SI], AL
    INC SI
    LOOP READ

    LEA DX, NEW_LINE
    MOV AH, 09H
    INT 21H

    LEA DX, MSGADD
    MOV AH, 09H
    INT 21H

    LEA DX, NEW_LINE
    MOV AH, 09H
    INT 21H

    MOV CX, 4
    LEA SI, USER_INP
    LEA DI, COURSES
PRINT:
    MOV AL, [SI]
    MOV BL, AL
    MOV AX, BX
    SHL AX, 3
    ADD AX, OFFSET COURSES
    MOV DX, AX

    MOV AH, 09H
    INT 21H

    LEA DX, NEW_LINE
    MOV AH, 09H
    INT 21H

    INC SI
    LOOP PRINT

    MOV AX, 4C00H
    INT 21H

MAIN ENDP
END MAIN
