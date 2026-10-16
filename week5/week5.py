# Exercise 1
import turtle


# import random
#
# for i in range(10):
#     print(random.random())

# Exercise 2

# import random
#
# for i in range(10):
#     print(random.randint(25,35))

# Exercise 3

# import math
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# d = math.sqrt((a**2 + b**2))
# print(d)

# c = math.hypot(int(input("YLength: ")), int(input("ZLength: ")))
# print(c)

# Exercise 4

# import math
# def areaOfCircle(r):
#     return math.pi * r**2
# print(areaOfCircle(int(input("Enter the radius of the circle: "))))

# Exercise 5

# import turtle
#
# def drowastar(t ,side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# drowastar(tess,100)
# screen.exitonclick()



# Exercise 6

# import turtle
#
# def draw_square(t, size):
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#
# alex = turtle.Turtle()
# screen = turtle.Screen()
# alex.pensize(3)
# alex.pencolor("pink")
# screen.bgcolor("lightgreen")
#
# for i in range(5):
#     draw_square(alex, 20)
#     alex.penup()
#     alex.forward(40)
#     alex.pendown()
#
# screen.exitonclick()

# Exercise 7
import turtle
def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)
alex = turtle.Turtle()
screen = turtle.Screen()
alex.pensize(3)
alex.pencolor("pink")
screen.bgcolor("lightgreen")
size = 20
for i in range(5):
    draw_square(alex, size)
    size += 20
    alex.penup()
    alex.goto(alex.xcor()-10, alex.ycor()-10)
    alex.pendown()

screen.exitonclick()