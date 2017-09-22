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
    return (1 / (2 * np.sqrt(x + 2))) - (1 / np.cos(x))**2

# Returns 10,000 samples over [0, 30]
x_ = np.linspace(0, 30, 10000)

# Calculate equations for each sample in the interval [0, 30]
y1_ = np.tan(x)
y2_ = np.sqrt(x + 2)

# Graphing the 2 sides of the equation in which they overlap the first 10 times
plt.axhline(y = 0, color = 'black')
plt.axvline(x = 0, color = 'black')
plt.scatter(x_, y1_, label = 'tan(x)', marker = '|')
plt.plot(x_, y2_, label = r'$\sqrt{x+2}$', color = 'orange')
plt.ylim(-10, 10)
plt.title('First 10 Solutions to ' + r'$\sqrt{x+2} = tan(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()        