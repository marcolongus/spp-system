import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from tqdm import tqdm,trange
from mean_field import mean_field
import os

N = 10000
L = 781

data       = "data/epidemia.txt"
epidemic = np.loadtxt(data)

plt.title('Pop. vs Time')

plt.xlabel("Time")
plt.ylabel("Population")
plt.ylim(0, 1)
plt.xlim(0, epidemic[:,3].max()+10)

since = -10000
time_step = 0.05
print('integrated time', -since*time_step),print()

label = ['Healthy', 'Infected', 'Refractary']

for i in range(3):
	plt.plot(epidemic[:,3], epidemic[:,i]/N, label=label[i])
	print(f'{label[i]} {round((epidemic[since:,i]/N).mean(),2)}' ,'+/-', f'{round((epidemic[since:,i]/N).std(),2)}' )

plt.legend()
plt.show()

print()
mean_field(N,L)

