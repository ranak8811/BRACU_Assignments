ORG 100H

.DATA



.CODE
   
MOV AL, 4

CMP AL, 1
JE PO

CMP AL, 3
JE PO

CMP AL, 2
JE PE

CMP AL, 4
JE PE

JMP END

PE:
MOV AH, 2
MOV DL, 'E'
INT 21H
JMP END

PO:
MOV AH, 2
MOV DL, 'O'
INT 21H   
   
END:   
RET