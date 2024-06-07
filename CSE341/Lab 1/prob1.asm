.MODEL SMALL

.STACK 100H

.DATA

A DB 5
B DB 3
               ; How to show value/output in the terminal❓
.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
               
    MOV AL, A    ; Move the value of A (byte) into AL (8-bit register)
    MOV BL, B    ; Move the value of B (byte) into BL (8-bit register)
               
    ADD AX, BX   ; Add the values of A and B
       
    MOV AH, 2    ; Function code for printing character
    MOV DL, 10   ; ASCII code for line feed (new line)
    INT 21H      ; DOS interrupt to print character
    MOV DL, 13   ; ASCII code for carriage return
    INT 21H      ; DOS interrupt to print character
             
             
    MOV AH, 2    ; Function code for printing character
    MOV DL, AL   ; Move the value in AL (result) into DL
    INT 21H      ; DOS interrupt to print character
    
    ; Terminate the program
    MOV AH, 4CH  ; Function code for program termination
    INT 21H      ; DOS interrupt to terminate program
    
MAIN ENDP
END MAIN
