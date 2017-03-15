#### This program tokenizes Windows paths based on the following specifications:

Tokenization should break each sub folder out into its own item in the list, it should also fabricate a token that contains all the directories excluding drive and filename:

`c:\Windows\system32\drivers` -> `['c:', 'windows', 'system32’, 'drivers', 'windows\system32\drivers']`

If a filename is found tokenization should be as follows:
`[<filename>.<ext>, <filename>, <ext>]`

Example:
`c:\windows\system32\svchost.exe` -> `['c:', 'windows’, 'system32', 'windows\system32', 'svchost.exe', 'svchost’, 'exe']`

#### The following files are included:
  - `main.py`
    - parses arguments and instantiates a `FilePathTokenizer` object
    - takes the following argument options:
>      -f or --filepaths | expects any number of file paths. You may assume that the file path is properly escaped for the platform on which it is running.
>      -i or --input | expects a file path to a file containing file paths
>      -s or --stdin | expects file paths on stdin
  - `tokenize_custom.py`
    - class object meant to tokenize Windows paths
  - `paths.txt`
    - an example text file for the -i or --input option

#### NOTE: the following version of Python was used:
```
kendall@kendall-XPS-8500:~/Development/path-parser$ python --version
Python 3.4.3
```

#### Test cases:
  - no arguments:
```
    Kendalls-MacBook-Pro:FilePathTokenizer kendallweihe$ python3 main.py
    You did not select an option
```
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
