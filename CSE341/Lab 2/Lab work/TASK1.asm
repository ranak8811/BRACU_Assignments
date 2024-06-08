
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h  

.DATA

A DB "Please insert a character: $"
     
.CODE

LEA DX, A
MOV AH, 9
INT 21H

MOV AH, 1
INT 21H

MOV DL, AL
MOV AH, 2
INT 21H

ret




