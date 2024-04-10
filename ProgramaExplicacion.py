import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(h, w, maxit=20, r=2): #funcion con 4 parametros
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5, 1.5, 4*h+1) #indica con cuantos decimales quiere trabajar np.linspace(start, stop, cantidad de numeros) para X
    y = np.linspace(-1.5, 1.5, 3*w+1) #indica con cuantos decimales quiere trabajar np.linspace(start, stop, cantidad de numeros) para Y
    A, B = np.meshgrid(x, y) #Devuelve una lista de matrices de coordenadas a partir de vectores de coordenadas.
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))