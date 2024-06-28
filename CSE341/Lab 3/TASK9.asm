ORG 100H

.DATA
PROMPT_MSG DB 'Enter a number (0-9): $'
DIVISIBLE_MSG DB 'The number is divisible by both 5 and 11.$'
NOT_DIVISIBLE_MSG DB 'The number is not divisible by both 5 and 11.$'

.CODE
START:
    ; Set segment registers
    MOV AX, @DATA
    MOV DS, AX
    MOV ES, AX

    ; Display prompt message
    ;MOV AH, 9
    ;LEA DX, PROMPT_MSG
    ;INT 21H

    ; Read a character from the keyboard
    ;MOV AH, 1
    ;INT 21H
    ;SUB AL, '0'    ; Convert ASCII to integer
    ;MOV BL, AL     ; Store the input number in BL
    
    MOV BL, 35

    ; Check if the number is divisible by 5
    MOV AX, 0      ; Clear AX
    MOV AL, BL     ; Move the input number to AX
    MOV CX, 5
    XOR DX, DX     ; Clear DX
    DIV CX         ; AX = AX / CX, DX = AX % CX
    CMP DX, 0
    JNE NOT_DIVISIBLE

    ; Check if the number is divisible by 11
    MOV AX, 0      ; Clear AX
    MOV AL, BL     ; Move the input number to AX
    MOV CX, 11
    XOR DX, DX     ; Clear DX
    DIV CX         ; AX = AX / CX, DX = AX % CX
    CMP DX, 0
    JNE NOT_DIVISIBLE

    ; If divisible by both 5 and 11
    MOV AH, 9
    LEA DX, DIVISIBLE_MSG
    INT 21H
    JMP END

NOT_DIVISIBLE:
    ; If not divisible by both 5 and 11
    MOV AH, 9
    LEA DX, NOT_DIVISIBLE_MSG
    INT 21H

END:
    ; Exit program
    MOV AX, 4C00H
    INT 21H

RET
