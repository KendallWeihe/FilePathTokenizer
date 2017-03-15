Test cases:
  - more than one period in the path
    - more than one period in the file
  - just one period in the path
  - no periods in the path
  - last directory is followed by a backslash
  - last directory is not followed by a backslash


List of assumptions:
  - backslash characters are properly escaped when passing paths as command line arguments
  - assume this is a Windows absolute path where the drive is always included
  - files may not always be at the end of the path

`tokenize_file_paths` is a bit lengthy for a function, but I wanted the code to be as robust as possible
