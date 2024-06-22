
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

.MODEL SMALL
.STACK 100H
   

.DATA
MSG1 DB 'LARGER$'
MSG2 DB 'SMALLER$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AL, 3
    MOV BL, 5
    
    CMP AL, BL
    JG PRINT_LARGE
    
    LEA DX, MSG2
    MOV AH, 09H
    INT 21H
    
    PRINT_LARGE:
    
    LEA DX, MSG1
    MOV AH, 09H
    INT 21H
    
    MOV AX, 4C00H
    INT 21H
    
    MAIN ENDP
END MAIN
    


; add your code here

ret




