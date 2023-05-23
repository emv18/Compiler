'''
Compiler
@Author Eduardo Morales Vizcarra & Diego Alejandro Iñiguez
'''

import os
import logging

class Semantic:
    def __init__(self, name_file, lexs):
        self.name_file= name_file
        self.lexs= lexs
        self.exes= []

        #Data for errors
        self.l_num_line= []
        self.errors= []
        self.descr_error= ''
        self.l_descr_error= []
        self.line_error= []

    def passSem(self):
        #prev_word= ''
        for word in self.lexs:
            if word[0] == '"': self.exes.append(word)
            #prev_word= word
        self.create_file(self.exes)

    def create_file(self, exes):
        try:
            os.remove(self.name_file)
        except:
            logging.info("There's no file created")
        space_words= 5
        cont= 1
        space= 0
        with open(self.name_file, "w") as f:
            f.write('@\n')
            for i in range(len(exes)):
                f.write(str(cont))
                for n in range(len(str(cont))):
                    space+= 1
                while(space < space_words):
                    f.write(' ')
                    space+= 1
                f.write('LIT   ' + exes[i] + ', 0\n')
                space= 0
                cont+= 1