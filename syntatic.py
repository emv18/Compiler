class Syntatic:
    def __init__(self, lexs, lines):
        self.lines= lines
        self.lexs= lexs
        self.v_cicle= False # This helps us detect a cicle
        self.open_end_cicle= False
        self.open_init_cicle= False

        #Tools
        self.new_word= []

        #Data for errors
        self.l_num_line= []
        self.errors= []
        self.descr_error= ''
        self.l_descr_error= []
        self.line_error= []

        #Tokens for detect errors
        self.t_errors= {'procedimiento': 'inicio',
                        'inicio': 'fin de procedimiento',
                        'repetir': 'hasta que',
                        'cuando': 'fin',
                        'si': 'sino',
                        'sea': 'otro',
                        'desde': 'hasta',
                        'funcion': 'fin de funcion',
                        '(': ')'}
        
    def passSyn(self):
        prev_word= ''
        for i in range(len(self.lines)):
            word= self.lexs[i]
            if prev_word == 'constantes':
                if word == ':=' or ';':
                    self.isError(i, word, self.open_end_cicle, self.open_init_cicle)
            try:
                if word == self.t_errors[word] and self.v_cicle == False:
                    self.open_end_cicle= True
                    self.isError(i, word, self.open_end_cicle, self.open_init_cicle)
                elif prev_word in self.t_errors:
                    self.v_cicle= True
                if self.v_cicle:
                    if word == self.t_errors[word]:
                        self.v_cicle= False
                if word == ';' and self.v_cicle == True:
                    self.open_init_cicle= True
                    self.isError(i, word, self.open_end_cicle, self.open_init_cicle)
            except: 
                continue
            prev_word= word
        return self.l_num_line, self.errors, self.l_descr_error, self.line_error
    
    def isError(self, i, word, open_end_cicle, open_init_cicle):
        self.l_num_line.append(self.lines[i])
        self.errors.append(word)
        if open_end_cicle == True:
            self.l_descr_error.append('Cerraste un ciclo sin empezarlo')
            self.open_end_cicle= False
        elif open_init_cicle == True:
            self.l_descr_error.append('Abriste un ciclo sin terminarlo')
            self.open_init_cicle= False
        else:
            self.l_descr_error.append('Hay un error sintáctico')
        for w in range(len(self.lines)):
            if self.lines[i] == self.lines[w]:
                self.new_word.append(self.lexs[w])
        self.new_word= "".join(self.new_word)
        self.line_error.append(self.new_word)
        self.new_word= []
        