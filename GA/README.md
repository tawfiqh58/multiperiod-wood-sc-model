#

Note: If you want to change input value you must have to follow
the same structure of excel sheet to put value also there will have deep
connection with the index size and parameter values you will have specified

- index match with given parameter value
- sheet format
- sheet sequence

DO NOT PUT ANY VALUE TO OTHER CELL IN WORKSHEET OUTSIDE THE TABLE RANGE
THEN IT WILL TAKE WRONG INPUT FROM YOUR WORKSHEET AND PROBABLY YOU WILL
GET AN ERROR

## How to run?

You already have to have install `python` and
`pip` (python package installer) in your computer then install
all dependencies by running below command

```cmd
pip install -r requirements.txt
```

or

```cmd
pip install openpyxl
pip install numpy
pip install matplotlib
pip install xlsxwriter
```

Run app:

```cmd
python3 main.py
```
