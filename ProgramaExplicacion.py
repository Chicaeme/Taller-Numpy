import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(h, w, maxit=20, r=2): #funcion con 4 parametros
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5, 1.5, 4*h+1) #indica con cuantos decimales quiere trabajar np.linspace(start, stop, cantidad de numeros) para X
    y = np.linspace(-1.5, 1.5, 3*w+1) #indica con cuantos decimales quiere trabajar np.linspace(start, stop, cantidad de numeros) para Y
    A, B = np.meshgrid(x, y) #A y B es la variable de una lista de matrices de coordenadas a partir de vectores de coordenadas.
    C = A + B*1j #En la variable C queda guardada la operación.
    z = np.zeros_like(C) #asigna ceros a C y queda guardado en Z
    divtime = maxit + np.zeros(z.shape, dtype=int) # divtime = 20 + llena de cero una matriz que esta compuesta por el tamaño de Z y cantidad de enteros.

    for i in range(maxit): #for es para crear un ciclo en el rango de 1 a 20
        z = z**2 + C #operación de la variable z al cuadrado y la variable C
        diverge = abs(z) > r                    #retorna el valor del argumento en diverge
        div_now = diverge & (divtime == maxit)  # div_now es que coge la variab le diverge y iguala divtime con maxit
        divtime[div_now] = i                    # divtime[div_now] = iterador
        z[diverge] = r                          # z[diverge] nos indica que vale 2

    return divtime #retorna en abs(z)>r
plt.clf()
plt.imshow(mandelbrot(400, 400))