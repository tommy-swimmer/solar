# Establish libraries
import pysolar
import datetime
from datetime import timedelta

# Establish time offset
offset = timedelta(hours=-6)
name = 'TFR'

# Equinox Date
equinox_date = datetime.datetime(2021, 3, 20, 12, 0, 0, 0, tzinfo=datetime.timezone(offset, name))

# Elevation and Azimuth Calculations
# Turtle Lake Refuge Coordinates (via Google Earth):
#				Latitude: 37
#				Longitude: -108
#               Note: inputs don't work with these?
latitude = 37
longitude = -108

TFR_altitude = pysolar.solar.get_altitude(latitude, longitude, equinox_date)
TFR_azimuth = pysolar.solar.get_azimuth(latitude, longitude, equinox_date)

# Irradiance Calculations
TFR_irradiance = pysolar.radiation.get_radiation_direct(equinox_date, TFR_altitude)

# Print out Results and Info
print('Altitude:', TFR_altitude)
print('Azimuth:', TFR_azimuth)
print('Irradiance:', TFR_irradiance)

# Solar Cell Efficiency Analysis
# Panel Dimensions: 68x37MM/2.67x1.45"
Panel_width = 37 # mm
Panel_length = 68 # mm
Panel_area = (Panel_width*Panel_length/(1000*1000)) # m^2
solar_panel_efficiency = 0.15 # percentage
Panel_power = (TFR_irradiance * Panel_area) * solar_panel_efficiency

# Print out results
print('\nPanel area:', Panel_area, 'm^2', sep=" ")
print('Panel power with Panel size and losses:', Panel_power, 'W', sep=" ")

