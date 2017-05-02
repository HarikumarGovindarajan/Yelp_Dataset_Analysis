import folium
import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd

# Import data from csv
df = pd.read_csv('C:/Hary/Bigdata/Apache/Data/Italian/0_0_0.csv', encoding = "ISO-8859-1")
df.head()
l1=list()
x1=df['italian']
l1=x1
print(len(l1))
length=len(l1)
map_osm = folium.Map(location=[33.3782141, -111.936102])

for i in range(length):
    str=l1[i]
    name=str.split(':')[0]
    lat=str.split(':')[1]
    lon = str.split(':')[2]
    folium.Marker([lat, lon], popup=name).add_to(map_osm)
map_osm.save('Italian.html')