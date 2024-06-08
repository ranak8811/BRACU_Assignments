
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.CODE

    MOV AH, 1
    INT 21H
    MOV BL, AL
    
    MOV AH, 2
    MOV DL, 0AH
    INT 21H
    MOV AH, 2
    MOV DL, 0DH
    INT 21H
             
    ADD BL, 32
    
    MOV AH, 2
    MOV DL, BL
    INT 21H

ret




