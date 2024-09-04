.MODEL SMALL
.STACK 100H

.DATA
A DW 1,2,3,4,5

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV CX, 5
    LEA SI, A
    
    START:
    MOV AX, [SI]
    ADD AX, 48
    MOV DL, AL
    MOV AH, 2
    INT 21H
    
    ADD SI, 2
    LOOP START
    
    MOV AH, 4CH
    INT 21H
    
    MAIN ENDP
END MAIN