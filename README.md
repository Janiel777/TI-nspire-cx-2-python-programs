## Índice
- Introduction
   - [About TI-nspire](#About)
   - [How to import the files](#How-to-import-the-files)
- Algoritmos
   - Matemáticas
      - [Gauss Jordan](#gauss-jordan)
      - [Inverse Matrix](#Inverse-Matrix)
   - Science
      - [Unit cells](#Celda-Unitaria)
   - Estadística
      - [Box plot](#Box-plot)
      - [Percentile graph](#Grafica-de-percentiles)
      - [Histogram](#Histograma)
      - [Measures-of-dispersion-and-central-tendency](#Medidas-de-dispersion-y-tendencia-central)

<a name="About"></a>
# About TI-nspire
This repository contains python programs that use the TI-nspire-cx-2 calculator model libraries to solve problems that you may frequently encounter if you are studying a university degree.

This is a graphing calculator which allows you to program and run codes in Python. Useful for creating any type of algorithm that makes it easy to make calculations, graphs and show procedures. In addition to the standard modules, it also includes some unique modules to work with the calculator's graphical interface.


| Standard Modules     | TI Modules                                                                     
|:--------------------:|------------:|
| Math (math)          |TI PlotLib (ti_plotlib) |
| Random (random)      |TI Hub (ti_hub)|
| Complex Math (cmath) |TI Rover (ti_rover)|
| Time (time)          |TI System (ti_system)|
|                      |TI Draw (ti_draw)|
|                      |TI Image (ti_image)|

These are all the models in which programming in Python is available:

| Handhelds                         | Desktop Software                     |
|-----------------------------------|-------------------------------------|
| TI-Nspire™ CX II                  | TI-Nspire™ CX Premium Teacher Software  |
| TI-Nspire™ CX II CAS              | TI-Nspire™ CX CAS Premium Teacher Software  |
| TI-Nspire™ CX II-T                | TI-Nspire™ CX Student Software  |
| TI-Nspire™ CX II-T CAS            | TI-Nspire™ CX CAS Student Software  |
| TI-Nspire™ CX II-C                |                                     |
| TI-Nspire™ CX II-C CAS            |                                     |

For more information you can go to the page <a href="https://education.ti.com/en/products?category=graphing-calculators" target="_blank"> Texas Instruments Graphing calculators</a>

To download the python TI modules [manual](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/files/12775095/TI-Nspire_Python_Programming_Guidebook_EN.6.pdf)

# How to import the files

1. First you will need to download the software that simulates the calculator on your computer. Instructions on how to install it are on the calculator packaging along with the license that allows you to use the student software.
   
2. Download the zip, unzip and save the folders with the tns files in this repository on your computer. The .py files are not necessary, they are in the repository to be able to see the code of the tns files. The calculator does not accept .py files.

   ![paso1](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/c4ff6118-913a-4515-be01-ea0f2427d4ae)

3. Open the software and look in the indicated tab for the tns files downloaded to your computer.

   ![paso2](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/0143125f-e021-42a6-922e-c64e618b404f)

4. Connect your calculator and verify that the software recognizes that it is connected. It should appear in the tab below on the left.

   ![paso3](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/722f8848-f675-4f96-8b7f-f49095d545f9)

5. Select the calculator and go to the "python" folder.
   
    ![paso4](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/5e18b733-43fb-44f6-a0e0-c732951d8338)

6. Drop the tns files into the python folder and you're done.


<a name="gauss-jordan"></a>
# Gauss Jordan

This algorithm in Python not only solves systems of nxn equations, but also shows the procedure. Let's take the following equation as an example:

![sistema de ecuaciones](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/2aa82c71-d16c-4291-ae1e-d7eaf20026b7)

1. When running the algorithm, it will ask us to enter the number of equations. Keep in mind that it is not designed to solve systems with a smaller number of equations than the number of unknowns.
2. Afterwards we introduce the coefficients of the equations separated by space and it will show us the matrix row operations necessary to perform in order to equal all the numbers above and below the diagonal to 0 and those on the diagonal equal to 1. Below is the output of the code for said equation system:

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

This algorithm follows the same idea as Gauss Jordan's, except that it expands the original matrix by adding the identity matrix to the right. It performs the necessary matrix row operations until the matrix on the left becomes the identity matrix. Resulting in the matrix on the right being the inverse of the original matrix we started with.

Let's take the following equation again as an example:

![sistema de ecuaciones](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/2aa82c71-d16c-4291-ae1e-d7eaf20026b7)

1. When running the code it will ask us to enter the size of the square matrix. It has to be square, nxn where n is the same number of columns as rows, since we are going to be expanding it with an identity matrix of the same size.
2. Then we enter the values of the coefficients separated by spaces. Below is an example of the code output:
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

<a name="Celda-Unitaria"></a>
# Unit cells

This algorithm draws a SC, BCC, FCC or HCP crystalline unit cell with the exact position of its atoms. Then it allows you to draw a vector or a plane on top of that cell. This graphical display is useful for knowing how many atoms the vector or plane intersects. This is useful for linear density and planar density problems.

When running the code, simply enter the number of each desired option and press enter. To enter vector or plane values, enter the values one by one. Below is an example of the code output and some examples of the drawings you can make.

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

This output results in the following drawing:


![FCCPlane111](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/d126bf97-7e32-4c8e-8373-8989aac73293)

The broken blue lines serve as projection lines to better visualize the perspective of the position of the atoms with the plane. On the other hand, the yellow lines represent the plane.

Another example to show what the vector would look like. This is in an HCP cell.

![HCPDirection121](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/9a343fa6-686e-45f2-935a-866d2295bad8)

In this case the vector is shown in green. Also with some projection lines to better visualize its height in the drawing.

Below are some more examples to visualize different variations.

### HCP structure with a plane (0 1 0)
![HCP_Plane010](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/0b89149e-0241-45d8-b1d5-a03bc1f720b9)

### BCC structure with a plane (2 2 0)
![BCC_Plane220](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/bd82c4ba-3c71-4c43-9186-46bdc443e16a)

### SC structure with a vector [2 2 4]
![SC_Direction224](https://github.com/Janiel777/TI-nspire-cx-2-python-programs/assets/95184925/d1a414f4-2861-41d1-a27b-56788f08bcc8)


<a name="Box-plot"></a>
# Box plot

This algorithm makes the calculations of the quantiles .25, .50, .75 and the IQR on a set of data entered through inputs. It also draws the graph and calculates to know if there are outliers or not. Below is an example of how the data is entered, as shown in the output of the calculations and the drawing of the graph:

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
# Percentile graph

This algorithm draws a percentile graph of a given data set through inputs. In addition to calculating and drawing a linear regression. This is useful for doing data analysis and knowing if there is any pattern in the data or if it was chosen randomly.

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
# Histogram

This algorithm draws a histogram of bars representing the frequency of elements belonging to intervals calculated from the range of the data set and a constant k.
Below is an example of the output and the graph:

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
# Measures of dispersion and centraltendency

This algorithm does not have any visual representation. From a set of data, whether a population or sample, it calculates all measures of central tendency and dispersion.
Below is an example of the output:

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

