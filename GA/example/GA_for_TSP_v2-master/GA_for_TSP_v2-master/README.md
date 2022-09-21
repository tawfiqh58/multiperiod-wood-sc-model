# GA_for_TSP_v2
Genetic Optimization Algorithm for Travelling Salesman Problems
-Mariano Crimi

## Description
This script takes a TSP standard file an attempts to solve the travelling salesman problem described in the file using genetic algorithms

## Requirements
1. Python 3.7
2. Libraries
   - tsplib95
   - tkinter
   - scypy

## Run the script
1) Install required libraries
2) Directly run the script **TSP\TSP.py** or open the VS solution (TSP.sln) and run.
3) Select a valid TSP file (Djbuti and Qatar are added to this repository

## Algorithm
Rationale for GA
Given that TSP's are in essence discrete optimization problems, GA seemed to be best heuristic solve the problem.  

The genetic algorithm attempts to resolve the travelling salesman problem using partially mapped crossover as the crossover operations to avoid unfeasible solutions. With these operator we get two offsprings from which we kepp the one with the best fit. In terms of selection criteria the algorithm is parameterized to perform both elitism and tournament selections. 
Maybe the "novelty" introduced by my algorithm is that the # of indiviudals kept in each generation is decreasing as the process reaches the maximum number of iterations (see stopping criteria). This is inspired by the simmulated annealing methodology but also by plant breeding techniques, in which the follow ac funnel approach:

![Plant Breeding Strategy](https://github.com/mcrimi/GA_for_TSP_v2/blob/master/plant_breeding.png?raw=true)

In all honesty, the results that I got with this methodology are not far off better from the ones that I would get from a fixed population per generation, but I thought it would be fun to try.


## Hyper-parameters
Initial population size = 500
Baseline of individuals selected for the next generation=  200
Percentage of crossing between top performant individuals = 1
Percentage of the crosse altered by random mutations= 0.15
Next generation selection strategy: Elitism (top ranking individuals)

## Stopping criterion
MAX_ITERATIONS = 300


## Ideas for extension
- Use regular crossover + penalty functions instead of using partially mapped crossover
- Introduce dominance-codominance models
- Other crossover operators: Cycle Crossover Operator, Order Crossover Operator


## Results

### Djbouti

Genes: [20, 23, 26, 25, 22, 24, 15, 13, 9, 8, 7, 3, 5, 11, 12, 28, 37, 38, 33, 34, 36, 31, 27, 19, 18, 17, 16, 6, 4, 2, 1, 10, 14, 21, 29, 30, 32, 35]
- Best Fitness: 7684
- Pop. Individuals: 400
- Evaluations: 269796
- Time (seconds): 86.76117780000004

![Djbouti](https://github.com/mcrimi/GA_for_TSP_v2/blob/master/Djbouti_convergence.png?raw=true)


### Qatar

Genes: [93, 103, 157, 192, 181, 177, 164, 138, 137, 134, 126, 139, 144, 153, 165, 170, 162, 147, 118, 14, 17, 71, 141, 150, 145, 156, 130, 101, 82, 109, 102, 122, 129, 121, 115, 96, 95, 78, 80, 113, 114, 112, 110, 67, 41, 55, 52, 56, 39, 47, 34, 61, 133, 135, 105, 69, 75, 161, 172, 182, 132, 127, 99, 94, 63, 20, 65, 85, 86, 98, 104, 119, 167, 155, 175, 189, 191, 180, 185, 193, 173, 174, 186, 179, 169, 163, 140, 142, 146, 149, 194, 188, 187, 176, 184, 123, 124, 43, 46, 29, 28, 22, 12, 10, 73, 116, 131, 136, 160, 143, 128, 120, 100, 68, 89, 111, 62, 59, 1, 6, 13, 23, 25, 26, 24, 45, 66, 58, 53, 48, 49, 54, 38, 15, 19, 151, 158, 148, 117, 92, 84, 50, 30, 35, 42, 44, 81, 154, 183, 190, 178, 168, 166, 171, 159, 152, 125, 90, 36, 2, 3, 9, 27, 32, 31, 83, 97, 106, 107, 108, 79, 77, 70, 74, 57, 64, 37, 40, 51, 18, 21, 33, 60, 88, 91, 87, 76, 72, 8, 16, 4, 7, 11, 5]	

- Best Fitness: 26013
- Pop. Individuals: 400
- Evaluations: 269796
- Time (seconds): 509.2694081000001

![Qatar](https://github.com/mcrimi/GA_for_TSP_v2/blob/master/Qatar_convergence.png?raw=true)

