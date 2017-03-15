import pdb
import sys
import argparse

# my custom tokenizer program
import tokenize_custom

# instantiate argparse object
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filepaths', nargs='*', help='any number of file paths')
parser.add_argument('-i', '--input', nargs='?', help='path to file containing file paths -- one per line')
parser.add_argument('-s', '--stdin',  help='enter the filepath to stdin, once program begins', action="store_true")

# grab args using argparse and put into dictionary
args = vars(parser.parse_args())

# instantiate a FilePathTokenizer object
tokenized = tokenize_custom.FilePathTokenizer()

# case where no arguments were given
if not (args['filepaths'] or args['input'] or args['stdin']):
    print("You did not select an option")
    sys.exit()

# call function based on user specified options
if args['filepaths']:
    tokenized.tokenize_file_paths(args['filepaths'])
if args['input']:
    fd = open(args['input'])
    tokenized.tokenize_fd(fd)
if args['stdin']:
    path = input("Enter the path: ")
    tokenized.tokenize_file_path(path)

# print the tokenized paths
tokenized.print_tokens()
