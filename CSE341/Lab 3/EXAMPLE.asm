data segment
; add your data here!
pkey db "press any key...$"
a db "Enter first number$"
b db "Enter second number$"
c db " is larger$"
ends
stack segment
dw 128 dup(0)
ends
code segment
start:
; set segment registers:
mov ax, data
mov ds, ax
mov es, ax
; add your code here
lea dx, a ;Print a
mov ah,9
int 21h
mov ah,1
int 21h
mov bl,al ;move input to bl
lea dx, b ;Print b
mov ah,9
int 21h
mov ah,1
int 21h
mov cl,al ;move input to cl
cmp cl,bl ;compare the two inputs
jg line1
mov dl,bl
mov ah,2
int 21h

lea dx, c
mov ah,9
int 21h
jmp e
line1:
mov dl,cl
mov ah,2
int 21h
lea dx, c
mov ah,9
int 21h
e:
lea dx, pkey
mov ah, 9
int 21h ;output string at ds:dx
;wait for any key....
mov ah, 1
int 21h
mov ax, 4c00h ;exit to operating system.
int 21h
ends
end start ; set entry point and stop the assembler.




