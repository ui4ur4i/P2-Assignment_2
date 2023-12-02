import re
class Preprocessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.processing_file = ""

    #Open and read the file
    def read_file(self):
        with open(self.file_path, 'r') as file:
            self.processing_file = file.read()

    #Eliminate and blank lines from the file
    def eliminate_blank_lines(self):
        self.processing_file = "\n".join(line for line in self.processing_file.splitlines() if line.strip())

    #Remove single-line and triple double-quote comments from the file
    def eliminate_comments(self):
        self.processing_file = re.sub(r'#.*', '', self.processing_file)
        self.processing_file = re.sub(r'"""(?:[^"]|"(?!"))*"""', '', self.processing_file)

    #Remove unnecessary spaces and tabs from the file
    def eliminate_spaces_tabs(self):
        self.processing_file = re.sub(r'[ \t]+', ' ', self.processing_file)

    #Remove import statements and annotations from the file
    def eliminate_import_annotations(self):
        self.processing_file = re.sub(r'import .*\n', '', self.processing_file)
        self.processing_file = re.sub(r'from .*\n', '', self.processing_file)
        self.processing_file = re.sub(r'@.*\n', '', self.processing_file)

    #Write the processed content to an output file
    def write_output_file(self, output_file_path="out1.py"):
        with open(output_file_path, 'w') as out_file:
            out_file.write(self.processing_file)

    #Display the processed content
    def display_output(self):
        print(self.processing_file)
        
preprocessor = Preprocessor('in1.py')
preprocessor.read_file()
preprocessor.eliminate_blank_lines()
preprocessor.eliminate_comments()
preprocessor.eliminate_spaces_tabs()
preprocessor.eliminate_import_annotations()
preprocessor.write_output_file()
preprocessor.display_output()
