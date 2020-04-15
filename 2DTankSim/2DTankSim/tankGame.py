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
        squared = abs((target.pos[1]-self.x)**2 + (target.pos[0]-self.y)**2)
        if squared != 0:
            distance = math.sqrt(squared)
        else:
            distance = 0
        if target.pos[1] > self.x and target.pos[0] > self.y:
            angle = math.degrees(math.atan((target.pos[0] - self.y)/(target.pos[1] - self.x)))
        elif target.pos[1] < self.x and target.pos[0] > self.y:
            angle = 180-math.degrees(math.asin((target.pos[0] - self.y) / distance))
        elif target.pos[1] < self.x and target.pos[0] < self.y:
            angle = 180+math.degrees(math.atan(abs(target.pos[0] - self.y)/abs(target.pos[1] - self.x)))
        elif target.pos[1] > self.x and target.pos[0] < self.y:
            angle = 360-math.degrees(math.acos(abs(target.pos[1] - self.x) / distance))
        else:
            angle = 0
        self.angle = math.radians(angle)
        self.move()

 
class wall:
    def __init__(self,x1,y1,x2,y2,color='blue'):
        self.x1 = x1
        self.y1 = y1
        self.color = color
def kmove():
    global velocity
    velocity=.01

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
    #return the next step you need to take to find this node, run after aStar()
    def nextStep(self, count):
        if(count > 20):
            print("Count > 20")
            return self
        if self.parent != None:
            if self.parent.parent != None:
                return self.parent.nextStep(count+1)
        return self
    def tracePath(self):
        print("Tracing Path",self)
        if(self.parent != None):
            self.parent.tracePath()
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
    mazeHeight = len(maze) - 1
    mazeWidth = len(maze[0]) - 1
    #print(mazeWidth, mazeHeight, y, x)
    if(x < 0 or y < 0 or x > mazeWidth or y > mazeHeight):
        return False
    if(maze[y][x].blocked == 0):
        return True
    return False

#Calculate 'manhatten' distance between 2 points, used for aStar
def h(start, end):
    dx = start[1] - end[1]
    dy = start[0] - end[0]
    return math.sqrt(dx**2 + dy**2)

#TODO: Reset all h, g, f values at the start
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
            #print(n)
            if n in closedSet:
                continue
            elif n in openSet:
                new_g = currentNode.g + 1
                if new_g < n.g:
                    n.parent = currentNode
                    n.h = h(n.pos,end)
                    n.g = n.parent.g + 1
                    n.f = n.g + n.h
            else:
                n.parent = currentNode
                n.h = h(n.pos,end)
                n.g = n.parent.g + 1
                n.f = n.g + n.h
                openSet.append(n)
        if len(openSet) == 0:
            break
        #currentNode = node with lowest F in openSet
        lowestF = 999999999
        for i in openSet:
            if i.f < lowestF:
                currentNode = i
                lowestF = i.f
        #remove current node from openset
        openSet.remove(currentNode)
        #add current node to closed set
        closedSet.append(currentNode)
    print("a* done")
    
def drawMaze(maze):
    for row in maze:
        for node in row:
            if node.blocked == 1:
                turtle.pu()
                turtle.goto(node.pos[1],node.pos[0])
                turtle.stamp()




maze = generateMaze(10,10,10)
showMaze(maze);
aStar(maze,(1,1),(4,4))
#maze[4][4].tracePath()
#print(maze[4][4].nextStep(0))

WORLD_MAX_X = 9
WORLD_MAX_Y = 9

screen = turtle.Screen()
screen.setup(500,500)
screen.setworldcoordinates(WORLD_MAX_X,WORLD_MAX_Y,0,0)
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

 

t1=tanks(8,8,45,.5,100,100,"blue","Tank 1",True)
#enemies = [tanks(2,2,45,.5,.005,100,"red","Tank 2",True), tanks(1,1,45,.5,.007,100,"green","Tank 3",True)]
enemies = [tanks(2,2,45,.5,.005,100,"red","Tank 2",True)]

 

screen.listen()

while not end :
    turtle.clear()
    #drawMaze(maze)
    control(t1)
    for i in enemies:
        #aStar(maze,(int(i.y),int(i.x)),(int(t1.y),int(t1.x)))
        #target = maze[int(t1.y)][int(t1.x)].nextStep(0)
        #print(target)
        #target.tracePath()
        #print("Player at: ",maze[int(t1.y)][int(t1.x)])
        #i.chase(target)
        pass
    
    screen.update()   
