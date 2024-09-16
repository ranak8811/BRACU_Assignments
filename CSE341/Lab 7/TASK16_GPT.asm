.MODEL SMALL
.STACK 100H
.DATA
x DW 3       ; Base (x)
n DW 6       ; Exponent (n)
result DW 1  ; Result initialized to 1

newline DB 0AH, 0DH, '$'  ; Newline for formatting
msg_result DB 'Result: $' ; Message to show the result

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AX, x         ; Load base (x) into AX
    MOV BX, n         ; Load exponent (n) into BX
    CALL POWER        ; Call the procedure to calculate x^n

    ; Display result
    LEA DX, msg_result
    MOV AH, 9
    INT 21H
    
    MOV AX, result    ; Move the result to AX for printing
    CALL PRINT_NUMBER ; Call procedure to print the result

    ; Print newline for formatting
    LEA DX, newline
    MOV AH, 9
    INT 21H

    ; Exit the program
    MOV AH, 4CH
    INT 21H

MAIN ENDP

; Procedure to calculate x^n
; Input: x (in AX), n (in BX)
; Output: result stored in memory
POWER PROC
    MOV AX, 1         ; Initialize AX (result accumulator) to 1
    MOV CX, BX        ; Move the exponent (n) to CX for counting

POWER_LOOP:
    CMP CX, 0         ; Check if n = 0
    JE DONE           ; If n = 0, we're done (x^0 = 1)
    
    MOV BX, x         ; Load the base (x) into BX
    MUL BX            ; Multiply AX by the base (x)
    
    DEC CX            ; Decrement the exponent (n)
    JNZ POWER_LOOP    ; Repeat if n > 0

DONE:
    MOV result, AX    ; Store the result in memory
    RET
POWER ENDP

; Procedure to print a number in AX
PRINT_NUMBER PROC
    MOV BX, 10        ; Divisor for decimal conversion
    XOR CX, CX        ; Clear CX for counting digits

CONVERT_LOOP:
    XOR DX, DX        ; Clear DX for division
    DIV BX            ; AX / BX -> AX (quotient), DX (remainder)
    PUSH DX           ; Push remainder (digit) on the stack
    INC CX            ; Increment digit counter
    CMP AX, 0         ; If quotient is 0, stop the loop
    JNE CONVERT_LOOP

PRINT_DIGITS:
    POP DX            ; Pop the digit from the stack
    ADD DL, '0'       ; Convert digit to ASCII
    MOV AH, 2         ; DOS interrupt to print a character
    INT 21H           ; Print the character
    LOOP PRINT_DIGITS ; Loop until all digits are printed

    RET
PRINT_NUMBER ENDP

END MAIN
