import turtle
print('vvedite n')
n=int(input())
for i in range(n):
   turtle.forward(50)
   turtle.stamp()
   turtle.backward(50)
   turtle.right(360/n)
