org 100h

.DATA
A DB 'Enter the first number: $'
B DB 'Enter the second number: $'
RESULT_PROMPT DB 'Subtraction result is: $'
NEWLINE DB 0DH, 0AH, '$'

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
    MOV AH, 9
    LEA DX, NEWLINE
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
    MOV AH, 9
    LEA DX, NEWLINE
    INT 21H
    
    ; Subtract second number from first
    SUB BL, CL
    
    ; Display the result prompt
    MOV AH, 9
    LEA DX, RESULT_PROMPT
    INT 21H
    
    ; Convert result to ASCII
    ADD BL, '0'
    
    ; Display the result
    MOV AH, 2
    MOV DL, BL
    INT 21H
    
    
    ; Exit
    MOV AH, 4CH
    INT 21H
    
    ret
main endp
end main
