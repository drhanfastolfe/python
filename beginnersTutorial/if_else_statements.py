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

elephant_weight = 3000
ant_weight = 0.1

if elephant_weight < ant_weight:
    square()
else:
    leonardo.forward(100)
    wn.exitonclick()