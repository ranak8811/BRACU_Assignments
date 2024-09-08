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
    
    OUTPUT:
    
    PUSH [SI]
    
    INC SI
    LOOP OUTPUT
    
    MOV AX, 4CH
    INT 21H
    
    MAIN ENDP
END MAIN