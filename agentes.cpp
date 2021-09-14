/* Autor: Benjamín R. Marcolongo. FAMAF-UNC.
 *---------------------------------------------------------------------------------------------------------
 * Programa para evolucionar un sistema de N agentes en el tiempo.
 *---------------------------------------------------------------------------------------------------------
 * Agentes:
 *		i.   Las velocidades de los N agentes pueden ser uniformes o tomadas aleatoriamente.
 *		      1. Las distribuciones por defecto son de tipo exponencial o de ley de potencias.
 *		ii.  Pueden interactuar a través de un potencial u otra forma (una red neuronal i.e).
 *			  1. El potencial por defecto es de esferas blandas.
 *		ii.  Están confinados a un toroide topológico-
 *			  1. El tamaño característico del toro se denota con L (lado del cuadrado).
 *		iii. Poseen un estado interno, caracterizado por un número entero.
 *			  1. Este estado puede o no interactaur con la dinámica espacial.
 *		iv.  El estado interno puede evolucionar en el tiempo.
 *			  1. Esta dinámica está regulada, genéricamente, con una distribución de poisson.
 *---------------------------------------------------------------------------------------------------------
 * Red compleja: falta programar
 *			i.  El programa trackea todo el sistema de interacciones y guarda la red compleja resultante.
 *			ii. La red compleja puede ser la asociada a la propagación del estado interno o la de contactos
 *---------------------------------------------------------------------------------------------------------
* Estuctura de datos para optimizar la búsqueda de interacciones entre agentes:
*	   i.   Utiliza un red-and-black tree implementado en c++ como set.
*	   ii.  Cada agente está indexado por un int.
*	   iii. Se construye una grilla con cuadrículas de tamaño 1x1 y cada a una se le asigna un set.
*	   iv.  Cada set contiene los agentes que están en cada cuadrícula proyectando su posción sobre la grilla..
 *---------------------------------------------------------------------------------------------------------		 
 */
#include <bits/stdc++.h>
#include "agentes.h"      

#define CHECK(val_1, val_2) if (val_1 % val_2 == 0)
#define TIME(val_1, val_2 ) (float)val_1 * val_2	

using namespace std;

int main(void){	
	/*DEFINICIÓN DE ARCHIVOS DE SALIDA DEL PROGRAMA*/
	ofstream FinalState ("data/evolution.txt");
	ofstream epidemic   ("data/epidemia.txt" );		//Estado de la epidemia en cada instante modulo m.
	ofstream anim       ("data/animacion.txt");
	ofstream metrica    ("data/metrica.txt", ios_base::app) ; 
	
	/*VARIABLES PARA CALCULAR METRICA Y PERFERMANCE*/
	float  updates = 0;      //contador de updates. 
	size_t start_s = clock();

	/*SIMULACION*/
	gen.seed(seed);  
	for (size_t n_simulaciones = 0; n_simulaciones < 1; n_simulaciones++)
	{
		print_header(n_simulaciones);		
		
		/*DECLARACIÓN DE VARIABLES*/
		vector<particle> system, 
						 system_new;
		vector<bool>     inter;        	//Flag de interacción.
		vector<size_t>   state_vector;	//En cada lugar contiene la población de cada estado.
		inter.resize(N,false);
		state_vector.resize(spin,0);

		/*DEFINIMOS E INICIALIZAMOS GRILLA*/
		vector<vector<set<size_t>>> grid;
		size_t num_grid = floor(L);
		grid.resize(num_grid);
		for (size_t i=0; i<grid.size(); i++) grid[i].resize(num_grid);

		/*CONDICIÓN INICIAL*/
		init_system(system, state_vector, grid);
		system_new.resize(system.size());
		print_state(state_vector);

		/*EVOLUCIÓN DEL SISTEMA*/		
		int TimeStep = 0;
		KIND i_max = 0, t_max = 0;
		while (state_vector[1] > 0)
		{
			CHECK (TimeStep, (int)1e02) print_epidemic_tofile(epidemic, state_vector, TimeStep);
			CHECK (TimeStep, (int)2e04) printf("Time: %0.f\n", TIME(TimeStep, delta_time));
			TimeStep ++;
			update_system(system, system_new, state_vector, grid, inter, TimeStep, anim);
			if (i_max < state_vector[1])
			{
				i_max = state_vector[1]; 
				t_max = TIME(TimeStep, delta_time);
			}
		} //WHILE

		updates += (float)TimeStep;

		/*ESCRITURA DE RESULTADOS*/
		print_finalstate_tofile(FinalState, state_vector, i_max, t_max, TimeStep);	//redefinir a tofile
		print_result_header();				
		print_state(state_vector);
		cout << endl;
	}  //FOR SIMUL
		
	int   stop_s       = clock();
	float cps          = (float)CLOCKS_PER_SEC;
	float time_elapsed = (float)(clock() - start_s)/cps;
	float metric       = updates*(float)N/time_elapsed;

	cout << "Time[seg]   : " << time_elapsed  << endl;
	cout << "Metrica[pps]: " << metric       << endl;
	
	metrica  << metric << endl;

	//Cerramos los archivos:
	FinalState.close();
	epidemic.close();
	anim.close();
	metrica.close();

	return 0;
}

