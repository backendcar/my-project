import folium
import pandas as pd

data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8, tiles = "Mapbox bright")

for lat, lon,elevation in zip(lat, lon, elevation) :

    folium.Marker(location = [lat, lon], popup = str(elevation)+" m", icon = folium.Icon(color = 'gray')).add_to(map)

map.save("map1.html")
