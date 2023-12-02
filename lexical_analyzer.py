import re

class LexicalAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.list_of_lexemes = []

    def read_file(self):
        #Open and read the file
        with open(self.file_path, 'r') as file:
            self.program_text = file.read()

    def perform_lexical_analysis(self):
        #Define regular expressions for various lexeme categories
        keyword_pattern = re.compile(r'\b(and|as|break|class|continue|def|del|elif|else|except|False|finally|for|from|None|nonlocal|not|or|pass|return|True|try|while|with|yield)\b')
        identifier_pattern = re.compile(r'\b[a-zA-Z_]\w*\b')
        operator_pattern = re.compile(r'[-+*/%=]=?|==|!=|<=?|>=?|and|or|not|in|is')
        punctuator_pattern = re.compile(r'[{}[\](),;:.]')
        literal_pattern = re.compile(r'\b(?:\d+\.\d*|\.\d+|\d+)[eE][-+]?\d+\b|\b\d+\.\d*\b|\b\d+\b|\b[\'"].*?[\'"]\b')
        comment_pattern = re.compile(r'#.*')
        annotation_pattern = re.compile(r'@[a-zA-Z_]\w*')
        import_pattern = re.compile(r'import [a-zA-Z_]\w*|from [a-zA-Z_]\w* import [a-zA-Z_]\w*')

        patterns = {
            'Keyword': keyword_pattern,
            'Identifier': identifier_pattern,
            'Operator': operator_pattern,
            'Punctuator': punctuator_pattern,
            'Literal': literal_pattern,
            'Comment': comment_pattern,
            'Annotation': annotation_pattern,
            'Import': import_pattern,
        }

        #Initialize the list to store lexemes
        self.list_of_lexemes = []

        for line in self.program_text.split('\n'):
            #Iterate through each lexeme category and find matches in the line
            for category, pattern in patterns.items():
                matches = pattern.finditer(line)
                #Append the matched lexemes to the list
                for match in matches:
                    self.list_of_lexemes.append((category, match.group()))

    #Display the identified lexemes                
    def display_lexemes(self):
        for lexeme in self.list_of_lexemes:
            print(f"Lexeme: {lexeme[1]}")

#Create an instance of LexicalAnalyzer
lexical_analyzer = LexicalAnalyzer('out2.py')
#Read the file
lexical_analyzer.read_file()
#Perform lexical analysis
lexical_analyzer.perform_lexical_analysis()
#Display the identified lexemes
lexical_analyzer.display_lexemes()
