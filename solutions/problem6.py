# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#----------#

# Note that the sum (1+...+n)=n(n+1)/2 and that the sum of squares (1^2+...+n^2)=n(n+1)(2n+1)/6
# Thus (1+...+n)^2=n^2(n+1)^2/4, so the difference is n^2(n+1)^2/4-n(n+1)(2n+1)/6

def sum_squares_minus_square_sum(n):
    return n**2*(n+1)**2/4-n*(n+1)*(2*n+1)/6

print(sum_squares_minus_square_sum(100))

#Completed on Mon, 23 Nov 2020, 18:09