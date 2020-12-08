# Establish libraries
import pysolar # this will need to be installed by using pip, if opening for the first time.
import datetime
from datetime import timedelta


# Establish time offset
offset = timedelta(hours=-6)
name = 'TFR' # Name of timezone location

# Equinox Date
# Equinox Date: 3/20 Assume Minute, Second, and Microsecond are all zero for now. Hour should be in 24 hour clock setting.
print('Enter year')
year = int(input())
print('Enter month')
month = int(input())
print('Enter day')
day = int(input())
print('Enter hour')
hour = int(input())
date = datetime.datetime(year, month, day, hour, 0, 0, 0, tzinfo=datetime.timezone(offset, name)) 

# Elevation and Azimuth Calculations
# Turtle Lake Refuge Coordinates (via Google Earth):
#				Latitude: 37
#				Longitude: -108
#               Note: inputs don't work with these?
print('Enter latitude')
latitude = int(input())
print('Latitude entered:', latitude)
print('Enter longitude')
longitude = int(input())
print('Longitude entered:', longitude)

TFR_altitude = pysolar.solar.get_altitude(latitude, longitude, date)
TFR_azimuth = pysolar.solar.get_azimuth(latitude, longitude, date)

# Irradiance Calculations
TFR_irradiance = pysolar.radiation.get_radiation_direct(date, TFR_altitude)

# Print out Results and Info
print('---------------------------------------', file = open("solar_data.txt", "a"))
print('---------- Solar Information ----------', file = open("solar_data.txt", "a"))
print('---------------------------------------', file = open("solar_data.txt", "a"))
print('Date:', date, name, 'timezone', sep=" ", file = open("solar_data.txt", "a"))
print('\nAltitude:', TFR_altitude, 'degrees', sep=" ", file = open("solar_data.txt", "a"))
print('Azimuth:', TFR_azimuth, 'degrees', sep=" ", file = open("solar_data.txt", "a"))
print('Irradiance:', TFR_irradiance, 'W/m^2', sep=" ", file = open("solar_data.txt", "a"))

# Solar Cell Efficiency Analysis
# Panel Dimensions: 68x37MM/2.67x1.45"
Panel_width = 37 # mm
Panel_length = 68 # mm
Panel_area = (Panel_width*Panel_length/(1000*1000)) # m^2
solar_panel_efficiency = 0.15 # percentage
Panel_power = (TFR_irradiance * Panel_area) * solar_panel_efficiency

# Print out results
print('\nPanel area:', Panel_area, 'm^2', sep=" ", file = open("solar_data.txt", "a"))
print('Panel power with Panel size and losses:', Panel_power, 'W', sep=" ", file = open("solar_data.txt", "a"))

print('---------------------------------------', file = open("solar_data.txt", "a"))
print('---------------------------------------', file = open("solar_data.txt", "a"))
print('---------------------------------------', file = open("solar_data.txt", "a"))

print('\nSuccess! Check solar_data.txt for exported data.')


# To-Do:
# - Figure out how to input an array of different latitudes for visualization purposes.