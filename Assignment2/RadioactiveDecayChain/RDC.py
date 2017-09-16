'''
Kyle Bludworth
Physics 420
September 9, 2017
'''
import math as m
import numpy as np
import random as r

# Probability of a given isotope with half-life "half_t" to decay
def p(half_t):
    return (m.log(2)/half_t)

Bi213_HALF_LIFE = 2760         # 46 minutes in seconds
Tl209_HALF_LIFE = 132          # 2.2 minutes in seconds
Pb209_HALF_LIFE = 198          # 3.3 minutes in seconds

Bi213_total = 10000
Tl209_total = 0
Pb209_total = 0
Bi209_total = 0

decay_rand = 0
route_rand = 0

for t in range(1, 2671):
    # Bi213 
    init_Bi213_total = Bi213_total
    for atom in range(1, init_Bi213_total):
        decay_rand = r.uniform(0, 1)
        if (decay_rand <= p(Bi213_HALF_LIFE)):
            Bi213_total -= 1
            route_rand = r.uniform(0, 1)
            if (route_rand < 0.9791):
                Pb209_total += 1
            else:
                Tl209_total += 1
          