.MODEL SMALL

.STACK 100H

.DATA

A DW 5
B DW 7

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
               
    MOV AX, A
    MOV BX, B
               
    SUB AX, BX




