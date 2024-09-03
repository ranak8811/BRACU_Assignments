.MODEL SMALL
.STACK 100H

.DATA
A DW 1,2,3,4

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    ;LIFO

    MOV CX, 4
    MOV SI, 0

    ; Push characters onto the stack
    PUSH_LOOP:
    MOV DX, A[SI]
    PUSH DX
    INC SI
    INC SI
    LOOP PUSH_LOOP
    
    
    MOV CX, 4
    ; Pop characters and display them in reverse order
    POP_LOOP:
    POP DX         
    MOV AH, 2
    ADD DX, 48          
    INT 21H
    LOOP POP_LOOP

    MOV AH, 4CH        
    INT 21H

MAIN ENDP
END MAIN
