import numpy as np
import random 

class Casilla:
    def __init__(self, fila, columna, prob = 3):
        self.fila = fila
        self.columna = columna
        self.obstaculo_o_camino(prob=prob)
        
    def obstaculo_o_camino(self, prob = 3):
        if random.randint(0, prob) != 0: # un 25% de probabilidad de que sea obstaculo
            self.tipo = 0 # camino
        else:
            self.tipo = 1 # obstaculo

    def ver_tipo(self):
        if self.tipo == 1:
            return "Obstaculo"
        elif self.tipo == -1:
            return "False Final"
        elif self.tipo == -2:
            return "True Final"
        elif self.tipo == 0:
            return "Camino"
        elif self.tipo == 2:
            return "Inicio"
        

class Laberinto:
    
    def __init__(self, n, k, bush = 3):
        self.filas = n
        self.salidas = k
        self.columnas = n
        self.matriz = np.empty((self.filas, self.columnas), dtype=object)
        self.densidad = bush
        self.generar_laberinto()
        

    def generar_laberinto(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                casilla = Casilla(i, j, prob=self.densidad)
                self.matriz[i][j] = casilla

        self.crear_paredes()
        self.casilla_inicio()

        #self.mostrar_laberinto()

    def mostrar_laberinto(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j].tipo == 0:
                    print(" . ", end="")
                elif self.matriz[i][j].tipo == -1:
                    print(" F ", end="")
                elif self.matriz[i][j].tipo == -2:
                    print(" T ", end="")
                elif self.matriz[i][j].tipo == 2:
                    print(" I ", end="")
                else:
                    print(" # ", end="")
            print()  # Nueva línea al final de cada fila
    

    def crear_paredes(self):
        borde = []

        for i in range(self.filas):
            borde.append((i, 0))                  # izquierda
            borde.append((i, self.columnas - 1))  # derecha
        for j in range(1, self.columnas - 1):
            borde.append((0, j))                  # arriba
            borde.append((self.filas - 1, j))     # abajo

        # elegir una salida real
        real = random.choice(borde)
        self.matriz[real[0]][real[1]].tipo = -2
        self.casilla_fin = self.matriz[real[0]][real[1]]

        # elegir k-1 salidas falsas sin repetir
        posibles_falsas = [pos for pos in borde if pos != real]
        falsas = random.sample(posibles_falsas, self.salidas - 1)

        for (i, j) in falsas:
            self.matriz[i][j].tipo = -1

    def casilla_inicio(self):
        i = random.randint(1, self.filas - 1)
        j = random.randint(1, self.columnas - 1)

        while self.matriz[i][j].tipo == -2 or self.matriz[i][j].tipo == -1:
            i = random.randint(1, self.filas - 2)
            j = random.randint(1, self.columnas - 2)

        self.matriz[i][j].tipo = 2
        self.casilla_i = self.matriz[i][j]

    def obtener_vecinos(self, casilla):
        vecinos = []
        fila = casilla.fila
        columna = casilla.columna

        # Arriba
        if fila > 0:
            vecinos.append(self.matriz[fila - 1][columna])
        # Abajo
        if fila < self.filas - 1:
            vecinos.append(self.matriz[fila + 1][columna])
        # Izquierda
        if columna > 0:
            vecinos.append(self.matriz[fila][columna - 1])
        # Derecha
        if columna < self.columnas - 1:
            vecinos.append(self.matriz[fila][columna + 1])

        return vecinos
    
    def cambiar_laberinto(self, bloqueados = None):
        for i in range(self.filas):
            for j in range(self.columnas):
                casilla = self.matriz[i][j]
                if casilla.tipo in [0, 1] and (bloqueados == None or casilla not in bloqueados): # solo cambio caminos y obstaculos y los que no están bloquedos
                    casilla.obstaculo_o_camino(prob = self.densidad)

    def heuristica(self, casilla):
        #obtiene la distancia de la casilla a la salida verdadera
        fila = casilla.fila
        col = casilla.columna

        return abs(fila - self.casilla_fin.fila) + abs(col - self.casilla_fin.columna)
    
    def hue_valores(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                casilla = self.matriz[i][j]
                print(" ", self.heuristica(casilla), " ", end="")
            print()