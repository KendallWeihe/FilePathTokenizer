import pdb
import sys
import argparse

import tokenize_custom

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filepaths', nargs='*', help='any number of file paths')
parser.add_argument('-i', '--inputs', nargs='?', help='path to file containing file paths -- one per line')
parser.add_argument('-s', '--stdin',  help='enter the filepath to stdin, once program begins', action="store_true")

args = vars(parser.parse_args())

tokenized = tokenize_custom.FilePathTokenizer()
if args['filepaths']:
    tokenized.tokenize_file_paths(args['filepaths'])
elif args['inputs']:
    tokenized.tokenize_fd(args['inputs'])
elif args['stdin']:
    path = input("Enter the path: ")
    tokenized.tokenize_file_path(path)
else:
    pdb.set_trace
    print("You did not select an option")
    sys.exit()

tokenized.print_tokens()