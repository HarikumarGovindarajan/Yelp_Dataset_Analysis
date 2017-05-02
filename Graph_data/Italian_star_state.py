import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd

# Import data from csv
df = pd.read_csv('C:/Hary/Bigdata/Apache/Data/Italian_stars/0_0_0.csv', encoding = "ISO-8859-1")
df.head()
state=df['state']
fiveS=df['fiveS']
fourpS=df['fourpS']
fourS=df['fourS']
threeps=df['threeps']
threes=df['threes']
twops=df['twops']
twos=df['twos']
oneps=df['oneps']
ones=df['ones']


trace1 = {
  "x": state,
  "y": fiveS,
  "marker": {"color": "rgb(23, 190, 207)"},
  "name": "5Star",
  "type": "bar",
  "uid": "159ab4"
}
trace3 = {
  "x": state,
  "y": fourS,
  "marker": {"color": "rgb(246, 178, 107)"},
  "name": "4Star",
  "type": "bar",
  "uid": "ddbf5d"
}
trace2 = {
  "x": state,
  "y": fourpS,
  "marker": {"color": "rgb(188, 189, 34)"},
  "name": "4.5Star",
  "type": "bar",
  "uid": "62cc1b"
}
trace4 = {
  "x": state,
  "y": threeps,
  "marker": {"color": "rgb(127, 127, 127)"},
  "name": "3.5Star",
  "type": "bar",
  "uid": "db903d"
}
trace5 = {
  "x": state,
  "y": threes,
  "marker": {"color": "rgb(227, 119, 194)"},
  "name": "3Star",
  "type": "bar",
  "uid": "a4b8a2"
}
trace6 = {
  "x": state,
  "y": twops,
  "marker": {"color": "rgb(148, 103, 189)"},
  "name": "2.5Star",
  "type": "bar",
  "uid": "a8de91"
}
trace7 = {
    "x": state,
    "y": twos,
  "marker": {"color": "rgb(147, 196, 125)"},
  "name": "2Star",
  "type": "bar",
  "uid": "40063c"
}
trace8 = {
    "x": state,
    "y": oneps,
  "marker": {"color": "rgb(31, 119, 180)"},
  "name": "1.5Star",
  "type": "bar",
  "uid": "38291f"
}
trace9 = {
  "x": state,
  "y": ones,
  "marker": {"color": "rgb(234, 153, 153)"},
  "name": "1Star",
  "type": "bar",
  "uid": "f46f4f"
}

data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9])
layout = {
  "annotations": [
    {
      "x": 0.1,
      "y": 0.3,
      "align": "center",
      "arrowcolor": "rgba(0, 0, 0, 0)",
      "arrowhead": 1,
      "arrowsize": 1,
      "arrowwidth": 0,
      "ax": -42,
      "ay": 218.858329773,
      "bgcolor": "rgba(0, 0, 0, 0)",
      "bordercolor": "rgba(0, 0, 0, 0)",
      "borderpad": 1,
      "borderwidth": 1,
      "font": {
        "color": "#444",
        "family": "\"Open sans\", verdana, arial, sans-serif",
        "size": 12
      },
      "opacity": 1,
      "showarrow": True,
      "text": "Source: <i>Yelp Dataset</i>",
      "textangle": 0,
      "xanchor": "auto",
      "xref": "paper",
      "yanchor": "auto",
      "yref": "paper"
    }
  ],
  "autosize": False,
  "bargap": 0.2,
  "bargroupgap": 0,
  "barmode": "stack",
  "boxgap": 0.3,
  "boxgroupgap": 0.3,
  "boxmode": "overlay",
  "dragmode": "zoom",
  "font": {
    "color": "#444",
    "family": "\"Open sans\", verdana, arial, sans-serif",
    "size": 12
  },
  "height": 700,
  "hidesources": False,
  "hovermode": "x",
  "legend": {
    "x": 1.02,
    "y": 1,
    "bgcolor": "#fff",
    "bordercolor": "#444",
    "borderwidth": 0,
    "font": {
      "color": "#444",
      "family": "\"Open sans\", verdana, arial, sans-serif",
      "size": 12
    },
    "traceorder": "reversed",
    "xanchor": "auto",
    "yanchor": "auto"
  },
  "margin": {
    "r": 80,
    "t": 100,
    "autoexpand": True,
    "b": 80,
    "l": 80,
    "pad": 2
  },
  "paper_bgcolor": "#fff",
  "plot_bgcolor": "#fff",
  "separators": ".,",
  "showlegend": True,
  "smith": False,
  "title": "<br>Distribution of Italian restaurant across US with star rating",
  "titlefont": {
    "color": "#444",
    "family": "\"Open sans\", verdana, arial, sans-serif",
    "size": 17
  },
  "width": 775,
  "xaxis": {
    "anchor": "y",
    "autorange": True,
    "domain": [0, 1],
    "dtick": 6,
    "exponentformat": "e",
    "gridcolor": "white",
    "gridwidth": 1,
    "linecolor": "#000",
    "linewidth": 1,
    "mirror": False,
    "nticks": 0,
    "overlaying": False,
    "position": 0,
    "range": [-0.5, 35.5],
    "rangemode": "normal",
    "showexponent": "all",
    "showgrid": False,
    "showline": False,
    "showticklabels": True,
    "tick0": 2,
    "tickangle": "auto",
    "tickcolor": "#000",
    "tickfont": {
      "color": "#444",
      "family": "\"Open sans\", verdana, arial, sans-serif",
      "size": 12
    },
    "ticklen": 5,
    "tickmode": "auto",
    "ticks": "",
    "tickwidth": 1,
    "title": "",
    "titlefont": {
      "color": "#444",
      "family": "\"Open sans\", verdana, arial, sans-serif",
      "size": 14
    },
    "type": "category",
    "zeroline": False,
    "zerolinecolor": "#000",
    "zerolinewidth": 1
  },
  "yaxis": {
    "anchor": "x",
    "autorange": True,
    "domain": [0, 1],
    "dtick": 20000,
    "exponentformat": "B",
    "gridcolor": "#eee",
    "gridwidth": 1,
    "linecolor": "#000",
    "linewidth": 1,
    "mirror": False,
    "nticks": 0,
    "overlaying": False,
    "position": 0,
    "range": [0, 167670.526316],
    "rangemode": "normal",
    "showexponent": "all",
    "showgrid": True,
    "showline": False,
    "showticklabels": True,
    "tick0": 0,
    "tickangle": "auto",
    "tickcolor": "#000",
    "tickfont": {
      "color": "#444",
      "family": "\"Open sans\", verdana, arial, sans-serif",
      "size": 12
    },
    "ticklen": 5,
    "tickmode": "auto",
    "ticks": "",
    "tickwidth": 1,
    "title": "",
    "titlefont": {
      "color": "#444",
      "family": "\"Open sans\", verdana, arial, sans-serif",
      "size": 14
    },
    "type": "linear",
    "zeroline": True,
    "zerolinecolor": "#444",
    "zerolinewidth": 1
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)