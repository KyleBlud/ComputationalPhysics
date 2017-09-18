'''
Author: Kyle Bludworth
Course: Physics 420
Creation date: September 17, 2017
'''
import math as m
import random as r
import matplotlib.pyplot as plt

# Probability of a given isotope with half-life "half_t" to decay
def p(half_t):
    return (m.log(2)/half_t)

Bi213_HALF_LIFE = 2760         # 46 minutes in seconds
Tl209_HALF_LIFE = 132          # 2.2 minutes in seconds
Pb209_HALF_LIFE = 198          # 3.3 minutes in seconds
TOTAL_TIME = 20000

Bi213_total = 10000
Tl209_total = 0
Pb209_total = 0
Bi209_total = 0

Bi213_vals = [10000]
Tl209_vals = [0]
Pb209_vals = [0]
Bi209_vals = [0]
time = [0]

decay_rand = 0
route_rand = 0

for t in range(1, TOTAL_TIME + 1):
    # Pb209
    init_Pb209_total = Pb209_total
    for atom in range(init_Pb209_total):
        decay_rand = r.uniform(0, 1)
        if (decay_rand <= p(Pb209_HALF_LIFE)):
            Pb209_total -= 1
            Bi209_total += 1
    # Tl209
    init_Tl209_total = Tl209_total
    for atom in range(init_Tl209_total):
        decay_rand = r.uniform(0, 1)
        if (decay_rand <= p(Tl209_HALF_LIFE)):
            Tl209_total -= 1
            Pb209_total += 1
    # Bi213 
    init_Bi213_total = Bi213_total
    for atom in range(init_Bi213_total):
        decay_rand = r.uniform(0, 1)
        if (decay_rand <= p(Bi213_HALF_LIFE)):
            Bi213_total -= 1
            route_rand = r.uniform(0, 1)
            if (route_rand < 0.9791):
                Pb209_total += 1
            else:
                Tl209_total += 1
    Bi213_vals.append(Bi213_total)
    Tl209_vals.append(Tl209_total)
    Pb209_vals.append(Pb209_total)
    Bi209_vals.append(Bi209_total)
    time.append(t)

plt.style.use('dark_background')
plt.plot(time, Bi213_vals, label = "Bi213")
plt.plot(time, Tl209_vals, label = "Tl209")
plt.plot(time, Pb209_vals, label = "Pb209")
plt.plot(time, Bi209_vals, label = "Bi209")
plt.xlabel("Time (s)")
plt.ylabel("Atoms")
plt.title("Radioactive Decay of 213Bi Isotope")
plt.legend()
plt.show()