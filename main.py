'''
Compiler
@Author Eduardo Morales Vizcarra & Diego Alejandro Iñiguez
'''

import lexer as lex
import syntatic as syn
import fileReader as fr

class Compiler:
    def __init__(self, name_file, lex_file, err_file):
        self.name_file= name_file # This is the file code we read to compile
        self.lex_file= lex_file # This is the file we create with the lex table
        self.err_file= err_file # This is the file we create to register all errrors

    def readFile(self):
        file= fr.File_reader(self.name_file) # We instantiate the filre reader class
        program= file.readCode() 
        
        lexer= lex.Lexer(self.lex_file) # We instantiate the lexer class
        lexer.pass_lex(program)

file_origin= './Inputs/codigo.eje'
file_token= './Outputs/tokens.lex'
file_errors= './Outputs/errors.err'
compiler= Compiler(file_origin, file_token, file_errors)
compiler.readFile()
        
