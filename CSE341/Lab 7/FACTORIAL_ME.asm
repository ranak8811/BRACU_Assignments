ORG 100H

.DATA
ANS DB ?

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AL, 5
    MOV CL, 4
    MOV BL, AL
    
    SUB BL, 1
    
    FACTORIAL_LOOP:
    MUL BL
    DEC BL
    LOOP FACTORIAL_LOOP
    
    MOV ANS, AL
    
    END MAIN
RET