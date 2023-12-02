class Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.result = ""

    #Open and read the file
    def read_file(self):
        with open(self.file_path, 'r') as file:
            self.result = file.read().replace('\n', '')
        #Add $ at the end of the output
        self.result += '$'

    #Open and rewrite the output in the file
    def write_output_file(self, output_file_path="out2.py"):
        with open(output_file_path, 'w') as out_file:
            out_file.write(self.result)

    #Display the output
    def display_output(self):
        print(self.result)

processor = Processor('out1.py')
processor.read_file()
processor.write_output_file()
processor.display_output()
