.MODEL SMALL
.STACK 100H

.DATA
    COURSES DB 'CSE110$', 'CSE111$', 'CSE220$', 'CSE221$', 'CSE341$', 'CSE340$', 'CSE471$', 'CSE422$', 'CSE423$', 'CSE460$'
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
READ_INPUT:
    MOV AH, 01H
    INT 21H
    SUB AL, '0'
    MOV [SI], AL
    INC SI
    LOOP READ_INPUT

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
PRINT_COURSES:
    MOV AL, [SI]        
    MOV BL, AL          
    MOV AX, BX          
    MOV BX, 7           
    MUL BX              
    ADD AX, OFFSET COURSES 
    MOV DX, AX          

    MOV AH, 09H
    INT 21H

    LEA DX, NEW_LINE
    MOV AH, 09H
    INT 21H

    INC SI              
    LOOP PRINT_COURSES

    MOV AX, 4CH
    INT 21H

MAIN ENDP
END MAIN
