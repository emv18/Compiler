'''
Compiler
@Author Eduardo Morales Vizcarra & Diego Alejandro Iñiguez
'''

import os
import logging

class Lexer:     
    def __init__(self, name_file):
        self.name_file= name_file # This is the file with the code to analize

        # These are tools
        self.v_alfa= False # This helps us detect alfabetico
        self.dot_comma= ';' 
        self.num_line= 0
        self.l_num_line= []

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
        self.t_cteAlfa= 'CteAlfa'
        self.t_cteLog= 'CteLog'
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
        self.ctes= {'CteEnt': self.t_cteEnt, 'CteReal': self.t_cteReal, 'CteAlfa': self.t_cteAlfa, 'CteLog': self.t_cteLog}

    def pass_lex(self, program):
        lexs= []
        tokens= []
        for line in program:
            self.num_line+= 1
            line_alfa= []
            if '"' not in line:
                line= line.split(" ")
            else: 
                line= list(line)
                for c in line:
                    if line[0] == ' ':
                        line.pop(0)
                line= "".join(line)
                line_alfa.append(line)
                line= line_alfa
            for word in line:
                n= word.split("\t")
                if(len(n)>1):
                    for w in n:
                        if w != '':
                            word= w
                word= word.lower()
                s= list(word)
                #print(word)
                if word == "" or word == ' ' or word == "\t" or s[0] == '':
                    continue
                elif word in self.delim:
                    lexs.append(word)
                    tokens.append(self.delim[word])
                    self.l_num_line.append(self.num_line)
                elif word in self.opArit: 
                    lexs.append(word)
                    tokens.append(self.opArit[word])
                    self.l_num_line.append(self.num_line)
                elif word in self.opRel: 
                    lexs.append(word)
                    tokens.append(self.opRel[word])
                    self.l_num_line.append(self.num_line)
                elif word in self.opLog: 
                    lexs.append(word)
                    tokens.append(self.opLog[word])
                    self.l_num_line.append(self.num_line)
                elif word in self.palRes: 
                    lexs.append(word)
                    tokens.append(self.palRes[word])
                    self.l_num_line.append(self.num_line)
                else:
                    valid, parms= self.checkChar(word)
                    if valid: 
                        for parm in parms:
                            s= list(parm)
                            if parm != '':
                                first_ch= list(parm)[0]
                            if first_ch in self.nums: 
                                lexs.append(parm)
                                self.l_num_line.append(self.num_line)
                            elif parm == self.t_cteEnt or parm == self.t_cteReal: 
                                tokens.append(parm)
                            elif parm in self.opAsig: 
                                lexs.append(parm)
                                tokens.append(self.opAsig[parm])
                                self.l_num_line.append(self.num_line)
                            elif parm in self.delim:
                                lexs.append(parm)
                                tokens.append(self.delim[parm])
                                self.l_num_line.append(self.num_line)
                            elif parm in self.palRes:
                                lexs.append(parm)
                                tokens.append(self.palRes[parm])
                                self.l_num_line.append(self.num_line)
                            elif parm[0] == '"' and parm[-1] == '"':
                                lexs.append(parm)
                                tokens.append(self.t_cteAlfa)   
                                self.l_num_line.append(self.num_line)
                            else:
                                if parm != " ":
                                    parm= list(parm)
                                    f_parm= parm[0]
                                    if f_parm == " ":
                                        parm.pop(0)
                                    parm= "".join(parm)
                                    lexs.append(parm)
                                    if(parm == 'verdadero' or parm == 'falso'):
                                        tokens.append(self.t_cteLog)
                                    else: 
                                        tokens.append(self.t_ident)
                                    self.l_num_line.append(self.num_line)
                    elif not valid:
                        print("Number not valid") 
        self.create_file(lexs, tokens)
        return lexs, self.l_num_line
    
    def checkChar(self, word):
        prev_char= ''
        valid= True
        ident= []
        nums= []
        parms= []
        for char in word:
            if not self.v_alfa:
                if char == self.dot_comma: 
                    ident= "".join(ident)
                    if ident != '':
                        parms.append(ident)
                    num= "".join(nums)
                    if num != '':
                        valid_num, num_type= self.isNumber(num)
                        if not valid_num: 
                            valid= False
                            break
                        parms.append(num) 
                        if num_type != '':
                            parms.append(num_type)
                    nums= []
                    parms.append(char)
                    break
                elif char in self.nums: nums.append(char)
                elif char in self.delim: 
                    ident= "".join(ident)
                    if ident != '':
                        parms.append(ident)
                    ident= []
                    if char == '.': 
                        if prev_char in self.nums:
                            nums.append(char)
                        else: 
                            num= "".join(nums)
                            if num != '':
                                valid_num, num_type= self.isNumber(num)
                                if not valid_num: 
                                    valid= False
                                    break
                                parms.append(num) 
                                if num_type != '':
                                    parms.append(num_type)
                            nums= []
                            parms.append(char)
                    else: parms.append(char)
                elif char in self.opArit: 
                    ident= "".join(ident)
                    if ident != '':
                        parms.append(ident)
                    parms.append(char)
                    ident= []
                    num= "".join(nums)
                    if num != '':
                        valid_num, num_type= self.isNumber(num)
                        if not valid_num: 
                            valid= False
                            break
                        parms.append(num) 
                        if num_type != '':
                            parms.append(num_type)
                    nums= []
                elif char in self.opRel: 
                    if char == '>' and prev_char == '<':
                        ident.append(prev_char)
                        ident.append(char)
                    ident= "".join(ident)
                    if ident != '':
                        parms.append(ident)
                    ident= []
                    num= "".join(nums)
                    if num != '':
                        valid_num, num_type= self.isNumber(num)
                        if not valid_num: 
                            valid= False
                            break
                        parms.append(num) 
                        if num_type != '':
                            parms.append(num_type)
                    nums= []
                    if char == '=':
                        if prev_char == ':':
                            parms.pop()
                            prev_char+= char
                            parms.append(prev_char)
                        else: parms.append(char)
                elif char in self.opLog: 
                    if char == 'y' or char == 'o':
                        if prev_char == ' ' or prev_char == '':
                            parms.append(char)
                        else: ident.append(char)
                    num= "".join(nums)
                    if num != '':
                        valid_num, num_type= self.isNumber(num)
                        if not valid_num: 
                            valid= False
                            break
                        parms.append(num) 
                        if num_type != '':
                            parms.append(num_type)
                    nums= []
                else: 
                    if char != ' ' and len(parms) != 0 and parms[-1] == 'o' and len(ident) == 0:
                        parms.pop()
                        ident.append(prev_char)
                    elif char != ' ' and len(parms) != 0 and parms[-1] == 'y' and len(ident) == 0:
                        parms.pop()
                        ident.append(prev_char)
                    elif char == '"':
                        self.v_alfa= True
                        ident= "".join(ident)
                        if ident != '':
                            parms.append(ident)
                        ident= []
                        num= "".join(nums)
                        if num != '':
                            valid_num, num_type= self.isNumber(num)
                            if not valid_num: 
                                valid= False
                                break
                            parms.append(num) 
                            if num_type != '':
                                parms.append(num_type)
                        nums= []
                        ident.append(char)
                        continue
                    if char != ' ':
                        ident.append(char)
                    elif char == ' ':
                        ident= "".join(ident)
                        if ident != '':
                            parms.append(ident)
                        ident= []
                        num= "".join(nums)
                        if num != '':
                            valid_num, num_type= self.isNumber(num)
                            if not valid_num: 
                                valid= False
                                break
                            parms.append(num) 
                            if num_type != '':
                                parms.append(num_type)
                        nums= []
            elif self.v_alfa: 
                ident.append(char)
                if char == '"':
                    self.v_alfa= False
                    ident= "".join(ident)
                    parms.append(ident)
                    ident= []
            prev_char= char
        if len(parms) != 0 and parms[-1] != self.dot_comma:
            ident= "".join(ident)
            if ident != '':
                parms.append(ident)
            num= "".join(nums)
            if num != '':
                valid_num, num_type= self.isNumber(num)
                if not valid_num: 
                    valid= False
                parms.append(num) 
                if num_type != '':
                    parms.append(num_type)
            nums= []
        elif len(parms) == 0:
            ident= "".join(ident)
            if ident != '':
                parms.append(ident)
            num= "".join(nums)
            if num != '':
                valid_num, num_type= self.isNumber(num)
                if not valid_num: 
                    valid= False
                parms.append(num) 
                if num_type != '':
                    parms.append(num_type)
            nums= []
        return valid, parms
    
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
        try:
            os.remove(self.name_file)
        except:
            logging.info("There's no file created")
        space_words= 50
        with open(self.name_file, "w") as f:
            f.write('--------------------------------------------------------\n')
            f.write('Lexema                                            Token\n')
            f.write('--------------------------------------------------------\n')
            for i in range(len(tokens)):
                space= 0
                for letter in lexers[i]:
                    space+= 1
                f.write(lexers[i])
                while(space < space_words):
                    f.write(' ')
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