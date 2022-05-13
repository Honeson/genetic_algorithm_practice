import numpy as np


# The equation I want to implement using genetic algorithm
# Y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6

# from the equation, 6 inputs (x1 to x6), 6 weights (w1 to w6)

equation_inputs = [8,-1,6.7,10,-6,-2.1]

# Number of weights to optimize is 6
num_weights = 6

# To determine the population size, we find the number of chromozones (individuals or solution) first
sol_per_pop = 8

# Each population will have sol_per_pop chromosomes and num_weights number of weights per chromosome
pop_size = (sol_per_pop, num_weights)

# Defining the initial population
new_pop = np.random.uniform(low=0.4, high=0.4, size=pop_size)