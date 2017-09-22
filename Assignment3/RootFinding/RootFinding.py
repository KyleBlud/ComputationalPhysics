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
x_ = np.linspace(-3, 3, 100)

# p(x) is returned for each element of x
y_ = np.polyval(coefficients, x_)

# Plotting the function such that all roots are visible
plt.axhline(y = 0, color = 'black')
plt.axvline(x = 0, color = 'black')
plt.plot(x_, y_)
for i in range(len(roots)):
    plt.plot([roots[i]], [0], marker = 'o', color = 'red')
plt.title(r'$f(x)=x^{3}-5x+3$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# Bracketing x values for each root
bracket_x_vals = [(-3, -2), (0, 1), (1.5, 2)]
# 7 digit accuracy
tolerance = 10**(-7)
# Number of iterations to converge to the predefined precision
iterations = 0
i = 0

print("Bracketing method:")
for x1, x2 in bracket_x_vals:
    a = x1
    b = x2
    while (abs(a - b) > tolerance):
        c = (a + b) / 2
        if (np.sign(f(c)) == np.sign(f(a))):
            a = c
        if (np.sign(f(c)) == np.sign(f(b))):
            b = c
        iterations += 1
    print("a = " + str(a) + "\nb = " + str(b) + "\nRoot = " + str(roots[i]))
    print("Iterations: " + str(iterations) + "\n")
    i += 1

# Stores recursive values of x
x = []
iterations = 0
i = 0

print("Secant Method:")
for x0, x1 in bracket_x_vals:
    x.append(x0)
    x.append(x1)
    n = len(x)
    while (abs(x[n - 1] - x[n - 2]) > tolerance):
        x.append(((x[n-2]*f(x[n-1]))-(x[n-1]*f(x[n-2])))/(f(x[n-1])-f(x[n-2])))
        n = len(x)
        iterations += 1
    print("Approximation: " + str(x[n - 1]) + "\nRoot = " + str(roots[i]))
    print("Iterations = " + str(iterations) + "\n")
    x.clear()
    i += 1