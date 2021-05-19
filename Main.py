'''Este es el main del algoritmo genetico'''
from time import time
from Genetic import Genetic
from Maze import Maze

if __name__ == "__main__":
	
    t_ini = time()

    Gen = Genetic(0.05)
    aMaze = Maze()
    Gen.MainProcess(aMaze)

    t_run = time() - t_ini
    print(f'El tiempo de ejecucion fue de {t_run} segundos')
