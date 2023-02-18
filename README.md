# hckmtrx-tools
## installation
`pip install hckmtrx-tools`

## how to use
get current directory of python file
```python
import hckmtrx_tools

# get file's directory with GetDirectory() function
path = hckmtrx_tools.GetDirectory(__file__)

# use it for different purposes (e.g. reading a file in the directory)
reader = open(f"{path}data.txt")
```

## demonstration
```
C:
|
|___folder1
|   |   folder1_main.py
|   |   folder1_data.txt
|   |
|   |___folder2
|       |   folder2_main.py
|       |   folder2_data.txt

D:
|
|___folder3
|   |   folder3_main.py
|   |   folder3_data.txt
```
### path variable in:
- folder1_main.py -> `C:\folder1\`
- folder2_main.py -> `C:\folder1\folder2\`
- folder3_main.py -> `D:\folder3\`