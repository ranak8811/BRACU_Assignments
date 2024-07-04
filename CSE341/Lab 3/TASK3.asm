
org 100h

.DATA

.CODE

MOV AX, 7

CMP AX, 0

JL MIN
JE EQL
JG MAX

MAX:
MOV BX, 1
JMP END

EQL:
MOV BX, 0
JMP END

MIN:
MOV BX, -1
JMP END

END:
ret




