#Animación de la epidemia a través de agentes. 
#arreglar este programa
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from tqdm import tqdm,trange
from mean_field import mean_field
import os

colores = ['blue','red', 'green', ]
archivo = "data/animacion.txt"

N = 1000
L = 200

##############################################################################################
#Animacion
##############################################################################################

def trayectoria(tpause = 0.01, animation = False):

	nsteps  = np.loadtxt(archivo, usecols=0).size/N
	fig, ax = plt.subplots()
	loop_range = int(nsteps);
	for i in trange(loop_range,mininterval=10):

		x = np.loadtxt(archivo, usecols=0, skiprows=N*i, max_rows=N)
		y = np.loadtxt(archivo, usecols=1, skiprows=N*i, max_rows=N)

		estado = np.loadtxt(archivo, usecols=3, skiprows=N*i, max_rows=N, dtype=int)

		plt.cla()

		plt.title("Agents system")
		plt.xlabel("x coordinate")
		plt.ylabel("y coordinate")

		plt.axis('square')
		plt.grid()
		plt.xlim(-1,L+1)
		plt.ylim(-1,L+1)

		for j in range(N):
			circ = patches.Circle((x[j],y[j]), 1, alpha=0.7, fc= colores[estado[j]])
			ax.add_patch(circ)

		plt.savefig("video/pic%.4i.png" %(i),dpi=70)
		#plt.pause(tpause)

	if animation:
		path = "C:/Users/Admin/Desktop/agent_system/video"
		print(os.getcwd())
		os.chdir(path)
		print(os.getcwd())
		os.system('cmd /k "ffmpeg -r 30 -f image2 -s 1920x1080 -i pic%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test2.mp4"')

####################################################################
####################################################################

##############################################################################################
#Plot epidemia
##############################################################################################

data       = "data/epidemia.txt"
healthy    = np.loadtxt(data, usecols=0)/N
infected   = np.loadtxt(data, usecols=1)/N
refractary = np.loadtxt(data, usecols=2)/N
tiempo     = np.loadtxt(data, usecols=3)

plt.title('Pop. vs Time')

plt.xlabel("Time")
plt.ylabel("Population")

plt.ylim(0, 1)
plt.xlim(0, tiempo.max()+10)
plt.plot(tiempo, healthy, label='healthy')
plt.plot(tiempo, infected, label='infected')
plt.plot(tiempo, refractary, label='refractary')
plt.plot(tiempo, refractary+infected+healthy)
plt.legend()
plt.show()

time_step = 0.05
since = -800000
print(-since*time_step)

print(f'Healthy  {round(healthy[since:].mean(),2)}' )
print(f'Infected {round(infected[since:].mean(),2)}')
print(f'Recovery {round(refractary[since:].mean(),2)}')

mean_field(N,100)


#trayectoria(0.01,False)