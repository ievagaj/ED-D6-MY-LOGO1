import turtle

# Screen conditions
s = turtle.Screen()
s.bgcolor("#424141")
s.setup(width=600, height=550)
s.title("My logo")

# Drawing conditions
a = turtle.Turtle()
a.pensize(5)
a.shape("classic")

# Circle
a.penup()
a.goto(0, -120)
a.pendown()
a.begin_fill()
a.color("white")
a.circle(150, 360)
a.end_fill()
a.penup()

# I
a.pensize(3)
a.pencolor("black")
a.goto(-70, -75)
a.pendown()
a.left(90)
a.forward(200)
a.penup()

# G
a.goto(90, 75)
a.pendown()
a.circle(50, 180)
a.forward(105)
a.circle(50, 180)
a.forward(25)
a.left(90)
a.forward(50)
a.penup()

# Black frame around logo
a.goto(0, -120)
a.pendown()
a.circle(-150, 360)

a.hideturtle()
turtle.done()