**Project Portfolio: https://github.com/calebyhan/CalebHan**

A CLI tool to see a tree of a directory.

To use this tool, you need to have Python 3.6 or higher installed. Download the repository and run the following command anywhere:

```
python \path_to\cli_tree.py -h
```

This will show the help message:

```
usage: cli_tree [-h] [-w [file_name]] [-hi hidden] [-d depth] [-i [ignore]] [-v] path

A CLI tool to see a tree of a directory.

positional arguments:
  path                  Path to the directory

optional arguments:
  -h, --help            show this help message and exit
  -w [file_name], --write [file_name]
                        Writes content to a file (default output.txt)
  -hi hidden, --hidden hidden
                        Shows hidden files (default False)
  -d depth, --depth depth
                        Sets depth of the tree (default max)
  -i [ignore], --ignore [ignore]
                        Ignores dirs with the given name (default None)
  -v, --version         show program's version number and exit

Made by: Caleb Han (https://github.com/calebyhan)
```

Example usage:

```
python \path_to\cli_tree.py C:\Users\user\Documents\GitHub\cli-tree -w output.txt -hi True -d 2 -i .git
```

This will output the file structure to `C:\Users\user\Documents\GitHub\cli-tree` to `output.txt`, showing hidden files, with a depth of 2, and ignoring the `.git` directory.
