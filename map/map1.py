import folium
m = folium.Map(location=[35.703516198859376, 51.35186252991974], zoom_start=30)
folium.TileLayer("stamen toner").add_to(m)
m.save("map1.html")
