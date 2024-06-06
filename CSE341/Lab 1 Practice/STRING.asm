.MODEL SMALL
.STACK 100H

.DATA
A DB 'BANGLADESH IS MY COUNTRY$'

.CODE 

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    
    EXIT:
    MOV AH, 4CH
    INT 21H
    MAIN ENDP
END MAIN


                                                         