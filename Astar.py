from Laberinto import Laberinto

def Astar_lab(lab : Laberinto):
    casilla_inicio = lab.casilla_i
    frontera = [casilla_inicio]
    wait = 0
    while frontera: 
        if len(frontera) == 0: # si el algoritmo no se puede mover en 3 tuernos, indica que no hay salida
            wait += 1
            if wait > 3:
                break
        else:
            wait = 0
        # elegir candidato por heurística
        casilla_actual = min(frontera, key=lambda x: lab.heuristica(x))
        if casilla_actual.tipo == -2:
            return True

        # vecinos según laberinto dinámico
        vecinos = lab.obtener_vecinos(casilla_actual)
        for v in vecinos:
            if v.tipo != 1:
                if v not in frontera: # evitar duplicados inmediatos
                    frontera.append(v) # guardamos los vecinos de nuestro espacio en el laberinto
        frontera.remove(casilla_actual)
        frontera = sorted(frontera, key=lambda x: lab.heuristica(x))[:2] # nos quedamos solo con los 3 con mejor heurisitca

        lab.cambiar_laberinto(bloqueados=frontera)

    #print("No hay salida posible.")
    return False


