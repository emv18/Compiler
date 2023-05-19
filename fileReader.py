class File_reader:
    def __init__(self, file):
        self.file= file

    def readCode(self):
        with open(self.file, 'r') as f:
            program= f.read()

        program= program.split('\n')
        #num_line= len(program)

        return program