# Timothy Rutkowski 02/27/2024 timothyRutkowski_lab4-3.py

# This program will draw a star pattern using a loop function with turtle graphics

# Imports turtle graphics
import turtle

# Define constants
START_X = 235 # Starting X coordinate
START_Y = -35 # Starting Y coordinate
NUM_LINES = 8 # Number of lines to draw
LINE_LENGTH = 500 # Length of each line
ANIMATION_SPEED = 0 # Animation speed
ANGLE = 135 # Angle to turn

# Move turtle to initial position
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

# Set the animation speed
turtle.speed(ANIMATION_SPEED)

# Loop function 
# Starts each line with the turtle tilted 135 degrees and draws 8 lines
for x in range(NUM_LINES):
    turtle.left(ANGLE)
    turtle.forward(LINE_LENGTH)
    
turtle.done()