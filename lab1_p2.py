####################################################
# APS106 lab1 Part 2 - Drawing initials with Turtle
####################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()

# use alex to draw your first and last initials
# TODO: WRITE YOUR CODE HERE

alex.pensize(10)
alex.up()

alex.goto(-100,0)
alex.left(90+29/2)
alex.down()
alex.color("blue")
alex.forward(100)
alex.goto(-100,0)
alex.right(29)
alex.forward(100)

alex.up()
alex.goto(-50,0)
alex.down()
alex.left(29/2)
alex.forward(98)
alex.goto(-50,0)
alex.right(90)
alex.forward(50)

alex.up()
alex.goto(28,0)
alex.down()
alex.left(90)
alex.forward(98/2)
alex.right(90)
alex.forward(50)
alex.up()
alex.goto(28,0)
alex.down()
alex.left(90)
alex.forward(98)
alex.right(90)
alex.forward(50)

turtle.done()
