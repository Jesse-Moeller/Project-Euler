# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
#----------#

import numpy as np

def is_palindrome(integer):
    return str(integer)==str(integer)[::-1]

def find_largest_palindrome_product(upper_bound):
    checked=[]
    position=upper_bound
    palindromes=[]
    for i in range(100,upper_bound):
        checked.append(position)
        for previous in checked:
            product=position*previous
            if is_palindrome(product):
                palindromes.append(product)
        position=position-1
    return max(palindromes)

print(find_largest_palindrome_product(999))

# Completed on Mon, 23 Nov 2020, 17:11