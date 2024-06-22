
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

; add your code here

.DATA

.CODE

MOV AH, 1
INT 21H
MOV BL, AL


MOV AH, 1
INT 21H
MOV CL, AL
SUB CL, '0'

ADD BL, CL

MOV AH, 2
MOV DL, BL
INT 21H


ret




