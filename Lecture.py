# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
# not necessary to import pprint; it only serves to make the data look nicer
from pprint import pprint as pp

# this endpoint returns data about astronauts currently in space
endpoint1 = 'http://api.open-notify.org/astros.json'

# making a call to the API
response = requests.get(endpoint1)

# make sure that your connection status code is 200, which means success!
# 404 is not found and 400 means that details have been entered correctly but something has gone wrong \
# such as a connection not being established
print(response.status_code)

# lets see what data about people in space we get back from the API response
data = response.json()
pp(data)

### EXERCISE 2 ###
"""
TASK: Make a call with a 'PAYLOAD' (special requirements) to the API endpoint
"""

import requests
from pprint import pprint as pp

# this endpoint tells us timings when the international space station will pass over a **given location** on Earth
endpoint2 = 'http://api.open-notify.org/iss-pass.json'

# As an input the API expects a latitude/longitude pair for the location of our interest
# Let's make a dictionary with these parameters, and then include them into our call to the API
# payload = { # these are coordinates for London
#     'lat': 51.507,
#     'lon': 0.1278
# }
payload = { # these are coordinates for New York
    'lat': 40.71,
    'lon': -74,
}

response = requests.get(endpoint2,params=payload)
print(response.status_code)

data = response.json()
pp(data)

# DO EXERCISE 3 TOMORROW WHEN I'M HOME