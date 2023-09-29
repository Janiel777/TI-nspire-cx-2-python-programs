import math
from ti_draw import *


def main():
  l = []
  #l = [2,2,2,3,4,4,4,5,5,5,5,5,6,6,6,6,8,8,9,9,9,9,10,12,12,14,17,18,18,20]
  N = int(input("Ingrese el numero de elementos: "))
  for i in range(N):
    l.append(int(input("Valor #" + str(i + 1) + ": ")))
  l.sort()

  k = round(math.sqrt(len(l)))
  print("k= round( sqrt(" + str(len(l)) + ") ) = ", k)
  
  rango = max(l) - min(l)
  print("rango = max - min =", rango)
  delta = rango / k
  print("delta = rango/k=", delta)
  counter = min(l)
  frecuency = {}
  clase = delta
  for i in range(len(l)):
    if (counter <= l[i] < counter + delta or (counter + delta == max(l) and counter <= l[i] <= counter + delta)):
      key = clase
      if (key in frecuency):
        frecuency[key] += 1
      else:
        frecuency[key] = 1
    else:
      counter += delta
      clase += delta
      if (counter <= l[i] < counter + delta):
        key = clase
        if (key in frecuency):
          frecuency[key] += 1
        else:
          frecuency[key] = 1
  
  tlx = list(frecuency.keys())
  tly = list(frecuency.values())
  lx = []
  ly = []
  for i in range(len(tlx)):
    index = tlx.index(min(tlx))
    lx.append(tlx[index])
    ly.append(tly[index])
    tlx.pop(index)
    tly.pop(index)
  print(lx,ly)
  

  
  x, y = get_screen_dim()
  width = 30
  maxHeight = y*3/4
  distance = len(lx) * width
  for i in range(len(lx)):
    set_color(0,255,0) if i % 2 == 0 else set_color(0,150,0)
    fill_rect(x/2 - distance/2+width*i, 3/4*y - ly[i]/N * maxHeight, width, ly[i]/N * maxHeight) 
    set_color(0,0,0)
    draw_rect(x/2 - distance/2+width*i, 3/4*y - ly[i]/N * maxHeight, width, ly[i]/N * maxHeight)
    draw_text(x/2 - distance/2+width*i + 5, 3/4*y - ly[i]/N * maxHeight - 5, str(round(ly[i],2)))
    draw_text(x/2 - distance/2+width*i + 5, 3/4*y + 15, str(round(lx[i],2)))
  draw_text(10,y*1/12,"K: " + str(k))
  draw_text(10,y*2/12,"Rango: " + str(rango))
  draw_text(10,y*3/12,"Delta: " + str(round(delta,2)))
  draw_text(10,y*11/12,str(min(l)) + " <= x < " + str(min(l)+delta) + "        " + str(max(l)-delta) + " <= x <= " + str(max(l)) )
main()



