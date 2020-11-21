import turtle

# Some sort of re-creation of sun path angle?

############### USE THIS CODE FOR ANGLE INPUTS IN THE FUTURE ################################
# I found this code from the turtle documentation. It could be useful for later fine-tuning.
summer_screen = turtle.Screen()
summer_angle = summer_screen.numinput("Enter angle","This is only a test at the moment",45, minval=0, maxval=90)
print('The summer angle is: {} degrees'.format(summer_angle))
print('\n')

winter_screen = turtle.Screen()
winter_angle = winter_screen.numinput("Test","Winter Angle",45, minval=0, maxval=90)
print('The winter angle is: {} degrees'.format(winter_angle))
print('\n')
#############################################################################################

# Window Settings and Animation Name

wn = turtle.Screen()
wn.title("Solar Angle Demo")
wn.bgcolor("white")

# Start with Summer?

summer = turtle.Turtle()
summer.hideturtle() # Hides turtle and just draws.

summer.left(summer_angle)
summer.forward(200)
summer.right(180)
summer.forward(400)

# Find out how to pause

# End with winter?

winter = winter_angle + 90 # There is definitely a better way to do this.

summer.left(winter)
summer.forward(400)
summer.right(180)
summer.forward(400)

print(summer.heading()) # Current heading of summer turtle
print(summer.position()) # Final ending position of summer turtle.

turtle.done()

# TO-DO
# Enter in more precise angles for Summer and Winter sun. DONE
# Continue fine-tuning the picture and maybe slow down the animation.
