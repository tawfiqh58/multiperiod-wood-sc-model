import xlsxwriter


def write(gen):
    # Create a workbook and add a worksheet.
    doc = xlsxwriter.Workbook('result.xlsx')
    ws = doc.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0

    a = [1, 2]
    b = [1, 2]
    e = [1, 2]
    eb = [1, 2]
    f = [1, 2]
    g = [1, 2]
    Gb = [1, 2]
    i = [1, 2]
    ix = [1, 2]
    ixx = [1, 2]
    j = [1, 2]
    ij = [1, 2, 3, 4]
    hj = [1, 2]
    m = [1, 2]
    p = [1, 2]
    t = [1, 2]
    v = [1, 2]
    Va = [1, 2]
    Bapm = [1, 2, 3, 4]
    ixj = [1, 2, 3, 4]
    # x, x1, x11, xb, xb1, w, w1, w11, wb, wb1, bo, u1, u_pt, u11, u111, yb, yb1, y, y1, y11, y111

    for supplier in range(len(a)):
        ws.write(row, 0, 'supplier '+ str(supplier + 1))
        for vehicle in range(len(v)):
            for day in range(len(t)):
                ws.write(row, 1, 'vehicle ' + str(vehicle + 1))
                ws.write(row, 2, 'day ' + str(day + 1))
                ws.write(row, 3, gen[0][supplier][vehicle][day])
                row += 1

    doc.close()

    return 'Success!'
