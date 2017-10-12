'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: October 8, 2017
'''
import math as m
from random import uniform
from numpy.random import normal
import matplotlib.pyplot as plt

# Each body has a position and velocity vector and a mass
class Body:
    def __init__(self, r, v, mass):
        self.r = r
        self.v = v
        self.mass = mass

# Returns if a point in space is within a sphere with a given radius
def point_in_sphere(x, y, z, radius):
    d = m.sqrt(x**2 + y**2 + z**2)
    return (d < radius)

def f(r_):
    # r = sqrt(x^2 + y^2 + z^2), same for v but with its components
    r = m.sqrt(r_[0]**2 + r_[1]**2 + r_[2]**2)
    # Interaction constants
    epsilon = 4.2*10**(-6)
    sigma = 0.02576
    return (((48 * epsilon) / r) * ((sigma / r)**12 - ((0.5) * (sigma / r)**6)))
    
def g(r_, v_):
    # r = sqrt(x^2 + y^2 + z^2), same for v but with its components
    r = m.sqrt(r_[0]**2 + r_[1]**2 + r_[2]**2)
    v = m.sqrt(v_[0]**2 + v_[1]**2 + v_[2]**2)
    # Interaction constants
    rho = 10**(-3)
    A = 7.85*10**(-5)
    a = 0.0025
    return (-(0.25) * rho * A * (v**2) * m.exp(-(r**2)/(2 * a**2)))
    
# Number of bodies in simulation
N = 100
# 20 cm = 0.2 meters
RADIUS = 0.2
# 1.5 cm/s = 0.015 m/s
WIDTH = 0.015
# 5 g = 0.005 kg
MASS = 0.005
# Standard deviation and mean of each velocity component (Maxwell–Boltzmann)
std_dev = (1 / m.sqrt(3)) * WIDTH
mean = 0
# List of bodies in the simulation
bodies = []
# 3D plots/figures for position (r) and velocity (v)
r_fig = plt.figure(1)
v_fig = plt.figure(2)
r_ax = r_fig.add_subplot(111, projection = '3d')
v_ax = v_fig.add_subplot(111, projection = '3d')

# Values of each component for position and velocity stored in an array for
# plotting
x_vals = []
y_vals = []
z_vals = []
u_vals = []
v_vals = []
w_vals = []

# Generate random x, y, z values for the position of a body and generate 
# random gaussian distributed u, v, w values for velocity. Accept these values
# as long as the position of the body is within a sphere of the given radius.
i = 0 
while (i < N):
    rand_x = uniform(-RADIUS, RADIUS)
    rand_y = uniform(-RADIUS, RADIUS)
    rand_z = uniform(-RADIUS, RADIUS)
    if (point_in_sphere(rand_x, rand_y, rand_z, RADIUS)):
        rand_u = normal(mean, std_dev)
        rand_v = normal(mean, std_dev)
        rand_w = normal(mean, std_dev)
        x_vals.append(rand_x)
        y_vals.append(rand_y)
        z_vals.append(rand_z)
        u_vals.append(rand_u)
        v_vals.append(rand_v)
        w_vals.append(rand_w)
        bodies.append(Body([rand_x, rand_y, rand_z],
                           [rand_u, rand_v, rand_w], MASS))
        i += 1

# PLot a 3D graph of the positions of each body        
r_ax.scatter(x_vals, y_vals, z_vals, marker = 'o', color = 'red')
r_ax.set_xlabel("x")
r_ax.set_ylabel("y")
r_ax.set_zlabel("z")
r_ax.set_xlim(-RADIUS, RADIUS)
r_ax.set_ylim(-RADIUS, RADIUS)
r_ax.set_zlim(-RADIUS, RADIUS)
r_fig.show()

# PLot a 3D graph of the velocities of each body  
v_ax.scatter(u_vals, v_vals, w_vals, marker = 'o', color = 'blue')
v_ax.set_xlabel("u")
v_ax.set_ylabel("v")
v_ax.set_zlabel("w")
v_fig.show()    