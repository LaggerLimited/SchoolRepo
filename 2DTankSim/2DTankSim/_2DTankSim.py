import turtle

import turtle, random
from math import *

#number of tanks, including the player
tank_quantity = 10

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

    def getPos(self):
        return [self.x_pos,self.y_pos]
    def addAngle(self, turn = 0):
        self.myTurtle.right(turn)
        self.angle=self.myTurtle.heading()
        return self.angle
    def moveForward(self, distance):
        self.myTurtle.forward(distance) 
        self.x_pos = self.myTurtle.pos()[0]
        self.y_pos = self.myTurtle.pos()[1]
    def draw(self):          
        pass
        #We currently use the turtle as the tank
    def turnTo(self,heading):
        self.myTurtle.seth(heading)
    def findNearestTarget():
        for i in range(0,tank_quantity):
            test_pos = tanks[i].getPos()
            print(test_pos)
            test_dist = false
    def shootingSolution(self, i):
        target_pos =tanks[i].getPos()
        squared = abs((target_pos[0]-self.x_pos)**2 + (target_pos[1]-self.y_pos)**2)
        if squared != 0:
            distance = sqrt(squared)
        else:
            distance = 0
        print("dist",distance)
        if target_pos[0] > self.x_pos and target_pos[1] > self.y_pos:
            print("q1")
            angle = degrees(atan((target_pos[1] - self.y_pos)/(target_pos[0] - self.x_pos)))
        elif target_pos[0] < self.x_pos and target_pos[1] > self.y_pos:
            print("q2")
            angle = 180-degrees(asin((target_pos[1] - self.y_pos) / distance))
        elif target_pos[0] < self.x_pos and target_pos[1] < self.y_pos:
            print("q3")
            angle = 180+degrees(atan(abs(target_pos[1] - self.y_pos)/abs(target_pos[0] - self.x_pos)))
        elif target_pos[0] > self.x_pos and target_pos[1] < self.y_pos:
            print("q4")
            angle = 360-degrees(acos(abs(target_pos[0] - self.x_pos) / distance))
        else:
            angle = 0
        print ("angle",angle)
        return angle

#Set up tanks
tanks = [Tank(30, 30, 90, 'yellow')]


for i in range(0,tank_quantity-1):
    tanks.append(Tank(random.randint(-200,200),random.randint(-200,200),random.randint(0,360),random.choice(['red','green','blue','black'])))

def keyUp():
    tanks[0].moveForward(5)
def keyLeft():
    tanks[0].addAngle(-5)
def keyRight():
    tanks[0].addAngle(5)
def keyDown():
    turtle.bye()

screen = turtle.Screen()			# Instantiate screen object
screen.setup(500,500)				# Screen Size 500 by 500 pixels
screen.bgcolor("lightgreen")		# Set background color
screen.title("2D Tank Sim")         # Set title at the top of the screen
screen.tracer(0)					# Turn turtle animation off for update drawings

screen.onkeypress(keyUp, "Up")
screen.onkeypress(keyLeft, "Left")
screen.onkeypress(keyRight, "Right")
screen.onkeypress(keyDown, "Down")


while True :                 # Infinite game loop

    
    screen.update()         # Display turtle drawing to the screen

    screen.listen()         # Listen for events like key presses
    for i in range(1,tank_quantity):
        tanks[i].turnTo(tanks[i].shootingSolution(0))