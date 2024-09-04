.MODEL SMALL
.STACK 100H

.DATA
a DW 1, 2, 3, 4, 5       ; Define an array of 5 words (2 bytes each)

.CODE
MAIN PROC
    MOV AX, @DATA        ; Initialize data segment
    MOV DS, AX

    MOV CX, 5            ; Number of elements in array
    LEA SI, a            ; Load effective address of array into SI

START:
    MOV AX, [SI]         ; Move the word (16-bit) from memory to AX
    ADD AX, 30H          ; Convert the word value to ASCII (only works for 1-9)
    MOV DL, AL           ; Move the lower byte (ASCII value) to DL
    MOV AH, 2            ; DOS print character function
    INT 21H              ; Print the character

    ADD SI, 2            ; Move to the next word (2 bytes forward)
    LOOP START           ; Loop until all elements are processed

    MOV AH, 4CH          ; Terminate program
    INT 21H

MAIN ENDP
END MAIN
