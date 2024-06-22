
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

; add your code here

.data
A DB 10

.code
MOV AH, 1
INT 21H

SUB AL, '0'
      
      
MOV CL, 10
MUL CL
MOV BL, AL


MOV AH, 1
INT 21H

SUB AL, '0'

MOV CL, AL

ADD BL, CL 

MOV AH, 1
INT 21H

SUB AL, '0'

MOV DL, 10
MUL DL
MOV CL, AL


MOV AH, 1
INT 21H
MOV CH, AL
SUB CH, '0'

MOV CH, AL

ADD CL, CH

MOV AL, CL



MUL BL



ret




