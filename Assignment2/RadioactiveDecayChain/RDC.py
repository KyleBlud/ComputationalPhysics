'''
Kyle Bludworth
Physics 420
September 9, 2017
'''
import math as m
import numpy as np
import random as r

# Probability of a given isotope with half-life "half_t" to decay at time "t"
def p(half_t, t):
    return (m.log(2)/half_t) * t

Bi213_HALF_LIFE = 2760         # 46 minutes in seconds
Tl209_HALF_LIFE = 132          # 2.2 minutes in seconds
Pb209_HALF_LIFE = 198          # 3.3 minutes in seconds

Bi213_total = 10000
Tl209_total = 0
Pb209_total = 0
Bi209_total = 0

# Holds the time in which each isotope decayed
Tl209_timestamps = []
Pb209_timestamps = []

decay_rand = 0
route_rand = 0

for t in range(1, 3000):
    # Bi213 
    init_Bi213_total = Bi213_total
    for atom in range(1, init_Bi213_total):
        decay_rand = r.uniform(0, 1)
        if (decay_rand <= p(Bi213_HALF_LIFE, t % Bi213_HALF_LIFE)):
            Bi213_total -= 1
            route_rand = r.uniform(0, 1)
            if (route_rand < 0.9791):
                Pb209_total += 1
                Pb209_timestamps.append(t)
            else:
                Tl209_total += 1
                Tl209_timestamps.append(t)

print("Bi213 Total: " + str(Bi213_total))
print("Pb209 Total: " + str(Pb209_total))
print("Tl209 Total: " + str(Tl209_total))            