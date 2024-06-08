
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h  

.DATA

A DB "Please insert a character: $"
     
.CODE

LEA DX, A
MOV AH, 9
INT 21H
      
;INPUT THE 1ST NUMBER
MOV AH, 1
INT 21H
MOV BL, AL

;INPUT THE 2ND NUMBER
MOV AH, 1
INT 21H
MOV CL, AL
          

ADD BL, CL

;NEW LINE
MOV DL, 0DH
MOV AH, 2
INT 21H

;CARRIAGE RETRUN
MOV DL, 0AH
MOV AH, 2
INT 21H

SUB BL, 48

MOV DL, BL
MOV AH, 2
INT 21H

ret




