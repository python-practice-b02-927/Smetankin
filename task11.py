import turtle
def print_eight(n):
	k=360//n
	for i in range(k):
		turtle.left(n)
		turtle.forward(1)
	for i in range(k):
		turtle.right(n)
		turtle.forward(1)
  

n=6
turtle.left(90)
for i in range(5):
	print_eight(n)
	n-=1
