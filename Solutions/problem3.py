# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
#----------#

# Lemma: The largest prime divisor of n is <= sqrt(n)

import numpy as np

big_number=600851475143
prime_divisors=[]
p=2

while p<np.sqrt(big_number)+1:
    if all(p%np.array(prime_divisors)) and big_number%p==0:
        prime_divisors.append(p)
    p=p+1

print(max(prime_divisors))


#Completed on Mon, 23 Nov 2020, 16:38