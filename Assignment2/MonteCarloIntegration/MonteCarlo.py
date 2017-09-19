'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 19, 2017
'''
import numpy as np
import random as r
import matplotlib.pyplot as plt

def f(x):
    return 1 / ((np.e**x + 1) * np.sqrt(x))

def p(x):
    return 1 / (2 * np.sqrt(x))

def monte_carlo(n, partB = False):
    summation = 0
    for i in range(1, n + 1):
        x = r.uniform(0, 1)
        summation += f(x) * p(x) if partB else f(x)
    estimate = summation / n
    return estimate

n_vals = []
p1_vals = []
p2_vals = []

n_vals.append(10)
p1_vals.append(monte_carlo(10))
p2_vals.append(monte_carlo(10, True))

for n in range(100, 1000000, 100):
    n_vals.append(n)
    p1_vals.append(monte_carlo(n))
    p2_vals.append(monte_carlo(n, True))

print("Done")

plt.style.use('dark_background')
plt.plot(n_vals, p1_vals, label = "p(x) = 1")
plt.plot(n_vals, p2_vals, label = "p(x) = 1/2sqrt(x)")
plt.axhline(y = 0.83893296, label = "Actual", color = "red", linestyle = "--")
plt.xscale("log")
plt.xlabel("Number of Samples")
plt.ylabel("Integral values")
#plt.title("Radioactive Decay of 213Bi Isotope")
plt.legend()
plt.show()