.model small
.stack 100h

.data
    
    stars   db '*******************************', 13, 10, '$'
    newline db 13, 10, '$'
    
    
    p_name  db 'Name: $'
    p_fname db 'Father Name: $'
    p_roll  db 'Roll No: $'
    p_inst  db 'Institute Name: $'

    
    b_name  db 30, ?, 30 dup('$')
    b_fname db 30, ?, 30 dup('$')
    b_roll  db 30, ?, 30 dup('$')
    b_inst  db 30, ?, 30 dup('$')

.code
main proc
    
    mov ax, @data
    mov ds, ax

    
    mov ah, 09h
    lea dx, stars
    int 21h

    
    mov ah, 09h
    lea dx, p_name
    int 21h
    
    mov ah, 0Ah         
    lea dx, b_name
    int 21h
    
    mov ah, 09h         
    lea dx, newline
    int 21h

    
    mov ah, 09h
    lea dx, p_fname
    int 21h
    
    mov ah, 0Ah
    lea dx, b_fname
    int 21h
    
    mov ah, 09h
    lea dx, newline
    int 21h

    ; 3. Print Roll No prompt and take input
    mov ah, 09h
    lea dx, p_roll
    int 21h
    
    mov ah, 0Ah
    lea dx, b_roll
    int 21h
    
    mov ah, 09h
    lea dx, newline
    int 21h

    
    mov ah, 09h
    lea dx, p_inst
    int 21h
    
    mov ah, 0Ah
    lea dx, b_inst
    int 21h
    
    mov ah, 09h
    lea dx, newline
    int 21h

    
    mov ah, 09h
    lea dx, stars
    int 21h

    
    mov ah, 4Ch
    int 21h
main endp
end main