import os

class Lexer:     
    def __init__(self, name_file):
        self.name_file= name_file

        # Tokens
        self.t_delim= 'delim'
        self.t_opArit= 'opArit'
        self.t_opRel= 'opRel'
        self.t_opLog= 'opLog'
        self.t_palRes= 'palRes'
        self.t_opAsig= 'opAsig'
        self.delim= {'.': self.t_delim, ',': self.t_delim, ';': self.t_delim, '(': self.t_delim, ')': self.t_delim, '[': self.t_delim, ']': self.t_delim, ':': self.t_delim, '<nl>': self.t_delim, '<tab>': self.t_delim} # This are the delimiter
        self.opArit= {'+': self.t_opArit, '-': self.t_opArit, '*': self.t_opArit, '/': self.t_opArit, '%': self.t_opArit, '^': self.t_opArit} # These are arithmetic operators
        self.opRel={'=': self.t_opRel, '<>': self.t_opRel, '<': self.t_opRel, '>': self.t_opRel, '<=': self.t_opRel, '>=': self.t_opRel} # These are relational operators
        self.opLog= {'y': self.t_opLog, 'o': self.t_opLog, 'no': self.t_opLog} # These are logical operators
        self.palRes= {'constantes': self.t_palRes, 
                       'variables': self.t_palRes, 
                       'real': self.t_palRes, 
                       'alfabetico': self.t_palRes, 
                       'logico': self.t_palRes, 
                       'entero': self.t_palRes, 
                       'funcion': self.t_palRes, 
                       'inicio': self.t_palRes, 
                       'fin': self.t_palRes, 
                       'de': self.t_palRes, 
                       'procedimiento': self.t_palRes, 
                       'regresa': self.t_palRes, 
                       'si': self.t_palRes, 
                       'hacer': self.t_palRes, 
                       'sino': self.t_palRes, 
                       'cuando': self.t_palRes, 
                       'el': self.t_palRes, 
                       'valor': self.t_palRes, 
                       'sea': self.t_palRes, 
                       'otro': self.t_palRes, 
                       'desde': self.t_palRes, 
                       'hasta': self.t_palRes, 
                       'incr': self.t_palRes, 
                       'decr': self.t_palRes, 
                       'repetir': self.t_palRes, 
                       'que': self.t_palRes, 
                       'mientras': self.t_palRes, 
                       'se': self.t_palRes, 
                       'cumpla': self.t_palRes, 
                       'continua': self.t_palRes, 
                       'interrumpe': self.t_palRes, 
                       'limpia': self.t_palRes, 
                       'lee': self.t_palRes, 
                       'imprime': self.t_palRes, 
                       'imprimenl': self.t_palRes, 
                       'verdadero': self.t_palRes, 
                       'falso': self.t_palRes} # These are reserved words
        self.opAsig= {':=': self.t_opAsig} # This is the assignation operator

    def pass_lex(self, program):
        lexs= []
        tokens= []
        #cont= 0
        for line in program:
            line= line.split(" ")
            for word in line:
                #print(str(cont) + ": " + word + "\n")
                #cont+= 1
                if word in self.delim:
                    lexs.append(word)
                    tokens.append(self.delim[word])
                elif word in self.opArit: 
                    lexs.append(word)
                    tokens.append(self.opArit[word])
                elif word in self.opRel: 
                    lexs.append(word)
                    tokens.append(self.opRel[word])
                elif word in self.opLog: 
                    lexs.append(word)
                    tokens.append(self.opLog[word])
                elif word in self.palRes: 
                    lexs.append(word)
                    tokens.append(self.palRes[word])
                elif word in self.opAsig: 
                    lexs.append(word)
                    tokens.append(self.opAsig[word])
        self.create_file(lexs, tokens)

    def create_file(self, lexers, tokens):
        #print(lexers)
        #print(tokens)
        os.remove("./" + self.name_file)
        space_words= 38
        with open(self.name_file, "w") as f:
            f.write('--------------------------------------------\n')
            f.write('Lexema                                Token\n')
            f.write('--------------------------------------------\n')
            for i in range(len(lexers)):
                space= 0
                for letter in lexers[i]:
                    space+= 1
                f.write(lexers[i])
                while(space < space_words):
                    f.write(' ')
                    #print(space)
                    space+= 1
                f.write(tokens[i] + '\n') 

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def identifyNumbers(self):      
        numbers = []
        for char in self:
            if(char.split(';')): identifier= char.split(';')
            identifier= identifier[0].split(" ")
            for i in identifier:
                if i.isdigit() or Compiler.isfloat(self, i):
                    numbers.append(i)
                    continue
        return numbers
    
    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
        
    def val_const(self, line, asig):
        #line= self.code[0]
        
        line_split= line.split(" ")
        line_split.pop(0)
        line_split= " ".join(line_split)
        word= line_split.split(asig)
        if(len(word) > 1):
            lexema= [asig, "<Ident>"]
            self.lexemas.append(lexema)
        else:
            error= [self.line, asig, "<lexico> Se esperaba "+asig, line]
            self.errores.append(error)                          
        return self.errores
    
    def val_var(self):
        return 'variable'
    
    def val_real(self):
        return 'real'
    
    def val_alf(self):
        return 'alfabetico'
    
    def val_log(self):
        return 'logico'
    
    def val_ent(self):
        return 'entero'
    
    def val_fun(self):
        return 'funcion'
    
    def val_ini(self):
        return 'inicia'
    
    def val_fin(self):
        return 'fin'
    
    def val_de(self):
        return 'de'
    
    def val_proc(self):
        return 'procedimiento'
    
    def val_reg(self):
        return 'regresa'
    
    def val_si(self):
        return 0
    
    def val_hacer(self):
        return 0
    
    def val_sino(self):
        return 0
    
    def val_cuando(self):
        return 0
    
    def val_el(self):
        return 0
    
    def val_valor(self):
        return 0
    
    def val_sea(self):
        return 0
    
    def val_otro(self):
        return 0
    
    def val_desde(self):
        return 0
    
    def val_hasta(self):
        return 0
    
    def val_incr(self):
        return 0
    
    def val_decr(self):
        return 0
    
    def val_rep(self):
        return 0
    
    def val_que(self):
        return 0
    
    def val_mien(self):
        return 0
    
    def val_se(self):
        return 0
    
    def val_cum(self):
        return 0
    
    def val_cont(self):
        return 0
    
    def val_inte(self):
        return 0
    
    def val_limpia(self):
        return 0
    
    def val_lee(self):
        return 0
    
    def val_imprime(self):
        return 0
    
    def val_imprimenl(self):
        return 0
    
    def val_verdadero(self):
        return 0
    
    def val_falso(self):
        return 0
    '''
    def identifyComments(self):
        comments= []
        for char in self:
            id_comment= []
            if("//" in  char):
                comment_init= char.find('//')
                id_comment.append(char[comment_init:])
            id_comment= " ".join(id_comment)
            comments.append(id_comment)
        for i in range(len(comments)):
            for i in comments:
                if(i == ''): comments.remove(i)
        return comments
    '''

    def identifyVariables(self):
        variables= []
        variables_res= ['real', 'alfabetico', 'logico', 'entero']
        for char in self:
            var= char.split(' ')
            if(var[0] == 'constantes' or var[0] == 'variables'):
                for i in variables_res:
                    if(i == var[1]):
                        if(var[2] == ':='):
                            if(var[1] == 'entero'):
                                number= var[3].split(';')
                                number= number[0]
                                semicolon= var[3].split('\n')
                                semicolon= semicolon[0]
                                if(number.isdigit()):
                                    if(semicolon[-1] == ';'):
                                        variables.append(var[0] + " " +var[1])
                                else: 
                                    continue
                            elif(var[1] == 'real'):
                                number= var[3].split(';')
                                number= number[0]
                                semicolon= var[3].split('\n')
                                semicolon= semicolon[0]
                                if(Compiler.isfloat(self, number)):
                                    if(semicolon[-1] == ';'):
                                        variables.append(var[0] + " " +var[1])
                                else: 
                                    continue
                            elif(var[1] == 'alfabetico'):
                                alfa= var[3].split(';')
                                alfa= alfa[0]
                                alfa_init= alfa[0]
                                alfa_end= alfa[-1]
                                semicolon= var[3].split('\n')
                                semicolon= semicolon[0]
                                if(alfa_init == '"' and alfa_end == '"'):
                                    if(semicolon[-1] == ';'):
                                        variables.append(var[0] + " " +var[1])
                                else: 
                                    continue
                            elif(var[1] == 'logico'):
                                logic= var[3].split(';')
                                logic= logic[0]
                                semicolon= var[3].split('\n')
                                semicolon= semicolon[0]
                                if(logic == 'verdadero' or logic == 'falso'):
                                    if(semicolon[-1] == ';'):
                                        variables.append(var[0] + " " +var[1])
                                else: 
                                    continue
        return variables