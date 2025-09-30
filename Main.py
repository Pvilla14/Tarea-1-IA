import time
import sys
from Laberinto import Laberinto
from bfs import bfs_lab
from Astar import Astar_lab
from gen import gen_lab

if __name__ == "__main__":

    if len(sys.argv) < 5: 
        sys.exit(1)
    
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    algorithm = sys.argv[3]
    bush = int(sys.argv[4])

    laberinto = Laberinto(n,k, bush=bush)

    if algorithm == 'gen':
        start = time.perf_counter()
        final = bfs_lab(laberinto)
        end = time.perf_counter()
    elif algorithm == 'bfs':
        start = time.perf_counter()
        final = gen_lab(laberinto)
        end = time.perf_counter()
    elif algorithm == 'Astr':
        start = time.perf_counter()
        final =Astar_lab(laberinto)
        end = time.perf_counter()
    print(f"{(end - start): .4f}s;{final};")


    