#################################################
# APS106 lab1 Part 1 - Drawing Shapes with Turtle
#################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()

# tell alex where to go
alex.setheading(90)     # make alex face north
alex.down()             # make alex put pen down
alex.forward(100)       # make alex go 100 forward
alex.right(90)          # make alex turn right 90 degree
alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(150)       # make alex go forward 150 steps

alex.setheading(0)      # make alex face east
alex.forward(50)       # make alex go 50 forward
alex.right(90)          # make alex turn right 90 degree
alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(150)       # make alex go forward 150 steps

alex.setheading(180)    # make alex face west
alex.forward(50)       # make alex go 50 forward
alex.right(90)          # make alex turn right 90 degree
alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(150)       # make alex go forward 150 steps

alex.setheading(270)    # make alex face south
alex.forward(50)        # make alex go 50 forward
alex.right(90)          # make alex turn right 90 degree
alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(150)       # make alex go forward 150 steps

turtle.done()
