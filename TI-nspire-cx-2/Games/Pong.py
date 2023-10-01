from ti_draw import * 
from ti_system import *

class Vector2:

  
  def __init__(self, c1,c2):
    self.c1 = c1
    self.c2 = c2

  def __add__(self, other):
      if isinstance(other, self.__class__):
          return Vector2(self.c1 + other.c1, self.c2 + other.c2)
      else:
          raise TypeError("La resta solo está definida para objetos de tipo Vector3")

  def __sub__(self, other):
      if isinstance(other, self.__class__):
          return Vector2(self.c1 - other.c1, self.c2 - other.c2)
      if isinstance(other, (int, float) ):
          return Vector2(self.c1 - other, self.c2 - other)
      else:
          raise TypeError("La suma solo está definida para objetos de tipo Vector3")

  def __lt__(self, other):
      if isinstance(other, self.__class__):
          return self.c1 < other.c1 and self.c2 < other.c2
      elif isinstance(other, (int, float) ):
          return self.c1 < other and self.c2 < other
      else:
          raise TypeError("La comparacion de < solo está definida para objetos de tipo Vector2 y numericos") 

  def __gt__(self, other):
      if isinstance(other, self.__class__):
          return self.c1 > other.c1 and self.c2 > other.c2
      elif isinstance(other, (int, float) ):
          return self.c1 > other and self.c2 > other
      else:
          raise TypeError("La comparacion de > solo está definida para objetos de tipo Vector2 y numericos") 

  def __mul__(self, other):
      if isinstance(other, self.__class__):
          # Multiplicación entre dos objetos de la misma clase
          return Vector2(self.c1 * other.c1, self.c2 * other.c2)
      elif isinstance(other, (int, float) ):
          # Multiplicación por un número (int o float)
          return Vector2(self.c1 * other, self.c2 * other)
      else:
          raise TypeError("La multiplicación solo está definida para objetos de tipo Vector2 y numericos")


class Entity:
            
  def __init__(self, x, y, w, h, v):
    self.coordinates = Vector2(x,y)
    self.velocity = v
    self.w = w
    self.h = h

  def translate(self):
    self.coordinates = self.coordinates.__add__(self.velocity)

  def collide(self, entity):
    collideInX = (abs(entity.coordinates.c1 - self.coordinates.c1) >= 0 and abs(entity.coordinates.c1 - self.coordinates.c1) <= self.w)
    collideInY = (abs(entity.coordinates.c2 - self.coordinates.c2) >= 0 and abs(entity.coordinates.c2 - self.coordinates.c2) <= self.h)
    return collideInX and collideInY

class Racket(Entity):
  def __init__(self, x, y, w, h, v):
    super().__init__(x, y, w, h, v)

  def mouseCheck(self, t):
    if(t[1] < self.coordinates.c2):
      self.velocity = Vector2(0, -12)
    elif(t[1] > self.coordinates.c2 + self.h):
      self.velocity = Vector2(0, 12)
    else:
      self.velocity = Vector2(0, 0)

  def tick(self):
    self.translate()

  def render(self):
    set_color(0,0,0)
    draw_rect(self.coordinates.c1, self.coordinates.c2, self.w, self.h) 

class Ball(Entity):
  def __init__(self, x, y, w, h, v):
    
    self.r = w/2
    super().__init__(x-self.r, y-self.r, w, h, v)

  def mouseCheck(self, t):
    pass

  def tick(self):
    if(self.coordinates.c2 < 0 or self.coordinates.c2 + self.h > get_screen_dim()[1] ):
      self.velocity = Vector2(self.velocity.c1, -1 * self.velocity.c2)
    self.translate()

  def render(self):
    set_color(0,0,0)
    draw_circle(self.coordinates.c1 + self.r, self.coordinates.c2 + self.r, self.r) 

def main():
  dimensions = get_screen_dim() 

  leftRacket = Racket(10,dimensions[1]/2, 5, 30, Vector2(0,0))
  rightRacket = Racket(dimensions[0] - 10, dimensions[1]/2, 5, 30, Vector2(0,0))
  ball = Ball(dimensions[0]/2-3, dimensions[1]/2-3, 6,6, Vector2(0,0))
  bounceCounter = 0
  maxBounce = 0

  def mouseCheck(t):
    leftRacket.mouseCheck(t)
    rightRacket.mouseCheck(t)
    ball.mouseCheck(t)

  def tick():
    nonlocal bounceCounter
    if(leftRacket.collide(ball) or rightRacket.collide(ball)):
      ball.velocity = Vector2(-1 * ball.velocity.c1, ball.velocity.c2)
      bounceCounter += 1

    if(ball.coordinates.c1 < 0 or ball.coordinates.c1 + ball.w > dimensions[0]):
      ball.velocity = Vector2(0,0)
      ball.coordinates = Vector2(dimensions[0]/2-3, dimensions[1]/2-3)
      bounceCounter = 0
  
    leftRacket.tick()
    rightRacket.tick()
    ball.tick()

    

  def render():
    clear()
    leftRacket.render()
    rightRacket.render()
    ball.render()


  ejecuciones_por_segundo = 10
  tiempo_actual = get_time_ms()
  while True:
    if get_key() == 'esc': break
    tiempo_actual_nuevo = get_time_ms()
    tiempo_transcurrido = tiempo_actual_nuevo - tiempo_actual
    
    if get_key() and ball.velocity.c1 == 0 and ball.velocity.c2 == 0: ball.velocity = Vector2(8,8)
    if ball.velocity.c1 == 0 and ball.velocity.c2 == 0: draw_text(70,20, "Press anny button to start")
    if ball.velocity.c1 != 0 and ball.velocity.c2 != 0:
      if maxBounce < bounceCounter: maxBounce = bounceCounter
      draw_text(100,20, "Bounces: " + str(bounceCounter))
      draw_text(100,35, "Max Bounces: " + str(maxBounce))
    
    if(tiempo_transcurrido >= 1000 / ejecuciones_por_segundo):
      
      
      mouseCheck(get_mouse())
      tick()
      render()

      
      tiempo_actual = tiempo_actual_nuevo


  
main()
 
