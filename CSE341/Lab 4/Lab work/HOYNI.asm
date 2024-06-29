ORG 100H  ; This is the standard starting address for DOS COM programs.

.DATA
.CODE

MOV AX, 1    ; Load 1 into AX register
INT 21H       ; Call DOS interrupt 21H, AH=1 (read character input)
MOV BL, AL    ; Move the input character from AL to BL

INT 21H       ; Call DOS interrupt 21H, AH=1 again (read another character input)

MOV CX, AL    ; Move the second input character from AL to CX
MOV DX, 0     ; Clear DX register

REPEAT_LOOP:
MOV DX, BX    ; Move the first input character from BL to DX
LOOP REPEAT_LOOP  ; Loop until CX (second input character) times

MOV DX, CX    ; Move CX to DX

RET           ; Return from the program

; Error handling can be omitted for simplicity
