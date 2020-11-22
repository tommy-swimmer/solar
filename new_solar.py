# New Solar Code Using SolarPy Library
# Tommy Swimmer
# Fort Lewis College
# November 20, 2020

# Hi.

# Helpful Tip: Use mkdir in any directory to make a folder. rm -r to remove it.

import pysolar
import datetime

date = datetime.datetime(2007, 2, 18, 15, 13, 1, 130320, tzinfo=datetime.timezone.utc)

test = pysolar.solar.get_altitude(42.206, -71.382, date)

print(test)
