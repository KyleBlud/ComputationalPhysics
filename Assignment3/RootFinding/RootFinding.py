'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 21, 2017
'''
import numpy as np
import matplotlib.pyplot as plt

# Coefficients of given polynomial
coefficients = [1, 0, -5, 3]
# Returns the roots of the polynomial based on coefficients
roots = np.roots(coefficients)

# Return evenly spaced numbers over [-3, 3]
x = np.linspace(-3, 3, 100)
# p(x) is returned for each element of x
y = np.polyval(coefficients, x)

plt.plot(x, y)
for i in range(len(roots)):
    plt.plot([roots[i]], [0], marker = 'o', color = 'red')
plt.title(r'$f(x)=x^{3}-5x+3$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y = 0, color = 'black')
plt.axvline(x = 0, color = 'black')
plt.grid(True)
plt.show()