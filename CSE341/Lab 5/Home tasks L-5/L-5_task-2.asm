.MODEL SMALL
.STACK 100H

.DATA
    arr DB 5 DUP(?)         
    msg1 DB 'Enter 5 Numbers (single digits) in Array:$'
    msg2 DB 'After Sorting Array:$'
    newline DB 0AH, 0DH, '$'

.CODE
MAIN PROC
    MOV AX, @DATA            
    MOV DS, AX

    LEA DX, msg1
    MOV AH, 9
    INT 21H

    MOV CX, 5
    MOV BX, OFFSET arr
    MOV AH, 1

INPUTS:
    INT 21H                  
    SUB AL, '0'              
    MOV [BX], AL             
    INC BX                   
    LOOP INPUTS              

    MOV CX, 5                
    DEC CX                   

OUTER_LOOP:
    MOV BX, CX
    MOV SI, 0

COMP_LOOP:
    MOV AL, arr[SI]          
    MOV DL, arr[SI+1]        

    CMP AL, DL               
    JBE NO_SWAP              

    MOV arr[SI], DL          
    MOV arr[SI+1], AL        

NO_SWAP:
    INC SI                   
    DEC BX                   
    JNZ COMP_LOOP            

    DEC CX                   
    JNZ OUTER_LOOP           

    MOV AH, 2
    MOV DL, 0AH
    INT 21H
    MOV DL, 0DH
    INT 21H

    LEA DX, msg2
    MOV AH, 9
    INT 21H

    MOV CX, 5
    MOV BX, OFFSET arr

OUTPUTS:
    MOV DL, [BX]             
    ADD DL, '0'              
    MOV AH, 2                
    INT 21H                  

    MOV DL, 32               
    MOV AH, 2
    INT 21H

    INC BX                   
    LOOP OUTPUTS             

    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN
