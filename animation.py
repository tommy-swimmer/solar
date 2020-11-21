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
player.color("yellow")

def player_animate():
    x = 0.5
    player.shape("circle")
    time.sleep(x) # pauses program for x seconds.
    player.shape("square") # changes the shape
    time.sleep(x) # pauses again.

while True:
    print("Main Loop")
    player_animate()







wn.mainloop() # This keeps the window open.

# TO-DO
# Credit Youtube video for the base code and link it.