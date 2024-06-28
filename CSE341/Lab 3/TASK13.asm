ORG 100H

.DATA
A DB ' Saturday$'
B DB ' Sunday$'
C DB ' Monday$'
D DB ' Tuesday$'
E DB ' Wednesday$'
F DB ' Thursday$'
G DB ' Friday$'

.CODE

MOV AX, @DATA
MOV DS, AX
MOV ES, AX

MOV AH, 1
INT 21H
MOV BL, AL

CMP BL, '1'
JE SAT

CMP BL, '2'
JE SUN

CMP BL, '3'
JE MON

CMP BL, '4'
JE TUE

CMP BL, '5'
JE WED

CMP BL, '6'
JE THU

CMP BL, '7'
JE FRI


JMP END


SAT:
MOV AH, 9
LEA DX, A
INT 21H
JMP END

SUN:
MOV AH, 9
LEA DX, B
INT 21H
JMP END

MON:
MOV AH, 9
LEA DX, C
INT 21H
JMP END

TUE:
MOV AH, 9
LEA DX, D
INT 21H
JMP END

WED:
MOV AH, 9
LEA DX, E
INT 21H
JMP END

THU:
MOV AH, 9
LEA DX, F
INT 21H
JMP END

FRI:
MOV AH, 9
LEA DX, G
INT 21H
JMP END

END:
RET  