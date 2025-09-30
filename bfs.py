import numpy as np
from Laberinto import Laberinto
from collections import deque

def bfs_lab(lab : Laberinto):

    matriz = lab.matriz
    m_visitados = np.zeros((lab.filas, lab.columnas), dtype=int)

    cola = deque()

    casilla = lab.casilla_i

    m_visitados[casilla.fila][casilla.columna] = 1

    cola.append(casilla)

    while cola:

        actual = cola.popleft()
        vecinos = lab.obtener_vecinos(actual)
        vecinos_caminos = [vecino for vecino in vecinos if vecino.tipo != 1] 
        hay_vecinos = False
        for v in vecinos_caminos:
            if m_visitados[v.fila][v.columna] == 0:
                m_visitados[v.fila][v.columna] = 1
                cola.append(v)
                hay_vecinos = True

            if v.tipo == -2:
                return True
        
        if not hay_vecinos and m_visitados[actual.fila][actual.columna] < 3:
            cola.append(actual) # si no hay vecinos, no avanzamos por esa rama, y esperaamos a que cambie el laberinto
            m_visitados[actual.fila][actual.columna] += 1

        lab.cambiar_laberinto(bloqueados=vecinos_caminos)
    return False



    

