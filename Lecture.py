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

# EXERCISE 3

import requests
from datetime import datetime
from pprint import pprint as pp

# this endpoint tells the current location for international space station
endpoint3 = 'http://api.open-notify.org/iss-now.json'

response = requests.get(endpoint3)

data = response.json()
pp(data)

timestamp = data['timestamp']
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
    dt = dt_object,
    lat = data['iss_position']['latitude'],
    lon = data['iss_position']['longitude'],
    our_msg = data['message']
)
print(msg)

with open('space_station_location.txt', 'a') as text_file:
    text_file.write(msg + '\n')

# EXERCISE 4

import requests
from pprint import pprint as pp

appid = 'Tester2021'  # key to connect to the API --> create a free account and paste your OWN key here

endpoint = 'http://api.openweathermap.org/data/2.5/weather' # see doc to customise your payload

payload = {
    'q': 'London,UK',
    'unit': 'metrics',
    'appid': appid,
}

response = requests.get(url=endpoint, params=payload)

data = response.json()


pp(data['name'])
pp(data['weather'])

pp(data)

# EXERCISE 5

import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number) # note how we manupulate the url to request data!

response = requests.get(url)
print(response)

pokemon = response.json()
pprint(pokemon)

# EXERCISE 6

import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

pprint(pokemon)
# PRINT THE NAME HERE
# PRINT THE HEIGHT HERE
# PRINT THE WEIGHT HERE

# use a for loop to iterate over the moves. Try to store all moves in a variable and see what it looks like.   
for i in pokemon['moves']:
    print(i['move']['name'])
    print(i['move']['height'])
    print(i['move']['weight'])