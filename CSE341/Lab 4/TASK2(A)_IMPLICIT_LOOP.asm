ORG 100H

.DATA

.CODE

MOV AX, 0       ; Initialize AX to 0 to store the sum
MOV CX, 50      ; Initialize CX to the number of terms in the sequence (since there are 50 terms in 1 + 4 + 7 + ... + 148)
MOV DX, 1       ; Initialize DX to 1 (first number in the sequence)

START:
ADD AX, DX      ; Add current number (DX) to AX
ADD DX, 3       ; Increment DX by 3 to get the next number in the sequence
LOOP START      ; Decrement CX and loop to START if CX is not zero

END:
RET
