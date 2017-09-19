'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 18, 2017
'''
import numpy as np

def f(x, alpha = 0):
    return 1 + (2 * x) + (3 * (x**2)) + (4 * (x**3)) + (alpha * (x**4))

def simpsons_rule(n, alpha = 0):
    x = []
    dx = 1 / n
    for i in range(n + 1):
        x.append(dx * i)
    odd_sum = 0
    even_sum = 0
    for j in range(1, n):
        if (j % 2 == 0):
            even_sum += f(x[j], alpha)
        else:
            odd_sum += f(x[j], alpha)
    estimate = f(x[0], alpha) + (4 * odd_sum) + (2 * even_sum) + f(x[n], alpha)
    estimate /= 3 * n
    return estimate

n_subintervals = [1, 10, 100, 1000, 10000, 100000]
alpha_vals = [0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]

print("For alpha = 0\n")
actual = 4
for n in  n_subintervals:
    estimate = simpsons_rule(n)
    print("n = " + str(n))
    print("Estimate = " + str(estimate))
    print("Actual = " + str(actual))
    print("Difference = {:.2e}".format(abs(estimate - actual)), end = "\n\n")

print("------------------------------------------------\n")

print("For alpha = 5\n")
actual = 5
for n in  n_subintervals:
    estimate = simpsons_rule(n, 5)
    print("n = " + str(n))
    print("Estimation = " + str(estimate))
    print("Actual = " + str(actual))
    print("Difference = {:.2e}".format(abs(estimate - actual)), end = "\n\n")

print("------------------------------------------------\n")

print("For n = 100,000")
actual = [4.002, 4.01, 4.02, 4.1, 4.2, 5, 6]
for i in range(len(alpha_vals)):
    estimate = simpsons_rule(100000, alpha_vals[i])
    print("alpha = " + str(alpha_vals[i]))
    print("Estimation = " + str(estimate))
    print("Actual = " + str(actual[i]))
    print("Difference = {:.2e}".format(abs(estimate - actual[i])), end = "\n\n")
