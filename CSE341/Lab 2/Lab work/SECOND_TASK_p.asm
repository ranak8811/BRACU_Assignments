
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA
A DW "Please insert a character: $"
B DW "Please insert another character: $"
C DW "HERE IS THE SUMMATION OF THOSE TWO NUMBERS: $"

.CODE
    
    MOV AX, @DATA
    MOV DS, AX
    
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
    
    MOV AH, 1
    INT 21H
    MOV CL, AL
    
    MOV AH, 2
    MOV DL, 0AH
    INT 21H
    
    MOV AH, 2
    MOV DL, 0DH
    INT 21H
    
    
    MOV AH, 9
    LEA DX, C
    INT 21H
    
    ADD BL, CL
    SUB BL, 48
    
    
    MOV AH, 2
    MOV DL, BL
    INT 21H
    
    


ret




