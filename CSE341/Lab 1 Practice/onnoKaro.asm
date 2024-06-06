.MODEL SMALL
.STACK 100H
.DATA                       
    ; DEFINE YOUR VARIABLES 
    ; The .data section is where you define and allocate memory for
    ; your program's data variables. This section typically contains 
    ; declarations for variables, constants, and strings that your program uses.
    
    A dw ?
    initial dw 5A3h
   
    
    
.CODE  
    ; The .code section is where you place your program's executable 
    ; instructions or code. It contains the actual assembly language
    ; instructions that perform tasks and computations.

    MAIN PROC
        
        MOV AX, @DATA
        MOV DS, AX
        
        ; YOUR CODE STARTS HERE 
        
        MOV AX, initial
        inc AX;
        
        
        MOV BX, 05ABh
        mul, BX;   
        

        
        ; YOUR CODE ENDS HERE   
        
        MOV AX, 4C00H
        INT 21H 
        
        
        
    MAIN ENDP
    END MAIN 