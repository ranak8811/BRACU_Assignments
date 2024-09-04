.MODEL SMALL
.STACK 100H

.DATA
NAME1 DB 4 DUP(?)

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    LEA SI, NAME1
    MOV CX, 4
    
    INPUT:
    MOV AH, 1
    INT 21H
    
    MOV [SI], AL
    INC SI
    
    LOOP INPUT
    
    MOV DL, 0AH
    MOV AH, 2
    INT 21H
    
    LEA SI, NAME1
    MOV CX, 4
    
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