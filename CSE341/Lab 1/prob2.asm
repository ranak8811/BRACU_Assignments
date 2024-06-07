.MODEL SMALL

.STACK 100H

.DATA

A DW 36DFh   ; Use 'h' to indicate that the value is hexadecimal
B DW 0AFh    ; Use 'h' to indicate that the value is hexadecimal

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
               
    MOV AX, A             
    MOV BX, B
  
    MUL BX       ; Multiply AX by BX (result in DX:AX)

    ; If you want to store the result in AX:
    ; MOV AX, DX

    MOV AH, 4CH
    INT 21H     
    
    MAIN ENDP 

END MAIN
