ORG 100H

.DATA

.CODE

MOV AX, 0       ; Initialize AX to 0 to store the sum
MOV CX, 1       ; Initialize CX to 1 (first number in the sequence)
MOV DX, 148     ; Initialize DX to 148 (end value of the sequence)

START:
CMP CX, DX      ; Compare current number (CX) with 148
JG END          ; If CX > 148, end the loop
ADD AX, CX      ; Add current number (CX) to AX
ADD CX, 3       ; Increment CX by 3 to get the next number in the sequence
JMP START       ; Repeat the loop

END:
RET
