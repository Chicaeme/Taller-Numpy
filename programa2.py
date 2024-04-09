#importar la biblioteca
#Hacer un ALIAS para no escribir completo. (np) es opcional

import numpy as np 

#formas de crear arreglos
#Una forma de crear arreglos ndarray es usando una lista

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