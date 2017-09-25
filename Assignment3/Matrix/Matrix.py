'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 24, 2017
'''
import numpy as np
from numpy.linalg import solve

A = np.array([[1, 1, 1], [2, 4, 6], [2, 12, 30]])
b = np.array([[-1], [0], [0]])
x = solve(A, b)
print(x)