# Exercise 1
import turtle
# ---setup---

wn = turtle.Screen()
wn.bgcolor("lightgreen")


tess = turtle.Turtle()
tess.speed(10)

# --- function ---
def drawPoly(t, somesides, somesize):
    for side in range(somesides):
        t.forward(somesize)
        t.left(360/somesides)

def drawSpiral(t, angle):
    size = 1
    for side in range(100):
        t.forward(size)
        t.right(angle)
        size = size + 2

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

def drawstar(someturtle, somesize):
    for i in range(5):
        someturtle.forward(somesize)
        someturtle.right(144)

def drawSprite(someturtle, legs , lenght):
    angle = 360/legs
    for i in range(legs):
        someturtle.forward(lenght)
        someturtle.backward(lenght)
        someturtle.left(angle)


# ---Exercises---

# Exercise 1
# drawPoly(tess, 8, 50)

# Exercise 2
# tess.pencolor("darkblue")
# for i in range(20):
#     drawPoly(tess, 4, 100)
#     tess.left(360/20)

# Exercise 3
# tess.pencolor("blue")
# tess.pensize(2)
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# drawSpiral(tess,90)
#
# tess.penup()
# tess.goto(150,0)
# tess.pendown()
# drawSpiral(tess,89)

# Exercise 4
# drawEquitriangle(tess, 100)

# Exercise 5
# tess.pencolor("hotpink")
# tess.penup()
# tess.goto(-150,0)
# tess.pendown()
# for i in range(5):
#     drawstar(tess, 100)
#     tess.penup()
#     tess.forward(350)
#     tess.right(144)
#     tess.pendown()

# Exercise 6
# drawSprite(tess, 15, 120)

# --- finish ---
wn.exitonclick()

