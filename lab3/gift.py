from graph import *
import math 
width=750
height=1000
windowSize(width, height)
canvasSize(width, height)
def zad_pl():
	def fon(r,g,b,x1,y1,x2,y2):
		penColor(r,g,b)
		brushColor(r,g,b)
		rectangle(x1,y1,x2,y2)
	x1=0
	y1=0

	x2=750
	y2=150
	fon(25, 25, 112, x1,y1,x2,y2)
	y1=y2
	y2=y2+50
	fon(123, 104, 238, x1,y1,x2,y2)
	y1=y2
	y2=y2+100
	fon(219, 112, 147, x1,y1,x2,y2)
	y1=y2
	y2=y2+150
	fon(255, 182, 193, x1,y1,x2,y2)
	y1=y2
	y2=y2+100
	fon(255, 165, 0, x1,y1,x2,y2)
	y1=y2
	y2=1000
	fon(0, 255, 255, x1,y1,x2,y2)
	def gora():
		yn=450
		penColor(255, 165, 0)
		brushColor(255, 165, 0)
		p=[(570,450),(595,360),(670,450)]
		polygon(p)

		penColor(255, 165, 0)
		brushColor(255, 165, 0)
		p=[(50,450),(155,380),(270,450)]
		polygon(p)	 
	gora()
	def sun():
		penColor(255, 255, 0)
		brushColor(255, 255, 0)
		circle(200,250, 50)
	sun()
zad_pl()

def oval(x1,y1,x2,r,color):
	penColor(color)	
	brushColor(color)
	while x1!=x2 :
		circle(x1, y1, r)
		x1+=1

def cosoi_oval(x1,y1,x2,y2,r,color):
	while x1!=x2 and y1!=y2 :
		circle(x1, y1, r)
		x1+=1
		y1+=1


def ptycha():
	
	brushColor("white")

	def oper1():	
		p=[(290,790),(210,710),(215,830)]#hvost
		polygon(p)
		penColor(0, 0, 0)
		p=[(350,790),(385,680),(300,710)]#osnov1
		polygon(p)
		p=[(385,680),(300,710),(200,670),(190,660)]#kryl1
		polygon(p)
		p=[(200,670),(190,660),(170,600),(210,660)]#kryl11
		polygon(p)

		penColor(255, 165, 0)#cluv
		brushColor(255, 165, 0)
		p=[(520,750),(570,735),(590,750),(585,760)]
		polygon(p)
		penColor(0, 0, 0)
		line(520, 750, 590, 750)
		
		penColor(255, 255, 255)
		oval(500,750,520,20,"white")
	
		
	def oper2():
		penColor(0, 0, 0)
		p=[(370,770),(395,660),(310,690)]#osnov2
		polygon(p)
		p=[(395,660),(310,690),(205,640),(195,630)]#kryl2
		polygon(p)
		p=[(205,640),(195,630),(175,570),(215,630)]#kryl22
		polygon(p)

	
	oper2()
	oper1()
	
	oval(460,770,500,15,"white")
	oval(315,790,415,40,"white")
	cosoi_oval(325,800,395,840,20,"white")#nogaverh1
	cosoi_oval(380,795,430,835,20,"white")#nogaverh2
	cosoi_oval(420,835,490,890,10,"white")#noganiz1
	cosoi_oval(320,800,450,890,10,"white")#noganiz2
	p=[(460,890),(510,875),(520,880)]#paltsy
	polygon(p)
	p=[(460,890),(510,890),(520,893)]#paltsy
	polygon(p)
	p=[(460,880),(510,910),(520,910)]#paltsy
	polygon(p)	


	p=[(410,890),(450,875),(460,880)]#paltsy
	polygon(p)
	p=[(410,890),(450,890),(460,893)]#paltsy
	polygon(p)
	p=[(410,880),(450,910),(460,910)]#paltsy
	polygon(p)
	
	
	
 
ptycha()
#glaz
penColor(0, 0, 0)
brushColor(0, 0, 0)
circle(520,740, 5)

def ryba():
	penColor(70, 130, 180)
	brushColor(70, 130, 180)
	p=[(500,950),(550,925),(570,925),(600,950),(570,960),(550,960)]
	polygon(p)
	p=[(500,950),(470,920),(460,960)]
	polygon(p)
	#plavniki
	penColor(255, 20, 147)
	brushColor(255, 20, 147)
	p=[(550,925),(570,925),(565,915),(530,915)]
	polygon(p)
	p=[(570,960),(585,975),(565,980)]
	polygon(p)
	#plav2
	p=[(530,957),(535,960),(535,970),(525,965)]
	polygon(p)
	#glaz
	penColor(0, 0, 0)
	brushColor(0, 0, 0)
	circle(580,945, 4)
ryba()	
def birds():
	
	penColor("white")
	penSize(5)
	a=100
	b=400
	R=40
	ygl=195
	ygl_rad=math.radians(ygl)
	x=R*math.cos(ygl_rad)+a
	y=R*math.sin(ygl_rad)+b
	moveTo(x,y)
	for i in range(190):
		ygl_rad=math.radians(ygl)
		x=R*math.cos(ygl_rad)+a
		y=R*math.sin(ygl_rad)+b
		lineTo(x, y)
		ygl+=1
	a=173
	b=430
	ygl=195
	ygl_rad=math.radians(ygl)
	x=R*math.cos(ygl_rad)+a
	y=R*math.sin(ygl_rad)+b
	moveTo(x,y)
	for i in range(190):
		ygl_rad=math.radians(ygl)
		x=R*math.cos(ygl_rad)+a
		y=R*math.sin(ygl_rad)+b
		lineTo(x, y)
		ygl+=1
		
	
#2
	penSize(2)
	a=600
	b=100
	R=20
	ygl=160
	ygl_rad=math.radians(ygl)
	x=R*math.cos(ygl_rad)+a
	y=R*math.sin(ygl_rad)+b
	moveTo(x,y)
	for i in range(180):
		ygl_rad=math.radians(ygl)
		x=R*math.cos(ygl_rad)+a
		y=R*math.sin(ygl_rad)+b
		lineTo(x, y)
		ygl+=1
	a=638
	b=90
	R=20
	ygl=160
	ygl_rad=math.radians(ygl)
	x=R*math.cos(ygl_rad)+a
	y=R*math.sin(ygl_rad)+b
	moveTo(x,y)
	for i in range(180):
		ygl_rad=math.radians(ygl)
		x=R*math.cos(ygl_rad)+a
		y=R*math.sin(ygl_rad)+b
		lineTo(x, y)
		ygl+=1
	
birds()	



run()

