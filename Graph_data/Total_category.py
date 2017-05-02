import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go


# Import data from csv
df = pd.read_csv('C:/Hary/Bigdata/Apache/Data/catg_type/0_0_0.csv', encoding = "ISO-8859-1")
df.head()
x1=df['category']
y1=df['Total_count']
print(x1)
print(y1)
data = [
    {
        'x': x1,
        'y': y1,
        'mode': 'markers',
        'marker': {
            'color': [120, 125, 130, 135, 140, 145],
            'size': [15, 25, 55, 75, 90, 120],
            'showscale': False
        }
    }
]

py.iplot(data, filename='List of Category')