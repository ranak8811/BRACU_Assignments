.MODEL SMALL
.STACK 100H

.DATA
A DB 1,2,3,4,5
B DB 5 DUP(?)
C DB "HELLO $"

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    ;MY CODE IS HERE
    ;POINTER / INDEX
    ; LEA WORKS AS POINTER
    
    MOV SI, 0
    MOV DL, A[SI]  ;ACCESSING ARRAY USING INDEX
    MOV AH, 2
    INT 21H
              
              
      ;FOR 16BIT ARRAY WE HAVE TO USE INC SI 2 TIMES
      ;TO GET THE NEXT VALUE
    
    
    
    MAIN ENDP
END MAIN