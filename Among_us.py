
                                  # Among Us Character using Python ( Turtle )


import turtle
import time

BODY_COLOR =  'red'
GLASS_COLOR = 'skyblue'

s = turtle.getscreen()
t = turtle.Turtle()

def body():
  t.fillcolor(BODY_COLOR)
  t.begin_fill()
  t.left(90)
  t.back(40)

  t.circle(50, -180)
  t.right(180)

  t.forward(200)
  t.right(180)
  t.circle(130, -180)
  t.left(15)
  t.circle(520, -20)
  t.backward(20)
  t.circle(50, -180)
  t.left(7)
  t.backward(30)
  t.left(90)
  t.penup()
  t.forward(30)
  t.left(15)
  t.pendown()
  t.circle(200,-30)
  t.back(30)
  t.end_fill()

def Glass():
  t.left(102)
  t.penup()
  t.forward(100)
  t.down()
  t.fillcolor(GLASS_COLOR)
  t.begin_fill()
  t.right(150)
  t.circle(90,-55)
  t.right(180)
  t.forward(1)
  t.right(180)
  t.circle(10, -65)
  t.backward(190)
  t.circle(50,-180)
  t.backward(170)
  t.circle(20, -65)
  t.end_fill()

def backpack():
  t.penup()
  t.right(90)
  t.forward(90)
  t.left(60)
  t.forward(70)
  t.right(90)
  t.pendown()
  t.fillcolor(BODY_COLOR)
  t.begin_fill()
  t.forward(20)
  t.right(180)
  t.circle(30, -30)
  t.circle(30 , -70)
  t.left(13)
  t.backward(120)
  t.circle(30, -30)
  t.circle(30 , -70)
  t.end_fill()

t.pensize(20)
t.speed(5)
body()
Glass()
backpack()
time.sleep(30)