import turtle

# Some sort of re-creation of sun path angle?

# Window Settings and Animation Name

wn = turtle.Screen()
wn.title("Solar Angle Demo")
wn.bgcolor("white")

# Start with Summer?

summer = turtle.Turtle()

summer.left(48)
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

# I found this code from the turtle documentation. It could be useful for later fine-tuning.
number_screen = turtle.Screen()
x = number_screen.numinput("Enter angle","Summer Angle")
print('The summer angle is:\n',x)

turtle.done()

# TO-DO
# Enter in more precise angles for Summer and Winter sun. DONE
