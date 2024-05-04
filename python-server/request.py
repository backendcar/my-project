import requests


URL = "http://maps.googleapis.com/maps/api/geocode/json"


location = "delhi technological university"

PARMAS = {'adress' : location}

r = requests.get(url = URL,params = PARMAS)

data = r.json()


latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lat']
formatted_address = data['results'][0]['formatted_address']

print("Latitude:%s\nLongitude:%s\nFormatted Address:%s%(latitude, longitude,formatted_address)")

