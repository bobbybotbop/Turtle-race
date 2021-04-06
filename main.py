import turtle 
from random import randint

course = turtle.Turtle()

course.penup()
course.goto(-140,140)
course.speed(0)
course.hideturtle()

for step in range(16):
 course.write(step)
 course.right(90)
 course.forward(10)
 course.pendown()
 course.forward(150)
 course.penup()
 course.backward(160)
 course.left(90)
 course.forward(20)

leo = turtle.Turtle()
leo.color("cyan","black")
leo.shape("turtle")
leo.penup()
leo.goto(-160,100)

John = turtle.Turtle()
John.color("greenyellow","black")
John.shape("turtle")
John.penup()
John.goto(-160,75)

E = turtle.Turtle()
E.color("red","black")
E.shape("turtle")
E.penup()
E.goto(-160,50)

REEEEE= turtle.Turtle()
REEEEE.color("gold","black")
REEEEE.shape("turtle")
REEEEE.penup()
REEEEE.goto(-160,25)

for turn in range(100):
 REEEEE.forward(randint(1,5))
 leo.forward(randint(1,5))
 E.forward(randint(1,5))
 John.forward(randint(1,5))







