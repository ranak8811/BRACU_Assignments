
; You may customize this and other start-up templates; 
; The location of this template is c:\emu8086\inc\0_com_template.txt

org 100h

.DATA
s db '**********',0DH,0AH,'$'

.CODE
    mov ax, @data
    mov ds, ax
    mov es, ax

    ; add your code here 
    
    lea dx, s
    mov ah, 9
    
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h
    int 21h

ret




