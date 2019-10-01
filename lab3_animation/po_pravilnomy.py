import graphics as gr
import math
SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

class Ball:
    def __init__(self,mass,coords,speed,acceleration):
        self.mass=mass
        self.coords=coords
        self.speed=speed
        self.acceleration=acceleration

g=0.02
def draw_telo(ball_1,ball_2, ball_3):
    coord()
    for i in A:

        circle=gr.Circle(i.coords,3)
        circle.setFill('red')
        circle.draw(window)

def coord():
    velocity()
    for i in A:
        i.coords=add(i.coords, i.speed)
def add(point1,point2):
    new_point=gr.Point(point1.x+point2.x , point1.y+point2.y)
    return new_point
def velocity():
    calculate_accelerations()
    for i in A:
        i.speed=add(i.speed,i.acceleration)

def calculate_accelerations():
    for i in range(3):
        A[i].acceleration = gr.Point(0,0)
        for j in range(3):
            if i != j:
              A[i].acceleration = add(A[i].acceleration, force(A[i], A[j]) )


def force(b1, b2):
    r = add(b1.coords, invert(b2.coords))
    norm_of_r_qubed = norm(r)
    return gr.Point(-g*r.x*b2.mass / norm_of_r_qubed, -g*r.y*b2.mass / norm_of_r_qubed)
def invert(point1):
    return gr.Point(-point1.x,-point1.y)
def norm(point1):
    return (point1.x * point1.x + point1.y * point1.y)**1.5



ball_1=Ball(30,gr.Point(400,350),gr.Point(0,0),gr.Point(0,0))
ball_2=Ball(40,gr.Point(450,400),gr.Point(0,0),gr.Point(0,0))
ball_3=Ball(50,gr.Point(350,400),gr.Point(0,0),gr.Point(0,0))
A=[ball_1,ball_2,ball_3]


 

while True:
    draw_telo(ball_1,ball_2, ball_3)
    gr.time.sleep(0.01)


#  Ожидание нажатия кнопки мыши по окну.
window.getMouse()

#  После того 
# как мы выполнили все нужные операции, окно следует закрыть.
window.close()