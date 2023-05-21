import os

class Lexer:     
    def __init__(self, name_file):
        self.name_file= name_file # This is the file with the code to analize

        # Tokens
        self.t_delim= 'delim'
        self.t_opArit= 'opArit'
        self.t_opRel= 'opRel'
        self.t_opLog= 'opLog'
        self.t_palRes= 'palRes'
        self.t_opAsig= 'opAsig'
        self.t_cteReal= 'CteReal'
        self.t_cteEnt= 'CteEnt'
        self.t_ident= 'Ident'
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
        self.nums= '1234567890' # This are valid numbers
        self.ctes= {'CteEnt': self.t_cteEnt, 'CteReal': self.t_cteReal}

    def pass_lex(self, program):
        prev_word= ''
        lexs= []
        tokens= []
        for line in program:
            line= line.split(" ")
            if line[0] in self.palRes:
                prev_word= line[0]
            #print(line[0])
            #print(line[0])
            for word in line:
                n= word.split("\t")
                if(len(n)>1):
                    for w in n:
                        if w != '':
                            word= w
                word= word.lower()
                if word == "":
                    continue
                elif word in self.delim:
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
                else:
                    valid, parms= self.checkChar(word, prev_word)
                    if valid: 
                        if prev_word == 'constantes':
                            for parm in parms:
                                first_ch= list(parm)[0]
                                if first_ch in self.nums: lexs.append(parm)
                                elif parm == self.t_cteEnt or parm == self.t_cteReal: tokens.append(parm)
                                elif parm in self.opAsig: 
                                    lexs.append(parm)
                                    tokens.append(self.opAsig[parm])
                                elif parm in self.delim:
                                    lexs.append(parm)
                                    tokens.append(self.delim[parm])
                                else:
                                    lexs.append(parm)
                                    tokens.append(self.t_ident)
                        elif prev_word == 'variables':
                            for parm in parms:
                                if parm in self.palRes:
                                    lexs.append(parm)
                                    tokens.append(self.palRes[parm])
                                elif parm in self.delim:
                                    lexs.append(parm)
                                    tokens.append(self.delim[parm])
                                else:
                                    lexs.append(parm)
                                    tokens.append(self.t_ident)
        self.create_file(lexs, tokens)

    def checkChar(self, word, prev_word):
        valid= True
        parms= []
        if prev_word == 'constantes':
            valid, parms= self.isConstant(word)
        elif prev_word == 'variables':
            valid, parms= self.isVariable(word)
        return valid, parms
    
    def isConstant(self, word):
        valid_const= True
        opAsig= []
        dot_comma= ';'
        new_word= []
        nums= []
        parms= []
        for char in word:
            if char == dot_comma: break
            elif char == ':' or char == '=': opAsig.append(char)
            elif char in self.nums or char == '.': nums.append(char)
            else: new_word.append(char)
        
        ident= "".join(new_word)
        num= "".join(nums)
        v_opAsig= "".join(opAsig)
        valid_num, num_type= self.isNumber(num)
        parms.append(ident)
        parms.append(v_opAsig) 
        parms.append(num) 
        parms.append(num_type)
        parms.append(dot_comma)

        return valid_const, parms
    
    def isVariable(self, word):
        valid_var= True
        dot_comma= ';'
        two_dots= ':'
        comma= ','
        ident= ''
        idents= []
        parms= []
        for char in word:
            #print(char)
            if char == dot_comma: 
                ident= "".join(idents)
                parms.append(ident)
                parms.append(char)  
                break
            elif char == comma: 
                ident= "".join(idents)
                idents= []
                parms.append(ident)
                parms.append(char)
            elif char == two_dots: 
                ident= "".join(idents)
                idents= []
                parms.append(ident)
                parms.append(char)
            else: idents.append(char)

        return valid_var, parms
    
    def isNumber(self, word):      
        isNumber= True
        type= self.t_cteEnt
        while(isNumber):
            for char in word:
                if char in self.nums: continue
                elif char == '.': 
                    isNumber, type= self.isFloat(word)
                    return isNumber, type
                else: 
                    isNumber= False
                    return isNumber, type
            break
        return isNumber, type
    
    def isFloat(self, word):
        isFloat= True
        type= self.t_cteReal
        while(isFloat):
            for char in word:
                if char in self.nums: continue
                elif char == '.': continue
                else: 
                    isFloat= False
                    return False, type
            break
        return isFloat, type
    
    def create_file(self, lexers, tokens):
        os.remove(self.name_file)
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