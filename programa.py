import numpy as np

# Crear un arreglo de una dimensión
arr1d = np.array([1, 2, 3, 4, 5])
print("Arreglo 1D:")
print(arr1d)

# Crear un arreglo de dos dimensiones (matriz)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nArreglo 2D (matriz):")
print(arr2d)

# Acceder a elementos de un arreglo
print("\nAcceder a elementos:")
print("Elemento en la fila 0, columna 1:", arr2d[0, 1])  # Accede al elemento en la fila 0, columna 1

# Operaciones matemáticas con arreglos
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("\nOperaciones matemáticas:")
print("Suma de arreglos:", arr1 + arr2)
print("Resta de arreglos:", arr1 - arr2)
print("Multiplicación de arreglos:", arr1 * arr2)
print("División de arreglos:", arr1 / arr2)

# Funciones matemáticas
print("\nFunciones matemáticas:")
print("Seno:", np.sin(arr1))
print("Coseno:", np.cos(arr1))
print("Exponencial:", np.exp(arr1))
print("Logaritmo natural:", np.log(arr1))
