.MODEL SMALL

FIND_MAX MACRO NUM1, NUM2, NUM3
    MOV AX, NUM1          ; Load the first number into AX
    CMP AX, NUM2          ; Compare AX with the second number
    JGE CHECK_THIRD       ; If AX >= NUM2, jump to check with the third number
    MOV AX, NUM2          ; Otherwise, NUM2 is greater, move it into AX

CHECK_THIRD:
    CMP AX, NUM3          ; Compare the larger of NUM1/NUM2 with the third number
    JGE MAX_FOUND         ; If AX >= NUM3, AX is the maximum
    MOV AX, NUM3          ; Otherwise, NUM3 is the largest

MAX_FOUND:
ENDM

.STACK 100H

.DATA
num1 DW 33            ; First number
num2 DW 9            ; Second number
num3 DW 11            ; Third number
msg_max DB 'The maximum number is: $'
newline DB 0AH, 0DH, '$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    ; Print the message
    LEA DX, msg_max
    MOV AH, 9
    INT 21H

    ; Call the FIND_MAX macro to get the maximum of num1, num2, num3
    FIND_MAX num1, num2, num3

    ; Convert the result in AX to ASCII and print it
    CALL print_number

    ; Print a newline for formatting
    LEA DX, newline
    MOV AH, 9
    INT 21H

    ; Terminate the program
    MOV AH, 4CH
    INT 21H

MAIN ENDP

print_number PROC
    ; Convert AX (result) to string and print
    MOV BX, 10         ; Divisor for decimal conversion
    MOV CX, 0          ; Clear CX to use it for counting digits

convert_loop:
    XOR DX, DX         ; Clear DX for division
    DIV BX             ; AX / BX -> AX (quotient), DX (remainder)
    PUSH DX            ; Push remainder (digit) on the stack
    INC CX             ; Increment digit counter
    CMP AX, 0          ; If quotient is 0, stop the loop
    JNE convert_loop

print_digits:
    POP DX             ; Pop the digit from the stack
    ADD DL, '0'        ; Convert digit to ASCII
    MOV AH, 2          ; DOS interrupt to print a character
    INT 21H            ; Print the character
    LOOP print_digits  ; Loop until all digits are printed

    RET
print_number ENDP

END MAIN
