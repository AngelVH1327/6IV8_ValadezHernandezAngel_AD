import numpy as np
import pandas as pd
from scipy.spatial import distance

# Definir las coordenadas de los puntos
puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
}

# Convertir las coordenadas a un DataFrame para facilitar el cálculo
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['x', 'y']
print("Coordenadas de los puntos:")
print(df_puntos)

# Inicializar DataFrames para almacenar las distancias
distancias_eu = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_mh = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_ch = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)

# Calcular las distancias
for i in df_puntos.index:
    for j in df_puntos.index:
        # Distancias euclidianas:
        distancias_eu.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
        # Distancias Manhattan:
        distancias_mh.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
        # Distancias Chebyshev:
        distancias_ch.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])

# Mostrar los resultados
print("\nDistancias euclidianas entre los puntos: ")
print(distancias_eu)
print("\nDistancias Manhattan entre los puntos: ")
print(distancias_mh)
print("\nDistancias Chebyshev entre los puntos: ")
print(distancias_ch)
