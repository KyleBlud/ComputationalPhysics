'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 21, 2017
'''
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**3 - (5 * x) + 3)

# Coefficients of given polynomial
coefficients = [1, 0, -5, 3]

# Returns the roots of the polynomial based on coefficients
roots = np.roots(coefficients)
roots.sort()

# Return evenly spaced numbers over [-3, 3]
x = np.linspace(-3, 3, 100)

# p(x) is returned for each element of x
y = np.polyval(coefficients, x)

# Plotting the function such that all roots are visible
plt.axhline(y = 0, color = 'black')
plt.axvline(x = 0, color = 'black')
plt.plot(x, y)
for i in range(len(roots)):
    plt.plot([roots[i]], [0], marker = 'o', color = 'red')
plt.title(r'$f(x)=x^{3}-5x+3$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# Bracketing x values for each root
bracket_x_vals = [(-3, -2), (0, 1), (1.5, 2)]
# 5 digit accuracy
tolerance = 10**(-7)

print("Bracketing method:")
for i in range(len(roots)):
    a = bracket_x_vals[i][0]
    b = bracket_x_vals[i][1]
    while (abs(a - b) > tolerance):
        c = (a + b) / 2
        if (np.sign(f(c)) == np.sign(f(a))):
            a = c
        if (np.sign(f(c)) == np.sign(f(b))):
            b = c
    print("a = " + str(a) + ", b = " + str(b) + ", root = " + str(roots[i]))
    
    