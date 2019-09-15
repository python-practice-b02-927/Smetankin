import turtle
def star(n,ygl_pov):
	for i in range(n):
		turtle.forward(200)
		turtle.right(ygl_pov)

def ygl(n):
	new_n=(n-1)/2
	new_mnogoyg=new_n+1
	ygl_new_mnog= (180*(new_mnogoyg-2)-(n-3)*(180-360/n)/2)/2
	ygl_star= 180-360/n-ygl_new_mnog*2
	ygl_pov=180-ygl_star
	return ygl_pov
def zapusk(n):
	ygl_pov=ygl(n)
	star(n,ygl_pov)

zapusk(5)
turtle.clear()
zapusk(11)

