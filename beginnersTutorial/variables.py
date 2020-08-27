import turtle

# Variables
a = 5
print(a)

b = "hello"
print(b)

credit_card = 4444333322221111
print(credit_card)

# Turtle
wn = turtle.Screen()
wn.setup(800, 600, 0, 0)
wn.bgcolor("black")
wn.title("Leonardo")

leonardo = turtle.Turtle()
leonardo.color("green")
leonardo.speed(10)
leonardo.pensize(3)
leonardo.shape("turtle")

leonardo.forward(100)
leonardo.right(90)
leonardo.forward(100)
leonardo.right(90)
leonardo.forward(100)
leonardo.right(90)
leonardo.forward(100)

wn.exitonclick()



