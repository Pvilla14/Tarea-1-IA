#!/bin/bash

# Algoritmos disponibles
algorithms=("bfs" "Astr" "gen")

# Tamaños de laberinto a probar
sizes=(5 10 20 50)

# Cantidades de salidas a probar
exits=(2 4 6 10)

# Probabilidades de pared
walls=(2 3 5)

for alg in "${algorithms[@]}"; do
    output_file="results_${alg}.csv"

    # Encabezado del CSV (se crea el archivo)
    echo "size,exits,algorithm,walls,time,final" > "$output_file"

    for n in "${sizes[@]}"; do
        for k in "${exits[@]}"; do
            for w in "${walls[@]}"; do
                i=0
                while [ $i -lt 200 ]; do
                    # Ejecuta el programa y captura salida
                    res=$(python3 Main.py "$n" "$k" "$alg" "$w")

                    # Limpia salida: separa por ";" → tiempo y final
                    tiempo=$(echo "$res" | cut -d';' -f1 | tr -d ' s')
                    final=$(echo "$res" | cut -d';' -f2)

                    # Guarda fila en CSV
                    echo "$n,$k,$alg,$w,$tiempo,$final" >> "$output_file"

                    ((i++))
                done
            done
        done
    done
done
