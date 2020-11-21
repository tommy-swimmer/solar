# Animation Practice in Python
# Tommy Swimmer
# Fort Lewis College
# November 20, 2020

import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("white")

player = turtle.Turtle()
player.shape("circle")
player.color("black")

# Define basic animation as a function
def player_animate():
    if player.shape() == "square":
        player.shape("circle")
    elif player.shape() == "circle":
        player.shape("square")
    
    # Set timer
    wn.ontimer(player_animate, 500)

player_animate()

# Create a while loop to call function.
while True:
    wn.update()
    print('It''s working')

# Update November 21, 2020: using ontimer Method. 

wn.mainloop() # This keeps the window open.

# TO-DO
# Credit Youtube video for the base code and link it.
