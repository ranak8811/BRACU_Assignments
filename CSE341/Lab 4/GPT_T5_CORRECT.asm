ORG 100H

.DATA

.CODE

MOV AX, 80H         ; Start with ASCII code 80h
MOV CX, 80H         ; CX will hold the current character code
MOV BX, 0           ; BX will count characters per line

DISPLAY:
    MOV AH, 2        ; DOS function to display a character
    MOV DL, CL       ; Load current character into DL
    INT 21H          ; Display the character

    ; Display a space
    MOV DL, ' '      
    INT 21H          

    INC CX           ; Move to the next character
    INC BX           ; Increment the character count per line

    CMP BX, 10       ; Check if 10 characters have been displayed
    JNE CONTINUE     ; If not, continue displaying characters

    ; New line after 10 characters
    MOV AH, 2        
    MOV DL, 0AH      ; Line feed (LF)
    INT 21H
    MOV DL, 0DH      ; Carriage return (CR)
    INT 21H
    MOV BX, 0        ; Reset the character count for the new line

CONTINUE:
    CMP CX, 0FFH     ; Check if the current character is FFh
    JG END           ; If greater, end the program
    JMP DISPLAY      ; Otherwise, continue displaying

END:
RET
