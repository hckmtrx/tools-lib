# hckmtrx-tools
## INSTALLATION
```shell
pip install hckmtrx-tools
```

## USAGE
### get parent directory of python file
```python
import hckmtrx_tools

# get file's parent directory
path = hckmtrx_tools.GetDirectory(__file__)

# use it for different purposes (e.g. reading a file in the directory)
reader = open(f"{path}data.txt")
```
### get n directories above parent directory of python file
```python
import hckmtrx_tools

# get n directories above the parent directory
directoryAbove = hckmtrx_tools.GetDirectory(__file__, 1)

# use it for different purposes (e.g. reading a file in the directory)
reader = open(f"{directoryAbove}data.txt")
```

## DEMONSTRATION
```
C:
|
|___folder1
|   |   folder1_main.py
|   |
|   |___folder2
|       |   folder2_main.py

D:
|
|___folder3
|   |   folder3_main.py
```
### [path](#get-parent-directory-of-python-file) variable in:
- folder1_main.py -> `C:\folder1\`
- folder2_main.py -> `C:\folder1\folder2\`
- folder3_main.py -> `D:\folder3\`
### [directoryAbove](#get-n-directories-above-parent-directory-of-python-file) variable in:
- folder1_main.py -> `C:\`
- folder2_main.py -> `C:\folder1\`
- folder3_main.py -> `D:\`
