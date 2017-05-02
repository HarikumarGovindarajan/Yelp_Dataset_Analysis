import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


# Import data from csv C:\Hary\Bigdata\Apache\Data\Final
df = pd.read_csv('C:/Hary/Bigdata/Apache/Data/Final/top_cultural_rest.csv', encoding = "ISO-8859-1")
df.head()
x1=df['Category']
y1=df['Count']
print(x1)
print(y1)
data = [
    {
        'x': x1,
        'y': y1,
        'mode': 'markers',
        'marker': {
            'color': [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175],
            'size': [125, 115, 105, 95, 85, 75, 65, 55, 45, 35, 25, 15 ],
            'showscale': False
        }
    }
]

py.iplot(data, filename='Top Cuisine')