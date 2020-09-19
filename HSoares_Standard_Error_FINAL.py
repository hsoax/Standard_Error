# Humberto Soares ; Assignment 1 ; Exercise 1: Standard Error
# -------------------------------------------
# packages
import random
random.seed(1)
from math import sqrt
import statistics

# Variable Input
population = list(range(1, 10001))

n_sample = [10, 20, 50, 100, 200, 500, 1000, 5000]

print('#Samples\tMean\tStd.Err')
# Use loop statement to pull and iterate sample sizes
for n in n_sample:
    sample = random.sample(population, n)
    # where sample command picks a random element from population with length n
    mean = statistics.mean(sample)
    # mean computes the sum of the sample divided by n, as defined in for loop
# statistical values
    stdv_s = statistics.stdev(sample)
    sterr_s = stdv_s/sqrt(n)
# Use of f strings to plot numbers in listed order
    print(f'{n:0>4d}\t{mean:.2f}\t{sterr_s:.2f}')
