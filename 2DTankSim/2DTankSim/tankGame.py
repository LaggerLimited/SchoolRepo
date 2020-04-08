import turtle
import math
import random
 

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

    #Taken from our old project. We calculated in degrees, and this project uses radians, so we convert at the end
    def chase(self, target):
        squared = abs((target.x-self.x)**2 + (target.y-self.y)**2)
        if squared != 0:
            distance = math.sqrt(squared)
        else:
            distance = 0
        if target.x > self.x and target.y > self.y:
            angle = math.degrees(math.atan((target.y - self.y)/(target.x - self.x)))
        elif target.x < self.x and target.y > self.y:
            angle = 180-math.degrees(math.asin((target.y - self.y) / distance))
        elif target.x < self.x and target.y < self.y:
            angle = 180+math.degrees(math.atan(abs(target.y - self.y)/abs(target.x - self.x)))
        elif target.x > self.x and target.y < self.y:
            angle = 360-math.degrees(math.acos(abs(target.x - self.x) / distance))
        else:
            angle = 0
        self.angle = math.radians(angle)
        self.move()

 

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
    t.move()


class MazeNode():
    def __init__(self, pos, parent=None):
        self.parent = parent
        self.pos = pos
        self.h = self.g =self.f = 0
        self.blocked = 0
    def __str__(self):
        #print("Position",self.pos,"parent",self.parent.pos,"h",self.h,"g",self.g,"f",self.f)
        return str(self.blocked)+"("+str(self.pos[0])+","+str(self.pos[1])+") "
#NOTE, maze is accessed as y,x NOT x,y
#0,0 is the upper left corner
def generateMaze(y,x,num_obs):
    maze = [[ MazeNode((y,x)) for x in range(0,x)] for y in range(0,y)]
    for i in range(0,num_obs):
      obs_x = random.randint(0,x-1)
      obs_y = random.randint(0,y-1)
      maze[obs_y][obs_x].blocked = 1
    return maze

#Display the maze in a human-friendly format
def showMaze(maze):
  for i in maze:
    for j in i:
      print(j, end='')
    print();

#Check if a square exists in the maze and is open
def checkSquare(maze,y,x):
    mazeHeight = len(maze)
    mazeWidth = len(maze[0])

    if(x < 0 or y < 0 or x > mazeWidth or y > mazeWidth):
        return False
    if(maze[y][x].blocked == 0):
        return True
    return False

def aStar(maze, start, end):
    nodeData = {}
    closedSet = []
    openSet =[]
    currentNode = maze[start[0]][start[1]]
    closedSet.append(currentNode)
    while currentNode != maze[end[0]][end[1]]:
        adjacent = []
        #Create a list of adjacent nodes
        if(checkSquare(maze,currentNode.pos[0]+1,currentNode.pos[1])):
            adjacent.append(maze[currentNode.pos[0]+1][currentNode.pos[1]])
        if(checkSquare(maze,currentNode.pos[0],currentNode.pos[1]-1)):
            adjacent.append(maze[currentNode.pos[0]][currentNode.pos[1]-1])
        if(checkSquare(maze,currentNode.pos[0]-1,currentNode.pos[1])):
            adjacent.append(maze[currentNode.pos[0]-1][currentNode.pos[1]])
        if(checkSquare(maze,currentNode.pos[0],currentNode.pos[1]+1)):
            adjacent.append(maze[currentNode.pos[0]][currentNode.pos[1]+1])
        for n in adjacent:
            print(n)
            if n in closedSet:
                continue
            elif n in openSet:
                #Compute new G (cost from start to n, using currentNode as parent)
                if new_g < n.g:
                    n.parent = currentNode
                    # compute n.h
                    #compute n.g
                    n.f = n.g + n.h
            else:
                n.parent = currentNode
                #compute n.h
                #compute n.g
                n.f = n.g + n.h
                openSet.append(n)
        if openSet == []:
            break
        #currentNode = node with lowest F in openSet
        #remove current node from openset
        #add current node to closed set

        break




maze = generateMaze(5,5,8)
showMaze(maze);
aStar(maze,(1,1),(3,3))

"""
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
enemies = [tanks(50,50,45,20,.75,100,"red","Tank 2",True), tanks(25,25,45,20,.5,100,"green","Tank 3",True)]

 

screen.listen()

while not end :
    turtle.clear()
    control(t1)
    for i in enemies:
        i.chase(t1)
    
    screen.update()   
"""