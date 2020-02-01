import turtle

# Global variables
forward = True
pos = 0

# Class that defines a tank object
class Tank:
    pos = [0,0]		# Tank position [x,y]
    heading = 0		# Heading or angle the tank is at
    ID = 0			# ID integer to differentiate this tank object from another
    speed = .2		# Tank movement speed
    health = 100	# Health starts at 100 and will deminish in battle
    active = True	# Boolean to control state of object (alive/dead)
    team = ""		# String value for a team name
    color = ""		# String value for color

def DrawTank(xpos, ypos, heading, color):
    # Set draw position
    tur.penup()
    tur.goto(xpos, ypos)			# Init position at left side of the screen
    tur.pendown()
    tur.setheading(heading)			# Set orientation of turtle 0-east 90-north 180-east 270-south
    tur.begin_fill()
    tur.fillcolor(color)
    tur.circle(30,steps= 64)
    tur.end_fill()
    tur.begin_fill()
    tur.fillcolor("black")
    tur.circle(20,steps = 3)
    tur.end_fill()

def Move(speed):
    global forward
    global pos

    if forward:             # Bounce back and forth on the screen
        pos+=speed

        if pos >= 440:
            forward = False
        player1.pos[0] = player1.pos[0] + speed
        player2.pos[0] = player2.pos[0] - speed
    else:
        pos-=speed

        if pos <= 0:
            forward = True
        player1.pos[0] = player1.pos[0] - speed
        player2.pos[0] = player2.pos[0] + speed

screen = turtle.Screen()			# Instantiate screen object
screen.setup(1000,1000)				# Screen Size 1000 by 1000 pixels
screen.bgcolor("lightgreen")		# Set background color
screen.tracer(0)					# Turn turtle animation off for update drawings
tur = turtle.Turtle()				# Create turtle object
tur.color("black")					# Set turtle color
tur.speed(0)						# Set speed to draw as fast as possible
tur.width(4)						# Set a wider draw path
tur.hideturtle()					# Hide the turtle

# Instantiate Tank objects for each player
player1 = Tank()
player1.ID = 1
player1.pos = [-440,-25]
player1.heading = 90
player1.color = "blue"

player2 = Tank()
player2.ID = 2
player2.pos = [440,-25]
player2.heading = -90
player2.color = "red"

while True :                 # Infinite game loop

    tur.clear()

    DrawTank(player1.pos[0],player1.pos[1],player1.heading,player1.color)
    DrawTank(player2.pos[0],player2.pos[1],player2.heading,player2.color)

    screen.update()         # Display turtle drawing to the screen

    Move(player1.speed)

