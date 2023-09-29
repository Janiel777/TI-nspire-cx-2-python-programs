import math
varianzaBool = 0

def moda(p):
  freq = {}
  for e in p:
    if(e in freq):
      freq[e] += 1
    else:
      freq[e] = 1
      
  return [k for k,v in freq.items() if  v == max(freq.values())]


def media(p):
  sum = 0
  for e in p:
    sum += e
  return sum/len(p)

def mediana(p):
  print("Conjunto:",p)
  if(len(p) % 2 != 0): return p[int(len(p)/2)]
  return ((p[int(len(p)/2)] + p[int(len(p)/2-1)])/2)

def varianza(p):
  print("Varianza: sumatoria momentos^2/n if poblacion else n-1")
  m = media(p)
  sum = 0
  for i in range(len(p)):
    sum += (p[i] - m)**2
    tabla.append([i+1, p[i], round(p[i] - m,2), round((p[i] - m)**2,2)])
  return sum/len(p) if varianzaBool else sum/(len(p) - 1)

def desviacionStandard(varianza):
  return math.sqrt(varianza)

def skewness(p):
  print("Skewness: sumatoria momentos^3/n/DS^3")
  m = media(p)
  sum = 0
  tabla[0].append("momento^3")
  for i in range(len(p)):
    sum += (p[i] - m)**3
    tabla[i+1].append(round((p[i] - m)**3,2))
  return sum/len(p)/desviacionStandard(v)**3

def kurtosis(p):
  print("kurtosis: (Sumatoria momentos^4/n/DS^4) - 3")
  m = media(p)
  sum = 0
  tabla[0].append("momento^4")
  for i in range(len(p)):
    sum += (p[i] - m)**4
    tabla[i+1].append(round((p[i] - m)**4,2))
  return (sum/len(p)/desviacionStandard(v)**4)-3

def rango(p):
  return max(p) - min(p)

def coeficienteDeVariacion(p):
  print("DS/abs(media)")
  return desviacionStandard(v)/abs(media(p))

def imprimir_lista_tabla(lista_de_listas, encabezados=None):
    for c in range(len(lista_de_listas[0])):
      for r in range(len(lista_de_listas)):
        if(c == 0): continue
        print(lista_de_listas[r][c])
  
def main():
  global tabla
  global varianzaBool
  tabla = []
  tabla.append(["i", "P1", "momento", "momento^2"])
  p = []
  varianzaBool = input("Ingrese 1 para poblacion, 0 para muestra: ") == "1"
  N = int(input("Ingrese el tamaño del conjunto: "))
  for i in range(1, N+1):
    p.append(float(input("Valor #" + str(i) + ": ")))
  p.sort()

  print("\nMedidas de tendencia central")
  print("Moda es: " + str(moda(p)))
  print("Media es: " + str(media(p)))
  print("Mediana es: " + str(mediana(p)) + "\n")
  
  print("Medidas de dispercion")
  print("Rango es: " + str(rango(p)))
  global v
  v = varianza(p)
  print("Varianza es: " + str(v))
  print("Raiz cuadrada de varianza")
  print("Desviacion estandar es: " + str(desviacionStandard(v)))
  print("Skewness es: " + str(skewness(p)))
  print("Kurtosis es: " + str(kurtosis(p)))
  print("Coeficiente de variacion es: " + str(coeficienteDeVariacion(p)) + "\n")
  
  imprimir_lista_tabla(tabla)

main()






