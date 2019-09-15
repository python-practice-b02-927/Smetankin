import turtle
def square(l):
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)

    turtle.penup() 
    for i in range(2):
        turtle.right(90)
        turtle.forward(5)
    turtle.pendown() 
    turtle.left(180)
n=0
l=10
while n<10:
    square(l)
    l+=10
    n+=1
