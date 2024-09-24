.MODEL SMALL
.STACK 100H

.DATA
    COURSES DB 'CSE110', 'CSE111', 'CSE220', 'CSE221', 'CSE341', 'CSE340', 'CSE471', 'CSE422', 'CSE423', 'CSE460'
    USER_INP DB 4 DUP(?)   
    MSG DB 'ENTER UP TO 4 DIGIT COURSE INDEXES: $'
    MSGADD DB 'ADDED COURSES:', 0DH, 0AH, '$'
    SEMESTER DW 10000      
    TUITION DW 20000      
    TOTAL DW ?           

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, MSG
    MOV AH, 09H
    INT 21H

    MOV SI, OFFSET USER_INP
    MOV CX, 4
INPUT_LOOP:
    MOV AH, 01H
    INT 21H
    CMP AL, 0DH    
    JE CALCULATE
    MOV [SI], AL   
    INC SI
    LOOP INPUT_LOOP

CALCULATE:
    MOV AX, SEMESTER
    MOV TOTAL, AX

    MOV SI, OFFSET USER_INP
    MOV CX, 4
    XOR BX, BX         

COURSE_LOOP:
    MOV AL, [SI]       
    CMP AL, 0          
    JE DONE_COURSE     
    SUB AL, '0'        
    INC BX             
    INC SI             
    LOOP COURSE_LOOP

DONE_COURSE:
    MOV AX, BX
    MOV DX, 0
    MOV CX, TUITION
    MUL CX             
    ADD TOTAL, AX      

ENDPGM:
    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN
