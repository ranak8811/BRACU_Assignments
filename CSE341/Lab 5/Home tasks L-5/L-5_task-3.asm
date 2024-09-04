.MODEL SMALL
.STACK 100H

.DATA

.CODE
MAIN PROC    
    MOV AH, 1
    INT 21H
    MOV BL, AL
    INT 21H
    MOV BH, AL
    INT 21H
    MOV CL, AL
    
    CMP BL, BH
    JGE A

B:
    CMP BH, CL
    JGE C
    CALL new_line
    MOV DL, CL
    INT 21H
    JMP END
    
C:
    CALL new_line
    MOV DL, BH
    INT 21H
    JMP END
    
A:
    CMP BL, CL
    JGE D
    CALL new_line
    MOV DL, CL
    INT 21H
    JMP END
    
D:
    CALL new_line
    MOV DL, BL
    INT 21H
    
END:
    MOV AH, 4CH
    INT 21H

new_line:
    MOV AH, 2
    MOV DL, 0AH
    INT 21H
    MOV DL, 0DH
    INT 21H
    RET
    
MAIN ENDP
END MAIN
