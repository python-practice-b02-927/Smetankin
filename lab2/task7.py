import turtle
df=1
f=0
k=360*7
turtle.forward(1)
for i in range(k):
    x=turtle.distance(0,0)
    turtle.left(df)
    f+=df
    l=(3.14*df/180)*(1+(f*3.14/180)**2)**0.5
    turtle.forward(l)

