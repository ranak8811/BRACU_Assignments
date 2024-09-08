.model small
.stack 100h 
.data
msg         db 10, 13, "Enter your name $ "
bufferSize  db 21  ; 20 char + RETURN
inputLength db 0   ; number of read characters
buffer      db 21 DUP("$") ; actual buffer

.code
main proc

mov ax, @data
mov ds, ax
lea dx, msg
mov ah, 09h ;output
int 21h

mov dx, offset bufferSize ; load our pointer to the beginning of the structure
mov ah, 10 ; GetLine function
int 21h

mov ax, @data 
mov ds , ax 
lea dx, buffer
mov ah, 09 ;output
int 21h

endp
end main   
