import xlsxwriter


def write(gen, value, analysis_value):
    # Create a workbook and add a worksheet.
    doc = xlsxwriter.Workbook('result.xlsx')
    ws = doc.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0

    a = [1, 2, 3] # supplier
    b = [1, 2, 3, 4, 5] # wholesaler
    e = [1, 2, 3, 4, 5] # retailer
    eb = [1, 2, 3, 4, 5]
    f = [1, 2]
    g = [1, 2]
    Gb = [1, 2]
    i = [1, 2]
    ix = [1, 2]
    ixx = [1, 2]
    j = [1, 2, 3, 4, 5] # collection-center
    ij = [1, 2]
    hj = [1, 2]
    m = [1, 2, 3] # material
    p = [1, 2, 3] # product
    t = [1, 2]
    v = [1, 2]
    Va = [1, 2]
    Bapm = [1, 2, 3]
    ixj = [1, 2]

    x = gen[0]
    x1 = gen[1]
    x11 = gen[2]
    xb = gen[3]
    xb1 = gen[4]
    
    # value will be found from constraints
    w = gen[5]
    w1 = gen[6]
    w11 = gen[7]
    wb = gen[8]
    wb1 = gen[9]

    bo = gen[10]
    u1 = gen[11]
    u_pt = gen[12]
    u11 = gen[13]
    u111 = gen[14]
    yb = gen[15]
    yb1 = gen[16]
    y = gen[17]
    y1 = gen[18]
    y11 = gen[19]
    y111 = gen[20]

    # x, x1, x11, xb, xb1, w, w1, w11, wb, wb1, bo, u1, u_pt, u11, u111, yb, yb1, y, y1, y11, y111

    ws.write(row, 0, "Optimization")
    row += 1
    ws.write(row, 0, 'Min.')
    ws.write(row, 1, value)
    row += 2
    
    ws.write(row, 0, 'Analysis')
    for _indx in range(len(analysis_value)): # sequence: trans, purchas, prod, mainten, short, envir
        if _indx == 0:
            ws.write(row, 0, 'Transportation Cost')
            ws.write(row, 1, analysis_value[0])
        elif _indx == 1:
            ws.write(row, 0, 'Purchasing Cost')
            ws.write(row, 1, analysis_value[1])
        elif _indx == 2:
            ws.write(row, 0, 'Production Cost')
            ws.write(row, 1, analysis_value[2])
        elif _indx == 3:
            ws.write(row, 0, 'Maintenance Cost')
            ws.write(row, 1, analysis_value[3])
        elif _indx == 4:
            ws.write(row, 0, 'Shortage Cost')
            ws.write(row, 1, analysis_value[4])
        elif _indx == 5:
            ws.write(row, 0, 'Environmental Cost')
            ws.write(row, 1, analysis_value[5])
        
        row += 1

    row += 1
    
    ws.write(row, 0, "w(a,v,t) The number of trip of vehicle v from supplier a to factory on day t")
    row += 1
    for _a in range(len(a)):
        ws.write(row, 0, 'supplier '+ str(_a + 1))
        for _v in range(len(v)):
            for _t in range(len(t)):
                ws.write(row, 1, 'vehicle ' + str(_v + 1))
                
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, w[_a][_v][_t])
                row += 1
    row += 1
    ws.write(row, 0, "w1(b,f,t) The number of trip of vehicle f from factory to wolesaler b on day t")
    row += 1
    for _b in range(len(b)):
        ws.write(row, 0, 'wholesaler '+ str(_b + 1))
        for _f in range(len(f)):
            for _t in range(len(t)):
                ws.write(row, 1, 'vehicle ' + str(_f + 1))
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, w1[_b][_f][_t])
                row += 1

    
    row += 1
    ws.write(row, 0, "w11(b,e,g,t) The number of trip of vehicle g from wholesaler b to retailer e on day t")
    row += 1
    for _b in range(len(b)):
        ws.write(row, 0, 'wholesaler '+ str(_b + 1))
        for _e in range(len(e)):
            ws.write(row, 1, 'retailer '+ str(_e + 1))
            for _g in range(len(g)):
                for _t in range(len(t)):
                    ws.write(row, 2, 'vehicle ' + str(_g + 1))
                    ws.write(row, 3, 'day ' + str(_t + 1))
                    ws.write(row, 4, w11[_b][_e][_g][_t])
                    row += 1
    
    row += 1
    ws.write(row, 0, "y111(b,e,g,p,t) THe number of product p transported by vehicle g from wholesaler b to retailer e on day t")
    row += 1
    for _b in range(len(b)):
        ws.write(row, 0, 'wholesaler '+ str(_b + 1))
        for _e in range(len(e)):
            ws.write(row, 1, 'retailer '+ str(_e + 1))
            for _g in range(len(g)):
                ws.write(row, 2, 'vehicle '+ str(_g + 1))
                for _p in range(len(p)):
                    for _t in range(len(t)):
                        ws.write(row, 3, 'product ' + str(_p + 1))
                        ws.write(row, 4, 'day ' + str(_t + 1))
                        ws.write(row, 5, y111[_b][_e][_g][_p][_t])
                        row += 1

    row += 1
    ws.write(row, 0, "bo(e,p,t) The amount of postponed orders of retailer from product p on day t")
    row += 1
    for _e in range(len(e)):
        ws.write(row, 0, 'retailer '+ str(_e + 1))
        for _p in range(len(p)):
            for _t in range(len(t)):
                ws.write(row, 1, 'product ' + str(_p + 1))
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, bo[_e][_p][_t])
                row += 1

    
    row += 1
    ws.write(row, 0, "u1(m,t) Storage inventory (weight) of wooden raw material m in the factory on day t")
    row += 1
    for _m in range(len(m)):
        ws.write(row, 0, 'material '+ str(_m + 1))
        for _t in range(len(t)):
            ws.write(row, 1, 'day ' + str(_t + 1))
            ws.write(row, 2, u1[_m][_t])
            row += 1
    
    row += 1
    ws.write(row, 0, "u_pt(p,t) Storage inventory (weight) of product p in the factory on day t")
    row += 1
    for _p in range(len(p)):
        ws.write(row, 0, 'product '+ str(_p + 1))
        for _t in range(len(t)):
            ws.write(row, 1, 'day ' + str(_t + 1))
            ws.write(row, 2, u_pt[_p][_t])
            row += 1

    row += 1
    ws.write(row, 0, "u11(b,p,t) Storage inventory of wholesaler b from product p on day t")
    row += 1
    for _b in range(len(b)):
        ws.write(row, 0, 'wholesaler '+ str(_b + 1))
        for _p in range(len(p)):
            for _t in range(len(t)):
                ws.write(row, 1, 'product ' + str(_p + 1))
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, u11[_b][_p][_t])
                row += 1
    
    row += 1
    ws.write(row, 0, "u111(e,p,t) Storage inventory of customer e from product p on day t")
    row += 1
    for _e in range(len(e)):
        ws.write(row, 0, 'retailer '+ str(_e + 1))
        for _p in range(len(p)):
            for _t in range(len(t)):
                ws.write(row, 1, 'product ' + str(_p + 1))
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, u111[_e][_p][_t])
                row += 1
    
    
    row += 1
    ws.write(row, 0, "wb(e,i,j,t) The number of trip of vehicle I from retailer e to collection center j on day t")
    row += 1
    for _e in range(len(e)):
        ws.write(row, 0, 'retailer '+ str(_e + 1))
        for _i in range(len(i)):
            ws.write(row, 1, 'vehicle '+ str(_i + 1))
            for _j in range(len(j)):
                for _t in range(len(t)):
                    ws.write(row, 2, 'collection-center ' + str(_j + 1))
                    ws.write(row, 3, 'day ' + str(_t + 1))
                    ws.write(row, 4, wb[_e][_i][_j][_t])
                    row += 1

    row += 1
    ws.write(row, 0, "wb1(ix,j,t) The number of vehicle ix from collection center j to the factory on day t")
    row += 1
    for _ix in range(len(ix)):
        ws.write(row, 0, 'vehicle '+ str(_ix + 1))
        for _j in range(len(j)):
            for _t in range(len(t)):
                ws.write(row, 1, 'collection-center ' + str(_j + 1))
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, wb1[_ix][_j][_t])
                row += 1
    row += 1
    ws.write(row, 0, "x(a,v,t) Binary veariable representing the departure or no-departure of vehicle v form supplier a to the factory on day t")
    row += 1
    for _a in range(len(a)):
        ws.write(row, 0, 'supplier '+ str(_a + 1))
        for _v in range(len(v)):
            for _t in range(len(t)):
                ws.write(row, 1, 'vehicle ' + str(_v + 1))
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, x[_a][_v][_t])
                row += 1
    row += 1
    ws.write(row, 0, "x1(b,f,t) Binary variable representing the departure or non-departure of vehicle f from factory to wholesaler b on day t")
    row += 1
    for _b in range(len(b)):
        ws.write(row, 0, 'wholesaler '+ str(_b + 1))
        for _f in range(len(f)):
            # ws.write(row, 1, 'vehicle ' + str(_f + 1))
            for _t in range(len(t)):
                ws.write(row, 1, 'vehicle ' + str(_f + 1))
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, x1[_b][_f][_t])
                row += 1
    
    row += 1
    ws.write(row, 0, "x11(b,e,g,t) Binary variable representing the departure or non-departure of vehicle g from wholesaler b  to retailer e on day t")
    row += 1
    for _b in range(len(b)):
        ws.write(row, 0, 'wholesaler '+ str(_b + 1))
        for _e in range(len(e)):
            ws.write(row, 1, 'retailer '+ str(_e + 1))
            for _g in range(len(g)):
                for _t in range(len(t)):
                    ws.write(row, 2, 'vehicle ' + str(_g + 1))
                    ws.write(row, 3, 'day ' + str(_t + 1))
                    ws.write(row, 4, x11[_b][_e][_g][_t])
                    row += 1
    
    row += 1
    ws.write(row, 0, "yb(e,i,j,p,t) The amount of product p sent from retailer e to collection center j to the factory by vehicle Ixx on day t")
    row += 1
    for _e in range(len(e)):
        ws.write(row, 0, 'wholesaler '+ str(_e + 1))
        for _i in range(len(i)):
            ws.write(row, 1, 'vehicle '+ str(_i + 1))
            for _j in range(len(j)):
                ws.write(row, 2, 'collection-center '+ str(_j + 1))
                for _p in range(len(p)):
                    for _t in range(len(t)):
                        ws.write(row, 3, 'product ' + str(_p + 1))
                        ws.write(row, 4, 'day ' + str(_t + 1))
                        ws.write(row, 5, yb[_e][_i][_j][_p][_t])
                        row += 1
    
    row += 1
    ws.write(row, 0, "yb1(ix,j,m,t) The amount of material m sent from collection center j to the factory by vehicle Ixx on day t")
    row += 1
    for _ix in range(len(ix)):
        ws.write(row, 0, 'vehicle '+ str(_ix + 1))
        for _j in range(len(j)):
            ws.write(row, 1, 'collection-center '+ str(_j + 1))
            for _m in range(len(m)):
                for _t in range(len(t)):
                    ws.write(row, 2, 'material ' + str(_m + 1))
                    ws.write(row, 3, 'day ' + str(_t + 1))
                    ws.write(row, 4, yb1[_ix][_j][_m][_t])
                    row += 1
    
    row += 1
    ws.write(row, 0, "y(a,v,m,t) The amount of wooden raw material m sent by vehicle v from supplier a to the factory on day t")
    row += 1
    for _a in range(len(a)):
        ws.write(row, 0, 'supplier '+ str(_a + 1))
        for _v in range(len(v)):
            ws.write(row, 1, 'vehicle '+ str(_v + 1))
            for _m in range(len(m)):
                for _t in range(len(t)):
                    ws.write(row, 2, 'material ' + str(_m + 1))
                    ws.write(row, 3, 'day ' + str(_t + 1))
                    ws.write(row, 4, y[_a][_v][_m][_t])
                    row += 1
    row += 1
    ws.write(row, 0, "y1(p,t) The number of manufactured products p by the factory on day t")
    row += 1
    for _p in range(len(p)):
        ws.write(row, 0, 'product '+ str(_p + 1))
        for _t in range(len(t)):
            ws.write(row, 1, 'day ' + str(_t + 1))
            ws.write(row, 2, y1[_p][_t])
            row += 1

    
    row += 1
    ws.write(row, 0, "y11(b,g,p,t) The number of products p sent by vehicle g from the factory to wholesaler b on day t")
    row += 1
    for _b in range(len(b)):
        ws.write(row, 0, 'wholesaler '+ str(_b + 1))
        for _g in range(len(g)):
            ws.write(row, 1, 'vehicle '+ str(_g + 1))
            for _p in range(len(p)):
                for _t in range(len(t)):
                    ws.write(row, 2, 'product ' + str(_p + 1))
                    ws.write(row, 3, 'day ' + str(_t + 1))
                    ws.write(row, 4, y11[_b][_g][_p][_t])
                    row += 1
    
    row += 1
    ws.write(row, 0, "xb(e,i,j,t) Binary variable representing the departure or non-departure of vehicle I from retailer e to collection center j on day t")
    row += 1
    for _e in range(len(e)):
        ws.write(row, 0, 'retailer '+ str(_e + 1))
        for _i in range(len(i)):
            ws.write(row, 1, 'vehicle '+ str(_i + 1))
            for _j in range(len(j)):
                for _t in range(len(t)):
                    ws.write(row, 2, 'collection-center ' + str(_j + 1))
                    ws.write(row, 3, 'day ' + str(_t + 1))
                    ws.write(row, 4, xb[_e][_i][_j][_t])
                    row += 1

    row += 1
    ws.write(row, 0, "xb1(ix,j,t) Binary variable representing the departure or non-departure of vehicle ix from collection center j to the factory on day t")
    row += 1
    for _ix in range(len(ix)):
        ws.write(row, 0, 'vehicle '+ str(_ix + 1))
        for _j in range(len(j)):
            for _t in range(len(t)):
                ws.write(row, 1, 'collection-center ' + str(_j + 1))
                ws.write(row, 2, 'day ' + str(_t + 1))
                ws.write(row, 3, xb1[_ix][_j][_t])
                row += 1
    

    doc.close()

    return 'result.xlsx'
