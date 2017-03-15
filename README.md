Test cases:
  - more than one period in the path
    - more than one period in the file
  - just one period in the path
  - no periods in the path
  - last directory is followed by a backslash
  - last directory is not followed by a backslash
  - no backslash's at all
  - backslash's are not escaped in the command line arguments
  - stdin one backslash with a key character such as "\t" or "\n"


List of assumptions:
  - backslash characters are properly escaped when passing paths as command line arguments
  - assume this is a Windows absolute path where the drive is always included
  - files may not always be at the end of the path
  - paths.txt can have no more than 2048 bytes -- this can can changed
  - the main.py only instantiates a single FilePathTokenizer object per run
  - paths in paths.txt have only a single backslash -- doesn't need to be escaped
  - paths from stdin do not have backslash's escaped

`tokenize_file_paths` is a bit lengthy for a function, but I wanted the code to be as robust as possible

I am unfamiliar with pep8 coding styles. For the purposes of time, this project did not take pep8 coding styles into account. However, I do plan on doing some reading in my free time to learn pep8 conventions.

Didn't use `pathlib` or the `os` packages to parse -- the purposes of this test were to measure my problem solving skills (not solve the problem in a few lines of code).

The print function prints tokens in the following order: 
