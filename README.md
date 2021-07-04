# US-TFG-1160
TFG Ref. 1160 - Estudio y comparativa de entornos GPU/CPU para problemas de ciencia de datos.

# Estructura
* /data - directorio no provisto, es el directorio por defecto donde poner ficheros de datos a leer por los notebooks.
	* Se recomienda el siguiente formato para no requerir cambios en el flujo de los notebooks:
	* /data/\<ciudad\>/\<nombre\>.csv
* /documents - documentación miscelánea, p.ej. hojas de datos de comparativas.
* /notebooks - directorio donde se guardan los notebooks de Jupyter para ejecutar.
* /utils - utilidades de tratamiento de datos, normalización y provisión de datos estáticos, tales como listas de columnas a leer/utilizar para fitting de modelos.

# Cuadernos

Estos son los cuadernos (*notebook*) de Jupyter disponibles:

1. nb1_visual.ipynb: descripción del proceso de lectura, manipulación y visualización de datos. Contiene una descripción en profundidad de los pasos seguidos durante la carga de datos y generación del *dataset* final. Los pasos empleados aquí son replicados en los demás cuadernos con pequeñas diferencias.
2. nb2_kmeans.ipynb: algoritmo k-medias (*K-means*) para el agrupamiento (*clustering*) de datos en dos dimensiones.
3. nb3_dbscan.ipynb: algoritmo DBSCAN para agrupamiento de datos donde hay grupos definidos.
4. nb4_knn.ipynb: algoritmo de cálculo de distancias entre puntos *K Nearest Neighbors* (*KNN*).
5. nb5_regression.ipynb: empleo de regresión linear simple para predicción de un objetivo y sobre datos tabulados con múltiples columnas.
6. nb6_coord.ipynb: uso de técnicas de descenso por coordenadas (*Coordinate Descent*) como alternativa más potente de regresión, así como para el cálculo de trayectorias de disminución de funciones de error.
7. nb7_other.ipynb: descripción de algunos casos de error en algoritmos que no se pudieron ejecutar correctamente.
8. nb8_dask.ipynb: cálculo de varios modelos empleando múltiples GPUs mediante el gestor multinodo de Dask.
