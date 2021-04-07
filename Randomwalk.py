import math
import numpy as np
#1st part: TotalSeconds      : 21.3433894

#want scattering over 31557600 s
#1st part sigma =0.00577
#change sigma to 57.7 N should be the number of seconds above
#for a year in a single step Eq 6.13

#2nd part:year: TotalSeconds      : 7.322083
#2nd part w/ stdev: TotalSeconds      : 7.0419291

def step(N): #pos, N, mu, sigma
    dx = np.random.normal(0.0, 324136.4, N)
    dy = np.random.normal(0.0, 324136.4, N)
    dz = np.random.normal(0.0, 324136.4, N)
    # pos[0] += np.sum(dx)
    # pos[1] += np.sum(dy)
    # pos[2] += np.sum(dz)
    return dx, dy, dz

#5) stdev=sqrt(10^8*number total seconds)*0.00577: 324136.4

#how long for photon to get distance greater than sun's radius
#experiment w/ number of steps. Enough steps you're pretty sure
#dx = normal(0.0, std, 10^8 or other). repeat for dy &dz

x = 0
y = 0
z = 0
r = 0
i = 0
T = []
rsun = 695700000 #m

#outFile = open("PhotondistancesSunsingle.txt", "w")
dx, dy, dz = step(31557600)
for photons in range(3):
     
    while (r < rsun):
        x += dx[i]
        y += dy[i]
        z += dz[i]
        r = np.sqrt(x**2+y**2+z**2)
        i += 1
        t = i #in years
    T = np.append(T, t)
    print(t)
    #outFile.write(str(dx[i]) + " " + str(dy[i]) + " " + str(dz[i]) + " " + str(r) + "\n")
#outFile.close()
print(np.average(T)) 
print(np.std(T))
#print(t)
#loop around ^ for multiple photons



# pos = [0.0, 0.0, 0.0]
# pos = step(pos, 31557600) #array: x, y, z


#outFile.write(str(pos[0]) + " " + str(pos[1]) + " " + str(pos[2]) + "\n")
# print(pos[0], " ", pos[1], " ", pos[2])
