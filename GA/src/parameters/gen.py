import random
from cd import get as _cd
from chxx import get as _chxx
from chxxx import get as _chxxx
from constants import get as _constants
from cr import get as _cr
from cz import get as _cz
from dem import get as _dem
from f import get as _f
from normal_table import get as _normal_table
from P import get as _P
from result import write as _write_result
from utils import convert_to_tuple

# create random solution


def random_population(boundary):

    # Binary
    x = [[[0 for wwx in range(len(t))] for wv in range(len(v))]
         for ww in range(len(a))]
    for supplier in range(len(a)):
        for vehicle in range(len(v)):
            for day in range(len(t)):
                x[supplier][vehicle][day] = random.randint(0, 1)

    x1 = [[[0 for wwx in range(len(t))] for wv in range(len(f))]
          for ww in range(len(b))]
    for wholesaler in range(len(b)):
        for vehicle in range(len(f)):
            for day in range(len(t)):
                x1[wholesaler][vehicle][day] = random.randint(0, 1)

    x11 = [[[[0 for wwx in range(len(t))] for wv in range(len(g))]
            for uxx in range(len(e))] for ww in range(len(b))]
    for wholesaler in range(len(b)):
        for retailer in range(len(e)):
            for vehicle in range(len(g)):
                for day in range(len(t)):
                    x11[wholesaler][retailer][vehicle][day] = random.randint(
                        0, 1)

    xb = [[[[0 for wwx in range(len(t))] for wv in range(len(j))]
           for uxx in range(len(i))] for ww in range(len(e))]
    for wholesaler in range(len(e)):
        for vehicle in range(len(i)):
            for collection in range(len(j)):
                for day in range(len(t)):
                    xb[wholesaler][vehicle][collection][day] = random.randint(
                        0, 1)

    xb1 = [[[0 for wwx in range(len(t))] for wv in range(len(j))]
           for ww in range(len(ix))]
    for vehicle in range(len(ix)):
        for collection in range(len(j)):
            for day in range(len(t)):
                xb1[vehicle][collection][day] = random.randint(0, 1)
    # ---

    # Positive
    w = [[[0 for wwx in range(len(t))] for wv in range(len(v))]
         for ww in range(len(a))]
    for supplier in range(len(a)):
        for vehicle in range(len(v)):
            for day in range(len(t)):
                bound = [0, 10]  # trip bound
                w[supplier][vehicle][day] = random.randint(bound[0],  bound[1])

    w1 = [[[0 for wwx in range(len(t))] for wv in range(len(f))]
          for ww in range(len(b))]
    for wholesaler in range(len(b)):
        for vehicle in range(len(f)):
            for day in range(len(t)):
                bound = [0, 10]  # trip bound
                w1[wholesaler][vehicle][day] = random.randint(
                    bound[0],  bound[1])

    w11 = [[[[0 for wwx in range(len(t))] for wv in range(len(g))]
            for uxx in range(len(e))] for ww in range(len(b))]
    for wholesaler in range(len(b)):
        for retailer in range(len(e)):
            for vehicle in range(len(g)):
                for day in range(len(t)):
                    bound = [0, 10]  # trip bound
                    w11[wholesaler][retailer][vehicle][day] = random.randint(
                        bound[0],  bound[1])

    wb = [[[[0 for wwx in range(len(t))] for wv in range(len(j))]
           for uxx in range(len(i))] for ww in range(len(e))]
    for wholesaler in range(len(e)):
        for vehicle in range(len(i)):
            for collection in range(len(j)):
                for day in range(len(t)):
                    bound = [0, 10]  # trip bound
                    wb[wholesaler][vehicle][collection][day] = random.randint(
                        bound[0],  bound[1])

    wb1 = [[[0 for wwx in range(len(t))] for wv in range(len(j))]
           for ww in range(len(ix))]
    for vehicle in range(len(ix)):
        for collection in range(len(j)):
            for day in range(len(t)):
                bound = [0, 10]  # trip bound
                wb1[vehicle][collection][day] = random.randint(bound[0],  bound[1])

    # postponed orders
    bo = [[[0 for wwx in range(len(t))] for wv in range(len(p))]
          for ww in range(len(e))]
    for retailer in range(len(e)):
        for product in range(len(p)):
            for day in range(len(t)):
                bound = [0, 100]  # postponed orders bound
                bo[retailer][product][day] = random.randint(
                    bound[0],  bound[1])

    u1 = [[0 for wwx in range(len(t))] for wv in range(len(m))]
    for material in range(len(m)):
        for day in range(len(t)):
            bound = [0, 2000]  # inventory bound factory
            u1[material][day] = random.randint(bound[0],  bound[1])

    u_pt = [[0 for wwx in range(len(t))] for wv in range(len(p))]
    for product in range(len(p)):
        for day in range(len(t)):
            bound = [0, 3000]  # inventory bound factory
            u_pt[product][day] = random.randint(bound[0],  bound[1])

    u11 = [[[0 for wwx in range(len(t))] for wv in range(len(p))]
           for ww in range(len(b))]
    for wholesaler in range(len(b)):
        for product in range(len(p)):
            for day in range(len(t)):
                bound = [0, 1000]  # inventory bound wholesaler
                u11[wholesaler][product][day] = random.randint(bound[0],  bound[1])

    u111 = [[[0 for wwx in range(len(t))]
             for wv in range(len(p))] for ww in range(len(e))]
    for retailer in range(len(e)):
        for product in range(len(p)):
            for day in range(len(t)):
                bound = [0, 500]  # inventory bound retailer
                u111[retailer][product][day] = random.randint(bound[0],  bound[1])

    yb = [[[[[0 for wwx in range(len(t))] for wwx in range(len(p))] for wv in range(
        len(j))] for uxx in range(len(i))] for ww in range(len(e))]
    for wholesaler in range(len(e)):
        for vehicle in range(len(i)):
            for collection in range(len(j)):
                for product in range(len(p)):
                    for day in range(len(t)):
                        bound = [0, 100]  # product sent bound from retailer
                        yb[wholesaler][vehicle][collection][product][day] = random.randint(
                            bound[0],  bound[1])

    yb1 = [[[[0 for wwx in range(len(t))] for wv in range(
        len(m))] for swv in range(len(j))] for cwv in range(len(ix))]
    for vehicle in range(len(ix)):
        for collection in range(len(j)):
            for material in range(len(m)):
                for day in range(len(t)):
                    bound = [0, 150]  # inventory bound collection center
                    yb1[vehicle][collection][material][day] = random.randint(
                        bound[0],  bound[1])

    y = [[[[0 for wwx in range(len(t))] for wv in range(len(m))]
          for wvf in range(len(v))] for wwsd in range(len(a))]
    for supplier in range(len(a)):
        for vehicle in range(len(v)):
            for material in range(len(m)):
                for day in range(len(t)):
                    bound = [0, 600]  # supplier bound
                    y[supplier][vehicle][material][day] = random.randint(
                        bound[0],  bound[1])

    y1 = [[0 for wwx in range(len(t))] for wv in range(len(p))]
    for product in range(len(p)):
        for day in range(len(t)):
            bound = [0, 300]  # mfg. product bound
            y1[product][day] = random.randint(bound[0],  bound[1])

    y11 = [[[[0 for wwx in range(len(t))]for uxx in range(
        len(p))] for wv in range(len(g))] for ww in range(len(b))]
    for wholesaler in range(len(b)):
        for vehicle in range(len(g)):
            for product in range(len(p)):
                for day in range(len(t)):
                    bound = [0, 200]  # product sent bound from factory
                    y11[wholesaler][vehicle][product][day] = random.randint(
                        bound[0],  bound[1])

    y111 = [[[[[0 for wwx in range(len(t))]for uxx in range(len(p))] for wv in range(
        len(g))] for ww in range(len(e))]for wsw in range(len(b))]
    for wholesaler in range(len(b)):
        for retailer in range(len(e)):
            for vehicle in range(len(g)):
                for product in range(len(p)):
                    for day in range(len(t)):
                        bound = [0, 160]  # product sent bound from wholesaler
                        y111[wholesaler][retailer][vehicle][product][day] = random.randint(
                            bound[0],  bound[1])

    return x, x1, x11, xb, xb1, w, w1, w11, wb, wb1, bo, u1, u_pt, u11, u111, yb, yb1, y, y1, y11, y111


def fitness_function(gen):
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

    panalty_cost = 0  # TODO: add constraints

    trans_cost = 0
    for _a in range(len(a)):
        for _v in range(len(Va)): # TODO: can check Belongs to
            for _t in range(len(t)):
                trans_cost += cx[_a][_v] * x[_a][_v][_t]
    for _a in range(len(a)):
        for _v in range(len(Va)):
            for _m in range(len(m)):
                for _t in range(len(t)):
                    trans_cost += cxx[_a][_m] * y[_a][_v][_m][_t]
    for _b in range(len(b)):
        for _f in range(len(f)):
            for _t in range(len(t)):
                trans_cost += cs[_b][_f] * x1[_b][_f][_t]
    for _b in range(len(b)):
        for _g in range(len(g)):
            for _p in range(len(p)):
                for _t in range(len(t)):
                    trans_cost += cf[_b][_p] * y11[_b][_g][_p][_t]
    for _b in range(len(b)):
        for _e in range(len(e)):
            for _g in range(len(g)):
                for _t in range(len(t)):
                    trans_cost += cr[_b][_e][_g] * x11[_b][_e][_g][_t]
    for _b in range(len(b)):
        for _e in range(len(e)):
            for _g in range(len(g)):
                for _p in range(len(p)):
                    for _t in range(len(t)):
                        trans_cost += cd[_b][_e][_p] * y111[_b][_e][_g][_p][_t]
    for _e in range(len(e)):
        for _i in range(len(i)):
            for _j in range(len(j)):
                for _t in range(len(t)):
                    trans_cost += fxd[_e][_i][_j] * xb[_e][_i][_j][_t]
    for _e in range(len(e)):
        for _i in range(len(i)):
            for _j in range(len(j)):
                for _p in range(len(p)):
                    for _t in range(len(t)):
                        trans_cost += cz[_e][_j][_p]*yb[_e][_i][_j][_p][_t]
    # print(fx) # ([60], [60])
    # print(xb1) # [[[0, 0], [1, 0]], [[0, 1], [0, 1]]]
    for _ix in range(len(ix)):
        for _j in range(len(j)):
            for _t in range(len(t)):
                # TODO: fix range issue
                # vehicle loop insert
                # trans_cost += fx[_ix][_j]*xb1[_ix][_j][_t]
                trans_cost += fx[_j][0]*xb1[_ix][_j][_t]
    for _ix in range(len(ix)):
        for _j in range(len(j)):
            for _m in range(len(m)):
                for _t in range(len(t)):
                    trans_cost += czx[_j][_m]*yb1[_ix][_j][_m][_t]
    # print('transportation cost: ', trans_cost)

    purchas_cost = 0
    for _a in range(len(a)):
        for _v in range(len(Va)):
            for _m in range(len(m)):
                for _t in range(len(t)):
                    purchas_cost += c[_m][_a] * y[_a][_v][_m][_t]
    for _e in range(len(e)):
        for _i in range(len(i)):
            for _j in range(len(j)):
                for _p in range(len(p)):
                    for _t in range(len(t)):
                        purchas_cost += ck[_e][_p]*yb[_e][_i][_j][_p][_t]
    # print('purchasing cost: ', purchas_cost)

    prod_cost = 0
    for _p in range(len(p)):
        for _t in range(len(t)):
            # TODO: single line input data re-structure
            prod_cost += ct[_p][0]*y1[_p][_t]
    # print('production cost: ', prod_cost)

    maintain_cost = 10
    for _m in range(len(m)):
        for _t in range(len(t)):
            maintain_cost += ch[_m][_t] * u1[_m][_t]
    for _p in range(len(p)):
        for _t in range(len(t)):
            maintain_cost += chx[_p][0]*u_pt[_p][_t]
    for _b in range(len(b)):
        for _p in range(len(p)):
            for _t in range(len(t)):
                maintain_cost += chxx[_b][_p][_t]*u11[_b][_p][_t]
    for _e in range(len(e)):
        for _p in range(len(p)):
            for _t in range(len(t)):
                maintain_cost += chxxx[_e][_p][_t]*u111[_e][_p][_t]
    # print('maintain cost: ', maintain_cost)

    shortage_cost = 0
    for _e in range(len(e)):
        for _p in range(len(p)):
            for _t in range(len(t)):
                shortage_cost += P[_e][_p][_t]*bo[_e][_p][_t]
    # print('shortage cost: ', shortage_cost)

    environ_cost = 0
    for _a in range(len(a)):
        for _v in range(len(v)):
            for _m in range(len(m)):
                for _t in range(len(t)):
                    environ_cost += y[_a][_v][_m][_t]
    for _ix in range(len(ix)):
        for _j in range(len(j)):
            for _m in range(len(m)):
                for _t in range(len(t)):
                    environ_cost -= yb1[_ix][_j][_m][_t]
    # print('environ cost: ', shortage_cost)

    # objective function
    z = trans_cost + purchas_cost + prod_cost + maintain_cost + \
        shortage_cost + environ_cost + panalty_cost

    print('z: ', z)
    if (z == 0):
        return 9999999
    return 1/z, z


def ga():
    # define ga
    global population_size
    population_size = 100

    # define parameters
    global T, Tx, Txx, ct, cs, cf, cpxx, alpha, I, Ix, ch, Ts, Tsx, ck, fx, czx, Sp, chx, Spx, cab, BR, c, cx, cxx, vol, volx, volxx, cd, chxx, chxxx, cr, cz, dem, fxd, P, cinv, Cinvx, M, BigM, Hd, cp, cpx, boundaries
    cd = _cd()
    chxx = _chxx()
    chxxx = _chxxx()
    cr = _cr()
    cz = _cz()
    dem = _dem()
    fxd = _f()  # * remaned
    P = _P()
    cinv, Cinvx, M, BigM, Hd, cp, cpx = _constants()
    T, Tx, Txx, ct, cs, cf, cpxx, alpha, I, Ix, ch, Ts, Tsx, ck, fx, czx, Sp, chx, Spx, cab, BR, c, cx, cxx, vol, volx, volxx = _normal_table()
    boundaries = []  # TODO: pass bound from here and input bound from sheet
    # ---

    # define index size
    global a, b, e, eb, f, g, Gb, i, ix, ixx, j, ij, hj, m, p, t, v, Va, Bapm, ixj

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
    # ---

    init_pop = []

    for _ in range(population_size):
        _random_pop = random_population(boundaries)
        init_pop.append(_random_pop)

    p1 = fitness_function(init_pop[0])
    p2 = fitness_function(init_pop[1])

    score = 0
    soln = []
    if (p2[0] > p1[0]):
        score = p2[1]
        soln = init_pop[1]
    else:
        score = p1[1]
        soln = init_pop[0]

    print('score:', score)  # which has more fitness value
    # print('soln gen:', soln)

    res = _write_result(soln, score)
    print(res)


ga()
