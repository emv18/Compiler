'''
Compiler
@Author Eduardo Morales Vizcarra & Diego Alejandro Iñiguez
'''

import lexer as lex
import syntatic as syn
import semantic as sem
import errorFile as err
import fileReader as fr

class Compiler:
    def __init__(self, name_file, lex_file, err_file, eje_file):
        self.name_file= name_file # This is the file code we read to compile
        self.lex_file= lex_file # This is the file we create with the lex table
        self.err_file= err_file # This is the file we create to register all errrors
        self.eje_file= eje_file # This is the execution file

    def readFile(self):
        file= fr.File_reader(self.name_file) # We instantiate the filre reader class
        program= file.readCode() 
        
        lexer= lex.Lexer(self.lex_file) # We instantiate the lexer class
        lexs, l_num_line= lexer.pass_lex(program)

        syntactic= syn.Syntatic(lexs, l_num_line)
        l_num_line, errors_l, l_descr_error, line_error= syntactic.passSyn()

        semantic= sem.Semantic(self.eje_file, lexs)
        semantic.passSem()

        errors= err.Error(self.err_file) # We instantiate the error class to create the error file
        errors.create_file(l_num_line, errors_l, l_descr_error, line_error)

file_origin= './Inputs/codigo.up'
#file_origin= './Inputs/ExamenFinal.up'
file_token= './Outputs/tokens.lex'
file_errors= './Outputs/errors.err'
file_eje= './Outputs/execution.eje'
compiler= Compiler(file_origin, file_token, file_errors, file_eje)
compiler.readFile()
        
