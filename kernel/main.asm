;RST 0
.org 0h
jmp start

;RST 1
.org 8h
ret

;RST 2
.org 10h
ret

;RST 3
.org 18h
ret

;RST 4
.org 20h
ret

;RST 5
.org 28h
ret

;RST 6
.org 30h
ret

;RST 7
org 38h
ret

start:
    hlt