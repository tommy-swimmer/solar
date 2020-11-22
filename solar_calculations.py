# This is a test script to optimize the length of an overhang for the optimal passive solar benefit of irradiance
# on the South wall of the Honey House

# This Code works as of: 11/18/2020, hello Github!

import numpy as np

# Make Wall
length = 10  # ft
height = 8  # ft
depth = 12  # ft
area = length * depth  # ft^2

# Area of the wall
print('The total area of the South-facing wall is:', area)

# Make Roof - Roof Pitch
roof_pitch = 10 # degrees

# Degrees available for solar elevation
degrees = np.linspace(26, 74, 48)  # Evenly spaced from 26 to 48? I'm not sure.
print('\n The degrees available are:', degrees)

# TO-DO
# 1. Find shaded area for array of degrees.
# 2. Optimize overhang length. 1' to 2' , angle is 10 degrees.
# 3. Open file and write to it, then display data in a separate file. Can test with other code if needed.

