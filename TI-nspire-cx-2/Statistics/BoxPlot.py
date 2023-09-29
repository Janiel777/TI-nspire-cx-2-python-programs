from ti_draw import *

def cuantila(l, d):
  print("Cuantila: " + str(d))
  k = int((len(l) + 1) * d) 
  print( "k=int((" + str(len(l)) + "+1)*" + str(d) + ")")
  qd = l[k-1] + ((len(l) + 1) * d - k) * (l[k] - l[k-1])
  print("Q" + str(d) + "=" + str(l[k-1]) + "+" + "((" + str(len(l)) + "+1)*" + str(d) + "-" + str(k) + ")*(" + str(l[k]) + "-" + str(l[k-1]) + ")")

  
  return qd

def outliers(l, IQR, Q, d):
  print("Q:",Q)
  print("Elements:",l)
  slice = []
  # if(Q in l):
  #   slice = l[:int(Q)] if (d == .25) else l[int(Q):]
  # else:
  #   index = l.index(int(Q))+1
  #   slice = l[:index] if (d == .25) else l[index:]
  if(d == .25):
    for i in range(len(l)):
      if(l[i] < Q):
        slice.append(l[i])
      else:
        break
  else:
    for i in range(len(l)-1,-1, -1):
      if(l[i] > Q):
        slice.append(l[i])
      else:
        break
  
  print("Slice:",slice)
  
  outliers = []
  for i in range(len(slice)):
    print("if abs(" + str(slice[i]) + "-" + str(Q)+") > " + str(IQR), abs(slice[i] - Q) > IQR)
    if(abs(slice[i] - Q) > IQR):
      outliers.append(slice[i])

  return outliers

def main():
  l = []
  #l = [2,2,2,3,4,4,4,5,5,5,5,5,6,6,6,6,8,8,9,9,9,9,10,12,12,14,17,18,18,20]
  N = int(input("Ingrese el numero de elementos: "))
  for i in range(N):
    l.append(float(input("Valor #" + str(i+1) + ": ")))
  l.sort()
  Q25 = cuantila(l,.25)
  Q50 = cuantila(l,.50)
  Q75 = cuantila(l,.75)
  IQR = (Q75 - Q25)* 1.5
  print("IQR = (" + str(Q75) + "-" + str(Q25) + ")* 1.5")
  print("Q25:", Q25)
  print("Q50:", Q50)
  print("Q75:", Q75)
  print("IQR:", IQR)
  print("Left outliers:")
  leftOutliers = outliers(l,IQR,Q25,.25)
  print("Right outliers:")
  rightOutliers = outliers(l,IQR,Q75,.75)
  notOutliers = [e for e in l if e not in leftOutliers + rightOutliers]
  
  print("Left Outliers:", leftOutliers)
  print("Right Outliers:", rightOutliers)
  x, y = get_screen_dim()
  
  draw_line(0,3/4*y,x,3/4*y)
  minn = min(l)
  maxx = max(l)
  l_noDuplicates = list(set(l))
  margin = 10
  offset = (x-margin*2)/(maxx - minn)
  boxLength = offset*(Q75 - Q25)
  
 
  for i in range(minn, maxx+1):
    set_color(0,0,0)
    draw_circle(margin+offset*(i - minn),3/4*y,1)
    if(i in leftOutliers + rightOutliers):
      set_color(255,0,0)
      draw_circle(margin+offset*(i - minn),y/2+12.5,4)
    elif(i in l_noDuplicates):
      set_color(0,0,255)
      draw_circle(margin+offset*(i - minn),y/2+12.5,2)
    else:
      set_color(0,0,0)
      draw_circle(margin+offset*(i - minn),y/2+12.5,1)
    if(i % 2 == 0):
      draw_text(margin+offset*(i - minn),3/4*y+20,str(i))

  set_color(0,0,0)
    
  draw_rect(margin + Q25 * offset - minn*offset,y/2,boxLength,25)
  draw_line(margin + Q50 * offset - minn*offset, y/2, margin + Q50 * offset - minn*offset, y/2 + 25)
  

  
  draw_text(1/18*x,+1/12*y,"Q.25: " + str(Q25))
  draw_text(1/18*x,2/12*y,"Q.50: " + str(Q50))
  draw_text(1/18*x,3/12*y,"Q.75: " + str(Q75))
  draw_text(1/18*x,4/12*y,"IQR: " + str(IQR))
  
  
main()
