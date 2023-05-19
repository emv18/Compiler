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
        lexs= []
        tokens= []
        for line in program:
            line= line.split(" ")
            for word in line:
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
                elif word in self.opAsig: 
                    lexs.append(word)
                    tokens.append(self.opAsig[word])
                else:
                    valid, v_type= self.checkChar(word)
                    if valid: 
                        if v_type in self.ctes:
                            lexs.append(word)
                            tokens.append(self.ctes[v_type])
        self.create_file(lexs, tokens)

    def checkChar(self, word):
        valid, v_type= self.isNumber(word)
        return valid, v_type

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
    
    def isfloat(self, word):
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