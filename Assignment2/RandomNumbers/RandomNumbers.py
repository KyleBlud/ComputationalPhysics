'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 16, 2017
'''
import random as r
import math as m
import turtle as t
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, x, y, in_circle):
        self.x = x
        self.y = y
        self.in_circle = in_circle
        
def is_coord_in_circle(x, y, center_x, center_y, radius):
    d = m.sqrt(m.pow(x - center_x, 2) + m.pow(y - center_y, 2))
    return (d < radius)

def calculate_ratio(n_circle, n):
    return ((4 * n_circle) / n)
        
# Total amount of coordinates to be generated. (Constant)
N_TOTAL = 10000

# Radius of circle (Constant)
RADIUS = 1

# Total amount of coordinates in the circle
n_circle = 0

# List of coordinates. Each element is an instance of Coordinate class.
coordinates = []

# Random x and y values. 
rand_x = 0
rand_y = 0
in_circle = False

# Center of circle coordinates
center_x = 0
center_y = 0

# Store the amount of points in the circle at a given total to be graphed.
# (n_total_vals[n], n_circle_vals[n])
ratio_vals = []
n_total_vals = []

for i in range(1, 10**6 + 1):
    rand_x = r.uniform(-1, 1)
    rand_y = r.uniform(-1, 1)
    in_circle = is_coord_in_circle(rand_x, rand_y, center_x, center_y, RADIUS)
    n_circle += 1 if in_circle else 0
    if (i <= N_TOTAL):
        coordinates.append(Coordinate(rand_x, rand_y, in_circle))
    if (i % 100 == 0 or i == 10):
        ratio_vals.append(calculate_ratio(n_circle, i))
        n_total_vals.append(i)

plt.style.use('dark_background')
plt.plot(n_total_vals, ratio_vals)
plt.axhline(y = 3.14, label = "Expected ratio", color = "red", linestyle = "--")
plt.title("Ratio of Randomly Generated Points Inside a Circle")
plt.xlabel("Number of Points")
plt.ylabel("Ratio of Points in Circle")
plt.xscale("log")
plt.legend()
plt.show()

wn = t.Screen()
bob = t.Turtle()
bob.hideturtle()
bob.speed("fastest")

# Draw the x and y axis
bob.pendown()
for i in range(1, 5):
    bob.forward(200)
    bob.home()
    bob.right(90 * i)

# Draw the inscribed circle
bob.goto(0, -100)
bob.circle(100)

# Plot each point (scaled to 100)
bob.penup()
for point in coordinates:
    dot_color = "blue" if point.in_circle else "red"
    bob.goto(point.x * 100, point.y * 100)
    bob.dot(3, dot_color)
