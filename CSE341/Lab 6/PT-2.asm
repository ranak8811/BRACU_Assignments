.MODEL SMALL
.STACK 100H

.DATA
A DB 1,2,3,4,5,6,7

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV CX, 7
    LEA SI, A
    
    PUSH_LOOP:
    
    PUSH [SI]
    
    INC SI
    LOOP PUSH_LOOP
    
    MOV CX, 7
    LEA SI, A
    
    POP_LOOP:
    POP [SI]
    
    INC SI
    LOOP POP_LOOP
    
    MOV AX, 4CH
    INT 21H
    
    MAIN ENDP
END MAIN