#!/usr/bin/env python3

# download data from the State of Washington "Electric Vehicle Population Data"
# https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2
# and save it to data/raw/ folder

import os
import requests

current_file_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file_path))

data_raw_folder = os.path.join(project_root, 'data', 'raw')

# create data/raw/ folder
if not os.path.exists(data_raw_folder):
    os.makedirs(data_raw_folder)

# download data
data_file_path = os.path.join(data_raw_folder, 'vehicleData.csv')

url = r'https://data.wa.gov/api/views/brw6-jymh/rows.csv?accessType=DOWNLOAD'
r = requests.get(url)
with open(data_file_path, 'wb') as f:
    f.write(r.content)

print('Data downloaded and saved to {}'.format(data_file_path))
