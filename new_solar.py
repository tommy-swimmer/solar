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

print('Test code:', test)
#

############################ Denver Prototype Test ############################
###############################################################################
# Prototype Code

# Establish timedelta and timezone name
offset = timedelta(hours=-6) # Set timezone offset from UTC
name = 'Denver'

# Equinox Date
date_real = datetime.datetime(2020, 3, 20, 12, 0, 0, 0, tzinfo=datetime.timezone(offset, name)) # figure out how to get correct time.

# Elevation and Azimuth calculations
denver_altitude = pysolar.solar.get_altitude(39.833, -98.583, date_real) # lat and long for Denver, answer should be around 49
denver_azimuth = pysolar.solar.get_azimuth(39.833, -98.583, date_real)
# As of 11/30/2020 got 50.2, close enough with NOAA of 49.29
# JK I had the timezone set wrong, to -7, which gave me 2% error
# Most current error is less than 0.01%

# NOAA Calculations
NOAA_denver_alt = 49.29
NOAA_denver_azi = 163.95

print('\nDenver altitude is:', denver_altitude, 'deg', sep=" ")
print('Denver azimuth is:', denver_azimuth, 'deg', sep=" ")

print('\nNOAA data altitude:', NOAA_denver_alt, 'deg', sep=" ")
print('NOAA data azimuth:', NOAA_denver_azi, 'deg', sep=" ")

print('\nNOAA altitude error is:', abs((denver_altitude-NOAA_denver_alt)/denver_altitude), 'deg', sep=" ")
print('NOAA azimuth error is:', abs((denver_azimuth-NOAA_denver_azi)/denver_azimuth), 'deg', sep=" ")

# TODO
# Fix UTC time for Denver altitude DONE

# Solar Irradiation Test: From 'Estimate of Clear-Sky Radiation'
denver_radiation = pysolar.radiation.get_radiation_direct(date_real, denver_altitude)
print('\nDenver irradiance:', denver_radiation, 'W/m^2', sep=" ")

# TODO
# Research irradiance data
# Make UI or prettier to use
# Enter TFR coordinates here:

########################################################
########################################################