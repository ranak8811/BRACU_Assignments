.MODEL SMALL
.STACK 100H

.DATA
A DB 1,2,3,4,5

.CODE 
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV CX, 5
    MOV SI, 0
    
    START:
    MOV DL, A[SI]
    ADD DL, 48
    MOV AH, 2
    INT 21H
    
    ADD SI, 1
    LOOP START
    
    MOV AH, 4CH
    INT 21H
    
    MAIN ENDP
END MAIN