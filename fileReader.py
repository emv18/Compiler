class File_reader:
    def __init__(self, file):
        self.file= file # This is the file with the code to read

    def readCode(self):
        with open(self.file, 'r') as f:
            program= f.read()
        program= program.split('\n') # We save the code based on lines
        return program