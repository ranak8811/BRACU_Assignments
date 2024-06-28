data segment
    ; add your data here!
    msg1 db "It is divisible by 5 and 11$"
    msg2 db "It is not divisible by 5 and 11$"
ends

stack segment
    dw   128  dup(0)
ends

code segment
start:
; set segment registers:
    mov ax, data
    mov ds, ax
    mov es, ax

    ; add your code here
    mov cx , 55
    mov bh , 5
    mov bl , 11
    
    mov ax , cx
    div bh
    cmp ah , 0
    je check11
    jmp noPrint
    
    check11:
        mov ax , cx
        div bl
        cmp ah , 0
        je print
        jmp noPrint
        
    print:
        
        lea dx, msg1
        mov ah, 9
        int 21h
        jmp exit 
        
    noPrint:
        lea dx, msg2
        mov ah, 9
        int 21h
        jmp exit
        
    exit:
    
    
ends

end start ; set entry point and stop the assembler.