ORG 100H

.DATA
validMsg DB 'Y$', 0
invalidMsg DB 'N$', 0

.CODE

start:
    ; Read first side
    MOV AH, 1
    INT 21H
    SUB AL, '0'   ; Convert ASCII to integer
    MOV BL, AL    ; Store it in BL

    ; Read second side
    MOV AH, 1
    INT 21H
    SUB AL, '0'   ; Convert ASCII to integer
    MOV BH, AL    ; Store it in BH

    ; Read third side
    MOV AH, 1
    INT 21H
    SUB AL, '0'   ; Convert ASCII to integer
    MOV CL, AL    ; Store it in CL

    ; Check if BL + BH > CL
    MOV AL, BL
    ADD AL, BH
    CMP AL, CL
    JLE NotValid

    ; Check if BL + CL > BH
    MOV AL, BL
    ADD AL, CL
    CMP AL, BH
    JLE NotValid

    ; Check if BH + CL > BL
    MOV AL, BH
    ADD AL, CL
    CMP AL, BL
    JLE NotValid

    ; If all checks passed, the triangle is valid
    LEA DX, validMsg
    JMP Print

NotValid:
    LEA DX, invalidMsg

Print:
    MOV AH, 9
    INT 21H

    ; Exit program
    MOV AX, 4C00H
    INT 21H

END start
