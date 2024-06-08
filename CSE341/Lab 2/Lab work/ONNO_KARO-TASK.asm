.model small
.stack 100h

.data
    a db "Enter the first number: $"
    b db "And the second number: $"
    msg db "th alphabet of the English language is: $"
    msg_char db 0

.code
main proc
    mov ax, @data
    mov ds, ax

    mov ah, 9
    lea dx, a
    int 21h

   
    mov ah, 1
    int 21h
    sub al, '0'
    mov bl, al   
    
    mov ah, 2
    mov dl, 10
    int 21h
    mov dl, 13
    int 21h

 
    mov ah, 9
    lea dx, b
    int 21h

   
    mov ah, 1
    int 21h
    sub al, '0'
    mul bl  
    add al, 'A' 
    mov msg_char, al
    
    mov ah, 2
    mov dl, 10
    int 21h
    mov dl, 13
    int 21h

    
    mov ah, 9
    lea dx, msg
    int 21h

    
    mov ah, 2
    mov dl, msg_char
    int 21h

    exit:
    main endp
end main



