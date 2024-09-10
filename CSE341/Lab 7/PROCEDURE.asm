ORG 100H
.DATA

A DB "AX REG BORO $" 
B DB "BX REG BORO $"
C DB "RETURN KORSE $"

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
    
    
    MOV AX, 2
    MOV BX, 3
    
    CALL MAXIMUM
    
    LEA DX, C
    MOV AH, 9
    INT 21H
    
    JMP FINAL_EXIT
    
    MAXIMUM PROC
        
        CMP AX, BX
        JG A_BORO
        
        LEA DX, B
        MOV AH, 9
        INT 21H
        
        JMP EXIT
        
        
        A_BORO:
        LEA DX, A
        MOV AH, 9
        INT 21H
        EXIT:
        
        
        RET
    MAXIMUM ENDP 
    
    FINAL_EXIT:
    MOV AH, 4CH
    INT 21H
END