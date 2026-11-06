import turtle
screen = turtle.Screen()
alex = turtle.Turtle()
def exam_marks(n):
    if n >= 90:
        return 'A'
    elif 80<=n<90:
        return 'B'
    elif 70<=n<80:
        return 'C'
    elif 60<=n<70:
        return 'D'
    elif n < 60:
        return 'F'

print(exam_marks(79.99999))
print(exam_marks(80))


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
    alex.pensize(3)


    for height in data:
        if height > 200:
            alex.fillcolor("red")
        elif 100 <= height < 200:
            alex.fillcolor("yellow")
        elif height < 100:
            alex.fillcolor("green")

        drawBar(alex, height, gap)
data = [48,117,200,240,160,260,220]

barChart(data)



def drawBar1(t , height, gap):
    if height >= 0:
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
    if height < 0:
        t.write("" + str(height))

        t.begin_fill()
        t.left(90)
        t.forward(height)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height)
        t.left(90)
        t.end_fill()




def barChart1(data):
    maxheight = max(data)
    num_bars = len(data)

    border = 10
    gap = (maxheight + border) / 25

    screen.bgcolor("lightgreen")
    right = 40 * num_bars + border
    top = maxheight + 4 * gap


    alex.color("blue")
    alex.pensize(3)


    for height in data1:
        if height > 200:
            alex.fillcolor("red")
        elif 100 <= height < 200:
            alex.fillcolor("yellow")
        elif height < 100:
            alex.fillcolor("green")

        drawBar1(alex, height, gap)
data1 = [-100,100,117,200,240,-160,260,-220]
barChart1(data1)
screen.exitonclick()

import math
def findHypot(a,b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

def findHypot2(a,b):
    hypotenuse = (a**2 + b**2)**0.5
    return hypotenuse

print(findHypot(3,4))
print(findHypot2(3,4))
