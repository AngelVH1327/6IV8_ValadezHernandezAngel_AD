import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

housing = pd.read_csv('ElementosBasicosEstadistica/housing.csv')


#Tabla
columns_to_analyze = ["median_house_value", "total_bedrooms", "population"]
df = housing[columns_to_analyze]

stats_summary = {
    "Media": df.mean(),
    "Mediana": df.median(),
    "Moda": df.mode().iloc[0],
    "Rango": df.max() - df.min(),
    "Varianza": df.var(),
    "Desviación estándar": df.std()
}

stats_df = pd.DataFrame(stats_summary)


#Grafico de dispersion
plt.hist(df["median_house_value"], bins=30, alpha=0.5, label="Median House Value", color='blue')
plt.hist(df["total_bedrooms"], bins=30, alpha=0.5, label="Total Bedrooms", color='red')
plt.hist(df["population"], bins=30, alpha=0.5, label="Population", color='green')

plt.axvline(df["median_house_value"].mean(), color='black', linestyle='dashed', linewidth=2, label="Promedio Median House Value")

plt.legend()
plt.title("Histograma Comparativo")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")


plt.show()
print(stats_df)


