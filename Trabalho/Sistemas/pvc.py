import numpy as np
import json

file = open('data.json',"r")
data = json.load(file)
boundConditions = data['boundary_conditions']
connect = data['connect']
tamBoundCond = len(boundConditions)
print(boundConditions)
print(connect)

vetorA = np.zeros(shape=(tamBoundCond,tamBoundCond))
vetorB = np.zeros(shape=(tamBoundCond,1))

for i in range(len(vetorB)):
    if boundConditions[i][0] == 1:
        vetorB[i] = boundConditions[i][1]    

for i in range(len(connect)):
    if boundConditions[i][0] == 0:
        if connect[i][0] != 0:
            vetorA[i][connect[i][0]-1] = 1
        if connect[i][1] != 0:
            vetorA[i][connect[i][1]-1] = 1
        if connect[i][2] != 0:
            vetorA[i][connect[i][2]-1] = 1
        if connect[i][3] != 0:
            vetorA[i][connect[i][3]-1] = 1
        if connect[i][4] != 0:
            vetorA[i][connect[i][4]-1] = -4
    else:
        vetorA[i][i] = 1


T = np.linalg.solve(vetorA,vetorB)

print(T)