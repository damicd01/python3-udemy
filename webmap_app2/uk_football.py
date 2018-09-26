import folium
import pandas
stadiums = pandas.read_csv("football_stadiums copy.csv")

map = folium.Map(location=[53.76,-2.70], zoom_start=6)
feature_group = folium.FeatureGroup(name="UK_football")

name = list(stadiums["Stadium"])
latitude = list(stadiums["Latitude"])
longitude = list(stadiums["Longitude"])

for latitude, longitude, name in zip(latitude, longitude, name):
    feature_group.add_child(folium.Marker(location=[latitude, longitude], popup=folium.Popup(str(name),parse_html=True), icon=folium.Icon(color='green')))
map.add_child(feature_group)

map.save("uk.html")
