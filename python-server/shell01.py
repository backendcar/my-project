Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... 
... 
... URL = "http://maps.googleapis.com/maps/api/geocode/json"
... 
... 
... location = "delhi technological university"
... 
... PARMAS = {'adress' : location}
... 
... r = requests.get(url = URL,params = PARMAS)
... 
... data = r.json()
... 
... 
... latitude = data['results'][0]['geometry']['location']['lat']
... longitude = data['results'][0]['geometry']['location']['lat']
... formatted_address = data['results'][0]['formatted_address']
... 
... print("Latitude:%s\nLongitude:%s\nFormatted Address:%s%(latitude, longitude,formatted_address)")
... 
SyntaxError: multiple statements found while compiling a single statement
>>> 
================================ RESTART: Shell ================================
>>> KeyboardInterrupt