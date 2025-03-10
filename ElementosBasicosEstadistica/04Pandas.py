import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#
print(df.head())

#mostrar ultimas 5 filas
print (df.tail())

#mostrar fila en especifico
print (df.iloc[7])

#mostrar la columna ocean proximity
print (df["ocean_proximity"])

#obtener la media de la columan total_rooms
mediadecuarto = df["total_rooms"].mean()
print('La media de total room es: ', mediadecuarto)

#obtener mediana
medianacuarto = df["median_house_value"].median()
print('La mediana de median house value es: ', medianacuarto)

#obtener suma de popular
salariototal = df["population"].sum()
print('El salario total es: ', salariototal)

#para poder filtrar
vamoshacerunfiltro = df[df['ocean_proximity'] == 'ISLAND']
print(vamoshacerunfiltro)

#vamos a hacer un grafico de dispercios
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])
#nombramos los ejes
plt.xlabel("Proximidad")
plt.ylabel("Precio")

plt.title("Grafico de Dispersion de Proximidad al oceano vs precio")
plt.show()