import json
import numpy as np
import matplotlib.pyplot as plt

with open("particles.json", "r") as file:
    model = json.load(file)

#PARAMETERS FROM MODEL
x = np.array([entry[0] for entry in model["coords"]]) # list of x coordinates
y = np.array([entry[1] for entry in model["coords"]]) # list of y coordinates

Np = len(x) # number of particles
k = model["k"] # k parameter
m = model["m"] # mass parameter
r = model["r"] # radius parameter

forces = np.array([entry for entry in model["forces"]])
forces = np.reshape(forces, (2*Np)) # forces in array shape

restrs = np.array([entry for entry in model["restrs"]])
restrs = np.reshape(restrs, (2*Np)) # restrictions in array shape

connect = np.array([entry for entry in model["connect"]])

# VARIABLES FOR SIMULATION
fi = np.zeros(2*Np)
u = np.zeros(2*Np)
v = np.zeros(2*Np)
a = (1./m)*forces
N = 100 # number of iterations
h = 0.00004 # delta time
d = np.zeros(N)

for i in range(N):
    v += a * (0.5 * h) # update velocity
    u += v * h # displacement
    # PARTICLES CONTACT
    for j in range(Np):
        if restrs[2 * j] == 1:
            u[2 * j] = 0
        if restrs[2 * j + 1] == 1:
            u[2 * j + 1] = 0
        xj = x[j] + u[2 * j]
        yj = y[j] + u[2 * j + 1]
        for ki in range(connect[j,0] - 1): # connect[j,0] is the number of contact particles of the j-th particle
            pk = connect[j, ki + 1] - 1
            xk = x[pk] + u[2 * pk] # x coordinate of pk, which has contact with j
            yk = y[pk] + u[2 * pk + 1] # same as above, but for y
            dx = xj - xk
            dy = yj - yk
            di = (dx**2 + dy**2) ** 0.5
            d2 = di - 2*r
            dx = d2 * dx/di
            dy = d2 * dy/di
            fi[2*j] = fi[2*j] + k * dx
            fi[2*j+1] = fi[2*j+1] + k * dy
        
    a = (1./m) * (forces - fi)
    v = v + a * (0.5 * h)
    fi = fi*0
    d[i] = u[17 * 2] # x displacement of particle 17

plt.plot(d)
plt.show()