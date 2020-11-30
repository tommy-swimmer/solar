# New Solar Code Using SolarPy Library
# Tommy Swimmer
# Fort Lewis College
# November 20, 2020

# Hi.

# Helpful Tip: Use mkdir in any directory to make a folder. rm -r to remove it.

# This all works finally!
import pysolar
import datetime
from datetime import timedelta

date = datetime.datetime(2007, 2, 18, 15, 13, 1, 130320, tzinfo=datetime.timezone.utc)

test = pysolar.solar.get_altitude(42.206, -71.382, date)

print(test)
#

# Prototype Code

# Establish timedelta and timezone name
offset = timedelta(hours=-7)
name = 'Denver'

# Equinox Date
date_real = datetime.datetime(2020, 3, 20, 12, 0, 0, 0, tzinfo=datetime.timezone(offset, name)) # figure out how to get correct time.

denver_altitude = pysolar.solar.get_altitude(39.833, -98.583, date_real) # lat and long for Denver, answer should be around 49
# As of 11/30/2020 got 50.2, close enough with NOAA of 49.29

print('Denver altitude is:', denver_altitude)
print('NOAA data altitude:', 49.29)
print('NOAA error is:', abs((denver_altitude-49.29)/denver_altitude))

# TODO
# Fix UTC time for Denver altitude
