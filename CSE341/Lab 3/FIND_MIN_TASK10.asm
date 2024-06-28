ORG 100H

.DATA

.CODE

MOV AH, 1         ; Read first number
INT 21H
MOV BL, AL        ; Store it in BL
INT 21H           ; Read second number
MOV BH, AL        ; Store it in BH
INT 21H           ; Read third number
MOV CL, AL        ; Store it in CL

CMP BL, BH        ; Compare BL with BH
JLE A             ; If BL <= BH, jump to A

B:
CMP BH, CL        ; Compare BH with CL
JLE C             ; If BH <= CL, jump to C
MOV AH, 2
MOV DL, CL        ; Otherwise, CL is the smallest
INT 21H
JMP END

C:
MOV AH, 2
MOV DL, BH        ; BH is the smallest
INT 21H
JMP END

A:
CMP BL, CL        ; Compare BL with CL
JLE D             ; If BL <= CL, jump to D
MOV AH, 2
MOV DL, CL        ; Otherwise, CL is the smallest
INT 21H
JMP END

D:
MOV AH, 2
MOV DL, BL        ; BL is the smallest
INT 21H

END:
RET
