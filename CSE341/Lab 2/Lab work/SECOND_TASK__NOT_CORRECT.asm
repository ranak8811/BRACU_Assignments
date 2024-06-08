org 100h

.DATA
A DB "Please insert a character: $"
B DB "Please insert another character: $"
C DB "HERE IS THE SUMMATION OF THOSE TWO NUMBERS: $"
NUM_STR DB "The result is: $"
RESULT DB ?

.CODE
main proc
    MOV AX, @DATA
    MOV DS, AX
    
    ; Prompt for the first number
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    ; Read the first number
    MOV AH, 1
    INT 21H
    SUB AL, '0'
    MOV BL, AL
    
    ; New line
    MOV AH, 2
    MOV DL, 0AH
    INT 21H
    MOV DL, 0DH
    INT 21H
    
    ; Prompt for the second number
    MOV AH, 9
    LEA DX, B
    INT 21H
    
    ; Read the second number
    MOV AH, 1
    INT 21H
    SUB AL, '0'
    MOV CL, AL
    
    ; New line
    MOV AH, 2
    MOV DL, 0AH
    INT 21H
    MOV DL, 0DH
    INT 21H
    
    ; Prompt for the sum
    MOV AH, 9
    LEA DX, C
    INT 21H
    
    ; Sum the numbers
    ADD BL, CL
    
    ; Convert to ASCII for display
    ADD BL, '0'
    
    ; Display result
    MOV AH, 9
    LEA DX, NUM_STR
    INT 21H
    MOV AH, 2
    MOV DL, BL
    INT 21H
    
    ; Exit
    MOV AH, 4CH
    INT 21H
    
    ret
main endp
end main
