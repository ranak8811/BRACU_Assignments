.MODEL SMALL

.STACK 100H

.DATA


.CODE
                 ;(1 + 2) * (3 - 1) / 5 + 3 + 2 - (1 * 2)

                 ; aitar jhamela ase❓
MAIN PROC
    
  MOV AX, @DATA
  MOV DS, AX
  
  
  MOV AX, 1
  MOV BX, 2
  ADD AX, BX
  
  MOV BX, 3
  MOV CX, 1
  SUB BX, CX
  
  MUL BX
  
  MOV CX, 5
  DIV CX
  
  MOV BX, 3
  ADD AX, BX

  ; Rest of your code (optional)

    MOV AX, 4C00H    ; Terminate the program
    INT 21H          ; DOS interrupt to exit program
MAIN ENDP

END MAIN


