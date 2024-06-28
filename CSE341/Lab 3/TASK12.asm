ORG 100H

.DATA

.CODE

MOV AX, @DATA
MOV DS, AX
MOV ES, AX


MOV AH, 1
INT 21H
MOV BL, AL

CMP BL, '0'
JE PI

CMP BL, '1'
JE PI

CMP BL, '2'
JE PI

CMP BL, '3'
JE PI

CMP BL, '4'
JE PK

CMP BL, '5'
JE PK

CMP BL, '6'
JE PK

CMP BL, '7'
JE P1

CMP BL, '8'
JE P1

CMP BL, '9'
JE P1

CMP BL, 'T'
JE PM

JMP END

PI:
MOV AH, 2
MOV DL, 'i'
INT 21H
JMP END

PK:
MOV AH, 2
MOV DL, 'k'
INT 21H
JMP END

P1:
MOV AH, 2
MOV DL, '1'
INT 21H
JMP END

PM:
MOV AH, 2
MOV DL, 'm'
INT 21H
JMP END

END:
RET