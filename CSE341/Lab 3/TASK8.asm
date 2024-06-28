ORG 100H

.DATA
A DB ' -> The letter is a vowel.$'
B DB ' -> The letter is a consonant.$'
C DB 'Enter an alphabet: $'

.CODE

MOV AH, 9
LEA DX, C
INT 21H

MOV AH, 1
INT 21H
MOV BL, AL

CMP BL, 'A'
JE PV

CMP BL, 'E'
JE PV

CMP BL, 'I'
JE PV

CMP BL, 'O'
JE PV

CMP BL, 'U'
JE PV



PC:
MOV AH, 9
LEA DX, B
INT 21H


JMP END

PV:
MOV AH, 9
LEA DX, A
INT 21H

END:
RET