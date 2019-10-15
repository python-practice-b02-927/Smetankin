import turtle
import math
def mnog(n,a,R0):
	i=n
	turtle.left(180-(90-(180/n)))
	while i>0:
		turtle.forward(a)
		turtle.left(360/n)
		i-=1
	turtle.right(180/n+90)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()
	return
#mnog(3,50)

#a=50
#ygol0=math.radians(180/3)
R0=20
for i in range(3,10):
	ygol0=math.radians(180/i)
	a=2*R0*math.sin(ygol0)
	R0+=10
	mnog(i,a,R0)