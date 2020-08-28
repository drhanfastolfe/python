import turtle

wn = turtle.Screen()
wn.setup(800, 600, 0, 0)
wn.bgcolor("black")
wn.title("Leonardo")

leonardo = turtle.Turtle()
leonardo.color("green")
leonardo.speed(5)
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

for count in range(10):
    square()