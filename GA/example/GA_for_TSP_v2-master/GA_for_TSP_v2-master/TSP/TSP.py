import tsplib95
import tkinter as tk
from tkinter import filedialog
from scipy.spatial import distance
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.optimize import Bounds
import random 
import copy
import matplotlib.pyplot as plt
from timeit import default_timer as timer



#Cumulative number of fitness function evaluations
n_EVALUATIONS = 0

#HYPERPARAMETERS
#---------------

# Initial population size 
INIT_POPULATION_SIZE= 500
# Baseline of individuals selected for the next generation
POPULATION_SIZE = 200

# Maximum number of iterations
MAX_ITERATIONS = 300

# Percentage of crossing between top performant individuals
MATING_RATE=1
# Percentage of the crosse altered by random mutations
MUTATION_RATE=0.15
#Next generation selection strategy.  E for elitism , T for tournament
SELECT_STRATEGY='E'


class Individual(object): 
	''' 
	Class representing individual in population 
	'''
	def __init__(self, chromosome,problem): 
		self.chromosome = chromosome 
		self.fitness = self.cal_fitness(problem)
		self.problem= problem
		

	@classmethod
	def create_genome(self, problem):
		alleles = list(problem.get_nodes())
		np.random.shuffle(alleles)
		return alleles
	
	def mate_pmx(self, par2, problem): 
        #this mating strategy uses partially mapped crossover to
        #avoid unfeasible solutions
		parents=[]
		parents.append(self.chromosome)
		parents.append(par2.chromosome)
		offspring=execute_pmx(parents)
		prob = random.random() 

		if prob < MUTATION_RATE:
			offspring[0] = swap_random(offspring[0])
			offspring[1] = swap_random(offspring[1])
		return offspring

	def cal_fitness(self , problem): 
		global n_EVALUATIONS
		cost=0
		for i in range(0, len(self.chromosome)-1):
			edge = self.chromosome[i], self.chromosome[i+1]
			cost += problem.get_weight(*edge)
		n_EVALUATIONS +=1
		return cost

def execute_pmx(parents):
    #The partially mapped crossover (PMX) was proposed by Goldberg and Lingle [25]. After choosing two random cut points on parents to build offspring, the portion between cut points, 
    #one parent’s string is mapped onto the other parent’s string and the remaining information is exchanged. 

    # P1 (348|271|65)
    # P2 (425|168|37)

    #Then we can fill further bits (from the original parents), for those which have no conflict as follows:#
    #O1= (xxx|168|xx)
    #O2= (xxx|271|xx)

    #Hence, the first  in the first offspring is 8 which comes from first parent but 8 is already in this offspring, so we check mapping  and see again 1 existing in this offspring, again check mapping , so 2 occupies at first ×. Similarly, the second × in first offspring is 6 which comes from first parent but 6 exists in this offspring; we check mapping  as well, so 7 occupies at second . Thus the offspring 1 is
    #O1=(342|168|75)

    #Analogously, we complete second offspring as well:
    #O2=(485|271|36)
    
    if len(parents) != 2:
        raise Exception('The number of parents is not two: {}'.format(len(parents)))

    offspring = [copy.deepcopy(parents[0]), copy.deepcopy(parents[1])]
    permutation_length = len(offspring[0])

    rand = random.random()
    if rand <= 1:
        cross_points = sorted([random.randint(0, permutation_length) for _ in range(2)])

        def _repeated(element, collection):
            c = 0
            for e in collection:
                if e == element:
                    c += 1
            return c > 1

        def _swap(data_a, data_b, cross_points):
            c1, c2 = cross_points
            new_a = data_a[:c1] + data_b[c1:c2] + data_a[c2:]
            new_b = data_b[:c1] + data_a[c1:c2] + data_b[c2:]
            return new_a, new_b

        def _map(swapped, cross_points):
            n = len(swapped[0])
            c1, c2 = cross_points
            s1, s2 = swapped
            map_ = s1[c1:c2], s2[c1:c2]
            for i_chromosome in range(n):
                if not c1 < i_chromosome < c2:
                    for i_son in range(2):
                        while _repeated(swapped[i_son][i_chromosome], swapped[i_son]):
                            map_index = map_[i_son].index(swapped[i_son][i_chromosome])
                            swapped[i_son][i_chromosome] = map_[1 - i_son][map_index]
            return s1, s2

        swapped = _swap(parents[0], parents[1], cross_points)
        mapped = _map(swapped, cross_points)

        offspring[0], offspring[1] = mapped

    return offspring

def swap_random(seq):
    idx = range(len(seq))
    i1, i2 = random.sample(idx, 2)
    seq[i1], seq[i2] = seq[i2], seq[i1]
    return seq


# Driver code 
def main(): 

    global POPULATION_SIZE
    global INIT_POPULATION_SIZE
    global MAX_ITERATIONS

    fits=np.array([])
    evals=np.array([])

    #Load TSP file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title = "Load your .TSP file")
    problem = tsplib95.load(file_path)

    #current generation 
    generation = 1
    found = False
    #list of individuals
    population = [] 

    # create initial population 
    for _ in range(INIT_POPULATION_SIZE): 
        alleles = Individual.create_genome(problem) 
        population.append(Individual(alleles,problem))
    
    start = timer()
    for _ in range(MAX_ITERATIONS):
        # new population size is the baseline plus a decreasing proportion of the initial population
        s = int(POPULATION_SIZE + (INIT_POPULATION_SIZE * (1- (generation/MAX_ITERATIONS))))

        new_generation = []
        
        if SELECT_STRATEGY=='E': #elitism
            # Perform Elitism, that mean SELECTION_RATE % of fittest population 
            # goes to the next generation 
            # sort the population in increasing order of fitness score 
            population = sorted(population, key = lambda x:x.fitness) 
            new_generation.extend(population[:s]) 
        
        elif SELECT_STRATEGY=='T':
            #Perform Tournament selection. take two random individuals with replacement from 
            #the population compare them
            #and take the best to the next generation
            survivors=[]
            for _ in range (s): 
                sparent1, sparent2 = random.sample(population,2) 
                
                if sparent1.fitness < sparent2.fitness: #choose the parent with best fitness
                    survivors.append(sparent1)
                else:
                    survivors.append(sparent2)

            new_generation.extend(survivors)

        else:
            print("Invalid selection strategy")       
              
        for _ in range (s):
            parent1 = random.choice(new_generation) 
            parent2 = random.choice(new_generation) 
            #partially mapped crossover
            offspring = parent1.mate_pmx(parent2, problem) 
            o_zero= Individual(offspring[0],problem)
            o_one= Individual(offspring[1],problem)
            #append only the best offspring to the next generation
            if o_zero.fitness>=o_one.fitness: 
                new_generation.append(o_one)
            else:
                new_generation.append(o_zero)

        population = new_generation 
        fits= np.append(fits,population[0].fitness)
        evals= np.append(evals,n_EVALUATIONS)
        print("Running.... Generation: {}\tGenes: {}\tBest Fitness: {}\tPop. Individuals: {}\tEval: {}".format(generation, population[0].chromosome, population[0].fitness,len(population),n_EVALUATIONS)) 

        generation += 1

    end = timer()
    print("OPTIMIZATION HAS FINISHED: Generation: {}\tGenes: {}\tBest Fitness: {}\tPop. Individua: {}\t# Evaluations: {}\tTime (seconds): {}".format(generation, population[0].chromosome, population[0].fitness,len(population),n_EVALUATIONS,end - start)) 

    #Plot convergence curve
    plt.figure()
    plt.suptitle("Evolution of states and costs of the evolutionary process")
    plt.subplot(121)
    plt.plot(fits, 'r')
    plt.title("Shortest tour distance by generation")
    plt.show()

if __name__ == '__main__': 
    main()
