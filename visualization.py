import numpy as np
import matplotlib.pyplot as plt
from mean_field import mean_field
import os

N = 1000
L = 150

data       = "data/epidemia.txt"
epidemic = np.loadtxt(data)

plt.title('Pop. vs Time')

plt.xlabel("Time")
plt.ylabel("Population")
plt.ylim(0, 1)
plt.xlim(0, epidemic[:,3].max()+10)


label = ['Healthy', 'Infected', 'Refractary']

for i in range(3):
	plt.scatter(epidemic[:,3], epidemic[:,i]/N, marker='.', label=label[i])
	print(epidemic[:,i].max())

plt.legend()
plt.show()



