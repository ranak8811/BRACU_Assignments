.MODEL SMALL
.STACK 100H

.DATA
X DB 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV CX, 6
    LEA SI, X
    
    START:
    MOV AX, [SI]
    ADD AX, 48
    MOV DL, AL
    MOV AH, 2
    INT 21H
    
    ADD SI, 3
    LOOP START
    
    MOV AH, 4CH
    INT 21H
    
    MAIN ENDP
END MAIN