ORG 100H

.DATA

.CODE

;MOV AX, 80H   ;won't work for AX coz al changes
               ;every time
MOV CX, 80H
MOV BX, 0

DISPLAY:
MOV AH, 2
MOV DL, CL
INT 21H

MOV DL, ' '
INT 21H

INC CX
INC BX

CMP BX, 10
JE LINE

CMP CX, 0FFH
JG END
JMP DISPLAY

LINE:
MOV AH, 2
MOV DL, 0AH
INT 21H
MOV DL, 0DH
INT 21H
MOV BX, 0
JMP DISPLAY

END:
RET