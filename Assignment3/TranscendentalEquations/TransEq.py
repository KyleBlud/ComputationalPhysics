'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 21, 2017
'''
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(x + 2) - np.tan(x)

def f_prime(x):
    return (1 / (2 * np.sqrt(x + 2))) - (1 / (np.cos(x)**2))

def newton(x):
    return (x - (f(x)/f_prime(x)))

# Returns 10,000 samples over [0, 30]
x_ = np.linspace(0, 30, 10000)

# Calculate equations for each sample in the interval [0, 30]
y1_ = np.tan(x_)
y2_ = np.sqrt(x_ + 2)

# Graphing both sides of the equation to see where they overlap first 10 times
plt.figure(figsize=(12, 4))
plt.axhline(y = 0, color = 'black')
plt.axvline(x = 0, color = 'black')
plt.scatter(x_, y1_, label = 'tan(x)', marker = '|')
plt.plot(x_, y2_, label = r'$\sqrt{x+2}$', color = 'orange')
plt.ylim(0, 10)
plt.title('First 10 Solutions to ' + r'$\sqrt{x+2} = tan(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(np.arange(31))
plt.yticks(np.arange(11))
plt.grid(True)
plt.legend()
plt.show() 

# Initial guesses that are close to zeroes of interest
initial_vals = [1, 4, 7.4, 10.6, 13.7, 17, 20.1, 23.3, 26.5, 29.6]
# 7 digit accuracy
tolerance = 10**(-7)
# x_0 is the current x while x_n is the next x
x_0 = 0
x_n = 0
# Number of iterations to converge to the predefined precision
# Start off at 1 since x_n is defined outside of while loop
iterations = 1

# Approximate a root using Newtons Method for each guess
for guess in initial_vals:
    x_0 = guess
    print("Initial guess: " + str(x_0))
    x_n = newton(x_0)
    while (abs(x_n - x_0) > tolerance):
        x_0 = x_n
        x_n = newton(x_0)
        iterations += 1
    print("Approximate root: " + str(x_n))
    print("Iterations: " + str(iterations) + "\n")
    iterations = 0