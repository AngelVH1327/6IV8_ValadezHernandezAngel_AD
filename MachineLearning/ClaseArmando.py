import numpy as np
import pandas as pd
from scipy.spatial import distance

##Definir las cordenadas de las tiendas

tiendas={
    'Tienda A':(1,1),
    'Tienda B':(1,5),
    'Tienda C':(7,1),
    'Tienda D':(3,3),
    'Tienda E':(4,8)
}

#Convertir lasll cordenadas a un dataframe para facilitar el calculo
df_tiendas=pd.DataFrame(tiendas).T
df_tiendas.columns=['x','y']
print("coordenadas de las tiendas:")
print(df_tiendas)

#Inicializar un dataframe para almacenar las distancias

distancias_eu=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_mh=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_ch=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

#Calcular las distancias
for i in df_tiendas.index:
    for j in df_tiendas.index:
        #Distancias euclidianas:
        distancias_eu.loc[i,j]=distance.euclidean(df_tiendas.loc[i],df_tiendas.loc[j])
        #Distancias manhattan:
        distancias_mh.loc[i,j]=distance.cityblock(df_tiendas.loc[i],df_tiendas.loc[j])
        #Distancias chebyshev:
        distancias_ch.loc[i,j]=distance.chebyshev(df_tiendas.loc[i],df_tiendas.loc[j])

#Mostrar los resultados
print("\nDistancias euclidianas entre las tiendas: ")
print(distancias_eu)
print("\nDistancias Manhattan entre las tiendas: ")
print(distancias_mh)
print("\nDistancias Chebyshev entre las tiendas: ")
print(distancias_ch)
