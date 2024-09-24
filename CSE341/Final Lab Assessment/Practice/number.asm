.MODEL SMALL
.STACK 100H

.DATA
    num db 10, 12, 3, 4, 5, 6, 11, 7, 8, 9
    msg db 'The 3rd index value is: $'
    val db ' ' ; Space for the character value

.CODE
MAIN PROC
    ; Initialize data segment
    MOV AX, @DATA
    MOV DS, AX

    ; Load the address of the 3rd element into AL
    MOV AL, [num + 5] ; Directly access the 3rd element

    ; Convert AL to ASCII
    ADD AL, '0'
    MOV val, AL ; Store the ASCII character in 'val'

    ; Display the message
    MOV AH, 9
    LEA DX, msg
    INT 21H

    ; Display the 3rd element
    MOV AH, 2
    MOV DL, val
    INT 21H

Exit:
    ; Exit program
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN
