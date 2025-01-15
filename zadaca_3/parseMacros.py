def _parse_macros(self):
    self._iter_lines(self._parce_macro)

def _mv(self, A, B):
    z = ["@"+A, "D=M", "@"+B, "M=D"]
    return z

def _swp(self, A, B):
    z = ["@temp", "M=0", "@"+A, "D=M", "@temp", "M=D", "@"+B, "D=M", "@"+A, "M=D", "@temp", "D=M", "@"+B, "M=D"]
    return z

def _add(self, A, B, D):
    z = ["@"+A, "D=M", "@"+B, "D=M+D", "@"+D, "M=D"]
    return z

def _while(self, A):
    self._cnt += 1
    z = ["(WHILE" + str(self._cnt) + ")", "@"+A, "D=M", "@END" + str(self._cnt), "D;JEQ"]
    return z

def _parse_macro(self, line, p, o):
    if line[0] == "$":
        lines = line[1:].split("(")
        macro = lines[0]
        if len(lines) > 1:
            arguments = lines[1]
            arguments_lista = arguments.replace(")", "".split(","))
			
            if macro == "MV":
                z = self._mv()
                return z
				
            elif macro == "SWP":
                z = self._swp
                return z
				
            elif macro == "ADD":
                z = self._add
                return z
				
            elif macro == "WHILE":
                z = self._while(arguments_lista[0])
                return z
				
            else:
                self._flag = False
                self._line = o
                self._errm = "Invalid macro"
            
    else:
        return z