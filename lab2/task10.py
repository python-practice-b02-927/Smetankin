import turtle
def print_eight():
    for i in range(360):
        turtle.left(1)
        turtle.forward(1)
    for i in range(360):
        turtle.right(1)
        turtle.forward(1)
  

for i in range(4):
    print_eight()
    turtle.left(60)

