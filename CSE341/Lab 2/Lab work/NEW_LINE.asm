
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

MOV AH, 1
INT 21H
MOV BL, AL
         
MOV DL, 0AH
MOV AH, 2
INT 21H

MOV DL, 0DH
MOV AH, 2
INT 21H         
                  
MOV DL, BL
MOV AH, 2         
INT 21H



ret




