import os

class Error:
    def __init__(self, name_file):
        self.name_file= name_file
    
    def create_file(self, num_lines, errors, descr, lines):
        os.remove(self.name_file)
        space_words= 38
        with open(self.name_file, "w") as f:
            f.write('------------------------------------------------------------------------\n')
            f.write('Línea               Error                Descripción               Línea del error\n')
            f.write('------------------------------------------------------------------------\n')
            for i in range(len(num_lines)):
                space= 0
                for a in num_lines[i]:
                    space+= 1
                f.write(num_lines[i])
                while(space < space_words):
                    f.write(' ')
                    space+= 1 

                space= 0
                for b in errors[i]:
                    space+= 1
                f.write(errors[i])
                while(space < space_words):
                    f.write(' ')
                    space+= 1

                space= 0
                for c in descr[i]:
                    space+= 1
                f.write(descr[i])
                while(space < space_words):
                    f.write(' ')
                    space+= 1
                f.write(lines[i] + '\n') 