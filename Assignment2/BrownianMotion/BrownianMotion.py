'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 16, 2017
'''
import random as r
import turtle as t

L = 101

wn = t.Screen()
wn.screensize(L, L)

jim = t.Turtle()
jim.hideturtle()
jim.speed("fastest")

directions = [0, 90, 180, 270]

for i in range(1000000):
    jim.setheading(r.choice(directions))
    jim.forward(1)