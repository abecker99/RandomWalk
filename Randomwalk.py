import math
import numpy as np

def step(N):
    dx = np.random.normal(0.0, 0.00577, N)
    dy = np.random.normal(0.0, 0.00577, N)
    dz = np.random.normal(0.0, 0.00577, N)
    x = np.sum(dx)
    y = np.sum(dy)
    z = np.sum(dz)
    return x, y, z

walk = step(10) #array: x, y, z
outFile = open("Photondistances.txt", "w")
outFile.write(str(walk[0]) + " " + str(walk[1]) + " " + str(walk[2]) + "\n")
outFile.close()

print(walk[0], " ", walk[1], " ", walk[2])