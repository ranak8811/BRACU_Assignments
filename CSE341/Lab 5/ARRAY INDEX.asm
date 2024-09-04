.MODEL SMALL
.STACK 100H

.DATA
a DB 1, 2, 3, 4, 5       ; Define an array of 5 bytes

.CODE
MAIN PROC
    MOV AX, @DATA        ; Initialize the data segment
    MOV DS, AX

    MOV CX, 5            ; Number of elements in array
    MOV SI, 0            ; Initialize SI to point to the first element of the array

START:
    MOV DL, a[SI]        ; Load the byte from array into DL
    ADD DL, 30H          ; Convert to ASCII character (assuming values 1-9)
    MOV AH, 2            ; DOS function to print character
    INT 21H              ; Print the character

    ADD SI, 1            ; Move to the next byte
    LOOP START           ; Repeat until CX reaches 0

    MOV AH, 4CH          ; Terminate the program
    INT 21H

MAIN ENDP
END MAIN
