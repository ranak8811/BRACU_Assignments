.MODEL SMALL

PRINT MACRO M1
    LEA DX, M1         
    MOV AH, 9          
    INT 21H            
ENDM

.STACK 100H
.DATA
A DB 'AMI BARI JABO $'        

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX         

    PRINT A           

    MOV AH, 4CH       
    INT 21H

MAIN ENDP
END MAIN