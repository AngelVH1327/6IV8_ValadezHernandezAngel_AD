import pandas as pd

#Escribir una fucnion que reciba un diccionario con las notas de los estdiantes del curso y devuelve una serie con minimo, maximo, media,desviacion tipica

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviacion Estandar'])
    return estadisticas

def aprobados(notas):
    notas = pd.Series(notas)
    return notas [notas >= 6].sort_values(ascending=False)

notas = {'Juan': 9, 'Juanita': 7, 'Pedro': 6.6, 'Fabian': 8.5, 'Maximiliano': 7.5, 'Sandra': 9.8, 'Rosario': 9}

print(aprobados(notas))