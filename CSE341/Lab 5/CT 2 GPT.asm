.MODEL SMALL
.STACK 100H

.DATA
x DB 15,14,13,12,11,10,9,8,7,6,5,4,3,2,1  ; Define an array with values from 15 to 1

.CODE
MAIN PROC
    MOV AX, @DATA      ; Initialize data segment
    MOV DS, AX

    MOV SI, 0          ; Initialize SI to point to the first element of the array

START_LOOP:
    MOV AL, x[SI]      ; Load the current value of the array into AL
    CMP AL, 1          ; Compare AL with 1
    JL END_LOOP        ; If AL < 1, exit the loop

    ADD AL, 30H        ; Convert to ASCII (since the numbers are between 1-15)
    MOV DL, AL         ; Move the ASCII value to DL for printing
    MOV AH, 2          ; DOS function to print character
    INT 21H            ; Print the character

    MOV DL, 0AH        ; Newline for output clarity (optional)
    MOV AH, 2
    INT 21H

    ADD SI, 3          ; Increment the array index by 3 to simulate x = x - 3
    JMP START_LOOP     ; Repeat the loop

END_LOOP:
    MOV AH, 4CH        ; Exit program
    INT 21H

MAIN ENDP
END MAIN
