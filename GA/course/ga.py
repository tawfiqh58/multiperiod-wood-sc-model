import numpy as np
import matplotlib.pyplot as plt
import random as rd

p_c = 1 # Probability of Crossover
p_m = 0.1 # Probability of Mutation
K = 3 # Tournament Selection
pop = 100 # Population Size
gen = 40 # Generation

# Initial Solution

# x and y index
# now guess each index has 13 element
# create cromosome
XY0 = np.array([0,0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1])
XY_Encoded_Before = np.array([0,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1]);

# Need to create an empty array
# same length as cromosome

# 100 population will be stored in
# this variable
n_list = np.empty((0,len(XY0)))

# 100 cromosome we want to put
for i in range(pop):
    # Shuffle the elements in the vector n times and store them
    rd.shuffle(XY0) # XY0 gets suffled here! [100 times]
    # It doesn't matter what you initially put in XY0
    # it will not use later on it just to create random
    # initial population and we are using rd.shuffle
    # method for that.
    
    n_list=np.vstack((n_list,XY0))

# --------------------------------------------------------

# Calculate Fitness value for x and y

a_X = -6 # Lower bound
b_X = 6 # Upper bound
l_X = (len(XY0)//2) # Length of chromosome X

a_Y = -6
b_Y = 6
l_Y = (len(XY0)//2) # Length of chromosome Y

# Precision = (UpperBound-LowerBound)/2**LengthOfX-1
# ** => power
Precision_X = (b_X-a_X)/((2**l_X)-1)
Precision_Y = (b_Y-a_Y)/((2**l_Y)-1)

# ---------------------------------------------------------
# Decodeing part

# Knowledge:
# How to convert binary to decimal
# For binary number with n digits:
# dn-1 ... d3 d2 d1 d0
# The decimal number is equal to the 
# sum of binary digits (dn) times their power of 2 (2n):
# decimal = d0×20 + d1×21 + d2×22 

# GET decoded value of X
z = 0
t = 1
X0_num_Sum = 0

for i in range(len(XY0)//2):
    # -t indicates that we evaluate 
    # array in backward
    X0_sum = XY0[-t]*(2**z)
    
    # and sum it
    X0_num_Sum = X0_num_Sum + X0_sum
    t = t+1
    z = z+1

Decoded_X = (X0_num_Sum*Precision_X) + a_X

# GET decoded value of Y
p = 0
u = 1 + (len(XY0)//2) # Y starts just after X cromosome
Y0_num_Sum = 0

for j in range(len(XY0)//2):
    Y0_sum = XY0[-u]*(2**p)
    Y0_num_Sum = Y0_num_Sum + Y0_sum
    u = u+1
    p = p+1
    
Decoded_Y = (Y0_num_Sum*Precision_Y) + a_Y

# See some results
print()
print(Decoded_X)
print(Decoded_Y)

def objective(x,y):
    # Z = (x**2+y-11)*22+(x+y**2-7)**2
    return ((x**2)+y-11)**2+(x+(y**2)-7)**2

# OF_So_Far = ((Decoded_X**2)+Decoded_Y-11)**2+(Decoded_X+(Decoded_Y**2)-7)**2
OF_So_Far = objective(Decoded_X,Decoded_Y)


print()
print(OF_So_Far)
# Obsr: We built some decoding mechanism to decode our
# X, Y value from binay string

# 
# We have 2 numbers here we have created cromosome guessing
# ?
# which has lenght 13x2=26
    

# So far we have done
# 1. declear property
# 2. create random population
# 3. decode vairables value

# ----------------------------------------------------------

Final_Best_in_Generation_X = []
FInal_Worse_in_Generation_X = []

For_Plotting_the_Best = np.empty((0,len(XY0)+1))

One_Final_Guy = np.empty((0,len(XY0)+2))
One_Final_Guy_Final = []

# In Tournament selection
# we will randomly choose 3 population 2x times
# each selection process can not have same parent twice
# then will decode there value and compare their fitness value
# among those 2 group who has the minimum 
# will be selected for the next generation parent from each group
# because we need 2 parents to create 2 children
# it will again loop and produce another 2 children
# this is how children is producing.
#
# Element of randomness
# Steps:
#   This is the next generation creation process
#   1. Pick 3 random population
#   2. Test fitness value
#   3. Again select 3 random population
#   4. Test fitness value
#   5. Finally select 2 parents one from each group

# Before going to generate next Generation
# we also need to calculate the best value of current Gen.
# who is the best among all the current population
# for the solution.
#
# Steps:
#   1. Calculate fitness value for each individual population
#   2. Store the best one value and his cromosome

# Elitism
# Directly replacing newly generated population by old best population
#
# Steps:
#   1. Store old best 10 population
#   2. Track worse 10 population of new generation
#   3. Replace worse by best