**Laberinto**
El laberinto que trabajamos nosotros es un laberinto dinamico con 5 tipos de casillas, las cuales son:

| Valor | Tipo | 
| 0 | camino |
| 1 | pared |
| 2 | inicio |
| -1 | salida falsa | 
| -2 | salida real |

La creación del laberinto consiste en una matriz con un tamaño indicado por el usuario, una cantidad de salidas indicadas por usuario, y finalmente, un valor que representa la densidad de paredes, el cual es inverso a esta proporción, ya que, por ejemplo, si el número es 5, la probabilidad de que una casilla sea pared va a ser de 1 entre 5.
Luego, se crean las paredes(salidas), eligiendo aleatoriamente k (con k el valor indicado por el usuario) casillas ubicadas en los laterales del laberinto, de las cuales la primera es la real, y las otras las falsas.
Finalmente, para cambiar el estado de las casillas lo que se hace es llamar casilla a casilla y selecionar una función dentro de estas que puede variar su estado entre camino o pared, dependiendo del parámetro de densidad antes explicado. Este metodo fue elegido dado que consideramos que el laberinto funciona mejor y mas aleatoriamente si todas las casillas pueden o no ser caminos, esto le entrega mas dificultad a los algoritmos, y permite mejores resultado y testeos mas únicos.


**Algoritmos Utilizados**
Para esta tarea se tomó la decisión de utilizar no solo 2 algoritmos sino que 3, 
uno no infomado, el cual es un bfs, uno si informado el cual es una variante del A*(A estrella),
y uno genético, el cual funciona segun la metodologia de mutaciones y convinaciones de caminos.

*BFS:*
El algoritmo de bfs funciona con una cola, la cual va ingresando los vecinos accesibles desde la posición inicial, y luego va ampliando el recorrido en función de los nuevos vecinos que se van añadiendo. Para controlar el tema del un laberinto movil, lo que se hace es bloquear los vecinos sobre los cuales tiene acceso el bfs, es decir, aquellos que están en la cola, esto dado que sería como si una persona estuviese parada ahí, por lo que el laberinto no puede cambiar en esos lugares. Finalmente, cuando resulta que uno de los vecinos a los cuales se expandío era la salida real, retorna True en significado de que logró encontrar la salida, de no ser así, retorna False.
Una medida de seguridad para que el bfs no se quede sin caminos por culpa de las paredes, si una casilla no logra expandir nada, se vuelve a agregar a la cola, pero para evitar que esto pase infinitamente, la matriz de visitados guarda un registro de cuantas veces se han vuelto a agregar las casillas, y si este supera las 3 veces, entonces ya no se agrega.

*Astar:*
Nuestro algoritmo AStar es una modificación al original, ya que, dado que consume un exeso de memoria en guardar el camino completo para luego volver al anterior como lo hace el dfs, pero en lugar de nosotros almacenar todo el camino, lo que hacemos es guardar solo los 3 nodos con mejor heurística antes de modificar el laberinto, esto para no tener que volver a evaluar todo el recorido, y poder mejorar el rendimiento. ¿Cómo se notó esto? Bueno pues se notó considerablemente, siendo este algoritmo el mas veloz en todas las pruebas y consistente en siempre encontrar la salida. Sumandole esto, para poder asegurarse el encontrar la salida, este algoritmo tiene la capacidad de esperar turnos a que el laberinto cambie en caso de no poder expandir las casillas por culpa de las paredes, lo que hace es quedarse parado, esperar a que cambie el laberinto, y luego volver a revisar, pero como no dejaremos que quede esperando infinitamente, le permitimos esperar solo 3 turnos, y si para ese entonces aun no puede moverse, pues damos por finalizado el intento y calificado como una falla y no un éxito de escape.
La heuristica que usamos para este algoritmo es la heurística manhattan, la cual obtiene la distancia de cierta casilla a la casilla de salida real, la cual está almasenada como una variable dentro de la clase Laberinto.

*Algoritmo Genético:*
El algoritmo geenético, como era de esperarse, es un poco mas complicado, pero su implementación fue inspirada en el código encontrado en [GeeksforGeeks](https://www.geeksforgeeks.org/dsa/genetic-algorithms/), el cual explica como encontrar una cadena de strings usando un algoritmo genético que la genere. En este caso, lo que hacemos es primero generar una cantidad de caminos, los cuales estan conformados por enteros del 0 al 3 con cada uno significando una dirección a la cual moverse en el laberinto([0,1,2,3] = [arriba, abajo, izquierda, derecha]); y luego calculamos el valor fitness de cada uno, para ello, simulamos los movimientos del camino en la matriz sin modificar aun, y vemos si este cumple con los requisitos, los cuales son no salirse del mapa ni intentar atravesar obstaculos, de no ser así es castigado con el valor fitness maximo (float('inf')), pero si logra avanzar sin fallar, se calcula la distancia de la casilla en la cual quedo hasta la meta. En este caso y por temas de complejidad y tiempo de solución no consideramos las posibles paredes en dicho camino, sino que obtenemos la distancia manhattan.
Luego se seleccionan los 20 mejores caminos en base al fitness, y los demás se crean a partir de crosover y mutación de otros caminos.
Finalmente cambiamos el laberinto, y repetimos el proceso. Decidimos dejar fijas la cantidad de caminos en 80 y la cantidad de genereciones en 300 con el fin de poder testear en nuestros computadores, sin tener que estar corriendo el código demasiado tiempo.

**Resultado**



**Reflexiones**