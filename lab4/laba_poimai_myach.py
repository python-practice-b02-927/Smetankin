
from tkinter import *
from random import randrange as rnd, choice
import time

"""создать словарь словарей от шариков по их id с параметрами? мув можем реализовать с помощью словаря для каждого
как рандом от 1 до 4 """
def endgame(name, points):
    global name1
    name1=name
    root2 = Tk()
    
    file = open('top_gamers.txt', 'a')
    file.write(str(points))
    file.write("\n")
    file.write(name1)
    file.write("\n")
    file.close()
    
    file=open('top_gamers.txt', 'r')

    root2.geometry('800x600')
    canv = Canvas(root2,bg='white')
    canv.pack(expand=4)
    


    button1 = Button(root2,text="Restart")
    players = Label(canv,bg='white', fg='black', width=100, height=50)
    
    head=file.readline()
    head+=file.readline()
    
    stroki=""
    D={}
    i=0
    for line in file:
        for k in  range(len(line)):
            if line[k]=='\\' or line[k]=='' :
                break
        line=line[:k]
        i+=1
        key=int(line)
        
        l=file.readline()
        D[key]=l
    
    
   
    spis=sorted(D,reverse=True)
    print(spis)
    for i in range(len(spis)):
        if i==10:
            break
        stroki+=str(i+1)+" "
        stroki+="Points: " + str(spis[i]) + " "
        stroki+="name: " + D[spis[i]]
    head+=stroki 
    players['text']=head
    
    
    def restart(event):
        global name1
        root2.destroy()
        game(name)
    file.close()
    
    players.pack()
    
    button1.pack()
    button1.bind('<Button-1>', restart)
    root2.mainloop()



def game(name):
    global life
    life=3
    root = Tk()
    root.geometry('800x600')
    global count,count_1
    count=0
    count_1=0
    canv = Canvas(root,bg='white')
    canv.focus_set()
    canv.pack(fill=BOTH,expand=1)
    color_number=[i for i in range(6)]
    
    colors = ['red','orange','yellow','green','blue',"black"]

    D={}
    keys=[]
    bomb_keys=[]
    def new_ball():
        global x,y,r,itend,count, count_1
        
        x = rnd(100,700)
        y = rnd(100,500)
        r = rnd(30,50)
        
        
        if len(D)<3:
            ball_color_number=choice(color_number)
            
            itend=canv.create_oval(x-r,y-r,x+r,y+r,fill = colors[ball_color_number], width=0)
            
            c_x=rnd(-20,20)
            c_y=rnd(-20,20)
            D[itend] = {"x_coord":x,"y_coord":y, "move_x":c_x, "move_y":c_y,"radius":r,"ball_color":ball_color_number}
            keys.append(itend)
            if D[itend]["ball_color"]==5:
                bomb_keys.append(itend)
                count_1+=1
            
        if count_1!=0:
            count+=1
        
        
        if count==4 and len(bomb_keys)!=0:
            del_numb_bomb=rnd(0,len(bomb_keys))
            print("nomer {}".format(del_numb_bomb))
            canv.delete(bomb_keys[del_numb_bomb])
            D.pop(bomb_keys[del_numb_bomb], None)
            keys.remove(bomb_keys[del_numb_bomb])
            print(keys)
            
            del bomb_keys[del_numb_bomb]
            count_1=0
            count=0
        for j in D:
            canv.move(j,D[j]["move_x"],D[j]["move_y"])
            D[j]["x_coord"]+=D[j]["move_x"]
            D[j]["y_coord"]+=D[j]["move_y"]
            if  D[j]["x_coord"]<=D[j]["radius"] or 800 - D[j]["x_coord"]<=D[j]["radius"]:
                D[j]["move_x"]=D[j]["move_x"]*(-1)
            if  D[j]["y_coord"]<=D[j]["radius"] or 600 - D[j]["y_coord"]<=D[j]["radius"]:
                D[j]["move_y"]=D[j]["move_y"]*(-1)

        if life!=0:
            root.after(1000,new_ball)
        else: 
            root.destroy()
            endgame(name,kek)

    
   
        
    
    player = Label(root,bg='white', fg="black", width=40)
    li = Label(root,bg='black', fg='white', width=20)
    player['text']= name
    global kek
    kek=0   
    def click(event):
        global kek,life, count, count_1
        for i in range(len(keys)-1,-1,-1):
            if keys[i]!=0:
                x_1=D[keys[i]]["x_coord"]
                y_1=D[keys[i]]["y_coord"]
                a = ((event.x - x_1)**2 + (event.y - y_1)**2)**0.5
                if a<=r: 
                    
                    if D[keys[i]]["ball_color"]==5:
                        life-=1
                        bomb_keys.remove(keys[i])
                        count_1=0
                        count=0
                    else:
                        kek+=1
                    canv.delete(keys[i])
                    D.pop(keys[i], None)

                    
                    li['text'] ="Points:{},Lifes:{}".format(str(kek),life)
                    keys[i]=0
            else:
                continue
            
            
    new_ball()
    player.pack()
    li.pack()
    canv.bind('<Button-1>', click)
    root.mainloop()

#///
def menu(): 
    root1 = Tk()
    root1.geometry('800x600')
    canv = Canvas(root1,bg='white')
    canv.pack(expand=4)
    button1 = Button(root1,text="Start")
    enter_name = Label(bg='white', fg='black', width=1000)
    enter_name['text']="Enter your name"
    e1 = Entry(width=50)
    enter_name.pack()
    e1.pack()

    def start(event):
        name = e1.get()
        root1.destroy()
        game(name)
        
    button1.pack()
    button1.bind('<Button-1>', start)

    root1.mainloop()

menu()

