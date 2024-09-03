ORG 100H

.DATA

.CODE

MOV AL, 2

MOV DL, AL
MOV AH, 2
MOV BL, 9  ; Counter for loop iterations

START:
CMP AL, BL  ; Compare before incrementing
JE END

INT 21H
INC AL
JMP START

END:
RET
