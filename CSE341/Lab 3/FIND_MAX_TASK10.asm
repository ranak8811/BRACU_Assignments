ORG 100H

.DATA

.CODE

MOV AH, 1
INT 21H
MOV BL, AL
INT 21H
MOV BH, AL
INT 21H
MOV CL, AL

CMP BL, BH
JGE A

B:
CMP BH, CL
JGE C
MOV AH, 2
MOV DL, CL
INT 21H
JMP END

C:
MOV AH, 2
MOV DL, BH
INT 21H
JMP END

A:
CMP BL, CL
JGE D
MOV AH, 2
MOV DL, CL
INT 21H
JMP END

D:
MOV AH, 2
MOV DL, BL
INT 21H

END:
RET