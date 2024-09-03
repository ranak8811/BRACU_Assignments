ORG 100H

.DATA

.CODE

MOV CX, 6

MOV BX, 128
MOV AH, 2
;MOV DX, BX ;Ata bahire rakhle just akta value print korrbe

START:
MOV DX, BX  ;Ata vitore rakhle different value print korbe
INT 21H
INC BX
LOOP START