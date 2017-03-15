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

#### Assumptions:
  - for option `-f` or `--filepaths`, the backslash characters must be escaped
    - i.e. `c:\path\to\dir` --> WRONG
    - i.e. `c:\\path\\to\\dir` --> RIGHT
  - for options `i` or `input` and `s` or `stdin`, the backslash characters must NOT be escaped
    - i.e. `c:\path\to\dir` --> RIGHT
    - i.e. `c:\\path\\to\\dir` --> WRONG
  - all paths must be of the Windows convention
    - a drive name followed by a path with the backslash separating directories
  - the file defined by the `i` or `input` option must be no more than 2048 bytes (this is a constant that can be changed)

#### Program output and test cases:
  - option `f` or `--filepaths`
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -f c:\\path\\to\\dir\\file.txt
    [c:, path, to, dir, file.txt, file, .txt, path\to\dir]
```
  - option `i` or `--input`
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -i paths.txt
    [c:, windows, system32, svchost.exe, svchost, .exe, windows\system32]
    [c:, n, t, svchost.exe, svchost, .exe, n\t]
    [c:, nwindows, tsystem32, svchost.exe, svchost, .exe, nwindows\tsystem32]
    [c:, windows, system32, svchost, windows\system32\svchost]
    [c:, windows, system32, windows\system32]
```
  - option `s` or `--stdin`
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -s
    Enter the path: c:\path\to\dir\file.txt
    [c:, path, to, dir, file.txt, file, .txt, path\to\dir]
```
  - no arguments:
```
    Kendalls-MacBook-Pro:FilePathTokenizer kendallweihe$ python3 main.py
    You did not select an option
```
  - all options selected:
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -s -i ./paths.txt -f c:\\win\\dows
    Enter the path: c:\win\dowsss
    [c:, windows, system32, svchost, windows\system32\svchost]
    [c:, nwindows, tsystem32, svchost.exe, svchost, .exe, nwindows\tsystem32]
    [c:, n, t, svchost.exe, svchost, .exe, n\t]
    [c:, windows, system32, windows\system32]
    [c:, win, dows, win\dows]
    [c:, win, dowsss, win\dowsss]
    [c:, windows, system32, svchost.exe, svchost, .exe, windows\system32]
```
  - invalid path -- no backslash characters
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -f c:pathtodir
    Invalid path, please check specifications
    [c:pathtodir]
```  
  - invalid path -- forwardslash characters instead
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -f c://path//to//dir
    Invalid path, please check specifications
    [c://path//to//dir]
```
  - more than one period in the path or file
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -f c:\\win\dows\file.file.txt
    [c:, windowsfile.file.txt, windowsfile.file, .txt, ]
```
  - no file, just a path
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -f c:\\path\\to\\dir
    [c:, path, to, dir, path\to\dir]
```
  - last directory is followed by a backslash
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -f c:\\path\\to\\dir\\
    [c:, path, to, dir, , path\to\dir\]
```
  - backslash's are not escaped in the command line arguments
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -f c:\path\to\dir
    Invalid path, please check specifications
    [c:pathtodir]
```
  - stdin an escape character coupled with a special character such as "\t" or "\n"
```
    kendall@kendall-XPS-8500:~/Development/path-parser$ python main.py -s
    Enter the path: c:\newline\tab
    [c:, newline, tab, newline\tab]
```

#### Final notes on the program:

I admit, `tokenize_file_paths()` is a bit lengthy for a function, but I wanted the code to be as robust as possible so that I could reuse that function for other purposes.

I am unfamiliar with pep8 coding styles. For the purposes of time, this project did not take pep8 coding styles into account. However, I do plan on doing some reading in my free time to learn pep8 conventions.

Something I learned during this project was how to implement a custom iterator -- the class: `CustomerIter`

I didn't use `pathlib` or the `os` packages to parse the path variables -- the purposes of this program were to measure my problem solving skills (not solve the problem in a few lines of code).

The print function prints tokens in the following order: `tokenized drive, directories, and file | tokenized file (file + extenstion) | absolute path to file or final directory`
