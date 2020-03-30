import turtle

import math

 

class tanks:
    def __init__(self,x,y,angle,size,v,health,color,name,active):
        self.x=x
        self.y=y
        self.size=size
        self.angle=angle
        self.v=v
        self.health=health
        self.color=color
        self.name=name
        self.active=active

    def draw(self):
        turtle.color(self.color)
        turtle.pu()
        turtle.goto(self.x,self.y-self.size)
        turtle.pd()
        turtle.setheading(0)
        turtle.circle(self.size)
        turtle.pu()
        turtle.goto(self.x,self.y)
        turtle.pd()
        turtle.goto(self.x+math.cos(self.angle)*self.size * 1.5,self.y+math.sin(self.angle)*self.size *1.5)
             
    def move(self):
        self.x+=math.cos(self.angle)* self.v
        self.y+=math.sin(self.angle)* self.v
        self.draw()

 

def kmove():
    global velocity
    velocity=1

def kstop():
    global velocity
    velocity =0

def kleft():
    global rotate
    rotate=.01

def kleftstop():
    global rotate
    rotate=0

def kright():
    global rotate
    rotate=-.01

def krightstop():
    global rotate
    rotate=0

def kend():
    global end
    end=1

 

def control(t):
    t.angle+=rotate
    t.v=velocity

 

screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0) 

 

screen.onkeypress(kmove, "Up")
screen.onkeyrelease(kstop, "Up")
screen.onkeypress(kleft, "Left")
screen.onkeyrelease(kleftstop, "Left")
screen.onkeypress(kright, "Right")
screen.onkeyrelease(krightstop, "Right")
screen.onkeypress(kend, "Escape")
turtle.speed(0)
turtle.hideturtle()
velocity=0
rotate=0
end=0

 

t1=tanks(100,100,45,20,100,100,"blue","Tank 1",True)

 

screen.listen()

while not end :
    control(t1)
    turtle.clear()
    t1.move()
    screen.update()   