
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA
MSG DB 'HELLO BANGLADESH$'

.CODE
LEA DX, MSG
MOV AH, 9
INT 21H

ret




