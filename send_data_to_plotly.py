from sense_hat import SenseHat
from pandas import DataFrame, read_csv
import pandas as pd
import os.path
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import numpy as np

def PlotData(x, temp, pres, hum):
    trace1 = go.Scatter(x=x, y=temp, name='Temperature')
    trace2 = go.Scatter(x=x, y=pres, name='Pressure')
    trace3 = go.Scatter(x=x, y=hum, name='Humidity')
    plotdata = [trace1, trace2, trace3]

    fig = tools.make_subplots(rows=3, cols=1)
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace3, 3, 1)
    fig.append_trace(trace2, 2, 1)
    
    py.plot(fig, filename='Coldframe', auto_open=False)


dataFile = '/home/pi/projects/sense/sense_hat_data.csv'
if os.path.isfile(dataFile):
    df = pd.read_csv(dataFile)
    date=df['Date']
    temp=df['Temperature_degC']
    pres=df['Pressure_mbar']
    hum=df['Humitity_percent']

    temp = ((temp * 9) / 5) + 32
    
    PlotData(date, temp, pres, hum)

    sense = SenseHat()
    sense.clear([0, 0, 0])
