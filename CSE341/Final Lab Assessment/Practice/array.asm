.MODEL SMALL
.STACK 100H

.DATA
    num db 10, 12, 3, 4, 5, 6, 11, 7, 8, 9
    msg db "Enter Number: $"
    msg1 db 10, 13, "Number is Found! $"
    msg2 db 10, 13, "Number is not Found! $"
    value db ?

.CODE
MAIN PROC
    ; Initialize data segment
    MOV AX, @DATA
    MOV DS, AX

    ; Display prompt message
    LEA DX, msg
    MOV AH, 09h
    INT 21h

    ; Read value from keyboard
    MOV AH, 01h
    INT 21h
    SUB AL, '0' ; Convert ASCII digit to binary
    MOV value, AL

    ; Set up for searching
    LEA SI, num  ; Move SI to point to the start of the array
    MOV CX, 10   ; Set the count of numbers to search
    MOV AL, value

Searching:
    MOV BL, [SI] ; Load current array element into BL
    CMP AL, BL   ; Compare with the value
    JZ NumFound   ; Jump if found
    INC SI       ; Move to the next element
    LOOP Searching ; Loop until CX is zero

    ; If not found
    LEA DX, msg2  
    MOV AH, 09h
    INT 21h       
    JMP Exit

NumFound:
    ; If found
    LEA DX, msg1  
    MOV AH, 09h
    INT 21h

Exit:
    ; Exit program
    MOV AX, 4C00H
    INT 21H
MAIN ENDP
END MAIN
