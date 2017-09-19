'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 16, 2017
'''
import random as r
import turtle as t

# Maginfied by 5 to see the movement through the lattice
L = 101 * 5

wn = t.Screen()
wn.setup(width = L, height = L)

jim = t.Turtle()
jim.hideturtle()
jim.speed("fastest")

directions = [(5, 0), (-5, 0), (0, 5), (0, -5)]

x = 0
y = 0

for i in range(1000000):
    (dx, dy) = r.choice(directions)
    while (jim.xcor() + dx > int(L/2) or jim.xcor() + dx < int(-L/2) or
           jim.ycor() + dy > int(L/2) or jim.ycor() + dy < int(-L/2)):
        (dx, dy) = r.choice(directions)
    x += dx
    y += dy
    jim.goto(x, y)
    