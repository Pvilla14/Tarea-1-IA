import random
from Laberinto import Laberinto

CAMINOS = 80

GENES = [0, 1, 2, 3] # 0 = arriba, 1 = abajo, 2 = izquierda, 3 = derecha

def crear_caminos(size_lab):
    global CAMINOS, GENES
    cant = 3 * size_lab # caminos de largo 2*n
    caminos = []
    for _ in range(CAMINOS):
        camino = random.choices(GENES, k = cant) # caminos de largo 2*n
        while len(camino) != cant:
            camino = random.choices(GENES, k = cant)
        caminos.append(camino)
    return caminos

def mutacion():
    global GENES
    return random.choice(GENES)

def convinacion(camino1, camino2):
    camino3 = []
    for c1, c2 in zip(camino1, camino2):
        prob = random.random()
        if prob < 0.4:
            camino3.append(c1)
        elif prob < 0.8:
            camino3.append(c2)
        else:
            camino3.append(mutacion())
    return camino3

def recorrer_camino(lab : Laberinto, camino):
    # camino es una lista de numeros [0,1,2,3] que representan [arriba, abajo, izquierda, derecha]
    actual = lab.casilla_i
    while camino:
        fila = actual.fila
        columna = actual.columna
        paso = camino.pop(0) # se saca el primer elemento del camino
        if paso == 0: # arriba
            if fila > 0 and  lab.matriz[fila - 1][columna].tipo != 1: # no es pared y no se sale del laberinto
                actual = lab.matriz[fila - 1][columna]
                if actual.tipo == -2:
                    return (True, actual) # si es la salida se devuelve True y la casilla donde queda
                else: continue
            else: 
                return (False, actual)
            
        if paso == 1: # abajo
            if fila < lab.filas - 1 and lab.matriz[fila + 1][columna].tipo != 1: # no es pared y no se sale del laberinto
                actual = lab.matriz[fila + 1][columna]
                if actual.tipo == -2:
                    return (True, actual) # si es la salida se devuelve True y la casilla donde queda
                else: continue
            else: 
                return (False, actual)
            
        if paso == 2: # izquierda
            if columna > 0 and lab.matriz[fila][columna - 1].tipo != 1: # no es pared y no se sale del laberinto
                actual = lab.matriz[fila][columna - 1]
                if actual.tipo == -2:
                    return (True, actual) # si es la salida se devuelve True y la casilla donde queda
                else: continue
            else: 
                return (False, actual)
            
        if paso == 3: # derecha
            if columna < lab.columnas - 1 and lab.matriz[fila][columna + 1].tipo != 1: # no es pared y no se sale del laberinto
                actual = lab.matriz[fila][columna + 1]
                if actual.tipo == -2:
                    return (True, actual) # si es la salida se devuelve True y la casilla donde queda
                else: continue
            else: 
                return (False, actual)

    if actual.tipo == -2:
        return (True, actual) # si es la salida se devuelve True y la casilla donde queda
    else:
        return(False,actual)

def dist_salida(lab : Laberinto, casilla):
    # distancia de manhattan a la salida verdadera
    for i in range(lab.filas):
        for j in range(lab.columnas):
            if lab.matriz[i][j].tipo == -2:
                return abs(casilla.fila - i) + abs(casilla.columna - j)

def fitness(lab : Laberinto, camino):
    camino_copy = camino.copy()
    while camino_copy != camino:
        camino_copy = camino.copy()
    (converge, casilla) = recorrer_camino(lab, camino_copy)
    if converge:
        return dist_salida(lab, casilla)
    else:
        return float('inf')
    
def gen_lab(lab: Laberinto):
    poblacion = crear_caminos(lab.filas)
    generaciones = 300
    for _ in range(generaciones):
        poblacion = sorted(poblacion, key=lambda x: fitness(lab, x))
        if fitness(lab, poblacion[0]) == 0:
            return True
        nueva_poblacion = [] 
        nueva_poblacion.append(poblacion[:20]) # se selecciona 10 caminos con mejor fitness
        while len(nueva_poblacion) < CAMINOS:
            padre1 = random.choice(nueva_poblacion)
            padre2 = random.choice(nueva_poblacion)
            hijo = convinacion(padre1, padre2)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion
        lab.cambiar_laberinto()
    #print("No hay salida posible.")
    return False