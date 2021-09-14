import numpy as np
import matplotlib.pyplot as plt
import math


def mean_field(N,L):

	vel = 0.1

	tau_i = 200
	tau_r = 500
	tau_t = 1
	r = 1
	sigma = 4*r

	rho = N/math.pow(L,2)
	#print('rho', rho)

	epsilon = 0.916
	K = 1.042
	omega =  K*math.pow(r/vel,epsilon)

	R_0 = (1 - math.exp(-omega/tau_t))*vel*sigma*rho*tau_i

	S = 1./R_0
	I = (1-S) * tau_i/(tau_i+tau_r)
	R = (1-S) * tau_r/(tau_i+tau_r)

	result = f'H:{round(S,2)} \nI:{round(I,2)} \nR:{round(R,2)}'
	print(result)
	
	return [S,I,R] 

if __name__ == '__main__':
	L = [100, 150, 200, 250]

	for element in L:
		print(element)
		mean_field(1024,element)


	rho = 0.016384

	N_L = math.sqrt(10000/rho)

	print('L=', N_L) 

	a = [0, 1, 2 , 3 , 4]
	print([a[-2:]])