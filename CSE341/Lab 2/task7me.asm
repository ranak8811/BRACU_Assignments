
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA
A DB 'ENTER A HEX DIGIT: $'
B DB 'IN DECIMAL IT IS 1$'

.CODE
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 1
    INT 21H
    MOV BL, AL
    
    MOV AH, 2
    MOV DL, 0AH
    INT 21H
    
    MOV AH, 2
    MOV DL, 0DH
    INT 21H
    
    MOV AH, 9
    LEA DX, B
    INT 21H
    
    SUB BL, 17
    
    MOV AH, 2
    MOV DL, BL
    INT 21H

ret




