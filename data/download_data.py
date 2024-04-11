#!/usr/bin/env python3

# download data from the State of Washington "Electric Vehicle Population Data"
# https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2
# and save it to data/raw/ folder

import os
import requests

# create data/raw/ folder
if not os.path.exists('data/raw'):
    os.makedirs('data/raw')

# download data
url = r'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
r = requests.get(url)
with open('data/raw/Electric_Vehicle_Population_Data.csv', 'wb') as f:
    f.write(r.content)

print('Data downloaded and saved to data/raw/Electric_Vehicle_Population_Data.csv')
