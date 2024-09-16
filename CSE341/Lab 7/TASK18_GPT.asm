.MODEL SMALL
.STACK 100H

.DATA
array DB 5, 10, 15, 20, 25    ; Array of 5 elements
msg_found DB 'Value found!$'   ; Message if value is found
msg_not_found DB 'Value not found.$' ; Message if value is not found
newline DB 0AH, 0DH, '$'       ; Newline for formatting
search_value DB 18             ; Value to search for (change this to test different values)

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    ; Call the procedure to search the array
    MOV AL, search_value       ; Load the value to search in AL
    CALL SEARCH_ARRAY          ; Call the search procedure

    ; Check the result (AX = 1 if found, AX = 0 if not found)
    CMP AX, 1
    JE FOUND_VALUE             ; If found, jump to print "found" message
    JMP NOT_FOUND_VALUE        ; Otherwise, jump to print "not found" message

FOUND_VALUE:
    LEA DX, msg_found          ; Load "Value found!" message
    MOV AH, 9                  ; DOS interrupt to print string
    INT 21H
    JMP FINISH                 ; Go to finish after printing message

NOT_FOUND_VALUE:
    LEA DX, msg_not_found      ; Load "Value not found." message
    MOV AH, 9                  ; DOS interrupt to print string
    INT 21H

FINISH:
    ; Print a newline for formatting
    LEA DX, newline
    MOV AH, 9
    INT 21H

    ; Exit the program
    MOV AH, 4CH
    INT 21H

MAIN ENDP


; Procedure to search the array
; Input: AL = value to search
; Output: AX = 1 if found, AX = 0 if not found
SEARCH_ARRAY PROC
    MOV SI, OFFSET array       ; SI points to the start of the array
    MOV CX, 5                  ; CX = 5 (number of elements in the array)

SEARCH_LOOP:
    CMP AL, [SI]               ; Compare the search value in AL with the current array element
    JE VALUE_FOUND             ; If equal, jump to "VALUE_FOUND"

    INC SI                     ; Move to the next element in the array
    DEC CX                     ; Decrement the counter
    JNZ SEARCH_LOOP            ; Repeat if more elements to check

    ; Value not found
    MOV AX, 0                  ; AX = 0 (value not found)
    RET

VALUE_FOUND:
    MOV AX, 1                  ; AX = 1 (value found)
    RET
SEARCH_ARRAY ENDP

END MAIN
