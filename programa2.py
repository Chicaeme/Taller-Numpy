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

#6) linspace funcion que es para decirle al programa con cuantos decimales quiero trabajar numpy.linspace=(start, stop, cantidad de numeros)

miArreglo= np.linspace(0,100,1000)
print(miArreglo)

#Funciones de operaciones

#elevado al cuadrado

a=np.array([5,10,15,20,25])
print(a)
b=np.array([3,4,7,9,56])
print(b)

#clase ndarray 

#a.sum
a=np.array([5,10,15,20,25])
c = a.sum()
print(c)

#a.min  valor minimo

#a.sort 

#a.mean saca la media

#DOS DIMENSIONES

a=np.array([[5,10,-1,20,25],[3,6,4,8,12]])
print(a)
print(a.sum()) #suma todo

#suma la fila
a=np.array([[5,10,-1,20,25], [3,6,4,8,12]])
print(a)
print(a.sum(axis=1))

#suma la columna
a=np.array([[5,10,-1,20,25], [3,6,4,8,12]])
print(a)
print(a.sum(axis=0))


#minimo de toda la matriz
a=np.array([[5,10,-1,20,25], [3,6,4,8,12]])
print(a)
print(a.min())

#cantidad de ejes * dimensiones
a=np.array([[5,10,-1,20,25], [3,6,4,8,12]])
print(a)
print(a.size)

#raiz cuadrada de toda la funcion
a=np.array([[5,10,-1,20,25], [3,6,4,8,12]])
print(a)
print(np.sqrt(a))

#exponencial
a=np.array([[5,10,-1,20,25], [3,6,4,8,12]])
print(a)
print(np.exp(a))


#METODO ADD suma los elementos es lo mismo que A+B 
a=np.array([[5,10,-1,20,25], [3,6,4,8,12]])
b=np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a)
print(b)
c= np.add(a,b)
print(c)

#n.round lo acerca al numero
import numpy as np 

a=np.array([7.3,9.9,3.9])

print(a.round())

#np.gradiente