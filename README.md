# Desarrollo de script para analisis de ventas 
Integrantes: Martino Bartoli

Para este trabajo elegí el Escenario B - Análisis de Ventas de una Pequeña Empresa, donde se busco desarrollar un script para una ferreteria que en base a una serie de datos, realice un analisis de ventas detallando; ventas totales, producto más vendido, etc. Además, el script genera un gráfico que permite ver la evolución de las ventas totales mes a mes. 

Para la organización y estructura de datos se utilizo un "Dataset de ventas simuladas" que tiene como características llevar; un registros diarios de ventas, contar con columnas típicas como fecha de venta y monto de ventas, y cuenta con un formato CSV fácilmente importable.

Para el desarrollo del script fue fundamental el uso de las librerias; "pandas y matplotlib" de python. Pandas permite manipular, limpiar y analizar datos estructurados. En el caso del tp, los datos vienen en un archivo de texto .csv el cual es transformado en una tabla ordenada y limpia, siendo de muy utilidad para organizar datos, realizar operaciones, etc. 

Por otro lado esta la librearia de matplotlib, esta permite realizar todo tipo de gráficos animados o no. Tiene una gran capacidad de personalización al poder crear lineas, gráficos de barras, y demás estilos visuales. Ambas librerias trabajan para presentar diferentes tipos de analisis de ventas, dando información muy valiosa para cualquier empresa donde se usen. 

## Instrucciones para ejecutar el script 
Para correr el análisis de ventas y generar el gráfico de evolución mensual, siga estos pasos dentro del entorno de Google Colab:

 **Clonar el repositorio:**
   Abra una celda de código en Colab y ejecute el siguiente comando para descargar el proyecto en el entorno local:
   ```bash
   !git clone [https://github.com/bartolimartino/TP-Organizaci-n-Empresarial.git](https://github.com/bartolimartino/TP-Organizaci-n-Empresarial.git)

   Una vez haya descargado el script, debe posicionarse dentro del directorio raiz del repositorio escribiendo el siguiente comando:
    %cd TP-Organizaci-n-Empresarial

   Por ultimo queda ejecutar el script mediante el comando:
    !python scripts/analisis_ventas.py
