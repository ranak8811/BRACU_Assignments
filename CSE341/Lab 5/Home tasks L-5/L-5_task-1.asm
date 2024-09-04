.MODEL SMALL
.STACK 100H

.DATA
N DB 4 DUP(?)

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV CX, 4
    LEA SI, N
    
    INPUT:  
    
    MOV AH, 1
    INT 21H
    
    MOV [SI], AL
    INC SI
    
    LOOP INPUT
    
    MOV DL, 0AH
    MOV AH, 2
    INT 21H
    
    MOV CX, 4
    LEA SI, N
    
    OUTPUT:
    
    MOV DL, [SI]
    MOV AH, 2
    INT 21H
    
    INC SI
    LOOP OUTPUT
    
    
    MOV AH, 4CH
    INT 21H
    
    MAIN ENDP
END MAIN