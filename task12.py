import turtle
def duga():
	for i in range(180):
		turtle.forward(1)
		turtle.right(1)
def small_duga():
	for i in range(30):
		turtle.forward(1)
		turtle.right(6)
turtle.left(90)
for i in range(7):
	if i%2==0:
		duga()
	else:
		small_duga()
