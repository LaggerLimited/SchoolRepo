import turtle
 
turtle.setup(1000,1000)
screen = turtle.Screen() 
screen.title("MovementExample") 
screen.bgcolor("lightgreen")
tur = turtle.Turtle() 
 
def h1():
  tur.forward(30)
 
def h2():
 tur.left(45)
 
def h3():
   tur.right(45)
 
def h4():
   screen.bye()

screen.onkeypress(h1, "Up")
screen.onkeypress(h2, "Left")
screen.onkeypress(h3, "Right")
screen.onkeypress(h4, "q")

screen.listen()
screen.mainloop()