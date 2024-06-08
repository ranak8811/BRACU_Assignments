
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA
A DB '**********$'
NL DB 0AH, 0DH, '$'

.CODE


    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 9
    LEA DX, NL
    INT 21H
    
    

ret




