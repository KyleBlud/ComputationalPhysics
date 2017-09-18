# Computational Physics
#### Assignment Descriptions:
- [Assignment 2](#assignment-2)
  - [Random Numbers](#random-numbers)
  - [Radioactive Decay Chain](#radioactive-decay-chain)
  - [Brownian Motion](#brownian-motion)
  - [Gauss Quadrature](#gauss-quadrature)
## Assignment 2
### Random Numbers
A) Generate samples of (x, y) coordinates that fill a square uniformly such that x & y values fall in a range between -1 and +1. Be able to specify the number of xy-pairs to be generated, N_total.

B) Count the number of points in your sample that happen to fall inside the inscribed circle centered at the origin with a radius = 1, N_circle. Calculate the ratio: Ratio = (4(N_circle))/N_total

C) Plot the sampled data over the entire range of the square. Please inscribe the circle used in part B. Points outside of the circle color red and points inside the circle color blue for N_total = 10,000.

D) Plot the ratio you calculated as a function of N_total. Vary N_total from 10 to 10^6. Does this ratio converge to a finite value? What should this value be? Does this make sense? Draw a dashed horizontal line denoting the expected ratio value.

### Radioactive Decay Chain
The isotope 213Bi decays to stable 209Bi via one of two different routes, with probabilities
and half-lives thus:

Starting with a sample consisting of 10 000 atoms of 213Bi, simulate the decay of the atoms
as in Example 10.1 by dividing time into slices of length δt = 1 s each and on each step
doing the following:

A) For each atom of 209Pb in turn, decide at random, with the appropriate probability,
whether it decays or not. (The probability can be calculated from Eq. (10.3) in the
book.) Count the total number that decay, subtract it from the number of 209Pb
atoms, and add it to the number of 209Bi atoms.

B) Now do the same for 209Tl, except that decaying atoms are subtracted from the total
for 209Tl and added to the total for 209Pb.

C) For 213Bi the situation is more complicated: when a 213Bi atom decays you have
to decide at random with the appropriate probability the route by which it decays.
Count the numbers that decay by each route and add and subtract accordingly.
Note that you have to work up the chain from the bottom like this, not down from the
top, to avoid inadvertently making the same atom decay twice on a single step.

Keep track of the number of atoms of each of the four isotopes at all times for 20,000
seconds and make a single graph showing the four numbers as a function of time on the
same axes.

### Brownian Motion
Brownian motion is the motion of a particle, such as smoke or dust particle, in a gas, as it is buffeted by random collisions with gas molecules. Make a simple computer simulation of such a particle (in two dimensions) as follows. The particle is confined to a square grid or lattice L x L squares on a side, so that its position can be represented by two integers i, j = 0 . . . L - 1. It starts in the middle of the grid. On each step of the simulation, choose a random direction - up, down, left, or right - and move the particle one step in that direction. The particle is doing a "random walk." The particle is not allowed to move outside the square of the lattice - if it tries to do so, choose a new random direction to move in.

Write a program to do this calculation from a million steps of the random walk with L = 101 and make an animation on the screen of the position of the particle. (We choose an odd length for the side of the square so that there is one lattice site exactly in the center.)

### Gauss Quadrature
Evaluate the	integral using	Gauss-Legendre Quadrature:

at	various	orders,	from	N=2,	4,	8,	16,	32.		Calculate	the	absolute	difference	between	the	
integral	estimate	for	each	N	with	the	true	answer,	I = 5(pi)^2 / 96.	
