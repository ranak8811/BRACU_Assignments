.MODEL SMALL
.STACK 100H

.DATA
array DB 10, 20, 30, 40, 50  ; Define an array of 5 random numbers
index_msg DB 'Enter index (0-4): $'
value_msg DB 'Enter value to add: $'
newline DB 0AH, 0DH, '$'

.CODE
MAIN PROC
    MOV AX, @DATA       ; Initialize the data segment
    MOV DS, AX

    ; Prompt for index input
    LEA DX, index_msg
    MOV AH, 9
    INT 21H

    MOV AH, 1           ; Take the first input (index)
    INT 21H
    SUB AL, '0'         ; Convert ASCII to numeric value
    MOV BL, AL          ; Store index in BL

    ; Prompt for value input
    LEA DX, value_msg
    MOV AH, 9
    INT 21H

    MOV AH, 1           ; Take the second input (value to add)
    INT 21H
    SUB AL, '0'         ; Convert ASCII to numeric value
    MOV CL, AL          ; Store the value in CL

    ; Add the value to the array element at the given index
    MOV SI, BX          ; Load the index into SI
    ADD array[SI], CL   ; Add the value in CL to the array element at index SI

    ; Optional: Print the updated array for verification
    MOV CX, 5           ; Set the loop counter to 5
    LEA SI, array       ; Load the address of the array into SI

PRINT_ARRAY:
    MOV DL, [SI]        ; Load the current array element into DL
    ADD DL, 30H         ; Convert it to ASCII
    MOV AH, 2           ; DOS function to print character
    INT 21H             ; Print the character

    LEA DX, newline     ; Print newline after each value
    MOV AH, 9
    INT 21H

    INC SI              ; Move to the next array element
    LOOP PRINT_ARRAY    ; Repeat for all array elements

    ; Terminate the program
    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN
