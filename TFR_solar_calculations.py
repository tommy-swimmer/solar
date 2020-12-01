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
latitude = 37
longitude = -108

TFR_altitude = pysolar.solar.get_altitude(latitude, longitude, equinox_date)
TFR_azimuth = pysolar.solar.get_azimuth(latitude, longitude, equinox_date)

# Irradiance Calculations
TFR_irradiance = pysolar.radiation.get_radiation_direct(equinox_date, TFR_altitude)

# Print out Results
print('Altitude:', TFR_altitude)
print('Azimuth:', TFR_azimuth)
print('Irradiance:', TFR_irradiance)
