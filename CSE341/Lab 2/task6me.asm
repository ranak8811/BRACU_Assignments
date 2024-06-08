org 100h

.DATA

A DB 'ENTER THREE INITIALS: $'
NewLine DB 0AH, 0DH, '$'


.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AH, 9
    LEA DX, A
    INT 21H
    
    MOV AH, 1
    INT 21H
    MOV BL, AL
    
    MOV AH, 1
    INT 21H
    MOV BH, AL
    
    MOV AH, 1
    INT 21H
    MOV CL, AL
    
    MOV AH, 9
    LEA DX, NewLine
    INT 21H
    
    MOV AH, 2
    LEA DL, BL
    INT 21H
    
    MOV AH, 9
    LEA DX, NewLine
    INT 21H
    
    MOV AH, 2
    MOV DL, BH
    INT 21H   
    
    MOV AH, 9
    LEA DX, NewLine
    INT 21H
    
    MOV AH, 2
    MOV DL, CL
    INT 21H

    EXIT:
    MOV AH, 4CH
    INT 21H
    MAIN ENDP
END MAIN





