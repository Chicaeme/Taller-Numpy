#importar la biblioteca
#Hacer un ALIAS para no escribir completo. (np) es opcional

import numpy as np 

#formas de crear arreglos
#1) Una forma de crear arreglos ndarray es usando una lista

miLista=[3, 5, 7, 9]

miArreglo= np.array(miLista)
#dimensiones
print(miArreglo.ndim)
#tamaño
print(miArreglo.shape)
#cantidad de elementos
print(miArreglo.size)
#imprime los enteros
print(miArreglo.dtype)

#exactamente lo de arriba pero sin escribir miLista
miArreglo2= np.array([3,6,7,90])


#float
miLista=[3.79, 5.89, 7, "Hola"]
miArreglo= np.array(miLista)
print(miArreglo)

#ARREGLOS DE DOS DIMENSIONES

miLista=[(1,3,5,7), (3,8,2,4)]
print(miArreglo.ndim) 

miLista=[[1,3,5,7], [3,8,2,4], [3,6,8,9]]
miArreglo= np.array(miLista, dtype=int)
print(miArreglo) 

#2) Usando funciones de ''relleno'' de arreglos

miArreglo= np.zeros((2,2,2))

print(miArreglo)

#cinco filas y cuatro columnas

miArreglo= np.zeros((5,4))

print(miArreglo)

#cuatro filas y cinco columnas

miArreglo= np.zeros((4,5))

print(miArreglo)

#3) con np.ones


miArreglo= np.ones((4,5))

print(miArreglo)

#4) con funcion empty pero sin ningun valor


miArreglo= np.empty((4,5))

print(miArreglo)

#5) Arange

miArreglo= np.arange(10)

print(miArreglo)
#con reshape modifica la dimension
miArreglo.reshape((2,10))
