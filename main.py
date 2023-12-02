import sys
from preprocessor import Preprocessor
from processor import Processor
from lexical_analyzer import LexicalAnalyzer

def main():
    #Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py input_file.py")
        sys.exit(1)

    #Get the input file from the command-line arguments
    input_file = sys.argv[1]

    #Task 1: Preprocess the source code
    preprocessor = Preprocessor("in1.py")
    preprocessor.read_file()
    preprocessor.eliminate_blank_lines()
    preprocessor.eliminate_comments()
    preprocessor.eliminate_spaces_tabs()
    preprocessor.eliminate_import_annotations()
    preprocessor.write_output_file()
    print('-----------------------------------------------------------')
    preprocessor.display_output()

    #Task 2: Process the output from Task 1
    processor = Processor("out1.py")
    processor.read_file()
    processor.write_output_file()
    print('-----------------------------------------------------------')
    processor.display_output()

    #Task 3: Perform lexical analysis on the processed code
    lexical_analyzer = LexicalAnalyzer("out2.py")
    lexical_analyzer.perform_lexical_analysis()
    print('-----------------------------------------------------------')
    lexical_analyzer.display_lexemes()

if __name__ == "__main__":
    main()
