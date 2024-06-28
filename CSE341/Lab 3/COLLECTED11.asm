.MODEL SMALL
 
.STACK 100H

.DATA 

;Triangle checker 

X DB "1st side: $ "
Y DB "2nd side: $ "
Z DB "3rd side: $ "
D DB "Y$"
E DB "N$" 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here 

MOV AH,9
LEA DX,x
INT 21h
 
MOV AH,1
INT 21h
MOV BH,AL
SUB BH,30h 
 
MOV AH,2     
MOV DL,0DH
INT 21h
MOV DL,0AH
INT 21h 
 
MOV AH,9
LEA DX,y
INT 21h
 
MOV AH,1
INT 21h
MOV BL,AL
SUB BL,30h  
 
MOV AH,2      
MOV DL,0DH
INT 21h
MOV DL,0AH
INT 21h
 
MOV AH,9
LEA DX,z
INT 21h
 
MOV AH,1
INT 21h
MOV CL,AL
SUB CL,30h 
 
MOV AH,2     
MOV DL,0DH
INT 21h
MOV DL,0AH
INT 21h 

MOV AL,BH
ADD AL,BL
CMP AL,CL
JLE L1
 
ADD BH,CL
CMP BH,BL
JLE L1
 
ADD BL,CL
CMP BL,BH
JLE L1
  
L2:
MOV AH,9
LEA DX,D
INT 21h 

JMP EXIT
 
L1:
MOV AH,9
LEA DX,E
INT 21h 
  
EXIT:    
;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  