import turtle
screen=turtle.Screen()
screen.setup(500,600,startx=0,starty=0)
t=turtle.Turtle()
turtle.bgcolor("black")
turtle.speed(1)
while(True):
    for i in range(6):
        for colors in["red","blue","indigo","yellow","brown","black","violet","orange","indigo","yellow"]:
            turtle.color(colors)
            turtle.circle(200)
            turtle.left(100)

