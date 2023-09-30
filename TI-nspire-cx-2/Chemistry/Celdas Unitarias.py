from ti_draw import * 
import math

class C:
  def __init__(self,x,y,h) -> None:
    self.x = x
    self.y = y
    self.h = h
  
def SC(cor, a):
  c1 = C(cor.x, cor.y, a)
  c2 = C(c1.x + a, c1.y, a)
  c3 = C(c1.x, c1.y + a, 0)
  c4 = C(c3.x + a, c3.y, 0)

  angle = math.pi/180 * 60
  compX = a * math.cos(angle)
  compY = a * math.sin(angle)

  c5 = C(c1.x + compX, c1.y - compY, a)
  c6 = C(c2.x + compX, c2.y - compY, a)
  c7 = C(c3.x + compX, c3.y - compY, 0)
  c8 = C(c4.x + compX, c4.y - compY, 0)

  return [c1,c2,c3,c4,c5,c6,c7,c8]

def BCC(cor, a):
  coordinates = SC(cor, a)

  c9XAxix_compX = (coordinates[6].x - coordinates[2].x) * 1/2
  c9XAxix_compY = (coordinates[2].y - coordinates[6].y) * 1/2
  c9YAxix_compX = (coordinates[7].x - coordinates[6].x) * 1/2
  c9ZAxix_compY = (coordinates[6].y - coordinates[5].y) * 1/2
  c9 = C(coordinates[6].x - c9XAxix_compX + c9YAxix_compX, coordinates[6].y + c9XAxix_compY - c9ZAxix_compY, a/2)
  
  coordinates.append(c9)
  return coordinates

def FCC(cor, a):
  coordinates = SC(cor, a)

  cXAxix_compX = (coordinates[6].x - coordinates[2].x) * 1/2
  cXAxix_compY = (coordinates[2].y - coordinates[6].y) * 1/2
  cYAxix_compX = (coordinates[7].x - coordinates[6].x) * 1/2

  c9 = C(coordinates[2].x + cXAxix_compX, coordinates[2].y - cXAxix_compY - a/2, a/2)
  c10 = C(coordinates[2].x + cYAxix_compX, coordinates[2].y - a/2, a/2)
  c11 = C(coordinates[2].x + cXAxix_compX + a, coordinates[2].y - cXAxix_compY - a/2, a/2)
  c12 = C(coordinates[6].x + a/2, coordinates[6].y - a/2, a/2)
  c13 = C(coordinates[2].x + cXAxix_compX + a/2, coordinates[2].y - cXAxix_compY, 0)
  c14 = C(coordinates[0].x + cXAxix_compX + a/2, coordinates[0].y - cXAxix_compY, a)
  return coordinates + [c9,c10,c11,c12,c13,c14]

def HCP(cor, a, c):
  c1 = C(cor.x, cor.y, c)
  c2 = C(c1.x + a, c1.y, c)
  c3 = C(c1.x, c1.y + c, 0)
  c4 = C(c2.x, c3.y, 0)

  angle = math.pi/180 * 60
  compX = a * math.cos(angle)
  compY = a * math.sin(angle)

  c5 = C(c1.x + compX, c1.y - compY, c)
  c6 = C(c2.x + compX, c2.y - compY, c)
  c7 = C(c3.x + compX, c3.y - compY, 0)
  c8 = C(c4.x + compX, c4.y - compY, 0)

  c9x = (c3.x + c7.x + c4.x)/3
  c9y = (c3.y + c7.y + c4.y)/3
  c9 = C(c9x, c9y - c/2, c/2)
  
  return [c1,c2,c3,c4,c5,c6,c7,c8,c9]

def linealDensity(coordinates):
  
  cXAxix_compX = (coordinates[6].x - coordinates[2].x)
  cXAxix_compY = (coordinates[2].y - coordinates[6].y)
  cXAxiz_compY = (coordinates[6].y - coordinates[4].y)

  l = []
  l.append(float(input("direction x: ")))
  l.append(float(input("direction y: ")))
  l.append(float(input("direction z: ")))

  m = max(l)
  for i in range(len(l)):
    if(m > 1): l[i] /= m

  lc1 = C(coordinates[6].x, coordinates[6].y, 0)
  lc2 = C(coordinates[6].x - cXAxix_compX * l[0] + (coordinates[7].x - coordinates[6].x) * l[1], coordinates[6].y + cXAxix_compY*l[0]  - (coordinates[6].y - coordinates[4].y) * l[2], cXAxiz_compY * l[2])
  
  return (lc1, lc2)

def planeDensity(coordinates):
  c = coordinates[2].y - coordinates[0].y
  a = coordinates[3].x - coordinates[2].x


  l = []
  l.append(float(input("intersection x: ")))
  l.append(float(input("intersection y: ")))
  l.append(float(input("intersection z: ")))

  for i in range(len(l)):
    if(l[i] != 0):
      l[i] = 1/l[i]

  xAxix_X = (coordinates[6].x - coordinates[2].x) * l[0]
  xAxix_Y = (coordinates[2].y - coordinates[6].y) * l[0]
  plane = []
  if(l[0] == 0 and l[1] == 0):
    p1 = C(coordinates[6].x, coordinates[6].y - (c*l[2]), c*l[2])
    p2 = C(coordinates[2].x, coordinates[2].y - (c*l[2]), c*l[2])
    p3 = C(coordinates[3].x, coordinates[3].y - (c*l[2]), c*l[2])
    p4 = C(coordinates[7].x, coordinates[7].y - (c*l[2]), c*l[2])
    plane.append(p1)
    plane.append(p2)
    plane.append(p3)
    plane.append(p4)
  elif(l[1] == 0 and l[2] == 0):
    p1 = C(coordinates[6].x - xAxix_X, coordinates[6].y + xAxix_Y, 0)
    p2 = C(p1.x, p1.y-c, c)
    p3 = C(p2.x + a, p2.y, c)
    p4 = C(p3.x, p3.y + c, 0)
    plane.append(p1)
    plane.append(p2)
    plane.append(p3)
    plane.append(p4)
  elif(l[0] == 0 and l[2] == 0):
    p1 = C(coordinates[6].x + a*l[1], coordinates[6].y, 0)
    p2 = C(coordinates[2].x + a*l[1], coordinates[2].y, 0)
    p3 = C(coordinates[0].x + a*l[1], coordinates[0].y, c)
    p4 = C(coordinates[4].x + a*l[1], coordinates[4].y, c)
    plane.append(p1)
    plane.append(p2)
    plane.append(p3)
    plane.append(p4)
  elif(l[0] == 0):
    p1 = C(coordinates[6].x, coordinates[6].y - c*l[2], c*l[2])
    p2 = C(coordinates[2].x, coordinates[2].y - c*l[2], c*l[2])
    p3 = C(coordinates[2].x + a*l[1], coordinates[2].y, 0)
    p4 = C(coordinates[6].x + a*l[1], coordinates[6].y, 0)
    plane.append(p1)
    plane.append(p2)
    plane.append(p3)
    plane.append(p4)
  elif(l[1] == 0):
    p1 = C(coordinates[6].x - xAxix_X, coordinates[6].y + xAxix_Y, 0)
    p2 = C(coordinates[6].x - xAxix_X + a, coordinates[6].y + xAxix_Y, 0)
    p3 = C(coordinates[7].x, coordinates[7].y - c*l[2], c*l[2])
    p4 = C(coordinates[6].x, coordinates[6].y - c*l[2], c*l[2])
    plane.append(p1)
    plane.append(p2)
    plane.append(p3)
    plane.append(p4)
  elif(l[2] == 0):
    p1 = C(coordinates[6].x - xAxix_X, coordinates[6].y + xAxix_Y, 0)
    p2 = C(p1.x, p1.y - c, c)
    p3 = C(coordinates[4].x + a*l[1], coordinates[4].y, c)
    p4 = C(coordinates[6].x + a*l[1], coordinates[6].y, 0)
    plane.append(p1)
    plane.append(p2)
    plane.append(p3)
    plane.append(p4)
  elif(l[0] != 0 and l[1] != 0 and l[2] != 0):
    p1 = C(coordinates[6].x - xAxix_X, coordinates[6].y + xAxix_Y, 0)
    p2 = C(coordinates[6].x + a*l[1], coordinates[6].y , 0)
    p3 = C(coordinates[6].x, coordinates[6].y - c*l[2], 0)
    plane.append(p1)
    plane.append(p2)
    plane.append(p3)
  return plane
  

def drawPlane(plane):
  set_color(255,255,0)
  for i in range(0, len(plane)-1):
    draw_line(plane[i].x, plane[i].y, plane[i+1].x, plane[i+1].y)
  draw_line(plane[-1].x, plane[-1].y, plane[0].x, plane[0].y)
  set_color(0,0,0)

def drawUnitCell(coordinates):
  
  c1 = coordinates[0]
  c2 = coordinates[1]
  c3 = coordinates[2]
  c4 = coordinates[3]
  c5 = coordinates[4]
  c6 = coordinates[5]
  c7 = coordinates[6]
  c8 = coordinates[7]

  set_color(0,0,0)
  draw_line(c1.x, c1.y, c2.x, c2.y)
  draw_line(c2.x, c2.y, c4.x, c4.y)
  draw_line(c3.x, c3.y, c4.x, c4.y)
  draw_line(c3.x, c3.y, c1.x, c1.y)
  
  draw_line(c1.x, c1.y, c5.x, c5.y)
  draw_line(c5.x, c5.y, c6.x, c6.y)
  draw_line(c6.x, c6.y, c8.x, c8.y)
  draw_line(c8.x, c8.y, c4.x, c4.y)
  draw_line(c6.x, c6.y, c2.x, c2.y)
  draw_line(c3.x, c3.y, c7.x, c7.y)
  draw_line(c7.x, c7.y, c8.x, c8.y)
  draw_line(c5.x, c5.y, c7.x, c7.y)

  for atomCor in coordinates:
    set_color(0,0,255)
    fill_circle(atomCor.x, atomCor.y, 4)  
    set_color(131,235,255)
    set_pen(1,1)
    draw_line(atomCor.x, atomCor.y, atomCor.x, atomCor.y + atomCor.h)
    set_pen(0,0)

def drawDirection(direction):
  set_color(0,153,76)
  draw_line(direction[0].x, direction[0].y, direction[1].x, direction[1].y)
  set_pen(1,2)
  draw_line(direction[1].x, direction[1].y, direction[1].x, direction[1].y + direction[1].h)
  set_pen(0,0)

def main():
  dimensions = get_screen_dim()
  xCenter = dimensions[0]/2
  yCenter = dimensions[1]/2
  a = 70
  c = 100
  unitCellCoordinates = C(xCenter - a, yCenter, a)
  
  coordinates = None
  direction = None
  plane = None
  
  print("1:BCC\n2:FCC\n3:SC\n4:HCP\n")
  choice = int(input("choice: "))
  
  if(choice == 1):
    coordinates = BCC(unitCellCoordinates, a)
  if(choice == 2):
    coordinates = FCC(unitCellCoordinates, a)
  if(choice == 3):
    coordinates = SC(unitCellCoordinates, a)
  if(choice == 4):
    coordinates = HCP(unitCellCoordinates, a, c)
  
  print("1: Direction\n2: Plane\n")
  choice = int(input("choice: "))
  if(choice == 1):
    direction = linealDensity(coordinates)
    drawDirection(direction)
  if(choice == 2):
    plane = planeDensity(coordinates)
    drawPlane(plane)
    
  drawUnitCell(coordinates)
  #paint_buffer() 
    
main()



