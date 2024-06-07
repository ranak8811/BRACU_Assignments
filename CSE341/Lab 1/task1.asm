.MODEL SMALL

.STACK 100H

.DATA

A DW 5
B DW 0

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
               
    mov AX, A           
    MOV BX, AX




