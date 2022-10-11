import random
import time
from numpy.random import randint
from numpy.random import rand
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
import matplotlib.pyplot as plt
import numpy as np

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
                wb1[vehicle][collection][day] = random.randint(
                    bound[0],  bound[1])

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
                u11[wholesaler][product][day] = random.randint(
                    bound[0],  bound[1])

    u111 = [[[0 for wwx in range(len(t))]
             for wv in range(len(p))] for ww in range(len(e))]
    for retailer in range(len(e)):
        for product in range(len(p)):
            for day in range(len(t)):
                bound = [0, 500]  # inventory bound retailer
                u111[retailer][product][day] = random.randint(
                    bound[0],  bound[1])

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

    return [x, x1, x11, xb, xb1, w, w1, w11, wb, wb1, bo, u1, u_pt, u11, u111, yb, yb1, y, y1, y11, y111]


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

    trans_cost = 0
    for _a in range(len(a)):
        for _v in range(len(Va)):  # TODO: can check Belongs to
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
                    # print(c[_m][_a]) # [[0, 0], [1, 0]]
                    # print(y[_a][_v][_m][_t]) # 80
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

    environ_cost_1 = 0
    for _a in range(len(a)):
        for _v in range(len(v)):
            for _m in range(len(m)):
                for _t in range(len(t)):
                    # print(y[_a][_v][_m][_t])
                    environ_cost_1 += y[_a][_v][_m][_t] # raw from supp to fac
    environ_cost_2 = 0
    for _ix in range(len(ix)):
        for _j in range(len(j)):
            for _m in range(len(m)):
                for _t in range(len(t)):
                    # print(yb1[_ix][_j][_m][_t])
                    environ_cost_2 += yb1[_ix][_j][_m][_t] # raw from coll to fac
    environ_cost = (cinv * environ_cost_1) - (Cinvx * environ_cost_2) # cinv cost of tree cut, cinvx benifit of tree saving
    print(cinv,environ_cost_1, environ_cost_2,Cinvx)
    print('environ cost: ',(cinv * environ_cost_1),(Cinvx * environ_cost_2), environ_cost)

    # constraints
    panalty_cost = 0
    # TODO: add all constraints
    # if anyone of them not meet then add panalty for that soln

    # constraints #1
    # 'Wastage return products'
    #
    # yIII is the number of product transported [veh-whol-retail-day]
    # 𝑢III is the storagte inventory of retailer
    # BR is the % of product that returns from retailer
    # yb is the amount of wooden waste sent from retailer to collection center
    #
    # yIII, uIII, yb
    # (∑∑𝑦III+𝑢III(t-1)−𝑢III)𝐵𝑅 = ∑∑𝑦𝑏; ∀e∈E,p∈P,t∈T
    for _e in range(len(e)):
        for _p in range(len(p)):
            for _t in range(len(t)):
                sum = 0
                for _b in range(len(b)):
                    for _g in range(len(g)):
                        sum += y111[_b][_e][_g][_p][_t]

                try:
                    sum += u111[_e][_p][_t-1]
                except:
                    print('')

                sum -= u111[_e][_p][_t]

                sum = sum * BR[_p][_e]

                for _j in range(len(j)):
                    for _i in range(len(i)):
                        sum -= yb[_e][_i][_j][_p][_t]

                # print('sum: ', sum)
                if sum != 0:
                    panalty_cost += abs(sum)* 2 # 200% palanty
                    # panalty_cost += 1000
                    # print('panalty 1000!')
                # else:
                #     print('') # constraint#1 fully meet!

    # constraints #2
    # 'Recycled materials'
    #
    # 𝛼 material consumption coefficient
    # yb is the amount of wooden waste sent from retailer to collection center
    # ybI is the amount of raw material sent from collection center to factory
    #
    # yb, ybI
    # ∑∑∑𝛼*𝑦𝑏 = ∑𝑦𝑏I; ∀m∈M,j∈J,t∈T
    for _m in range(len(m)):
        for _j in range(len(j)):
            for _t in range(len(t)):

                sum = 0
                for _e in range(len(e)):
                    for _i in range(len(i)):
                        for _p in range(len(p)):
                            sum += alpha[_m][_p] * yb[_e][_i][_j][_p][_t]

                for _ix in range(len(ix)):
                    sum -= yb1[_ix][_j][_m][_t]
                
                if sum != 0:
                    panalty_cost += abs(sum)* 2 # 200% palanty

    # constraints #3
    for _t in range(len(t)):

        sum = 0
        for _m in range(len(m)):
            # TODO: re-structure input
            sum += I[_m][0]*u1[_m][_t]
        
        sum -= cp

        # print(sum)
        if sum > 0:
            panalty_cost += abs(sum)*2

    # constraints #4
    for _t in range(len(t)):

        sum = 0
        for _p in range(len(p)):
            # TODO: re-structure input
            sum += Ix[_p][0]*u_pt[_p][_t]
        
        sum -= cpx

        # print(sum)
        if sum > 0:
            panalty_cost += abs(sum)*2

    # constraints #5
    for _b in range(len(b)):
        for _t in range(len(t)):

            sum = 0
            for _p in range(len(p)):
                # TODO: re-structure input
                # print(Ix[_p][0])
                # print(u1[_b][_p][_t])
                sum += Ix[_p][0]*u11[_b][_p][_t]
            
            # TODO: re-structure input
            sum -= cpxx[_b][0]

            # print(sum)
            if sum > 0:
                panalty_cost += abs(sum)*2

    # constraints #6
    # 80% duplicate constraint with #7
    # for _t in range(len(t)):
    #     for _m in range(len(m)):

    #         sum = 0

    #         for _a in range(len(a)):
    #             for _v in range(len(v)):
    #                 sum += y[_a][_v][_m][_t]
            
    #         try:
    #             sum += u1[_m][_t-1]
    #         except:
    #             print('index out range')
            
    #         for _p in range(len(p)):
    #             sum -= alpha[_m][_p]*y1[_p][_t]
            
    #         sum -= u1[_m][_t]

    #         if sum != 0:
    #                 panalty_cost += abs(sum)* 2 # 200% palanty

    # constraints #7
    for _t in range(len(t)):
        for _m in range(len(m)):

            sum = 0

            for _a in range(len(a)):
                for _v in range(len(v)):
                    sum += y[_a][_v][_m][_t]
            
            for _j in range(len(j)):
                for _ix in range(len(ix)):
                    sum += yb1[_ix][_j][_m][_t]
            
            try:
                sum += u1[_m][_t-1]
            except:
                print('index out range')
            
            for _p in range(len(p)):
                sum -= alpha[_m][_p]*y1[_p][_t]
            
            sum -= u1[_m][_t]
            
            if sum != 0:
                    panalty_cost += abs(sum)* 2 # 200% palanty

    # constraints #8
    for _p in range(len(p)):
        for _t in range(len(t)):

            sum = 0

            sum += y1[_p][_t]

            try:
                sum += u1[_p][_t-1]
            except:
                print('index out range')

            for _b in range(len(b)):
                for _g in range(len(g)):
                    sum -= y11[_b][_g][_p][_t]
            sum -= u1[_p][_t]

            if sum != 0:
                    panalty_cost += abs(sum)* 2 # 200% palanty

    # constraints #9
    for _b in range(len(b)):
        for _p in range(len(p)):
            for _t in range(len(t)):

                sum = 0

                for _g in range(len(g)):
                    sum += y11[_b][_g][_p][_t]
                
                try:
                    sum += u11[_b][_p][_t-1]
                except:
                    print('index out range')
                
                for _e in range(len(e)):
                    for _g in range(len(g)):
                        sum -= y111[_b][_e][_g][_p][_t]

                sum -= u11[_b][_p][_t]

                if sum != 0:
                    panalty_cost += abs(sum)* 2 # 200% palanty

    # constraints #10
    for _e in range(len(e)):
        for _p in range(len(p)):
            for _t in range(len(t)):

                sum = 0

                for _b in range(len(b)):
                    for _g in range(len(g)):
                        sum += y111[_b][_e][_g][_p][_t]

                try:
                    sum += u111[_e][_p][_t-1]
                except:
                    print('index out range')
                
                sum += bo[_e][_p][_t]

                sum -= dem[_e][_p][_t]
                sum -= u111[_e][_p][_t]

                if sum != 0:
                    panalty_cost += abs(sum)* 2 # 200% palanty

    # constraints #11
    for _b in range(len(b)):
        for _f in range(len(f)):
            for _t in range(len(t)):

                sum = 0

                sum += w1[_b][_f][_t]

                sum -= M*x1[_b][_f][_t]

                if sum > 0:
                    panalty_cost += abs(sum)*2

    # constraints #12
    for _b in range(len(b)):
        for _e in range(len(eb)):
            for _g in range(len(Gb)):
                for _t in range(len(t)):
                    sum = 0
                    sum += w11[_b][_e][_g][_t]
                    sum -= BigM*x11[_b][_e][_g][_t]
                    if sum > 0:
                        panalty_cost += abs(sum)*2

    # constraints #13
    for _j in range(len(j)):
        for _i in range(len(i)):
            for _e in range(len(hj)):
                for _t in range(len(t)):
                    sum = 0
                    sum += wb[_e][_i][_j][_t]
                    sum -= M*xb[_e][_i][_j][_t]
                    if sum > 0:
                        panalty_cost += abs(sum)*2

    # constraints #14
    for _a in range(len(a)):
        for _v in range(len(Va)):
            for _t in range(len(t)):
                sum = 0
                # TODO: re-structure input
                sum += w[_a][_v][_t]*T[_a][0]
                sum -= Hd*x[_a][_v][_t]
                if sum > 0:
                        panalty_cost += abs(sum)*2

    # constraints #15
    for _f in range(len(f)):
        for _t in range(len(t)):
            sum = 0
            for _b in range(len(b)):
                # TODO: re-structure input
                sum += w1[_b][_f][_t]*Tx[_b][0]
            sum -= Hd
            if sum > 0:
                panalty_cost += abs(sum)*2

    # constraints #16
    for _b in range(len(b)):
        for _g in range(len(Gb)):
            for _t in range(len(t)):
                sum = 0
                for _e in range(len(e)):
                    sum += w11[_b][_e][_g][_t]*Txx[_b][_e]
                sum -= Hd
                if sum > 0:
                    panalty_cost += abs(sum)*2

    # constraints #17
    for _i in range(len(i)): # TODO: ij giving out of range
        for _j in range(len(j)):
            for _t in range(len(t)):
                sum = 0
                for _e in range(len(e)): # TODO: hj
                    # TODO: re-structure input
                    
                    # TypeError: 'int' object is not subscriptable
                    # meaning that you dis-order sequence

                    # print(wb[_e][_i][_j][_t])
                    # print(Ts[_e][_j])

                    sum += wb[_e][_i][_j][_t]*Ts[_e][_j]
                sum -= Hd
                if sum > 0:
                    panalty_cost += abs(sum)*2
                    
    # constraints #18
    for _ix in range(len(ix)): # TODO: ij giving out of range
        for _j in range(len(j)):
            for _t in range(len(t)):
                sum = 0
                # TODO: re-structure input
                sum += wb1[_ix][_j][_t]*Tsx[_j][0]
                sum -= Hd*xb1[_ix][_j][_t]
                if sum > 0:
                    panalty_cost += abs(sum)*2

    # constraints #19
    for _a in range(len(a)):
        for _v in range(len(Va)):
            for _t in range(len(t)):
                sum = 0
                for _m in range(len(m)):
                    # TODO: ij giving out of range
                    sum += I[_m][0]*y[_a][_v][_m][_t]

                # TODO: ij giving out of range
                sum -= vol[_v][0]*w[_a][_v][_t]
                if sum > 0:
                    panalty_cost += abs(sum)*2

    # constraints #20
    for _b in range(len(b)):
        for _f in range(len(f)):
            for _g in range(len(Gb)):
                for _t in range(len(t)):
                    sum = 0
                    for _p in range(len(p)):
                        # TODO: ij giving out of range
                        sum += Ix[_p][0]*y11[_b][_g][_p][_t]

                    # TODO: ij giving out of range
                    sum -= volx[_f][0]*w1[_b][_f][_t]
                    if sum > 0:
                        panalty_cost += abs(sum)*2

    # constraints #21
    for _b in range(len(b)):
        for _e in range(len(eb)):
            for _g in range(len(Gb)):
                for _t in range(len(t)):
                    sum = 0
                    for _p in range(len(p)):
                        # TODO: ij giving out of range
                        sum += Ix[_p][0]*y111[_b][_e][_g][_p][_t]
                    
                    # TODO: ij giving out of range
                    sum -= volxx[_g][0]*w11[_b][_e][_g][_t]
                    if sum > 0:
                        panalty_cost += abs(sum)*2

    # constraints #22
    for _e in range(len(e)): # TODO: Ej
        for _i in range(len(i)): # TODO: ij
            for _j in range(len(j)):
                for _t in range(len(t)):
                    sum = 0
                    for _p in range(len(p)):
                        # TODO: ij giving out of range
                        sum += Ix[_p][0]*yb[_e][_i][_j][_p][_t]

                    # TODO: ij giving out of range                    
                    sum -= Sp[_g][0]*wb[_e][_i][_j][_t]
                    if sum > 0:
                        panalty_cost += abs(sum)*2

    # constraints #23
    for _ix in range(len(ix)): # TODO: ij
        for _j in range(len(j)):
            for _t in range(len(t)):
                sum = 0
                for _m in range(len(m)):
                    # TODO: ij giving out of range
                    sum += I[_m][0]*yb1[_ix][_j][_m][_t]

                # TODO: ij giving out of range
                sum -= Spx[_ix][0]*wb1[_ix][_j][_t]
                if sum > 0:
                    panalty_cost += abs(sum)*2

    # objective function
    z = trans_cost + purchas_cost + prod_cost + maintain_cost + \
        shortage_cost + environ_cost + panalty_cost
    analysis_result = (trans_cost, purchas_cost, prod_cost, maintain_cost, shortage_cost, environ_cost)
    # print('z: ', z) # TODO: all are 386390 wired!
    if (z == 0):
        return 9999999, z
    return 1/z, z, analysis_result

# tournament selection or
# parent selection base on best value


def selection(pop, scores, k=3):
    # first random selection
    selection_ix = randint(len(pop))
    for ix_123 in randint(0, len(pop), k - 1):
        # check if better (e.g. perform a tournament)
        if scores[ix_123] < scores[selection_ix]:
            selection_ix = ix_123
    return pop[selection_ix]

# crossover two parents to create two children
# by copy or mixing the parent (recombination)


def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        pt = randint(1, len(p1) - 2)
        # perform crossover
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]

# mutation operator
# reversion and swap method
# pass parent1 for child1
# pass parent2 for child2
def mutation(p, child, r_mut):
    # randomly choose 2 index between gen len
    # swap index from parent to child
    
    indexx_1_mut = random.randint(0,  len(p)-1)
    indexx_2_mut = random.randint(0,  len(p)-1)
    if rand() < r_mut:
        # swap the index
        child[indexx_1_mut] = p[indexx_1_mut]
        child[indexx_2_mut] = p[indexx_2_mut]
        
    # reversion you can do a loop
    # index1+1 index2-1
    # swap index from parent to child

def ga():
    start_time = time.time()
    # define ga
    global population_size, generation_size, mutation_rate, cross_rate
    population_size = 10
    generation_size = 2
    cross_rate = 0.9
    mutation_rate = 0.3

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
    # ---

    init_pop = []

    for _ in range(population_size):
        _random_pop = random_population(boundaries)
        init_pop.append(_random_pop)

    # z_fun=fitness_function(init_pop[0])
    # print(z_fun)
    # return

    next_pop = []
    best_of_each_gen = [0]
    best, best_eval = 0, fitness_function(init_pop[0])[0]
    optimize_value = 0
    analysis_value = (0,0,0,0,0,0) # trans, purchas, prod, mainten, short, envir

    for idx in range(generation_size):
        curr_pop = []
        if idx == 0:
            curr_pop = init_pop
        else:
            curr_pop = next_pop

        # this_gen_topper = 0
        # this_gen_topper_score = 0
        this_gen_scrors = [fitness_function(curr_pop[pop_idx])[
            0] for pop_idx in range(population_size)]

        # check for new best solution
        for indxx in range(population_size):
            if this_gen_scrors[indxx] > best_eval:
                best, best_eval = curr_pop[indxx], this_gen_scrors[indxx]
                _fit_val =fitness_function(curr_pop[indxx])
                optimize_value = _fit_val[1]
                analysis_value = _fit_val[2]
                # this_gen_topper = best
                # this_gen_topper_score = best_eval

        selected = [selection(curr_pop, this_gen_scrors)
                    for _ in range(population_size)]

        children = list()
        for idxe in range(0, population_size, 2):
            # get selected parents in pairs
            p1, p2 = selected[idxe], selected[idxe + 1]
            # crossover and mutation
            mut_indx=0
            for cross_21 in crossover(p1, p2, cross_rate):
                # mutation
                if mut_indx==0:
                    mutation(p1, cross_21, mutation_rate)
                else:
                    mutation(p2, cross_21, mutation_rate)
                # store for next generation
                children.append(cross_21)
                mut_indx+=1

        # replace population
        next_pop = children

        # for pp in range(population_size):

        # _fitness = fitness_function(init_pop[pp])
        # this_gen_scrors.append(_fitness[0])

        # p1 = fitness_function(init_pop[0])
        # p2 = fitness_function(init_pop[1])

        # score = 0
        # soln = []
        # if (p2[0] > p1[0]):
        #     score = p2[1]
        #     soln = init_pop[1]
        # else:
        #     score = p1[1]
        #     soln = init_pop[0]

        # print('score:', score)  # which has more fitness value
        # print('soln gen:', soln)

        this_gen_scrors.sort()
        this_gen_topper_score = this_gen_scrors[len(this_gen_scrors)-1]
        best_of_each_gen.append(this_gen_topper_score)
        print('gen#: ', idx+1)

    # res = _write_result(soln, score)
    # print(res)

    res = _write_result(best, optimize_value, analysis_value)
    print(res)

    xaxis = np.array(list(range(0, generation_size+1)))
    yaxis = np.array(best_of_each_gen)
    # # print(xaxis)
    # # print(yaxis)
    plt.plot(xaxis, yaxis)
    print("Completed! in: %.2fs" % (time.time() - start_time))
    plt.show()


ga()
