# genetic algorithm search for continuous function optimization
from numpy.random import randint
from numpy.random import rand


# objective function
def objective(x):
    return x[0] ** 2.0 + x[1] ** 2.0 # x1squar + x2squar


# decode bitstring to numbers/how many variable inside
# that bitstring
# WHY bitstring to numbers is IMPORTANT🚨
# A: Because we need the real or int number 
#    to calculate objective function
#
# Powerful decoder for N number of variable inside a cromosome
# bounds:(array[array]) is holding upper and lower bounds of each variable
# n_bits:(int) is the length of bits per variable, equal for all variable
# bitstring:(array) is your cromosome where you put all the variables sequencially in bit from
#
# guessing you have sequencially put variables in bounds and bitstring
# but maybe you can ignore this logic
# but what you will get in decoded array list is according to your bound sequence
def decode(bounds, n_bits, bitstring):
    decoded = list() # all decoded value will be stored here

    largest = 2 ** n_bits # the possible largest value of this given bit size/variable/index

    for i in range(len(bounds)): # `bounds` actually means number of variable in this bitstring/cromosome

        # extract the substring
        start, end = i * n_bits, (i * n_bits) + n_bits
        # guess n_bits = 10
        # 0, 10
        # 10, 20
        # 20, 30
        # 30, 40
        # .., ..
        # actually we are spliting cromosome to identify the index variable
        # and then decode it to get what is the number denoting that string

        # we are taking that portion of cromosome
        # we are cutting the bitstring equally here!!
        substring = bitstring[start:end]
        # output: [1,0,1,0,1,0,1]

        # convert bitstring to a string of chars
        chars = ''.join([str(s) for s in substring])
        # output: 1010101

        # convert string to integer 
        # using built-in method int(binaryString,2)
        # 2 denotes binary conversion
        integer = int(chars, 2) # convert binary to int;
        # note: you can convert decimal instead if required using
        # raw How to convert binary to decimal method.
        # output: 85

        # scale integer to desired range
        # value = lowerBound + ratio * range
        # value = -6 + .5 * 12 = 0
        # value = -6 + .1 * 12 = -4.8
        # value = -6 + 1 * 12 = 6
        # cause:
        # that means the value could only very within this given range 
        # not more or less than that varibale range
        value = bounds[i][0] + (integer / largest) * (bounds[i][1] - bounds[i][0])
        # (bounds[i][1] - bounds[i][0]) = bound interval distance
        # x = -6
        # x = 6
        # bound = []
        # bound[0]=[-6,6]
        # bound[0][0]=-6
        # bound[0][1]=6
        # value = -6 + (85/127)*(6-(-6)) = -6 + 12 = 6

        # already decoded
        # store
        decoded.append(value)
    return decoded


# tournament selection
# if you don't pass k
# it will guess 3
def selection(population, scores, k=3):
    # first select random people
    selection_ix = randint(len(population))

    # k = number of randomness
    # select 2 other people randomly
    # test there score
    # who has better score choose him
    for ix in randint(0, len(population), k - 1):
        # check score
        if scores[ix] < scores[selection_ix]:
            # if score is higher select him
            selection_ix = ix
    
    # return selected one
    return population[selection_ix]


# crossover two parents to create two children
def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    
    # check propability of recombination
    if rand() < r_cross:
        # select crossover point 
        # but not at the last bit
        point = randint(1, len(p1) - 2)
        
        # perform crossover
        c1 = p1[:point] + p2[point:]
        c2 = p2[:point] + p1[point:]

    return [c1, c2]


# mutation
def mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        # check propability of mutation
        if rand() < r_mut:
            # flip bits
            bitstring[i] = 1 - bitstring[i]


# genetic algorithm
# genetic algorithm takes objective function 
# and algorithm parameters
def genetic_algorithm(objective, bounds, n_bits, n_iter, no_of_population, r_cross, r_mut):
    # initial population of random bitstring array [[1,2,3],[2,1,3]..] list of list
    # this is a bit array
    #
    # randint gives you an array but we want list
    # IF WE DON'T SAY .tolist() it will give you [array([1, .. 1]), array([1,..])] list of array
    # we don't want array object we want list obj
    # like this: [[1,2,3],[2,1,3]..] list of list
    # so use tolist() with randint
    # the 3rd argument of randinit is the shape
    # and first 2 are the range to pick an int
    population = [randint(0, 2, n_bits * len(bounds)).tolist() for _ in range(no_of_population)]
    # we are generating bitstring
    # randint within value [0,2] which means 0,1 only and 
    # the length of that array will be no_of_bits_per_variable*variables_length
    
    # track the best solution
    # taking population's first bit array and generate a number accordingly then pass it 
    # to objective func and store it as the best_eval for now
    # decoded and returns two value as array [val1, val2] and pass it to objective func
    # and this obj func only can handle pos1 and pos2
    # that's mean if you write different objective function with pos3 exist then it will git you an error
    # 🚨Q. does our objective function has more than 2 pos used?
    top_result, generations_topper = 0, objective(decode(bounds, n_bits, population[0]))

    # iterate generations
    for gen in range(n_iter):
        
        # decode population
        # this is now a number array
        # this number is generated from previous population's each bit array
        # 🚨each array contains two numbers why??
        decoded = [decode(bounds, n_bits, p) for p in population]

        # calculate objective value of each population
        # score list
        scores = [objective(d) for d in decoded]

        # check who is the best
        for i in range(no_of_population):
            if scores[i] < generations_topper:
                # store this people who got the lowest value
                top_result, generations_topper = population[i], scores[i]
                # print("gen: %d decode: f(%s) = %f new best soln" % (gen, decoded[i], scores[i]))

        # select parents
        # passing peoples and people's scores each time
        # and randomly two people value checked and and passed the highter one people
        # bit people
        # select 100x times
        selected = [selection(population, scores) for _ in range(no_of_population)]

        # create the next generation
        # store babies
        children = list()

        # select 2 parents
        # couple interval
        for i in range(0, no_of_population, 2):
            
            # couple:
            # these people are previously selected
            # now we just sequencially select 2 of them
            # to make a couple
            p1, p2 = selected[i], selected[i + 1]
            
            # cross with mutation
            # crossing here! 
            # it returns 2 child
            # that means this loop will do 2 times
            for bitstr in crossover(p1, p2, r_cross):
                
                # mutation and randomly bit flips on any position
                
                # 🚨why it dosen't impact the result?
                # because we choose 100 population and selecting
                # the best one.

                # mutation here!
                # bitstr holds 2 child
                mutation(bitstr, r_mut) # it doesn't return anything
                # because we work with the current bitstring
                
                # next gen child
                # add one child
                children.append(bitstr)

            # finish producing 2 child
            # loop pop/2=50 times
            # give you again 100 children

        # finish generating new population
        # now
        # replace old population
        population = children
        # loop for next gen
    
    # finished iteration loop

    # return best result among all generation
    return [top_result, generations_topper]


# define range for input
input_bounds = [[-5.0, 5.0], [-5.0, 5.0]]

# define the total iterations
no_of_iteration = 100

# bits per variable
no_of_bits = 16 # equal as 0-655356 range
# no_of_bits range should be greater than you max variable bound 

# define the population size
no_of_population = 100

# crossover rate
cross_rate = 0.9

# mutation rate
mutation_rate = 1.0 / (float(no_of_bits) * len(input_bounds))

# perform the genetic algorithm search
best, score = genetic_algorithm(objective, input_bounds, no_of_bits, no_of_iteration, no_of_population, cross_rate, mutation_rate)
# print('Done!')
decoded = decode(input_bounds, no_of_bits, best)
# print('solution: f(%s) = %f ans.' % (decoded, score))
print('result: f(%s,%s) Z= %f' % (decoded[0], decoded[1], score))
