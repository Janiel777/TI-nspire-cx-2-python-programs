# Plotting (x,y) & Text
#================================
import ti_plotlib as plt
#================================
p = []
d = []
N = int(input("Ingrese el tamaño de la poblacion: "))
for i in range(1,N+1):
  p.append(float(input("Valor#" + str(i) + ": ")))
  d.append(float(i/(N+1)))

plt.auto_window(p,d)
plt.axes()
plt.grid(min(p),min(d),"dotted")
plt.axes("on")

plt.scatter(p,d,"x")
plt.lin_reg(p,d)



