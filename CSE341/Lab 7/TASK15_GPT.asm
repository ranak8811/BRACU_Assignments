.MODEL SMALL
.STACK 100H

.DATA
numbers DW 10, 57, 25, 55, 30, 12  ; Array of numbers to find maximum from
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

    ; Initialize registers
    MOV CX, 5             ; Number of elements in the array
    MOV BX, OFFSET numbers ; BX points to the start of the numbers array

    ; Load the first number as the current maximum
    MOV AX, [BX]          ; AX holds the current maximum
    ADD BX, 2             ; Move BX to the next number in the array

    ; Find maximum of all numbers in the array
    DEC CX                ; Already have the first number, so reduce loop count
FIND_MAX_LOOP:
    CALL MAX_TWO_NUMBERS   ; Call procedure to compare AX with the next number
    ADD BX, 2              ; Move to the next number in the array
    LOOP FIND_MAX_LOOP     ; Repeat until all numbers are compared

    ; AX now holds the maximum value
    CALL print_number      ; Print the result

    ; Print a newline for formatting
    LEA DX, newline
    MOV AH, 9
    INT 21H

    ; Terminate the program
    MOV AH, 4CH
    INT 21H

MAIN ENDP


; Procedure to find the maximum between two numbers
; Input: AX contains the current maximum, BX points to the next number in the array
; Output: AX will hold the maximum between the two numbers
MAX_TWO_NUMBERS PROC
    MOV DX, [BX]         ; Load the next number into DX
    CMP AX, DX           ; Compare AX with DX
    JGE RETURN_MAX       ; If AX >= DX, AX remains the max
    MOV AX, DX           ; Otherwise, DX is the new max

RETURN_MAX:
    RET
MAX_TWO_NUMBERS ENDP

; Procedure to print the number in AX
print_number PROC
    MOV BX, 10           ; Divisor for decimal conversion
    MOV CX, 0            ; Clear CX to use it for counting digits

convert_loop:
    XOR DX, DX           ; Clear DX for division
    DIV BX               ; AX / BX -> AX (quotient), DX (remainder)
    PUSH DX              ; Push remainder (digit) on the stack
    INC CX               ; Increment digit counter
    CMP AX, 0            ; If quotient is 0, stop the loop
    JNE convert_loop

print_digits:
    POP DX               ; Pop the digit from the stack
    ADD DL, '0'          ; Convert digit to ASCII
    MOV AH, 2            ; DOS interrupt to print a character
    INT 21H              ; Print the character
    LOOP print_digits    ; Loop until all digits are printed

    RET
print_number ENDP

END MAIN
