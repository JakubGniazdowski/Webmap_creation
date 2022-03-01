
import folium
import pandas

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return"red"


data= pandas.read_csv("Volcanoes_USA.txt")
lon=list(data["LON"])
lat=list(data["LAT"])
elev=list(data["ELEV"])

map= folium.Map(location=[38.58,-99.09], zoom_start=6)
fg=folium.FeatureGroup(name="My map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m"  ,icon=folium.Icon(color=color_producer(el)  )))
fg.add_child(folium.Marker(location=[52.25935646735977, 20.931151314934958], popup="miejsce zamieszkania poważnego przestępcy",icon=folium.Icon(color="pink")))

fg.add_child(folium.GeoJson(data=open('115 world.json', 'r',encoding="utf-8-sig").read(), 
style_function= lambda x:{'fillColor':"green" if x['properties']['POP2005']<10000000 
else "orange" if 10000000<= x['properties']['POP2005']<200000000 else 'red'}))


map.add_child(fg)

map.save("map1.html")






