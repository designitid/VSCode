org 00H
		
toggle: MOV P1, #01H
        CPL A
        MOV P1, A
        JMP toggle

end		