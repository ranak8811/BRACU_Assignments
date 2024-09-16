.MODEL SMALL

FACTORIAL MACRO NUM
    MOV AX, NUM        ; Load the number into AX
    MOV CX, AX         ; Store the original number in CX
    DEC CX             ; Decrement CX by 1 (since n! = n * (n-1) * ... * 1)
    
    FACT_LOOP:
    CMP CX, 0          ; Check if CX is 0
    JE END_FACTORIAL   ; If CX is 0, we are done
    MUL CX             ; Multiply AX by CX (AX = AX * CX)
    DEC CX             ; Decrement CX by 1
    JMP FACT_LOOP      ; Repeat until CX = 0
    
    END_FACTORIAL:
ENDM

.STACK 100H
.DATA
    num DW 6           ; Define the number whose factorial we want (e.g., 5!)
    msg DB 'Factorial: $'
    newline DB 0AH, 0DH, '$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX         ; Initialize data segment

    LEA DX, msg        ; Load the message to print
    MOV AH, 9
    INT 21H            ; Print message

    FACTORIAL num      ; Calculate factorial of 'num'

    ; Convert result in AX to string and print it
    CALL print_number  ; Print the result

    MOV AH, 4CH        ; Exit to DOS
    INT 21H

MAIN ENDP

print_number PROC
    ; Convert AX (result) to string and print
    MOV BX, 10         ; Divisor for decimal conversion
    MOV CX, 0          ; Clear CX to use as a counter for digits
    
convert_loop:
    XOR DX, DX         ; Clear DX for division
    DIV BX             ; AX / BX, quotient in AX, remainder in DX
    PUSH DX            ; Store the remainder (digit)
    INC CX             ; Increment digit count
    CMP AX, 0          ; If AX is 0, stop the loop
    JNE convert_loop

print_digits:
    POP DX             ; Get the stored digit
    ADD DL, '0'        ; Convert digit to ASCII
    MOV AH, 2
    INT 21H            ; Print the digit
    LOOP print_digits  ; Print all digits

    ; Print newline
    LEA DX, newline
    MOV AH, 9
    INT 21H

    RET
print_number ENDP

END MAIN
