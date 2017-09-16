'''
Kyle Bludworth
Physics 420
September 9, 2017
'''
import random as r
import math as m
import turtle as t

class Coordinate:
    def __init__(self, x, y, in_circle):
        self.x = x
        self.y = y
        self.in_circle = in_circle
        
def is_coord_in_circle(x, y, center_x, center_y, radius):
    d = m.sqrt(m.pow(x - center_x, 2) + m.pow(y - center_y, 2))
    return (d < radius)
        
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

for i in range(0, N_TOTAL):
    rand_x = r.uniform(-1, 1)
    rand_y = r.uniform(-1, 1)
    in_circle = is_coord_in_circle(rand_x, rand_y, center_x, center_y, RADIUS)
    n_circle += 1 if in_circle else 0
    coordinates.append(Coordinate(rand_x, rand_y, in_circle))

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