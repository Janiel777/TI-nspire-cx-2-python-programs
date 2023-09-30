# TI-nspire-cx-2-python-programs
This repository contains python programs that use the TI-nspire-cx-2 calculator model libraries to solve problems that you may frequently encounter if you are studying a university degree.


## Índice

1. [Matemáticas](#matematicas)
   1.1 [Gauss Jordan](#gauss-jordan)
   1.2 [Inverse Matrix](#Inverse-Matrix)
2. [Química](#quimica)
   2.1 [Celda Unitaria](#Celda-Unitaria)
3. [Estadística](#estadistica)
   3.1 [Box plot](#Box-plot)
   3.2 [Grafica de percentiles](#Grafica-de-percentiles)
   3.3 [Histograma](#Histograma)
   3.4 [Medidas-de-dispersion-y-tendencia-central](#Medidas-de-dispersion-y-tendencia-central)

<a name="matematicas"></a>
## Matemáticas

<a name="gauss-jordan"></a>
### Gauss Jordan

Este algoritmo en python, no solamente resuelve sistemas de ecuaciones nxn, si no que tambien muestra el procedimiento. Tomemos de ejemplo la siguiente ecuacion:

![sistema de ecuaciones](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/2aa82c71-d16c-4291-ae1e-d7eaf20026b7)

1. Al correr el algoritmo, nos va a pedir que introduscamos el numero de ecuaciones. Tengan en cuenta que no esta pensado para resolver sistemas con menor numero de ecuaciones al de las incognitas. 
2. Despues introducimos los coeficientes de las ecuaciones separado por espacio y nos va a mostrar las operaciones de filas de matrices necesarias a realizar para poder igualar todos los numeros por encima y debajo de la diagonal a 0 y los de la diagonal iguales a 1. A continuacion este es el output del codigo para dicho sistema de ecuacion:

```
#Running GaussJordan.py
from GaussJordan import *
Enter the number of equations: 3
Enter row {} (elements separated by spaces): 1 1 -2 9
Enter row {} (elements separated by spaces): 2 -1 4 4
Enter row {} (elements separated by spaces): 2 -1 6 -1
R1/1
['1', '1', '-2', '9']
['2', '-1', '4', '4']
['2', '-1', '6', '-1']

R2 - R1*2
['1', '1', '-2', '9']
['0', '-3', '8', '-14']
['2', '-1', '6', '-1']

R3 - R1*2
['1', '1', '-2', '9']
['0', '-3', '8', '-14']
['0', '-3', '10', '-19']

R2/-3
['1', '1', '-2', '9']
['0', '1', '-8/3', '14/3']
['0', '-3', '10', '-19']

R3 - R2*-3
['1', '1', '-2', '9']
['0', '1', '-8/3', '14/3']
['0', '0', '2', '-5']

R3/2
['1', '1', '-2', '9']
['0', '1', '-8/3', '14/3']
['0', '0', '1', '-5/2']

R2 - R3*-8/3
['1', '1', '-2', '9']
['0', '1', '0', '-2']
['0', '0', '1', '-5/2']

R1 - R3*-2
['1', '1', '0', '4']
['0', '1', '0', '-2']
['0', '0', '1', '-5/2']

R1 - R2*1
['1', '0', '0', '6']
['0', '1', '0', '-2']
['0', '0', '1', '-5/2']

The solution is:  ['6', '-2', '-5/2']
```
<a name="Inverse-Matrix"></a>
### Inverse Matrix

Este algoritmo sigue la misma idea que el de Gauss Jordan solo que amplia la matriz original añadiendo a la derecha la matriz identidad. Hace las operaciones de filas de matrices necesarios hasta hacer que la matriz de la izquierda se convierta en la matriz identidad. Resultando que la matriz de la derecha va a ser la inversa de la matriz original con la que empezamos.

Tomemos de ejemplo de nuevo la siguiente ecuacion:

![sistema de ecuaciones](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/2aa82c71-d16c-4291-ae1e-d7eaf20026b7)

1. Al correr el codigo nos va a pedir que introduscamos el tamaño de la matriz cuadrada. Tiene que ser cuadrada, nxn donde n es el mismo numero de columnas que de filas, ya que la vamos a estar ampliando con una matriz identidad de igual tamaño.
2. Despues introducimos los valores de los coeficientes separados por espacios, sin incluir las constantes a la derecha de los signos de igual.
A continuacion un ejemplo del output del codigo:
```
#Running InverseMatrix.py
from InverseMatrix import *
Enter the size of the square matrix: 3
Enter row 1 (elements separated by spaces): 1 1 -2 9
Enter row 2 (elements separated by spaces): 2 -1 4 4
Enter row 3 (elements separated by spaces): 2 -1 6 -1
The original matrix is:
1 1 -2 9
2 -1 4 4
2 -1 6 -1

R1/1
1 1 -2 1 0 0
2 -1 4 0 1 0
2 -1 6 0 0 1

R2 - R1*2
1 1 -2 1 0 0
0 -3 8 -2 1 0
2 -1 6 0 0 1

R3 - R1*2
1 1 -2 1 0 0
0 -3 8 -2 1 0
0 -3 10 -2 0 1

R2/-3
1 1 -2 1 0 0
0 1 -8/3 2/3 -1/3 0
0 -3 10 -2 0 1

R1 - R2*1
1 0 2/3 1/3 1/3 0
0 1 -8/3 2/3 -1/3 0
0 -3 10 -2 0 1

R3 - R2*-3
1 0 2/3 1/3 1/3 0
0 1 -8/3 2/3 -1/3 0
0 0 2 0 -1 1

R3/2
1 0 2/3 1/3 1/3 0
0 1 -8/3 2/3 -1/3 0
0 0 1 0 -1/2 1/2

R1 - R3*2/3
1 0 0 1/3 2/3 -1/3
0 1 -8/3 2/3 -1/3 0
0 0 1 0 -1/2 1/2

R2 - R3*-8/3
1 0 0 1/3 2/3 -1/3
0 1 0 2/3 -5/3 4/3
0 0 1 0 -1/2 1/2

The inverse of the matrix is:
1/3 2/3 -1/3
2/3 -5/3 4/3
0 -1/2 1/2
```

<a name="quimica"></a>
## Química 

<a name="Celda-Unitaria"></a>
### Celda Unitaria

Este algoritmo dibuja una celda unitaria cristalina SC, BCC, FCC o HCP con la posicion de sus atomos. Despues te permite dibujar encima de esa celda un vector o un plano. Esta visualizacion grafica es util para saber cuantos atomos interseca el verctor o el plano. Esto es util para para algunos problemas de densidad lineal y densidad planar.



<a name="estadistica"></a>
## Estadística

<a name="Box-plot"></a>
### Box plot

Contenido de la sección de Box plot.

<a name="Grafica-de-percentiles"></a>
### Grafica de percentiles

Contenido de la sección de Grafica de percentiles.

<a name="Histograma"></a>
### Histograma

Contenido de la sección de Histograma.

<a name="Medidas-de-dispersion-y-tendencia-central"></a>
### Medidas-de-dispersion-y-tendencia-central

Contenido de la sección de Medidas-de-dispersion-y-tendencia-central.


