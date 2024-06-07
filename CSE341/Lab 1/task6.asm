.MODEL SMALL

.STACK 100H

.DATA

A DW 5
B DW 3
               ;A = B - (A - 1); use dec
.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
               
    MOV AX, A
    MOV BX, B
               
    DEC AX
    SUB BX, AX
    MOV A, BX


