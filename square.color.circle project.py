#initalizing

import turtle
keisha = turtle.Turtle()
import random
turtle.colormode(255)



#functions
def randomDot():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    s = random.randint(0,50)
   
    keisha.begin_fill()
    keisha.color(r,g,b)
    keisha.circle(s)
    keisha.end_fill()
    print(r)
    print(b)
    print(g)
    
def square():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    keisha.begin_fill()
    keisha.color(r,g,b)
    
    for i in range(4):
        keisha.forward(40)
        keisha.left(90)
    keisha.end_fill()

#main
for i in range(10):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    o = random.randint(-200,200)
    p= random.randint(-200,200)
    randomDot()
    keisha.penup()
    keisha.goto(x,y)
    keisha.pendown()
    square()
    keisha.penup()
    keisha.goto(o,p)
    keisha.pendown()
