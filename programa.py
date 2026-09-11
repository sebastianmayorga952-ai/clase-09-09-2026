# primero intalar bibliotecas 
# segundo importar las bibliotecas en el archivo en donde los voy a usar 
# tercerro usar los elementos de la biblioteca 
#un geodataframe es una tablas de datos en donde al menos una columna 
#contien datos espaciales vectoriales (puntos, lineas o poligonos) y que tiene un sistema de referencia de coordenadas asociado.

#leer archivos que tengan datos espaciales 
 #archivo json 

import geopandas as gpd

archivo = gpd.read_file("custom.geo.json")

