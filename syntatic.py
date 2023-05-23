'''
Compiler
@Author Eduardo Morales Vizcarra & Diego Alejandro Iñiguez
'''
import logging

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
        self.t_errors= {'cuando': 'fin',
                        'si': 'hacer',
                        'hacer': 'sino',
                        'sea': 'otro',
                        'desde': 'hasta',
                        '(': ')'}
        
    def passSyn(self):
        prev_word= ''
        word_init= ''
        prev_line= 1
        for i in range(len(self.lines)):
            current_line= self.lines[i]
            word= self.lexs[i]
            try:
                if word in self.t_errors:
                    self.v_cicle= True
                    word_init= word
            except:
                logging.info("The token is not a key")
            try:
                if self.t_errors[word] and self.v_cicle == False:
                    self.open_end_cicle= True
                    self.isError(i, self.t_errors[word_init], self.open_end_cicle, self.open_init_cicle)
            except:
                logging.info("The token is not a key")
            try:
                if self.v_cicle:
                    if word == self.t_errors[word_init]:
                        self.v_cicle= False
                        word_init= ''
            except:
                logging.info("The token is not a key")
            try:
                if word == ';' and self.v_cicle == True:
                    self.open_init_cicle= True
                    self.isError(i, word_init, self.open_end_cicle, self.open_init_cicle)
            except: 
                logging.info("The token is not a key")
            
            prev_word= word
            if word == ';':
                self.v_cicle= False
            '''
            if prev_line != current_line:
                prev_line+= 1
                self.v_cicle= False
            '''
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
        