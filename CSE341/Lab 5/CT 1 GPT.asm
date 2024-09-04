.MODEL SMALL
.STACK 100H

.DATA
x DB 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15  ; Define an array with values from 1 to 15

.CODE
MAIN PROC
    MOV AX, @DATA      ; Initialize data segment
    MOV DS, AX

    MOV SI, 0          ; Initialize SI to point to the first element of the array

START_LOOP:
    MOV AL, x[SI]      ; Load the current value of the array into AL
    CMP AL, 15         ; Compare AL with 15
    JGE END_LOOP       ; If AL >= 15, exit the loop

    ADD AL, 30H        ; Convert to ASCII (since the numbers are between 1-15)
    MOV DL, AL         ; Move the ASCII value to DL for printing
    MOV AH, 2          ; DOS function to print character
    INT 21H            ; Print the character

    MOV DL, 0AH        ; Newline for output clarity (optional)
    MOV AH, 2
    INT 21H

    ADD SI, 3          ; Increment the array index by 3 (similar to x = x + 3)
    JMP START_LOOP     ; Repeat the loop

END_LOOP:
    MOV AH, 4CH        ; Exit program
    INT 21H

MAIN ENDP
END MAIN
