.MODEL SMALL

.STACK 100H

.DATA

A DW 5
B DW 7
C DW 0

.CODE

MAIN PROC
    MOV AX, @DATA
    MOV DS, AX
               
    MOV AX, A
    MOV BX, B
               
    MOV CX, AX
    MOV AX, BX
    MOV BX, CX




