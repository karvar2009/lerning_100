from turtle import *
from random import randint
# x = 50; y = 50; radius = 200; white_or_black = 0; shag = 40


def target (x, y, radius, shag):
    c = Turtle()
    c.hideturtle()
    c.speed(0)
    white_or_black = 0
    while radius > 10:
        c.penup()
        c.goto(x, y-radius)
        c.pendown()
        c.begin_fill()
        if white_or_black == 0:
            c.fillcolor('black'); white_or_black = 1
        else:
            c.fillcolor('white'); white_or_black = 0
        c.circle(radius)
        c.end_fill()
        radius-=shag



def papino_zadanie(x, y, dlina, shirina, color):
    c = Turtle()
    c.penup()
    c.pencolor(color)
    c.hideturtle()
    c.speed(0)
    c.pensize(1)
    c.goto(x, y)
    c.begin_fill()
    for i in [1,2]:
        c.fd(dlina)
        c.lt(90)
        c.fd(shirina)
        c.lt(90)
    c.fillcolor(color)
    c.end_fill()
    c.penup()
    c.goto(x+dlina/2, y+shirina)
    c.pendown()
    c.lt(90)
    c.pensize(shirina/10)
    c.pencolor("black")
    c.fd(shirina/2)
    c.pencolor("yellow")
    c.fd(shirina/4)


def circles (x, y, color_1, color_2, color_3,radius ,interval):
    c = Turtle()
    c.penup()
    c.pencolor(color_1)
    c.hideturtle()
    c.speed(0)
    c.pensize(1)
    c.goto(x, y)
    c.pendown()

    c.begin_fill()
    c.fillcolor(color_1)
    c.circle(radius)
    c.fd(interval)
    c.pencolor(color_2)
    c.end_fill()

    c.begin_fill()
    c.fillcolor(color_2)
    c.circle(radius)
    c.fd(interval)
    c.pencolor(color_3)
    c.end_fill()

    c.begin_fill()
    c.fillcolor(color_3)
    c.circle(radius)
    c.end_fill()

def click(x,y):
    c = Turtle()
    c.penup()
    c.goto(x, y)
    global Xcen
    global Ycen
    Xcen = x
    Ycen = y


circles(-200,200,'yellow','blue','green',50,30)
papino_zadanie(-200, -300, 100, 50, 'pink')
papino_zadanie(-0, -300, 100, 50, 'pink')
papino_zadanie(200, -300, 100, 50, 'pink')
target (50, 50, 200, 40)

t = Turtle()
s = Screen()
t.forward(0)
t.speed(0)
t.penup()
t.ht()

def tloc(x, y):
  t.penup()
  t.goto(x,y)
  global Xcen
  global Ycen
  Xcen = x
  Ycen = y

Xcen = 0
Ycen = 0
while True:
    s.onclick(tloc)
    t.penup()
    t.goto(Xcen, Ycen)
    t.pendown()

    t.dot(30, 'red')
    t.penup()
    t.goto(Xcen, Ycen)



tloc(0, 0)

done()