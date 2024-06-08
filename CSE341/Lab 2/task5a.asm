
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.CODE
    MOV AH, 2
    MOV DL, '?'
    INT 21H

ret




