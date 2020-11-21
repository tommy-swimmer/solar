import turtle

# Some sort of recreation of sun path angle?

# Start with Summer?

summer = turtle.Turtle()

summer.left(70)
summer.forward(200)
summer.right(180)
summer.forward(400)

# Find out how to pause

# End with winter?

winter = 26+180 # There is definitely a better way to do this.

summer.right(winter)
summer.forward(400)
summer.right(180)
summer.forward(400)
summer.right(180)

turtle.done()

# TO-DO
# Enter in more precise angles for Summer and Winter sun.
