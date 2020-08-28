import turtle

wn = turtle.Screen()
wn.setup(800, 600, 0, 0)
wn.bgcolor("black")
wn.title("Leonardo")

leonardo = turtle.Turtle()
leonardo.color("green")
leonardo.speed(1)
leonardo.pensize(3)
leonardo.shape("turtle")

def square():
    leonardo.forward(100)
    leonardo.right(90)
    leonardo.forward(100)
    leonardo.right(90)
    leonardo.forward(100)
    leonardo.right(90)
    leonardo.forward(100)
    
    wn.exitonclick()

leo = 'happy'
i = 0
while leo == 'sad':
    leonardo.forward(10 + i)
    leonardo.right(90)
    i = i + 2
    