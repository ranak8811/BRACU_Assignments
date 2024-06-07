.MODEL SMALL

.STACK 100H

.DATA

A DW 5
B DW 3

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
               
    MOV AX, A
    MOV BX, B
               
    ADD AX, BX
    SUB BX, AX
    ADD AX, BX
    NEG BX




