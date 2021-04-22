import matplotlib.pyplot as plt
plt.rcParams['agg.path.chunksize'] = 10000

X = []
Y = []
Z = []

inFile = open("PhotondistancesSunsingle.txt", "r")
for line in inFile:
    x, y, z, r = line.split(" ")
    X.append(float(x))
    Y.append(float(y))
    Z.append(float(z))
inFile.close()

# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.plot(X,Y)
# plt.show()

# plt.xlabel("$y$")
# plt.ylabel("$z$")
# plt.plot(Y,Z)
# plt.show()

plt.xlabel("$x$")
plt.ylabel("$z$")
plt.plot(X,Z)
plt.show()