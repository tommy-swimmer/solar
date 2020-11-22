# New Solar Code Using SolarPy Library
# Tommy Swimmer
# Fort Lewis College
# November 20, 2020

# Hi.

# Helpful Tip: Use mkdir in any directory to make a folder. rm -r to remove it.

# This all works finally!
import pysolar
import datetime

date = datetime.datetime(2007, 2, 18, 15, 13, 1, 130320, tzinfo=datetime.timezone.utc)

test = pysolar.solar.get_altitude(42.206, -71.382, date)

print(test)
#

# Prototype Code

# Equinox Date
date_real = datetime.datetime(2020, 3, 20, 12, 0, 0, 0, tzinfo=datetime.timezone.utc) # figure out how to get correct time.

tfr = pysolar.solar.get_altitude(39.833, -98.583, date_real) # lat and long for Denver

print('Denver altitude is:', tfr)

# TODO
# Fix UTC time for Denver altitude
