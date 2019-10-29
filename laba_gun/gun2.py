from random import randrange as rnd, choice
import tkinter as tk
import math
import time


# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
global gravity
gravity = 1

class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
    
    
    def move(self):
        if self.x + self.vx >=800:
            canv.delete(self.id)
        self.x += self.vx
        self.vy -= gravity 
        if self.y - self.vy >=470:
            self.y=470
            self.vy = -self.vy/3
            self.vx -= self.vx/3
        self.y -= self.vy
        self.set_coords()
        

        
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        distance = ((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5 
        if distance <= (self.r + obj.r): 
            return True
        return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.tang=math.tan(self.an)
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
            self.tang=math.tan(self.an)
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Points():
    def __init__(self,value=0):
        
        self.value = 0
        self.id_points = canv.create_text(30,30,text = self.value,font = '28')
        
    def tabel(self):
        #canv.coords(self.id_points, -10, -10, -10, -10)
        canv.itemconfig(self.id_points, text=self.value)
    def hit(self, points=1):
        """Попадание шарика в цель."""
        point.value+= points
        point.tabel()

point = Points(0)





class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        #self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 450)
        r = self.r = rnd(10, 50)
        self.vx = rnd(1, 8)
        self.vy = rnd(2, 10)

        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
    def move(self):
        if self.x + self.vx >=800:
            self.x = 800
            self.vx = -self.vx
        if self.x + self.vx <=0:
            self.x = 0
            self.vx = -self.vx
        self.x += self.vx
        
        if self.y - self.vy >=470:
            self.y=470
            self.vy = -self.vy
        if self.y - self.vy <=0:
            self.y=0
            self.vy = -self.vy
        self.y -= self.vy
        self.set_coords()


    
        



targ = []
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []







def new_game(event=""):
    
    global gun, t1, screen1, balls, bullet
    canv.itemconfig(screen1, text='')
    t1 = target()
    t2 = target()
    t1.new_target()
    t2.new_target()
    targ = [t1]
    targ += [t2]

    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = 0.03
    
    button_pressed = True
    
    def final_button_released(event):
        print("I AM FUCKING RELEASED!!!!111!!1!!")
        global button_pressed 
        button_pressed = False

        new_game("")


    while t1.live or t2.live or balls or button_pressed:
        if t1.live==1 or t2.live==1:
            t1.move()
            t2.move()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                point.hit(1)
                canv.delete(t1.id)
            if b.hittest(t2) and t2.live:
                t2.live = 0
                point.hit(1)
                canv.delete(t2.id)
            
            if t1.live == 0 and t2.live == 0:
                
                for i in targ:
                    canv.delete(i.id)
                    targ=[]
                for i in balls:
                    canv.delete(i.id)
                    balls = []     
                
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + 'выстрелов')
                
                canv.bind('<Button-1>',"")
                canv.bind('<ButtonRelease-1>',final_button_released)
                time.sleep(0.03)
                
                
                

                
                
                
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    
    root.after(750, new_game)


new_game()

root.mainloop()