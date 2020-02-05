import turtle

import turtle, random
from math import *

class Tank:
    def __init__(self, x=0, y=0, ang=0, color='red'):
        self.x_pos = x
        self.y_pos = y
        self.angle = ang
        self.name = ""
        self.active = True
        self.team = 0
        self.color = color
        self.health = 100
        self.myTurtle = turtle.Turtle()
        self.myTurtle.color(self.color)
        self.myTurtle.up()
        self.myTurtle.speed('fastest')
        self.myTurtle.goto(self.x_pos,self.y_pos)

    def getX(self):
        return self.x_pos
    def getY(self):
        return self.x_pos
    def addAngle(self, turn = 0):
        self.myTurtle.right(turn)
        self.angle=self.myTurtle.heading()
        return self.angle
    def moveForward(self, distance):
        self.myTurtle.forward(distance) 
        self.x_pos = self.myTurtle.pos()[0]
        self.y_pos += self.myTurtle.pos()[1]
    def draw(self):          
        pass
        #We currently use the turtle as the tank

#Set up tanks
tanks = [Tank(30, 30, 90, 'yellow')]

for i in range(0,4):
    tanks.append(Tank(random.randint(-50,50),random.randint(-50,50),random.randint(0,360),random.choice(['red','green','blue','black'])))

def keyUp():
    tanks[0].moveForward(5)
def keyLeft():
    tanks[0].addAngle(-5)
def keyRight():
    tanks[0].addAngle(5)

screen = turtle.Screen()			# Instantiate screen object
screen.setup(500,500)				# Screen Size 1000 by 1000 pixels
screen.bgcolor("lightgreen")		# Set background color
screen.title("2D Tank Sim")         # Set title at the top of the screen
screen.tracer(0)					# Turn turtle animation off for update drawings

screen.onkeypress(keyUp, "Up")
screen.onkeypress(keyLeft, "Left")
screen.onkeypress(keyRight, "Right")



while True :                 # Infinite game loop

    
    screen.update()         # Display turtle drawing to the screen
    screen.listen()         # Listen for events like key presses
    for i in range(1,5):
        tanks[i].moveForward(1)
        tanks[i].addAngle(random.randint(-2,5))