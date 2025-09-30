import time
import csv
from Laberinto import Laberinto
from bfs import bfs_lab
from Astar import Astar_lab
from gen import gen_lab

# Algoritmos disponibles
algorithms = ["bfs"]

# Tamaños de laberinto a probar
sizes = [50, 100]

# Cantidades de salidas a probar
exits = [6, 10]

# Probabilidades de que una casilla sea pared (más chico = más paredes)
bush_probs = [2, 3, 5]

# Iteraciones por configuración
num_iter = 50

# Archivos de salida
output_files = {
    "bfs": "results_bfs.csv",
    "Astr": "results_Astr.csv",
    "gen": "results_gen.csv"
}

def run_experiments():
    for alg in algorithms:
        filename = output_files[alg]
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["n", "k", "algorithm", "bush", "time", "success"])  # encabezado

            for n in sizes:
                for k in exits:
                    for bush in bush_probs:
                        for _ in range(num_iter):
                            lab = Laberinto(n, k, bush)

                            start = time.perf_counter()
                            if alg == "bfs":
                                final = bfs_lab(lab)
                            elif alg == "Astr":
                                final = Astar_lab(lab)
                            elif alg == "gen":
                                final = gen_lab(lab)
                            else:
                                raise ValueError(f"Algoritmo no reconocido: {alg}")
                            end = time.perf_counter()

                            writer.writerow([n, k, alg, bush, round(end - start, 4), final])
                    print(k)
                print(n)
        print(alg)


if __name__ == "__main__":
    run_experiments()
