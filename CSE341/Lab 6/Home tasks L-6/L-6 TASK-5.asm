.MODEL SMALL
.STACK 100H

.DATA
    input_buffer DB 255
    input_length DB ?
    input_string DB 255 DUP('$')
    output_string DB 255 DUP('$')
    space DB ' '
    newline DB 0DH, 0AH, '$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    LEA DX, input_buffer
    MOV AH, 0AH
    INT 21H

    LEA SI, input_buffer+2
    LEA DI, output_string

    MOV CX, 0

process_input:
    MOV AL, [SI]
    CMP AL, 0DH
    JE finish_word

    CMP AL, ' '
    JE reverse_word

    PUSH AX
    INC CX
    INC SI
    JMP process_input

reverse_word:
reverse_loop:
    CMP CX, 0
    JE add_space

    POP AX
    MOV [DI], AL
    INC DI
    DEC CX
    JMP reverse_loop

add_space:
    MOV AL, space
    MOV [DI], AL
    INC DI
    INC SI
    JMP process_input

finish_word:
reverse_last_word:
    CMP CX, 0
    JE end_program

    POP AX
    MOV [DI], AL
    INC DI
    DEC CX
    JMP reverse_last_word

end_program:
    LEA DX, newline
    MOV AH, 09H
    INT 21H

    MOV AL, '$'
    MOV [DI], AL

    LEA DX, output_string
    MOV AH, 09H
    INT 21H

    LEA DX, newline
    MOV AH, 09H
    INT 21H

    MOV AH, 4CH
    INT 21H

MAIN ENDP
END MAIN
