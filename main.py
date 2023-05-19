'''
Compiler
@Author Eduardo Morales Vizcarra & Diego Alejandro Iñiguez
'''

import lexer as lex
import syntatic as syn
import fileReader as fr

class Compiler:
    def __init__(self, name_file, lex_file, err_file):
        self.name_file= name_file # This is the code we read
        self.lex_file= lex_file
        self.err_file= err_file

    def readFile(self):
        file= fr.File_reader(self.name_file)
        program= file.readCode()
        
        lexer= lex.Lexer(self.lex_file)
        lexer.pass_lex(program)
        #print(program)
        #print(num_line)


compiler= Compiler('codigo.eje', 'tokens.lex', 'errors.err')
compiler.readFile()
        
