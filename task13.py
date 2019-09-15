import turtle
def licso():
 turtle.speed(10)
 turtle.color("yellow")
 turtle.begin_fill()
 for i in range(360):
  turtle.right(1)
  turtle.forward(1)
 turtle.end_fill()
 turtle.penup()
def nose():
 turtle.speed(1)
 turtle.goto(0, -50)
 turtle.left(90)
 turtle.color("black")
 turtle.width(5)
 turtle.pendown()
 turtle.forward(20)
 turtle.penup()
def eyes1():
 
 turtle.width(1)
 turtle.color("blue")
 turtle.goto(15,-25)
 turtle.pendown()
 turtle.begin_fill()
 for i in range(60):
  turtle.right(6)
  turtle.forward(1)
 turtle.end_fill()
 turtle.penup()
def eyes2():
 turtle.width(1)
 turtle.color("blue")
 turtle.goto(-15,-25)
 turtle.pendown()
 turtle.begin_fill()
 for i in range(60):
  turtle.left(6)
  turtle.forward(1)
 turtle.end_fill() 
 turtle.penup()
def rot():
 turtle.right(180)
 turtle.goto(30,-60)
 turtle.color("red")
 turtle.width(5)
 turtle.pendown()
 for i in range(90):
  turtle.right(2)
  turtle.forward(1)

licso()
nose()
eyes1()
eyes2()
rot()
