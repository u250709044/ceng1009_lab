import turtle
import math

alex = turtle.Turtle()
screen = turtle.Screen()
alex.speed(0)


def sumTo(n):
    total =  (n * (n + 1)) / 2
    return total

def sumTo2(m):
    total = 0
    for i in range(m + 1):
       total += i
    return total

def mySqrt(x):
    guess = x/2
    for i in range(20):
        guess = (1/2) * (guess + x / guess)
    return guess


def drowstar(t , n , size):
        aci = 180-180/n
        for i in range(n):
            alex.forward(size)
            alex.right(aci)


def drawSprite(someturtle , legs , lenght):
    angle = 360 /legs
    someturtle.forward(lenght)
    someturtle.backward(lenght)
    someturtle.left(angle)

def fancySquare():
    def drawtriangle():
        for i in range(3):
            alex.right(30)
            alex.forward(40)
            alex.left(150)
    def drawsprite(n):
        for i in range(n):
            alex.forward(70)
            alex.begin_fill()
            drawtriangle()
            alex.end_fill()
            alex.backward(70)
            alex.right(360/n)
    def drawsquare():
        for i in range(4):
            alex.forward(250)
            drawsprite(8)
            alex.right(90)
    drawsquare()

def iswhat(n):
    if n < 0:
        return "negative"
    elif n > 0:
        return "positive"
    else:
        return "zero"



def drawBar(t , height, gap):
    t.penup()
    t.left(90)
    t.forward(height + gap)
    t.write("" + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown()

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def barChart(data):
    maxheight = max(data)
    num_bars = len(data)

    border = 10
    gap = (maxheight + border) / 25

    screen.bgcolor("lightgreen")
    right = 40 * num_bars + border
    top = maxheight + 4 * gap
    screen.setworldcoordinates(-border , -border , right , top)

    alex.color("blue")
    alex.fillcolor("red")
    alex.pensize(3)

    for height in data:
        drawBar(alex, height, gap)
data = [48,117,200,240,160,260,220]










# Exercise 1

# n = int(input("Enter a Number: "))
# print(sumTo(n))

# Exercise 2
# drowstar(alex ,10,100)

# Exercise 3
# m = int(input("Enter a Number: "))
# print(sumTo2(m))

# Exercise 4
# n = int(input("Enter a number: "))
# print(mySqrt(n))
# print(math.sqrt(n))

# Exercise 5
# fancySquare()

# Exercise 6
# print(iswhat(3))
# print(iswhat(-1))
# print(iswhat(0))

# Exercise 7
barChart(data)

screen.exitonclick()



