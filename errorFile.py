import os
import logging

class Error:
    def __init__(self, name_file):
        self.name_file= name_file
    
    def create_file(self, l_num_line, errors, l_descr_error, line_error):
        try:
            os.remove(self.name_file)
        except:
            logging.info("There's no file created")
        space_words= 25
        with open(self.name_file, "w") as f:
            if len(l_num_line) == 0:
                f.write('No erros have been detected in the workspace')
            else:
                f.write('--------------------------------------------------------------------------------------------------------------------\n')
                f.write('Línea               Error                     Descripción                                  Línea del error\n')
                f.write('--------------------------------------------------------------------------------------------------------------------\n')
                for i in range(len(l_num_line)):
                    space= 0
                    for a in l_num_line:
                        space+= 1
                    f.write(str(l_num_line[i]))
                    while(space < space_words):
                        f.write(' ')
                        space+= 1 

                    space= 0
                    for b in errors:
                        space+= 1
                    f.write(str(errors[i]))
                    while(space < space_words):
                        f.write(' ')
                        space+= 1

                    space= 0
                    for c in l_descr_error:
                        space+= 1
                    f.write(str(l_descr_error[i]))
                    while(space < space_words):
                        f.write(' ')
                        space+= 1

                    space= 0

                    for d in line_error:
                        space+= 1
                    f.write(str(line_error[i]) + '\n')

                    space= 0