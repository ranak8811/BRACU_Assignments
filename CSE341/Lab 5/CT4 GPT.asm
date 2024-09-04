.MODEL SMALL
.STACK 100H

.DATA
name1 DB 'John'    ; Define a 4-character name (e.g., "John")

.CODE
MAIN PROC
    MOV AX, @DATA    ; Initialize the data segment
    MOV DS, AX

    MOV CX, 4        ; Set the loop counter to 4 (number of characters in the name)
    LEA SI, name1     ; Load the address of the name into SI

    ADD SI, CX       ; Point SI to one byte past the last character
    DEC SI           ; Adjust SI to point to the last character (CX-1)

REVERSE_LOOP:
    MOV DL, [SI]     ; Load the current character from the array into DL
    MOV AH, 2        ; DOS function to print character
    INT 21H          ; Print the character

    DEC SI           ; Move to the previous character in the array
    LOOP REVERSE_LOOP ; Repeat until all characters are printed

    MOV AH, 4CH      ; Terminate the program
    INT 21H

MAIN ENDP
END MAIN
