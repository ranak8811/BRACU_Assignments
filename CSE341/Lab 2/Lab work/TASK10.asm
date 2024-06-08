
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA

.CODE     

MOV AX, 813AH
MOV BX, 94A2H

ADD AX, BX



ret




