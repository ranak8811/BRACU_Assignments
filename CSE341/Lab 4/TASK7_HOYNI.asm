ORG 100h

.DATA
buffer DB 255  ; Buffer size (max length of input)
       DB ?    ; Actual number of characters read (excluding carriage return)
       DB 255 DUP(?) ; Space for the characters

.CODE

MOV CL, 0
MOV CH, 0
MOV DL, 0
MOV DH, 0

CHECK:
MOV AH, 1
INT 21H

MOV BL, AL
CMP CL, CH
JE PUT

PUT:
MOV DH, DL  

MOV AH, 2
MOV DL, BL
INT 21H

MOV AH, 0Ah

   
MOV DX, OFFSET buffer 
INT 21h        


RET
