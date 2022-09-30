import utils
from openpyxl import load_workbook

def get():
    doc = load_workbook(filename='constants.xlsx')
    ws = doc.active

    data = [[0 for _ in range(2, ws.max_column+1)]
        for _ in range(2, ws.max_row+1)]

    # assign values
    for i in range(2, ws.max_row+1):
        for j in range(2, ws.max_column+1):
            data[i-2][j-2] = ws.cell(i, j).value

    d = utils.convert_to_tuple(data)
    # print(d) # ([100], [10000000], [1000000000], [12], [8000], [8000])
    return d