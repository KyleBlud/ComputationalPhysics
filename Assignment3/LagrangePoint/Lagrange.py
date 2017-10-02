'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: October 1, 2017
'''
def f(r):
    return ((7.086*10**-12) * r**5) - ((5.448*10**-3) * r**4) + ((1.047*10**6) * r**3) - ((3.938*10**14) * r**2) + ((3.065*10**23) * r) - (5.891*10**31)

def f_prime(r):
    return ((3.543*10**-11) * r**4) - ((2.179*10**-2) * r**3) + ((3.141*10**6) * r**2) - ((7.876*10**14) * r) + (3.065*10**23)

def newton(x):
    return (x - (f(x)/f_prime(x)))

# Initial guess of what the root may be
guess = 3.26*10**8
# 7 digit accuracy
tolerance = 10**(-7)
# x_0 is the current x while x_n is the next x
x_0 = 0
x_n = 0
# Number of iterations to converge to the predefined precision
# Start off at 1 since x_n is defined outside of while loop
iterations = 1

# Approximate a root using Newtons Method for each guess
x_0 = guess
print("Initial guess: {:.2e}".format(x_0))
x_n = newton(x_0)
while (abs(x_n - x_0) > tolerance):
    x_0 = x_n
    x_n = newton(x_0)
    iterations += 1
print("Approximate root: {:.5e}".format(x_n))
print("Iterations: " + str(iterations) + "\n")
iterations = 0