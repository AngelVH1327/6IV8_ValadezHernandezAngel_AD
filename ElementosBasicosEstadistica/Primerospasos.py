import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Cargar archivos Excel
catalogo = pd.read_excel('Catalogo_sucursal.xlsx')
proyecto = pd.read_excel('proyecto1.xlsx')
# Combinar los excel
datos = proyecto.merge(catalogo, on='id_sucursal')


# 1. Conocer las ventas totales del comercio
ventas_totales = datos['ventas_tot'].sum()
print(f"Ventas totales del comercio: ${ventas_totales:.2f}")
 
# 2. Conocer cuantos socios tienen adeudo y cuantos ño tienen adeudo con su porcentaje correspondiente
conteo_adeudo = datos['B_adeudo'].value_counts()
porcentaje_adeudo = datos['B_adeudo'].value_counts(normalize=True) * 100

print("Conteo", conteo_adeudo)
print("Porcentaje", porcentaje_adeudo.round(2))

# 3. Grafica donde se pueda observar las ventas totales respecto del tiempo en una grafica de barras
ventas_por_mes = datos.groupby('B_mes')['ventas_tot'].sum()

plt.figure(figsize=(12,6))
ventas_por_mes.plot(kind='bar', color='skyblue')
plt.title("Ventas totales respecto al tiempo")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.grid()
plt.show()


# 4. Grafica donde se pueda visualizar la desviación estándar de los pagos realizados del comercio respecto del tiempo
std_pagos_mes = datos.groupby('B_mes')['pagos_tot'].std()

plt.figure(figsize=(12,6))
std_pagos_mes.plot(marker='o', linestyle='-', color='purple')
plt.title("Desviación estándar de pagos respecto al tiempo")
plt.xlabel("Mes")
plt.ylabel("Desviación estándar")
plt.grid()
plt.show()


# 5. Cuanto es la deuda total de los clientes
deuda_total = datos['adeudo_actual'].sum()
print(f"Deuda total clientes: ${deuda_total:.2f}")


# 6. Cuanto es el porcentaje de utilidad del comercio a partir de el total de las ventas respecto del adeudo 
utilidad = ventas_totales - deuda_total
porcentaje_utilidad = (utilidad / ventas_totales) * 100
print(f"Porcentaje de utilidad del comercio: {porcentaje_utilidad:.2f}%")


# 7. Crear un grafico circular de ventas por sucursal.
ventas_sucursal = datos.groupby('suc')['ventas_tot'].sum()

plt.figure(figsize=(8,8))
ventas_sucursal.plot(kind='pie', autopct='%1.1f%%', cmap='tab20')
plt.title("Ventas por sucursal")
plt.ylabel('')
plt.show()


# 8. Presentar un grafico de cuales son las deudas totales por cada sucursal respecto del margen de utilidad de cada sucursal.
deuda_sucursal = datos.groupby('suc')['adeudo_actual'].sum()
utilidad_sucursal = ventas_sucursal - deuda_sucursal

indices = np.arange(len(ventas_sucursal))
ancho = 0.35

plt.figure(figsize=(12,6))
plt.bar(indices - ancho/2, deuda_sucursal, ancho, color='red', label='Deuda total')
plt.bar(indices + ancho/2, utilidad_sucursal, ancho, color='green', label='Margen utilidad')

plt.xlabel('Sucursal')
plt.ylabel('Monto')
plt.title('Deuda total vs Margen de utilidad por sucursal')
plt.xticks(indices, ventas_sucursal.index)
plt.legend()
plt.grid()
plt.show()