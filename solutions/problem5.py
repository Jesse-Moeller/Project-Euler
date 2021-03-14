# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#----------#

import numpy as np

print(np.lcm.reduce(np.arange(1,21)))

#Completed on Mon, 23 Nov 2020, 17:25