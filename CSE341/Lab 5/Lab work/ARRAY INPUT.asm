.DATA

NAME1 DB 7 DUP(?)

.CODE

MAIN PROC
    
    MOV AX, @DATA
    MOV DS, AX
    
    LEA SI, NAME1
    
    MOV CX, 7
    
    INPUT_LOOP:
    MOV AH, 1
    INT 21H
    
    MOV [SI], AL
    INC SI
    
    LOOP INPUT_LOOP
    
    
    LEA SI, NAME1
    
    MOV CX, 7
    
    OUTPUT_LOOP:
    MOV DL, [SI]
    MOV AH, 2
    INT 21H
    
    
    INC SI
    
    LOOP OUTPUT_LOOP