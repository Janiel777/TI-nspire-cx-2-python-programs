## Índice
- Introduction
   - [About TI-nspire](#About)
   - [How to import the files](#How-to-import-the-files)
- Algoritmos
   - Matemáticas
      - [Gauss Jordan](#gauss-jordan)
      - [Inverse Matrix](#Inverse-Matrix)
   - Science
      - [Celda Unitaria](#Celda-Unitaria)
   - Estadística
      - [Box plot](#Box-plot)
      - [Grafica de percentiles](#Grafica-de-percentiles)
      - [Histograma](#Histograma)
      - [Medidas-de-dispersion-y-tendencia-central](#Medidas-de-dispersion-y-tendencia-central)

<a name="About"></a>
# About TI-nspire
This repository contains python programs that use the TI-nspire-cx-2 calculator model libraries to solve problems that you may frequently encounter if you are studying a university degree.

Esta es una calculadora grafica la cual permite programar y correr codigos en python. Util para crear cualquier tipo de algoritmo que facilite hacer calculos, graficas y mostrar procedimiento. Ademas de los modulos standard, esta tambien incluye unos modulos unicos para poder trabajar con la interfaz grafica de la calculadora. 


| Standard Modules     | TI Modules                                                                     
|:--------------------:|------------:|
| Math (math)          |TI PlotLib (ti_plotlib) |
| Random (random)      |TI Hub (ti_hub)|
| Complex Math (cmath) |TI Rover (ti_rover)|
| Time (time)          |TI System (ti_system)|
|                      |TI Draw (ti_draw)|
|                      |TI Image (ti_image)|

Si tienes un modelo distinto a la TI-nspire-cx-2, estas son todos los modelos en los que esta disponible usar python:

| Handhelds                         | Desktop Software                     |
|-----------------------------------|-------------------------------------|
| TI-Nspire™ CX II                  | TI-Nspire™ CX Premium Teacher Software  |
| TI-Nspire™ CX II CAS              | TI-Nspire™ CX CAS Premium Teacher Software  |
| TI-Nspire™ CX II-T                | TI-Nspire™ CX Student Software  |
| TI-Nspire™ CX II-T CAS            | TI-Nspire™ CX CAS Student Software  |
| TI-Nspire™ CX II-C                |                                     |
| TI-Nspire™ CX II-C CAS            |                                     |

Para mas informacion pueden entrar a la pagina <a href="https://education.ti.com/en/products?category=graphing-calculators" target="_blank"> Texas Instruments Graphing calculators</a>

Para descargar el manual de los modulos TI de python [Manual](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/files/12775095/TI-Nspire_Python_Programming_Guidebook_EN.6.pdf)

# How to import the files

1. Primero va a necesitar descargar el software que simula la calculadora en la computadora. Las instrucciones de como instalarlo estan en el empaque de la calculadora junto a la licencia que permite utilizar el software de estudiante.
   
2. Descargue el zip y descomprima y guarde en su computadora las carpetas con los archivos tns en este repositorio. Los archivos .py no son necesarios, estan en el repositorio para poder ver el codigo de los archivos tns. La calculadora no acepta archivos .py.

   ![paso1](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/c4ff6118-913a-4515-be01-ea0f2427d4ae)

3. Abra el software y busque en la pestaña señalada, los archivos tns descargados en su computadora.

   ![paso2](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/0143125f-e021-42a6-922e-c64e618b404f)

4. Conecte su calculadora y verifique que el software reconosca que esta conectada. Debera aparecer en la pestaña abajo en la izquierda.

   ![paso3](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/722f8848-f675-4f96-8b7f-f49095d545f9)

5. Seleccione la calculadora y dirijase a la carpeta "python".
   
    ![paso4](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/5e18b733-43fb-44f6-a0e0-c732951d8338)

6. Suelte los archivos tns en la carpeta python y listo.

<a name="matematicas"></a>
<!-- Matemáticas -->
# Matemáticas

![portada matematicas](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/4a0fb6e3-2661-4ca1-acef-bdcd0c066091)


<a name="gauss-jordan"></a>
# Gauss Jordan

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
# Inverse Matrix

Este algoritmo sigue la misma idea que el de Gauss Jordan solo que amplia la matriz original añadiendo a la derecha la matriz identidad. Hace las operaciones de filas de matrices necesarios hasta hacer que la matriz de la izquierda se convierta en la matriz identidad. Resultando que la matriz de la derecha va a ser la inversa de la matriz original con la que empezamos.

Tomemos de ejemplo de nuevo la siguiente ecuacion:

![sistema de ecuaciones](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/2aa82c71-d16c-4291-ae1e-d7eaf20026b7)

1. Al correr el codigo nos va a pedir que introduscamos el tamaño de la matriz cuadrada. Tiene que ser cuadrada, nxn donde n es el mismo numero de columnas que de filas, ya que la vamos a estar ampliando con una matriz identidad de igual tamaño.
2. Despues introducimos los valores de los coeficientes separados por espacios. A continuacion un ejemplo del output del codigo:
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
# Science 

![Portada ciencias](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/16aacf75-21b7-443c-b9eb-971614095436)

<a name="Celda-Unitaria"></a>
# Celda Unitaria

Este algoritmo dibuja una celda unitaria cristalina SC, BCC, FCC o HCP con la posicion exacta de sus atomos. Despues te permite dibujar encima de esa celda un vector o un plano. Esta visualizacion grafica es util para saber cuantos atomos interseca el vector o el plano. Esto es util para problemas de densidad lineal y densidad planar. 

Al correr el codigo simplemente ve introduciendo el numero de cada opcion deseada y presionando enter. Para ingresar los valores del vector o del plano, introdusca los valores uno a uno. A continuacion un ejemplo del output del codigo y de algunos ejemplos de los dibujos que puede realizar.

```
#Running CeldaUnitaria.py
from CeldaUnitaria import *
1:BCC
2:FCC
3:SC
4:HCP

choice: 2
1: Direction
2: Plane

choice: 2
intersection x: 1
intersection y: 1
intersection z: 1
```

Este output resulta en el siguiente dibujo:


![FCCPlane111](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/d126bf97-7e32-4c8e-8373-8989aac73293)

Las lineas entrecortadas de color azul sirven como lineas de proyeccion para poder visualizar mejor la perspectiva de la posicion de los atomos con el plano. Por otra parte, las lineas de color amarillo representan el plano.

Otro ejemplo para mostrar como se veria el vector. Esta es en una celda HCP.

![HCPDirection121](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/9a343fa6-686e-45f2-935a-866d2295bad8)

En este caso el vector se muestra de color verde. Tambien con unas lineas de proyeccion para poder visualizar mejor su altura en el dibujo.

A continuacion unos ejemplos mas para visualizar distintas variaciones

Estructura HCP con un plano (0 1 0)
![HCP_Plane010](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/0b89149e-0241-45d8-b1d5-a03bc1f720b9)

Estructura BCC con un plano (2 2 0)
![BCC_Plane220](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/bd82c4ba-3c71-4c43-9186-46bdc443e16a)

Estructura SC con un vector [2 2 4]
![SC_Direction224](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/d1a414f4-2861-41d1-a27b-56788f08bcc8)




<a name="estadistica"></a>
# Estadística

![portada estadistica](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/23598588-49cc-49e3-8dfb-f53e6e4b77c6)


<a name="Box-plot"></a>
# Box plot

Este algoritmo hace los calculos de las cuantilas .25, .50, .75 y del IQR sobre un conjunto de datos ingresado a travez de inputs. Ademas hace el dibujo de la grafica y los calculos para saber si hay outliers o no. A continuacion un ejemplo de como se ingresan los datos, como muestra el output de los calculos y el dibujo de la grafica:

```
#Running BoxPlot.py
from BoxPlot import *
Ingrese el numero de elementos: 10
Valor #1: 9
Valor #2: 3
Valor #3: 1
Valor #4: 3
Valor #5: 10
Valor #6: 11
Valor #7: 3
Valor #8: 4
Valor #9: 5
Valor #10: 7
Cuantila: 0.25
k=int((10+1)*0.25)
Q0.25=3.0+((10+1)*0.25-2)*(3.0-3.0)
Cuantila: 0.5
k=int((10+1)*0.5)
Q0.5=4.0+((10+1)*0.5-5)*(5.0-4.0)
Cuantila: 0.75
k=int((10+1)*0.75)
Q0.75=9.0+((10+1)*0.75-8)*(10.0-9.0)
IQR = (9.25-3.0)* 1.5
Q25: 3.0
Q50: 4.5
Q75: 9.25
IQR: 9.375
Left outliers:
Q: 3.0
Elements: [1.0, 3.0, 3.0, 3.0, 4.0, 5.0, 7.0, 9.0, 10
.0, 11.0]
Slice: [1.0]
if abs(1.0-3.0) > 9.375 False
Right outliers:
Q: 9.25
Elements: [1.0, 3.0, 3.0, 3.0, 4.0, 5.0, 7.0, 9.0, 10
.0, 11.0]
Slice: [11.0, 10.0]
if abs(11.0-9.25) > 9.375 False
if abs(10.0-9.25) > 9.375 False
Left Outliers: []
Right Outlier
```

![BoxPlotExample](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/4048a590-6989-42bc-b242-e646a9607e22)



<a name="Grafica-de-percentiles"></a>
# Grafica de percentiles

Este algoritmo dibuja una grafica de percentiles de un conjunto de datos dados a travez de inputs. Ademas de calcular y dibujar una regresion lineal. Esto es util para hacer analisis de datos y saber si hay algun patron en los datos o si fueron escogidos aleatoriamente. 

```
#Running Estadistica.py
from Estadistica import *
Ingrese el tamaño de la poblacion: 10
Valor#1: 1
Valor#2: 3
Valor#3: 2
Valor#4: 9
Valor#5: 5
Valor#6: 6
Valor#7: 4
Valor#8: 2
Valor#9: 4
Valor#10: 3
```

![GraficaDePercentiles](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/3c51ccad-4852-48c9-8b5d-75df2dfa156e)


<a name="Histograma"></a>
# Histograma

Este algoritmo dibuja un histograma de barras que representan la frecuencia de elementos que pertenecen a intervalos calculado a partir del rango del conjunto de datos y de una constante k.
A continuacion un ejemplo de el output y de la grafica:

```
#Running Histograma.py
from Histograma import *
Ingrese el numero de elementos: 10
Valor #1: 4
Valor #2: 2
Valor #3: 3
Valor #4: 6
Valor #5: 3
Valor #6: 7
Valor #7: 9
Valor #8: 10
Valor #9: 2
Valor #10: 1
k= round( sqrt(10) ) =  3
rango = max - min = 9
delta = rango/k= 3.0
[3.0, 6.0, 9.0] [5, 2, 3]
#Running Histograma.py
from Histograma import *
Ingrese el numero de elementos: 15
Valor #1: 1
Valor #2: 5
Valor #3: 10
Valor #4: 2
Valor #5: 5
Valor #6: 11
Valor #7: 13
Valor #8: 8
Valor #9: 9
Valor #10: 1
Valor #11: 14
Valor #12: 14
Valor #13: 14
Valor #14: 11
Valor #15: 10
k= round( sqrt(15) ) =  4
rango = max - min = 13
delta = rango/k= 3.25
[3.25, 6.5, 9.75, 13.0] [3, 2, 4, 6]
```

![Histograma](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/cb78767c-f8f1-4dd2-bb32-c82680b9a92b)


<a name="Medidas-de-dispersion-y-tendencia-central"></a>
# Medidas-de-dispersion-y-tendencia-central

Este algoritmo no tiene alguna representacion visual. A partir de un conjunto de datos, ya sea una poblacion o muestra, este calcula todas las medidas de tendencia central y de dispercion. 
A continuacion un ejemplo del output:

```
#Running Estadistica.py
from Estadistica import *
Ingrese 1 para poblacion, 0 para muestra: 1
Ingrese el tamaño del conjunto: 10
Valor #1: 1
Valor #2: 4
Valor #3: 9
Valor #4: 10
Valor #5: 2
Valor #6: 5
Valor #7: 7
Valor #8: 7
Valor #9: 7
Valor #10: 3

Medidas de tendencia central
Moda es: [7.0]
Media es: 5.5
Conjunto: [1.0, 2.0, 3.0, 4.0, 5.0, 7.0, 7.0, 7.0, 9.0
, 10.0]
Mediana es: 6.0

Medidas de dispercion
Rango es: 9.0
Varianza: sumatoria momentos^2/n if poblacion 
else n-1
Varianza es: 8.050000000000001
Raiz cuadrada de varianza
Desviacion estandar es: 2.837252191822222
Skewness: sumatoria momentos^3/n/DS^3
Skewness es: -0.03940476019659735
kurtosis: (Sumatoria momentos^4/n/DS^4) - 3
Kurtosis es: -1.179661278500058
DS/abs(media)
Coeficiente de variacion es: 0.515864034876767
6

P1
1.0
2.0
3.0
4.0
5.0
7.0
7.0
7.0
9.0
10.0
momento
-4.5
-3.5
-2.5
-1.5
-0.5
1.5
1.5
1.5
3.5
4.5
momento^2
20.25
12.25
6.25
2.25
0.25
2.25
2.25
2.25
12.25
20.25
momento^3
-91.12
-42.88
-15.62
-3.38
-0.12
3.38
3.38
3.38
42.88
91.12
momento^4
410.06
150.06
39.06000000000001
5.06
0.06
5.06
5.06
5.06
150.06
41
```
![TexasInstruments-Logo svg](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/c86f7a60-f585-489c-9a78-b7acf4f0d2a4)


[Texas-Instrument]: 
[Texas-Instrument-URL]: (https://education.ti.com/en/products?category=graphing-calculators)
