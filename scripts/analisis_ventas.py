import pandas as pd
import matplotlib.pyplot as plt

 
# 1. El dataset se carga en el dataframe para posteriormente trabajar con el
df = pd.read_csv('datos/dataset.csv')

# Transforma las fechas de texto a formato fecha (datetime) para poder ordenarlas cronológicamente
df['fecha_de_venta'] = pd.to_datetime(df['fecha_de_venta'])

# CÁLCULO GENERAL: Monto de cada venta (Precio x Cantidad)
# La forma en que se realiza este calculo es gracias a una propiedad de panda llamada vectorización, en lugar de ir fila por fila va por columnas.
# Python toma la columna entera de precios y la multiplica uno a uno por los valores de la columna de cantidades. Fila 1 con Fila 1, Fila 2 con Fila 2, y así sucesivamente.
df['monto_total'] = df['precio'] * df['cantidad_vendida']

# Se suman el total de todas las ventas
ventas_totales = df['monto_total'].sum()

# Producto más vendido
# En esta primera linea se juntan todas las filas que tienen el mismo nombre de producto y crea un
# "paquete" para cada tipo de producto, y luego suma las cantidades de cada tipo de herramienta
unidades_por_producto = df.groupby('producto')['cantidad_vendida'].sum()

# En esta linea se busca el "PRODUCTO" que tenga la cantidad más alta de unidades vendidas.
producto_mas_vendido = unidades_por_producto.idxmax()

# Esta linea hace algo parecido a la anterior, solo que esta muestra el "NUMERO" de unidades vendidas más grande
cantidad_mas_vendida = unidades_por_producto.max()

# Ventas por mes
df['mes'] = df['fecha_de_venta'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['monto_total'].sum()


# 3. Informe Final
print("="*50)
print("   INFORME DE VENTAS - FERRETERÍA")
print("="*50)
print(f"🔹 Ventas Totales de la Empresa: ${ventas_totales:,.2f}")
print(f"🔹 Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")
print("\n🔹 Ventas por Mes (Evolución Financiera):")
print(ventas_por_mes.to_string())
print("="*50)


# 4. Crear Gráfico: EVOLUCIÓN DE VENTAS
plt.figure(figsize=(9, 5))

# Graficamos con una línea para ver la evolución mes a mes
ventas_por_mes.plot(kind='line', marker='o', color='forestgreen', linewidth=2)

# Configuración estética del gráfico (Títulos, etiquetas de ejes y cuadrícula de lectura)
plt.title('Evolución Mensual de Ventas ($)', fontsize=14, fontweight='bold')
plt.xlabel('Meses (Año-Mes)', fontsize=11)
plt.ylabel('Recaudación ($)', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Guardamos el gráfico directo en la carpeta /resultados como .png
plt.savefig('resultados/evolucion_ventas.png')
