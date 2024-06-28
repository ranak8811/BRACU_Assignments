org 100h

.DATA

MSG1 DB 'Character in AL comes first: $'
MSG2 DB 'Character in BL comes first: $'
CHAR DB 0

.CODE

start:
    ; Load AL and BL with example extended ASCII characters
    MOV AL, 0C0h ; Example character (À)
    MOV BL, 0B5h ; Example character (µ)

    ; Compare AL and BL
    CMP AL, BL
    JL AL_First ; Jump if AL < BL

    ; If we are here, BL is less than or equal to AL
    MOV CHAR, BL
    LEA DX, MSG2
    JMP Print_Result

AL_First:
    ; If we are here, AL is less than BL
    MOV CHAR, AL
    LEA DX, MSG1

Print_Result:
    ; Print the appropriate message
    MOV AH, 9
    INT 21h

    ; Print the character that comes first
    MOV DL, CHAR
    MOV AH, 2
    INT 21h

    ; Exit the program
    MOV AH, 4Ch
    INT 21h

ret

END start




